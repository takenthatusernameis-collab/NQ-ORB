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
                # RVOL: avg volume of 20 preceding completed 15min bars (exclude breakout bar)
                # Get all bars before this one on same or previous days
                all_bars_before = df15[df15['datetime_et'] < bar['datetime_et']].copy()
                # Get last 20 completed 15min bars
                prev_20 = all_bars_before.tail(self.config.rvol_lookback)
                if len(prev_20) < self.config.rvol_lookback:
                    break  # not enough history
                avg_vol_20 = prev_20['volume'].mean()
                rvol = bar['volume'] / avg_vol_20 if avg_vol_20 > 0 else 0

                # ATR filter
                atr_pct = bar['atr_pct']
                if pd.isna(atr_pct):
                    break

                # Both filters must pass
                if rvol < self.config.rvol_min:
                    break  # first breakout only, filter failed - don't look for later
                if atr_pct < self.config.atr_min_pct or atr_pct > self.config.atr_max_pct:
                    break  # filter failed

                # Eligible trade - determine entry
                # Primary: next 15min bar open
                # Find next bar
                next_bars = df15[df15['datetime_et'] > bar['datetime_et']].copy()
                next_bars = next_bars.sort_values('datetime_et')
                if len(next_bars) == 0:
                    break
                entry_bar = next_bars.iloc[0]
                entry_price = entry_bar['open']

                # Calculate stop and target
                atr_val = bar['atr14']
                if direction == 'long':
                    stop_price = entry_price - self.config.stop_atr_mult * atr_val
                    risk_points = entry_price - stop_price
                    target_price = entry_price + self.config.target_stop_mult * risk_points
                else:
                    stop_price = entry_price + self.config.stop_atr_mult * atr_val
                    risk_points = stop_price - entry_price
                    target_price = entry_price - self.config.target_stop_mult * risk_points

                # Position sizing
                risk_per_contract = risk_points * self.config.mnq_multiplier
                if risk_per_contract <= 0:
                    break
                contracts = int(self.config.risk_usd / risk_per_contract)
                if contracts < 1:
                    break

                # Record trade (simplified - no actual exit simulation yet)
                trade = {
                    'date': trading_date,
                    'direction': direction,
                    'breakout_bar_time': bar['datetime_et'],
                    'entry_bar_time': entry_bar['datetime_et'],
                    'entry_price': entry_price,
                    'stop_price': stop_price,
                    'target_price': target_price,
                    'or_high': or_high,
                    'or_low': or_low,
                    'atr14': atr_val,
                    'atr_pct': atr_pct,
                    'rvol': rvol,
                    'risk_points': risk_points,
                    'contracts': contracts,
                    'risk_usd': risk_per_contract * contracts,
                }
                trades.append(trade)
                break  # only first trade per day

        self.trades = trades
        return trades
