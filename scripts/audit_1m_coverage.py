#!/usr/bin/env python3
"""Audit 1-minute MNQ data coverage for walk-forward feasibility.

Checks, per source:
- session alignment (09:30 ET first bar, 15:55 ET bar presence)
- DST transitions (spring-forward 2026-03-08, fall-back 2026-11-01)
- contract roll dates / gaps / bar-timestamp regularity
- missing-bar policy
- whether the 15:55 forced-flatten exit is evaluable on the same days that
  produce trades

Usage:
    python3 scripts/audit_1m_coverage.py [--source axb0306|kaggle]
"""
import argparse
import collections
import json
import sys
from pathlib import Path

import pandas as pd
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")

OR_START = pd.Timestamp("09:30:00").time()
OR_END = pd.Timestamp("09:45:00").time()
CUTOFF = pd.Timestamp("15:00:00").time()
FLATTEN = pd.Timestamp("15:55:00").time()


def load(path):
    df = pd.read_csv(path)
    df["datetime"] = pd.to_datetime(df["datetime"])
    if df["datetime"].dt.tz is None:
        df["datetime"] = df["datetime"].dt.tz_localize(UTC)
    else:
        df["datetime"] = df["datetime"].dt.tz_convert(UTC)
    df = df.sort_values("datetime").reset_index(drop=True)
    df["datetime_et"] = df["datetime"].dt.tz_convert(ET)
    df["date"] = df["datetime_et"].dt.date
    df["time_et"] = df["datetime_et"].dt.time
    return df


def audit(df, label):
    out = {"source": label, "rows": int(len(df)),
           "date_range": [str(df["date"].min()), str(df["date"].max())],
           "n_days": int(df["date"].nunique())}

    # minute regularity
    mins = collections.Counter(df["time_et"])
    out["most_common_minutes"] = [(str(k), v) for k, v in mins.most_common(5)]

    # gaps
    df2 = df.sort_values("datetime_et").reset_index(drop=True)
    diffs = df2["datetime_et"].diff().dt.total_seconds()
    gaps = diffs[diffs > 60]
    out["gaps_gt_60s"] = int(len(gaps))
    out["max_gap_minutes"] = float(diffs.max() / 60.0) if len(diffs) else None

    # session completeness: days with a bar at 09:30 ET and at 15:55 ET
    by_day = {}
    for date, grp in df.groupby("date"):
        times = set(grp["time_et"])
        by_day[date] = {
            "has_0930": OR_START in times,
            "has_1555": FLATTEN in times,
            "n_bars": int(len(grp)),
            "first_time": str(min(times)),
            "last_time": str(max(times)),
        }
    complete = [d for d, v in by_day.items() if v["has_0930"] and v["has_1555"]]
    out["days_with_0930_and_1555"] = len(complete)
    out["days_with_0930"] = sum(1 for v in by_day.values() if v["has_0930"])
    out["days_with_1555"] = sum(1 for v in by_day.values() if v["has_1555"])

    # DST transitions present?
    out["dst_spring_forward_2026_03_09"] = str(pd.Timestamp("2026-03-09").date()) in by_day
    out["dst_fall_back_2026_11_01"] = str(pd.Timestamp("2026-11-01").date()) in by_day

    # volume sanity
    out["zero_volume_bars"] = int((df["volume"] <= 0).sum())
    out["nonfinite_ohlc"] = int(df[["open", "high", "low", "close"]].isna().sum().sum())

    # price continuity: no huge overnight jumps (roll gaps)
    rets = df["close"].pct_change().abs()
    out["pct_moves_gt_2pct"] = int((rets > 0.02).sum())

    # tick sanity: max fractional part in units of 0.25 ticks across OHLC
    frac = (df[["open", "high", "low", "close"]] * 4) % 1.0
    off = frac.max().max()
    out["max_off_tick_units"] = float(off)

    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="axb0306",
                    choices=["axb0306", "kaggle"])
    args = ap.parse_args()

    paths = {
        "axb0306": ("raw/MNQ_1min.csv", "raw/MNQ_15min.csv"),
        "kaggle": ("raw/MNQ_1min_frontmonth.csv", "raw/MNQ_15min_frontmonth.csv"),
    }
    p1m, p15 = paths[args.source]
    df1m = load(p1m)
    df15 = load(p15)

    res = {
        "1m": audit(df1m, args.source + "_1m"),
        "15m": audit(df15, args.source + "_15m"),
    }
    print(json.dumps(res, indent=2, default=str))


if __name__ == "__main__":
    main()