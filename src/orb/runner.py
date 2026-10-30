#!/usr/bin/env python3
"""Run ORB backtest on downloaded data."""
import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from orb.data_loader import DataLoader
from orb.backtest import BacktestEngine
from orb.orb_logic import ORBConfig

def main():
    loader = DataLoader(data_dir="data")

    # Try to load from common locations
    mnq_15m_paths = [
        "raw/MNQ_15min.csv",
        "data/MNQ_15min.csv",
        "../raw/MNQ_15min.csv",
    ]

    mnq_1m_paths = [
        "raw/MNQ_1min.csv",
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
    for t in trades[:10]:
        print(f"{t['date']} {t['direction']} entry={t['entry_price']:.2f} stop={t['stop_price']:.2f} target={t['target_price']:.2f} rvol={t['rvol']:.2f} atr%={t['atr_pct']:.3f} contracts={t['contracts']}")

    # Save trades
    import json
    os.makedirs('artifacts', exist_ok=True)
    with open('artifacts/trades_baseline.json', 'w') as f:
        json.dump(trades, f, indent=2, default=str)
    print("\nSaved to artifacts/trades_baseline.json")

if __name__ == '__main__':
    main()
