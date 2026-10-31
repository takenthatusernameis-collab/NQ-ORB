#!/usr/bin/env python3
"""Run ORB backtest on downloaded data."""
import argparse
import json
import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from orb.data_loader import DataLoader
from orb.backtest import BacktestEngine
from orb.orb_logic import ORBConfig


def compute_metrics(trades):
    metrics = {}
    metrics['trade_count'] = len(trades)
    completed = [t for t in trades if t.get('net_pnl') is not None]
    metrics['completed_trades'] = len(completed)
    if len(completed) == 0:
        return metrics
    wins = [t for t in completed if t['net_pnl'] > 0]
    losses = [t for t in completed if t['net_pnl'] < 0]
    breakeven = [t for t in completed if t['net_pnl'] == 0]
    metrics['wins'] = len(wins)
    metrics['losses'] = len(losses)
    metrics['breakeven'] = len(breakeven)
    metrics['win_rate'] = len(wins) / len(completed)
    gross = sum(t['gross_pnl'] for t in completed)
    net = sum(t['net_pnl'] for t in completed)
    costs = sum(t.get('costs_total') or 0 for t in completed)
    metrics['gross_pnl'] = gross
    metrics['net_pnl'] = net
    metrics['total_costs'] = costs
    # R multiples
    r_list = []
    for t in completed:
        rp = t.get('risk_points') or 0
        if rp > 0 and t.get('direction') == 'long':
            r = (t['exit_price_fill'] - t['entry_price_fill']) / rp
        elif rp > 0 and t.get('direction') == 'short':
            r = (t['entry_price_fill'] - t['exit_price_fill']) / rp
        else:
            r = 0
        r_list.append(r)
    metrics['avg_r'] = sum(r_list) / len(r_list) if r_list else 0
    metrics['avg_win_r'] = sum(r for r in r_list if r > 0) / len([r for r in r_list if r > 0]) if len([r for r in r_list if r > 0]) > 0 else 0
    metrics['avg_loss_r'] = sum(r for r in r_list if r < 0) / len([r for r in r_list if r < 0]) if len([r for r in r_list if r < 0]) > 0 else 0
    metrics['expectancy_r'] = metrics['avg_r']
    metrics['expectancy_usd'] = sum(t['net_pnl'] for t in completed) / len(completed)
    # profit factor
    sum_wins = sum(t['net_pnl'] for t in completed if t['net_pnl'] > 0)
    sum_losses = abs(sum(t['net_pnl'] for t in completed if t['net_pnl'] < 0))
    metrics['profit_factor'] = sum_wins / sum_losses if sum_losses > 0 else float('inf')
    # max dd (simple)
    equity = 0
    max_dd = 0
    peak = 0
    for t in completed:
        equity += t['net_pnl']
        if equity > peak:
            peak = equity
        dd = peak - equity
        if dd > max_dd:
            max_dd = dd
    metrics['max_drawdown_usd'] = max_dd
    # long/short
    long_t = [t for t in completed if t['direction'] == 'long']
    short_t = [t for t in completed if t['direction'] == 'short']
    metrics['long_trades'] = len(long_t)
    metrics['short_trades'] = len(short_t)
    if long_t:
        metrics['long_net_pnl'] = sum(t['net_pnl'] for t in long_t)
    if short_t:
        metrics['short_net_pnl'] = sum(t['net_pnl'] for t in short_t)
    return metrics


def main():
    parser = argparse.ArgumentParser(description="Run NQ ORB backtest")
    parser.add_argument("--prefix", default="full", help="output filename prefix")
    args = parser.parse_args()

    loader = DataLoader(data_dir="data")

    mnq_15m_paths = [
        "raw/MNQ_15min_frontmonth.csv",  # Kaggle front-month, 2022-11..2025-11
        "raw/MNQ_15min.csv",             # axb0306 sample, 2026-01..2026-04
        "data/MNQ_15min.csv",
        "../raw/MNQ_15min.csv",
    ]

    mnq_1m_paths = [
        "raw/MNQ_1min_frontmonth.csv",   # Kaggle front-month, 2022-11..2025-11
        "raw/MNQ_1min.csv",              # axb0306 sample, 2026-01..2026-04
        "data/MNQ_1min.csv",
    ]

    df15 = None
    df1m = None

    for p in mnq_15m_paths:
        if os.path.exists(p):
            print(f"Loading 15min from {p}")
            df15 = loader.load_csv(p)
            break

    for p in mnq_1m_paths:
        if os.path.exists(p):
            print(f"Loading 1min from {p}")
            df1m = loader.load_csv(p)
            break

    if df15 is None:
        print("No 15min data found. Run data download first.")
        sys.exit(1)

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