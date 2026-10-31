#!/usr/bin/env python3
"""Build a front-month MNQ continuous series from the Kaggle GLBX MDP3 OHLCV dump.

Source: brandenmorris/mnq-1-minute-data-5132025-11122025 (Databento GLBX.MDP3,
ohlcv-1m schema, symbol MNQ.FUT, stype_in=parent). Raw data is per-contract
instrument_id with no roll adjustment, so we construct the front month by
selecting, per calendar date, the contract with the largest daily volume.
Front-month dominance is 100% on every date in the sample (verified), so the
selection is unambiguous.

Outputs (UTC timestamps, datetime,open,high,low,close,volume):
  raw/MNQ_1min_frontmonth.csv   - front-month 1-minute bars
  raw/MNQ_15min_frontmonth.csv  - front-month 15-minute bars (built by
                                  aggregating the 1-minute front-month bars)

No roll adjustment is applied: prices are actual traded prices, which matches
the STRATEGY_RULES.txt requirement that back-adjusted prices must not be
treated as executable fills.
"""
import hashlib
import os
import sys
from pathlib import Path

import pandas as pd
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = Path(
    "/home/runner/work/_temp/kilo-home/.cache/kagglehub/datasets/"
    "brandenmorris/mnq-1-minute-data-5132025-11122025/versions/1/"
    "MNQ_OHLCV_5-13-2025--11-12-2025"
)
SRC_CSV = SRC_DIR / "glbx-mdp3-20221116-20251112.ohlcv-1m.csv"
OUT_DIR = ROOT / "raw"
OUT_DIR.mkdir(exist_ok=True)

UTC = ZoneInfo("UTC")


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    print(f"Loading {SRC_CSV}")
    df = pd.read_csv(SRC_CSV)
    print(f"  rows={len(df)} cols={df.columns.tolist()}")

    df["ts"] = pd.to_datetime(df["ts_event"], utc=True)
    df["date"] = df["ts"].dt.date

    # Per-date front month = contract with max daily volume. Select per date so
    # that a contract active only in early sample dates is not carried forward
    # into later dates where it is no longer the front month.
    daily = df.groupby(["date", "instrument_id"])["volume"].sum().reset_index()
    idx = daily.groupby("date")["volume"].idxmax()
    fm_map = daily.loc[idx, ["date", "instrument_id"]].set_index("date")["instrument_id"]
    print(f"  front-month selection spans {len(fm_map)} dates, "
          f"{fm_map.nunique()} distinct contracts")

    fm = df[df.apply(lambda r: fm_map.get(r["date"]) == r["instrument_id"], axis=1)].copy()
    fm = fm.sort_values("ts").reset_index(drop=True)
    dup = fm["ts"].duplicated().sum()
    print(f"  front-month rows={len(fm)} duplicate timestamps={dup}")

    # Drop any residual duplicate timestamps (keep first).
    fm = fm.drop_duplicates(subset="ts", keep="first")

    out1m = fm[["ts", "open", "high", "low", "close", "volume"]].rename(
        columns={"ts": "datetime"}
    )
    out1m = out1m.sort_values("datetime").reset_index(drop=True)
    out1m["datetime"] = out1m["datetime"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    p1m = OUT_DIR / "MNQ_1min_frontmonth.csv"
    out1m.to_csv(p1m, index=False)
    print(f"Wrote {p1m} rows={len(out1m)} "
          f"range={out1m['datetime'].iloc[0]} -> {out1m['datetime'].iloc[-1]}")

    # Aggregate to 15-minute bars from the 1-minute front-month bars.
    dt = pd.to_datetime(out1m["datetime"], utc=True)
    grp = dt.dt.floor("15min")
    agg = (
        pd.DataFrame({"datetime": grp, "open": out1m["open"],
                      "high": out1m["high"], "low": out1m["low"],
                      "close": out1m["close"], "volume": out1m["volume"]})
        .groupby("datetime")
        .agg({"open": "first", "high": "max", "low": "min",
              "close": "last", "volume": "sum"})
        .reset_index()
        .sort_values("datetime")
    )
    agg["datetime"] = agg["datetime"].dt.strftime("%Y-%m-%dT%H:%M:%S")
    p15 = OUT_DIR / "MNQ_15min_frontmonth.csv"
    agg.to_csv(p15, index=False)
    print(f"Wrote {p15} rows={len(agg)} "
          f"range={agg['datetime'].iloc[0]} -> {agg['datetime'].iloc[-1]}")

    print("\nSHA-256:")
    print(f"  {p1m.name}: {sha256_of(p1m)}")
    print(f"  {p15.name}: {sha256_of(p15)}")
    print(f"  source 1m csv: {sha256_of(SRC_CSV)}")


if __name__ == "__main__":
    main()