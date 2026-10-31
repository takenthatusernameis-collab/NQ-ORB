#!/usr/bin/env python3
"""Run ORB backtest on downloaded data."""
import argparse
import json
import os
import sys
from pathlib import Path

import pandas as pd

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from orb.data_loader import DataLoader
from orb.backtest import BacktestEngine
from orb.orb_logic import ORBConfig


def _summarize(sub_trades):
    """Aggregate a list of trades into a metrics dict (gross/net/costs/R)."""
    if not sub_trades:
        return {"count": 0}
    wins = [t for t in sub_trades if t['net_pnl'] > 0]
    losses = [t for t in sub_trades if t['net_pnl'] < 0]
    r_list = []
    for t in sub_trades:
        rp = t.get('risk_points') or 0
        if rp > 0 and t.get('direction') == 'long':
            r_list.append((t['exit_price_fill'] - t['entry_price_fill']) / rp)
        elif rp > 0 and t.get('direction') == 'short':
            r_list.append((t['entry_price_fill'] - t['exit_price_fill']) / rp)
        else:
            r_list.append(0.0)
    return {
        "count": len(sub_trades),
        "wins": len(wins),
        "losses": len(losses),
        "win_rate": len(wins) / len(sub_trades),
        "gross_pnl": sum(t['gross_pnl'] for t in sub_trades),
        "net_pnl": sum(t['net_pnl'] for t in sub_trades),
        "costs": sum(t.get('costs_total') or 0 for t in sub_trades),
        "avg_r": sum(r_list) / len(r_list) if r_list else 0.0,
        "expectancy_usd": sum(t['net_pnl'] for t in sub_trades) / len(sub_trades),
        "profit_factor": (sum(t['net_pnl'] for t in sub_trades if t['net_pnl'] > 0)
                          / abs(sum(t['net_pnl'] for t in sub_trades if t['net_pnl'] < 0))
                          if sum(t['net_pnl'] for t in sub_trades if t['net_pnl'] < 0) < 0 else float('inf')),
        "long_trades": len([t for t in sub_trades if t['direction'] == 'long']),
        "short_trades": len([t for t in sub_trades if t['direction'] == 'short']),
        "avg_win_r": (sum(r for r, t in zip(r_list, sub_trades) if t['net_pnl'] > 0) / len(wins)) if wins else 0.0,
        "avg_loss_r": (abs(sum(r for r, t in zip(r_list, sub_trades) if t['net_pnl'] < 0)) / len(losses)) if losses else 0.0,
        "avg_win_usd": (sum(t['net_pnl'] for t in wins) / len(wins)) if wins else 0.0,
        "avg_loss_usd": (abs(sum(t['net_pnl'] for t in losses) / len(losses))) if losses else 0.0,
    }


