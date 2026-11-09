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


def _date_bounds(trades):
    """Return (min_date, max_date) over the completed ledger."""
    return min(t['date'] for t in trades), max(t['date'] for t in trades)


def walk_forward_date_60_20_20(trades, min_train_days=30):
    """Yield a single date-based chronological 60/20/20 split.

    The trade ledger is bucketed by trading DATE (never shuffled) into three
    contiguous windows: train (60%), validation (20%), test (20%). The final
    test window is untouched by any parameter selection. Windows are derived
    from the distinct trading dates present in the ledger, so the split is
    stable regardless of how many trades fall on any single date.

    Yields exactly one tuple: (train_trades, val_trades, test_trades,
    {train_dates, val_dates, test_dates, n_days}).
    """
    dates = sorted({t['date'] for t in trades})
    n = len(dates)
    if n < 30:
        return
    n_train = max(int(round(n * 0.6)), min_train_days)
    n_val = int(round(n * 0.2))
    n_test = n - n_train - n_val
    if n_test < 1:
        return
    train_dates = set(dates[:n_train])
    val_dates = set(dates[n_train:n_train + n_val])
    test_dates = set(dates[n_train + n_val:])
    train = [t for t in trades if t['date'] in train_dates]
    val = [t for t in trades if t['date'] in val_dates]
    test = [t for t in trades if t['date'] in test_dates]
    yield (train, val, test, {
        "train_dates": [str(d) for d in dates[:n_train]],
        "val_dates": [str(d) for d in dates[n_train:n_train + n_val]],
        "test_dates": [str(d) for d in dates[n_train + n_val:]],
        "n_days": n,
        "train_days": n_train,
        "val_days": n_val,
        "test_days": n_test,
    })


def main():
    parser = argparse.ArgumentParser(description="Walk-forward evaluation")
    parser.add_argument("--source", default="kaggle", choices=["axb0306", "kaggle", "getdata"])
    parser.add_argument("--window-trades", type=int, default=150)
    parser.add_argument("--step-trades", type=int, default=50)
    parser.add_argument("--method", default="rolling_trade_index",
                        choices=["rolling_trade_index", "date_60_20_20"],
                        help="rolling_trade_index = existing rolling windows; "
                             "date_60_20_20 = single date-based 60/20/20 split "
                             "with final test untouched.")
    parser.add_argument("--min-train-days", type=int, default=30)
    parser.add_argument("--out", default="artifacts/walk_forward.json")
    args = parser.parse_args()

    trades_path = f"artifacts/trades_{args.source}.json"
    if not os.path.exists(trades_path):
        print(f"Missing trades file: {trades_path}")
        sys.exit(1)

    trades = load_trades(trades_path)
    completed = [t for t in trades if t.get('net_pnl') is not None]
    completed.sort(key=lambda t: (t['date'], t.get('breakout_bar_time', '')))

    if args.method == "date_60_20_20":
        windows = list(walk_forward_date_60_20_20(completed, args.min_train_days))
        if not windows:
            print(f"Not enough trading dates ({len({t['date'] for t in completed})}) "
                  f"for date-based 60/20/20 (need >= 30)")
            sys.exit(1)
        (train, val, test, date_meta) = windows[0]
        train_m = _summarize(train)
        val_m = _summarize(val)
        test_m = _summarize(test)
        results = [{
            "train_window": [0, len(train)],
            "val_window": [len(train), len(train) + len(val)],
            "test_window": [len(train) + len(val), len(train) + len(val) + len(test)],
            "train": {k: train_m[k] for k in ('count', 'win_rate', 'net_pnl', 'gross_pnl', 'profit_factor') if k in train_m},
            "val": {k: val_m[k] for k in ('count', 'win_rate', 'net_pnl', 'gross_pnl', 'profit_factor') if k in val_m},
            "test": {k: test_m[k] for k in ('count', 'win_rate', 'net_pnl', 'gross_pnl', 'profit_factor') if k in test_m},
            "test_dates": {"start": date_meta["test_dates"][0], "end": date_meta["test_dates"][-1]},
            "val_dates": {"start": date_meta["val_dates"][0], "end": date_meta["val_dates"][-1]},
            "train_dates": {"start": date_meta["train_dates"][0], "end": date_meta["train_dates"][-1]},
            "date_meta": date_meta,
        }]

        out = {
            "source": args.source,
            "method": "date_based_chronological_60_20_20",
            "total_trades": len(completed),
            "n_days": date_meta["n_days"],
            "train_days": date_meta["train_days"],
            "val_days": date_meta["val_days"],
            "test_days": date_meta["test_days"],
            "n_windows": len(results),
            "windows": results,
            "note": (
                "Chronological date-based 60/20/20 split of the trade ledger. "
                "Windows are contiguous by trading DATE (never shuffled). The "
                "final test window is untouched by any parameter selection and "
                "is re-derived from the raw trade ledger on every run. No "
                "strategy or parameter changes were made; this reports the "
                "frozen baseline only."
            ),
        }
    else:
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
    print(f"Wrote {len(results)} walk-forward window(s) to {args.out}")
    for r in results:
        print(f"  train[{r['train_window'][0]}:{r['train_window'][1]}] "
              f"-> test[{r['test_window'][0]}:{r['test_window'][1]}] "
              f"test net=${r['test']['net_pnl']:.2f} "
              f"({r['test_dates']['start']}..{r['test_dates']['end']})")


if __name__ == "__main__":
    main()