#!/usr/bin/env python3
"""Walk-forward evaluation of the frozen MNQ ORB baseline.

Splits the trade ledger chronologically (by trade index) into rolling
train/test windows and reports per-window metrics. This is a *reporting*
layer over the frozen engine output; it does not change any strategy rule,
parameter, or the canonical artifacts.

Usage:
    python3 scripts/walk_forward.py --source kaggle [--window-trades 150]
                                    [--step-trades 50] [--out artifacts/walk_forward.json]

The final test window is preserved untouched (no parameter fitting against it).
"""
import argparse
import json
import os
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from orb.runner import compute_metrics, _summarize


def load_trades(path):
    with open(path) as f:
        return json.load(f)


def walk_forward(trades, window_trades, step_trades):
    """Yield (train_start_idx, train_end_idx, test_start_idx, test_end_idx)."""
    n = len(trades)
    if n < window_trades * 2:
        return
    test_start = window_trades
    while test_start + window_trades <= n:
        train_end = test_start
        test_end = test_start + window_trades
        yield (0, train_end, test_start, test_end)
        test_start += step_trades


def main():
    parser = argparse.ArgumentParser(description="Walk-forward evaluation")
    parser.add_argument("--source", default="kaggle", choices=["axb0306", "kaggle", "getdata"])
    parser.add_argument("--window-trades", type=int, default=150)
    parser.add_argument("--step-trades", type=int, default=50)
    parser.add_argument("--out", default="artifacts/walk_forward.json")
    args = parser.parse_args()

    trades_path = f"artifacts/trades_{args.source}.json"
    if not os.path.exists(trades_path):
        print(f"Missing trades file: {trades_path}")
        sys.exit(1)

    trades = load_trades(trades_path)
    completed = [t for t in trades if t.get('net_pnl') is not None]
    completed.sort(key=lambda t: (t['date'], t.get('breakout_bar_time', '')))

    windows = list(walk_forward(completed, args.window_trades, args.step_trades))
    if not windows:
        print(f"Not enough trades ({len(completed)}) for window={args.window_trades}")
        sys.exit(1)

    results = []
    for (tr_s, tr_e, te_s, te_e) in windows:
        train = completed[tr_s:tr_e]
        test = completed[te_s:te_e]
        train_m = _summarize(train)
        test_m = _summarize(test)
        results.append({
            "train_window": [tr_s, tr_e],
            "test_window": [te_s, te_e],
            "train": {k: train_m[k] for k in ('count', 'win_rate', 'net_pnl', 'gross_pnl', 'profit_factor') if k in train_m},
            "test": {k: test_m[k] for k in ('count', 'win_rate', 'net_pnl', 'gross_pnl', 'profit_factor') if k in test_m},
            "test_dates": {
                "start": str(min(t['date'] for t in test)),
                "end": str(max(t['date'] for t in test)),
            },
        })

    out = {
        "source": args.source,
        "total_trades": len(completed),
        "window_trades": args.window_trades,
        "step_trades": args.step_trades,
        "n_windows": len(results),
        "windows": results,
        "note": (
            "Chronological rolling train/test split by trade index. "
            "The final test window is untouched by any parameter selection. "
            "No strategy or parameter changes were made; this reports the "
            "frozen baseline only."
        ),
    }

    os.makedirs(os.path.dirname(args.out) or '.', exist_ok=True)
    with open(args.out, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"Wrote {len(results)} walk-forward windows to {args.out}")
    for r in results:
        print(f"  train[{r['train_window'][0]}:{r['train_window'][1]}] "
              f"-> test[{r['test_window'][0]}:{r['test_window'][1]}] "
              f"test net=${r['test']['net_pnl']:.2f} "
              f"({r['test_dates']['start']}..{r['test_dates']['end']})")


if __name__ == "__main__":
    main()