def compute_metrics(trades):
    metrics = {}
    metrics['trade_count'] = len(trades)
    completed = [t for t in trades if t.get('net_pnl') is not None]
    metrics['completed_trades'] = len(completed)
    if len(completed) == 0:
        return metrics
    metrics.update(_summarize(completed))

    # Long/short split: full metric set per direction (pooled metrics above are
    # not sufficient on their own; AGENTS.md requires long/short splits).
    long_trades = [t for t in completed if t.get('direction') == 'long']
    short_trades = [t for t in completed if t.get('direction') == 'short']
    metrics['long_short_split'] = {
        'long': _summarize(long_trades),
        'short': _summarize(short_trades),
    }

    # max drawdown
    equity = 0.0
    peak = 0.0
    max_dd = 0.0
    for t in completed:
        equity += t['net_pnl']
        if equity > peak:
            peak = equity
        dd = peak - equity
        if dd > max_dd:
            max_dd = dd
    metrics['max_drawdown_usd'] = max_dd

    # Chronological train/val/test splits (60/20/20 by trade order).
    n = len(completed)
    if n >= 30:
        n_train = int(n * 0.6)
        n_val = int(n * 0.2)
        train = completed[:n_train]
        val = completed[n_train:n_train + n_val]
        test = completed[n_train + n_val:]
        metrics['chronological_splits'] = {
            "train": _summarize(train),
            "val": _summarize(val),
            "test": _summarize(test),
            "train_long_short": _summarize([t for t in train if t.get('direction') == 'long']),
            "train_short_short": _summarize([t for t in train if t.get('direction') == 'short']),
            "val_long_short": _summarize([t for t in val if t.get('direction') == 'long']),
            "val_short_short": _summarize([t for t in val if t.get('direction') == 'short']),
            "test_long_short": _summarize([t for t in test if t.get('direction') == 'long']),
            "test_short_short": _summarize([t for t in test if t.get('direction') == 'short']),
            "date_range": {
                "start": str(min(t['date'] for t in completed)),
                "end": str(max(t['date'] for t in completed)),
                "n_days": len({t['date'] for t in completed}),
            },
        }

    # Return frequency for annualization: one trade per day at most, so use
    # trading-day frequency. CAGR uses the calendar span of the sample.
    trade_dates = sorted({t['date'] for t in completed})
    if len(trade_dates) >= 2:
        start_d = pd.to_datetime(min(trade_dates))
        end_d = pd.to_datetime(max(trade_dates))
        years = max((end_d - start_d).days / 365.25, 1e-6)
        # Final equity relative to a $1 starting capital (capital convention: $1)
        final_equity = 1.0 + (sum(t['net_pnl'] for t in completed) / 10000.0)
        if final_equity > 0:
            metrics['cagr'] = (final_equity ** (1.0 / years)) - 1.0
        else:
            metrics['cagr'] = None
        metrics['capital_convention'] = 'synthetic $10,000 starting capital; CAGR = (final/initial)^(1/years)-1 on net P&L'
        metrics['years_covered'] = years
    else:
        metrics['cagr'] = None
        metrics['capital_convention'] = 'insufficient date span'

    # Sharpe / Sortino on per-trade returns (trade-frequency annualization).
    # Annualization factor: trades per year ≈ 252 trading days / avg trades per day.
    # With max 1 trade/day this is ~252; report the factor used.
    r_list_all = []
    for t in completed:
        rp = t.get('risk_points') or 0
        if rp > 0 and t.get('direction') == 'long':
            r_list_all.append((t['exit_price_fill'] - t['entry_price_fill']) / rp)
        elif rp > 0 and t.get('direction') == 'short':
            r_list_all.append((t['entry_price_fill'] - t['exit_price_fill']) / rp)
        else:
            r_list_all.append(0.0)
    if len(r_list_all) >= 2:
        mean_r = sum(r_list_all) / len(r_list_all)
        var_r = sum((r - mean_r) ** 2 for r in r_list_all) / (len(r_list_all) - 1)
        std_r = var_r ** 0.5
        if std_r > 0:
            metrics['sharpe_r'] = (mean_r / std_r) * (252.0 ** 0.5)
        else:
            metrics['sharpe_r'] = None
        downside = [r for r in r_list_all if r < 0]
        if len(downside) >= 1:
            dd_var = sum((r - 0.0) ** 2 for r in downside) / len(downside)
            dd_std = dd_var ** 0.5
            metrics['sortino_r'] = (mean_r / dd_std) * (252.0 ** 0.5) if dd_std > 0 else None
        else:
            metrics['sortino_r'] = None
        metrics['sharpe_sortino_note'] = (
            'annualized from per-trade R returns with factor sqrt(252); '
            'return frequency = per completed trade (max 1/day)'
        )
    else:
        metrics['sharpe_r'] = None
        metrics['sortino_r'] = None

    # Worst day (largest single-day net loss) and best day
    by_day = {}
    for t in completed:
        by_day[t['date']] = by_day.get(t['date'], 0.0) + (t['net_pnl'] or 0.0)
    if by_day:
        metrics['worst_day_usd'] = min(by_day.values())
        metrics['best_day_usd'] = max(by_day.values())
        metrics['worst_day_date'] = min(by_day, key=by_day.get)
        metrics['best_day_date'] = max(by_day, key=by_day.get)

    # Monthly / yearly breakdown
    monthly = {}
    yearly = {}
    for t in completed:
        m = str(t['date'])[:7]
        y = str(t['date'])[:4]
        monthly[m] = monthly.get(m, 0.0) + (t['net_pnl'] or 0.0)
        yearly[y] = yearly.get(y, 0.0) + (t['net_pnl'] or 0.0)
    metrics['monthly_net_pnl'] = dict(sorted(monthly.items()))
    metrics['yearly_net_pnl'] = dict(sorted(yearly.items()))

    # Exposure / time in market: count bars held per trade relative to day length.
    exposure_bars = 0
    total_bars = 0
    for t in completed:
        try:
            entry_dt = pd.Timestamp(t['entry_bar_time'])
            exit_dt = pd.Timestamp(t['exit_time']) if t.get('exit_time') else entry_dt
            held = max((exit_dt - entry_dt).total_seconds() / 900.0, 0.0)  # 15-min bar units
            exposure_bars += held
            total_bars += 27.0  # 09:30-16:00 ET = 27 fifteen-minute bars
        except Exception:
            continue
    if total_bars > 0:
        metrics['exposure_pct'] = (exposure_bars / total_bars) * 100.0
    else:
        metrics['exposure_pct'] = None
    metrics['exposure_note'] = 'bars held / 27 possible 15-min bars per session (09:30-16:00 ET)'

    # Cost sensitivity: vary slippage multiplier and commission+fee multiplier.
    # Slippage is embedded in the fill prices, so recompute gross PnL from the
    # stored raw entry/exit prices for each slippage scenario.
    tick = 0.25
    base_slip = 1.0
    base_cost = 1.0
    sensitivity = []
    for slip_mult in [0.5, 1.0, 1.5, 2.0]:
        for cost_mult in [0.8, 1.0, 1.2]:
            net = 0.0
            for t in completed:
                if t.get('exit_price') is None:
                    continue
                slip = slip_mult * tick
                if t['direction'] == 'long':
                    entry_fill = t['entry_price_raw'] + slip
                    exit_fill = t['exit_price'] - slip
                    gross = (exit_fill - entry_fill) * 2.0 * t['contracts']
                else:
                    entry_fill = t['entry_price_raw'] - slip
                    exit_fill = t['exit_price'] + slip
                    gross = (entry_fill - exit_fill) * 2.0 * t['contracts']
                per_side_cost = (t['costs_total'] / (t['contracts'] * 2.0)) if t['contracts'] else 0.0
                new_cost = per_side_cost * cost_mult
                net += gross - new_cost * t['contracts'] * 2.0
            sensitivity.append({
                "slip_mult": slip_mult,
                "cost_mult": cost_mult,
                "net_pnl": net,
            })
    metrics['cost_sensitivity'] = sensitivity

    # Signal-close entry sensitivity (separate scenario only, never mixed with primary).
    # Primary uses next-bar-open; this recomputes using the breakout bar's close as the fill.
    signal_close = []
    for slip_mult in [0.5, 1.0, 1.5, 2.0]:
        net = 0.0
        gross = 0.0
        for t in completed:
            if t.get('exit_price') is None:
                continue
            slip = slip_mult * tick
            entry_raw = t['entry_price_raw']  # this is the next-bar open in primary mode
            # Signal-close scenario: fill at the breakout bar close instead.
            sc_entry = t.get('breakout_close')
            if sc_entry is None:
                continue
            if t['direction'] == 'long':
                entry_fill = sc_entry + slip
                exit_fill = t['exit_price'] - slip
                g = (exit_fill - entry_fill) * 2.0 * t['contracts']
            else:
                entry_fill = sc_entry - slip
                exit_fill = t['exit_price'] + slip
                g = (entry_fill - exit_fill) * 2.0 * t['contracts']
            gross += g
            per_side_cost = (t['costs_total'] / (t['contracts'] * 2.0)) if t['contracts'] else 0.0
            net += g - per_side_cost * t['contracts'] * 2.0
        signal_close.append({"slip_mult": slip_mult, "gross_pnl": gross, "net_pnl": net})
    metrics['signal_close_entry_sensitivity'] = signal_close
    metrics['signal_close_note'] = (
        'Separate sensitivity only: fills at breakout-bar close instead of next-bar open. '
        'Not used for primary results.'
    )

    return metrics


