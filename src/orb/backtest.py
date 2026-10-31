"""Backtest engine for NQ ORB."""
import pandas as pd
import numpy as np
from datetime import date, time, timedelta
from typing import List, Dict, Any
from zoneinfo import ZoneInfo

from .orb_logic import ORBConfig, ORBStrategy
from .indicators import wilder_atr

ET = ZoneInfo("America/New_York")


class BacktestEngine:
    def __init__(self, config: ORBConfig = None):
        self.config = config or ORBConfig()
        self.strategy = ORBStrategy(self.config)
        self.trades = []

    def _apply_costs_per_side(self, price: float, side: str) -> float:
        """Apply slippage per side. For entry, slippage is adverse."""
        tick = self.config.tick_size
        slip_ticks = self.config.slippage_ticks
        slip = slip_ticks * tick
        if side == 'buy':
            return price + slip
        elif side == 'sell':
            return price - slip
        return price

    def _round_to_tick(self, price: float) -> float:
        tick = self.config.tick_size
        # Round to nearest tick without improving fill in a weird way; just round
        return round(round(price / tick) * tick, 10)

    def run(self, df_15m: pd.DataFrame, df_1m: pd.DataFrame = None):
        """Run backtest on 15min data with optional 1min for flatten/ordering."""
        df15 = df_15m.copy()
        # Ensure ET columns
        if 'datetime_et' not in df15.columns:
            df15['datetime_et'] = df15['datetime'].dt.tz_convert(ET)
        if 'date' not in df15.columns:
            df15['date'] = df15['datetime_et'].dt.date
        if 'time_et' not in df15.columns:
            df15['time_et'] = df15['datetime_et'].dt.time

        # Compute ATR on 15min
        df15['atr14'] = wilder_atr(df15, self.config.atr_length)
        df15['atr_pct'] = (df15['atr14'] / df15['close']) * 100.0

        df1m = None
        if df_1m is not None:
            df1m = df_1m.copy()
            if 'datetime_et' not in df1m.columns:
                df1m['datetime_et'] = df1m['datetime'].dt.tz_convert(ET)
            if 'date' not in df1m.columns:
                df1m['date'] = df1m['datetime_et'].dt.date
            if 'time_et' not in df1m.columns:
                df1m['time_et'] = df1m['datetime_et'].dt.time

        trades = []
        # Get trading dates
        dates = sorted(df15['date'].unique())

        for trading_date in dates:
            # Check if we already took trade this day
            day_trades = [t for t in trades if t['date'] == trading_date]
            if len(day_trades) >= self.config.max_trades_per_day:
                continue

            # Build OR
            or_info = self.strategy.build_opening_range(df15, trading_date)
            if not or_info:
                continue
            or_high = or_info['high']
            or_low = or_info['low']

            # Get bars after OR for this date
            post_or = df15[(df15['date'] == trading_date) &
                          (df15['time_et'] >= self.config.or_end)].copy()
            post_or = post_or.sort_values('datetime_et')

            # Look for first breakout
            for idx, bar in post_or.iterrows():
                bar_time = bar['time_et']
                # No new entry at or after 15:00
                if bar_time >= self.config.no_new_entry_after:
                    break

                # Check for breakout
                long_break = bar['close'] > or_high  # close strictly above
                short_break = bar['close'] < or_low  # close strictly below

                if not (long_break or short_break):
                    continue

                direction = 'long' if long_break else 'short'

                # Check filters on breakout bar
                all_bars_before = df15[df15['datetime_et'] < bar['datetime_et']].copy()
                prev_20 = all_bars_before.tail(self.config.rvol_lookback)
                if len(prev_20) < self.config.rvol_lookback:
                    break
                avg_vol_20 = prev_20['volume'].mean()
                rvol = bar['volume'] / avg_vol_20 if avg_vol_20 > 0 else 0

                atr_pct = bar['atr_pct']
                if pd.isna(atr_pct):
                    break

                if rvol < self.config.rvol_min:
                    break
                if atr_pct < self.config.atr_min_pct or atr_pct > self.config.atr_max_pct:
                    break

                # Eligible trade - entry on next 15min bar open.
                # Constrain to the SAME trading date so a late breakout cannot
                # silently roll its entry into the next session.
                next_bars = df15[(df15['datetime_et'] > bar['datetime_et']) &
                                  (df15['date'] == trading_date)].copy()
                next_bars = next_bars.sort_values('datetime_et')
                if len(next_bars) == 0:
                    break
                entry_bar = next_bars.iloc[0]
                entry_price_raw = entry_bar['open']
                entry_price_raw = self._round_to_tick(entry_price_raw)

                # Apply slippage on entry (adverse)
                if direction == 'long':
                    entry_price_fill = self._apply_costs_per_side(entry_price_raw, 'buy')
                else:
                    entry_price_fill = self._apply_costs_per_side(entry_price_raw, 'sell')
                entry_price_fill = self._round_to_tick(entry_price_fill)

                # Calculate stop and target from entry price for sizing/risk; use signal bar ATR for stop multiple per spec
                atr_val = bar['atr14']
                if direction == 'long':
                    stop_price = entry_price_raw - self.config.stop_atr_mult * atr_val  # planned stop from raw entry
                    risk_points = entry_price_raw - stop_price
                    target_price = entry_price_raw + self.config.target_stop_mult * risk_points
                else:
                    stop_price = entry_price_raw + self.config.stop_atr_mult * atr_val
                    risk_points = stop_price - entry_price_raw
                    target_price = entry_price_raw - self.config.target_stop_mult * risk_points

                stop_price = self._round_to_tick(stop_price)
                target_price = self._round_to_tick(target_price)

                # Position sizing
                risk_per_contract = risk_points * self.config.mnq_multiplier
                if risk_per_contract <= 0:
                    break
                contracts = int(self.config.risk_usd / risk_per_contract)
                if contracts < 1:
                    break

                # Simulate exit using 1min if available
                exit_price = None
                exit_reason = None
                exit_time = None
                if df1m is not None and len(df1m) > 0:
                    # Get 1min bars after entry
                    df1m_day = df1m[(df1m['date'] == trading_date) & (df1m['datetime_et'] >= entry_bar['datetime_et'])].copy()
                    df1m_day = df1m_day.sort_values('datetime_et')
                    flattened = False
                    for _, mbar in df1m_day.iterrows():
                        mtime = mbar['time_et']
                        # Check flatten first? Flatten at 15:55 - if we reach/past, flatten
                        if mtime >= self.config.forced_flatten:
                            # Flatten at or after 15:55; use this bar's close/open as reasonable; prefer close if in range
                            exit_price = mbar['close']
                            exit_reason = 'flatten_1555'
                            exit_time = mbar['datetime_et']
                            flattened = True
                            break
                        if direction == 'long':
                            hit_stop = mbar['low'] <= stop_price
                            hit_target = mbar['high'] >= target_price
                        else:
                            hit_stop = mbar['high'] >= stop_price
                            hit_target = mbar['low'] <= target_price
                        if hit_stop and hit_target:
                            # stop first on ambiguity
                            exit_price = stop_price
                            exit_reason = 'stop_first_ambiguous'
                            exit_time = mbar['datetime_et']
                            break
                        elif hit_stop:
                            exit_price = stop_price
                            exit_reason = 'stop'
                            exit_time = mbar['datetime_et']
                            break
                        elif hit_target:
                            exit_price = target_price
                            exit_reason = 'target'
                            exit_time = mbar['datetime_et']
                            break
                    if not flattened and exit_price is None:
                        # No hit found by end of day - flatten at last bar before/at cutoff? look for any bar at 15:55
                        # try to find bar at or after 15:55
                        df1m_flat = df1m[(df1m['date'] == trading_date) & (df1m['time_et'] >= self.config.forced_flatten)].copy()
                        if len(df1m_flat) > 0:
                            mbarf = df1m_flat.sort_values('datetime_et').iloc[0]
                            exit_price = mbarf['open'] if mbarf['time_et'] == self.config.forced_flatten else mbarf['close']
                            exit_reason = 'flatten_1555'
                            exit_time = mbarf['datetime_et']
                        else:
                            # use last bar of day
                            last = df1m_day.tail(1)
                            if len(last) > 0:
                                exit_price = last.iloc[0]['close']
                                exit_reason = 'eod'
                                exit_time = last.iloc[0]['datetime_et']
                else:
                    # No 1min data - cannot reliably determine intrabar/flatten; mark as unverified
                    exit_price = None
                    exit_reason = 'no_1min_data_unverified'
                    exit_time = None

                # Apply slippage on exit
                if exit_price is not None and exit_reason != 'no_1min_data_unverified':
                    exit_price_fill = self._round_to_tick(exit_price)
                    if direction == 'long':
                        # selling to exit
                        exit_price_fill = self._apply_costs_per_side(exit_price_fill, 'sell')
                    else:
                        # buying to cover
                        exit_price_fill = self._apply_costs_per_side(exit_price_fill, 'buy')
                    exit_price_fill = self._round_to_tick(exit_price_fill)
                else:
                    exit_price_fill = None

                # Compute PnL
                gross_pnl = None
                net_pnl = None
                if exit_price_fill is not None and exit_reason != 'no_1min_data_unverified':
                    if direction == 'long':
                        gross_pnl = (exit_price_fill - entry_price_fill) * self.config.mnq_multiplier * contracts
                    else:
                        gross_pnl = (entry_price_fill - exit_price_fill) * self.config.mnq_multiplier * contracts
                    # Costs: commissions + fees per side * contracts * 2 sides
                    costs = contracts * 2.0 * (self.config.commission_per_side + self.config.fee_per_side)
                    net_pnl = gross_pnl - costs
                else:
                    gross_pnl = None
                    net_pnl = None

                trade = {
                    'date': str(trading_date),
                    'direction': direction,
                    'breakout_bar_time': str(bar['datetime_et']),
                    'breakout_close': bar['close'],
                    'entry_bar_time': str(entry_bar['datetime_et']),
                    'entry_price_raw': entry_price_raw,
                    'entry_price_fill': entry_price_fill,
                    'stop_price': stop_price,
                    'target_price': target_price,
                    'or_high': or_high,
                    'or_low': or_low,
                    'atr14': atr_val,
                    'atr_pct': atr_pct,
                    'rvol': rvol,
                    'risk_points': risk_points,
                    'contracts': contracts,
                    'risk_usd_planned': risk_per_contract * contracts,
                    'exit_price': exit_price,
                    'exit_price_fill': exit_price_fill,
                    'exit_reason': exit_reason,
                    'exit_time': str(exit_time) if exit_time is not None else None,
                    'gross_pnl': gross_pnl,
                    'net_pnl': net_pnl,
                    'costs_total': contracts * 2.0 * (self.config.commission_per_side + self.config.fee_per_side) if exit_price_fill is not None and exit_reason != 'no_1min_data_unverified' else None,
                }
                trades.append(trade)
                break  # only first trade per day

        self.trades = trades
        return trades