def _resolve_paths(source: str):
    """Map a named data source to its 15min/1min CSV paths.

    Sources are explicit so a run can never silently use the wrong dataset.
    """
    if source == "axb0306":
        return ("raw/MNQ_15min.csv", "raw/MNQ_1min.csv")
    if source == "kaggle":
        return ("raw/MNQ_15min_frontmonth.csv", "raw/MNQ_1min_frontmonth.csv")
    raise ValueError(f"Unknown source '{source}'. Use 'axb0306' or 'kaggle'.")


def main():
    parser = argparse.ArgumentParser(description="Run NQ ORB backtest")
    parser.add_argument("--prefix", default="full", help="output filename prefix")
    parser.add_argument("--source", default="axb0306",
                        choices=["axb0306", "kaggle"],
                        help="data source to run on (default: axb0306)")
    args = parser.parse_args()

    loader = DataLoader(data_dir="data")

    p15, p1m = _resolve_paths(args.source)
    for p in (p15, p1m):
        if not os.path.exists(p):
            print(f"Missing required data file: {p}")
            sys.exit(1)

    df15 = loader.load_csv(p15)
    print(f"Loaded 15min from {p15} ({len(df15)} rows)")
    df1m = loader.load_csv(p1m)
    print(f"Loaded 1min from {p1m} ({len(df1m)} rows)")

    df15 = loader.to_et(df15)
    if df1m is not None:
        df1m = loader.to_et(df1m)

    config = ORBConfig()
    engine = BacktestEngine(config)
    trades = engine.run(df15, df1m)

    print(f"\nFound {len(trades)} trades")
    for t in trades[:5]:
        print(f"{t['date']} {t['direction']} entry_fill={t['entry_price_fill']:.2f} stop={t['stop_price']:.2f} target={t['target_price']:.2f} exit_reason={t.get('exit_reason')} net={t.get('net_pnl')}")

    metrics = compute_metrics(trades)
    metrics['data_source'] = args.source
    metrics['data_file_15m'] = p15
    metrics['data_file_1m'] = p1m
    print("\n=== METRICS ===")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    os.makedirs('artifacts', exist_ok=True)
    with open(f'artifacts/trades_{args.prefix}.json', 'w') as f:
        json.dump(trades, f, indent=2, default=str)
    with open(f'artifacts/metrics_{args.prefix}.json', 'w') as f:
        json.dump(metrics, f, indent=2, default=str)
    print(f"\nSaved to artifacts/trades_{args.prefix}.json and artifacts/metrics_{args.prefix}.json")


if __name__ == '__main__':
    main()