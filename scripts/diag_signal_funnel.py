#!/usr/bin/env python3
"""Diagnostic: signal funnel on the Kaggle front-month 15m series.

Counts, per trading day:
  - days with an OR built
  - days with a first close-beyond-range breakout (long or short)
  - of those, how many pass RVOL>=1.0 and 0.10%<=ATR%<=0.60%
  - of those, how many pass the entry-cutoff (breakout bar < 15:00 ET)
  - of those, how many pass sizing (>=1 contract)
  - of those, how many pass the next-bar-open entry availability

This is read-only analysis; it does not change the frozen baseline.
"""
import sys
from pathlib import Path

import pandas as pd
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from orb.data_loader import DataLoader
from orb.indicators import wilder_atr
from orb.orb_logic import ORBConfig

ET = ZoneInfo("America/New_York")


def main():
    loader = DataLoader()
    df15 = loader.load_csv("raw/MNQ_15min_frontmonth.csv")
    df15 = loader.to_et(df15)
    cfg = ORBConfig()
    df15["atr14"] = wilder_atr(df15, cfg.atr_length)
    df15["atr_pct"] = (df15["atr14"] / df15["close"]) * 100.0

    dates = sorted(df15["date"].unique())
    n_or = n_break = n_filt = n_cutoff = n_size = n_entry = 0
    no_or_days = 0
    for d in dates:
        day = df15[df15["date"] == d].sort_values("datetime_et")
        or_bars = day[(day["time_et"] >= cfg.or_start) & (day["time_et"] < cfg.or_end)]
        if len(or_bars) == 0:
            no_or_days += 1
            continue
        n_or += 1
        or_high = or_bars["high"].max()
        or_low = or_bars["low"].min()
        post = day[day["time_et"] >= cfg.or_end]
        hit = False
        for _, bar in post.iterrows():
            if bar["time_et"] >= cfg.no_new_entry_after:
                break
            long_b = bar["close"] > or_high
            short_b = bar["close"] < or_low
            if not (long_b or short_b):
                continue
            n_break += 1
            hit = True
            prev = df15[df15["datetime_et"] < bar["datetime_et"]]
            p20 = prev.tail(cfg.rvol_lookback)
            if len(p20) < cfg.rvol_lookback:
                break
            avgv = p20["volume"].mean()
            rvol = bar["volume"] / avgv if avgv > 0 else 0.0
            atrp = bar["atr_pct"]
            if pd.isna(atrp):
                break
            ok = (rvol >= cfg.rvol_min) and (cfg.atr_min_pct <= atrp <= cfg.atr_max_pct)
            if not ok:
                break
            n_filt += 1
            # cutoff already enforced by loop break above
            n_cutoff += 1
            atr = bar["atr14"]
            if pd.isna(atrp) or pd.isna(atr):
                break
            if long_b:
                stop = bar["close"] - cfg.stop_atr_mult * atr
                risk = bar["close"] - stop
            else:
                stop = bar["close"] + cfg.stop_atr_mult * atr
                risk = stop - bar["close"]
            if risk <= 0:
                break
            contracts = int(cfg.risk_usd / (risk * cfg.mnq_multiplier))
            if contracts < 1:
                break
            n_size += 1
            nxt = df15[df15["datetime_et"] > bar["datetime_et"]]
            if len(nxt) == 0:
                break
            n_entry += 1
            break  # first breakout only
        # else: no breakout today

    print(f"trading dates: {len(dates)}")
    print(f"dates with OR built: {n_or} (no OR: {no_or_days})")
    print(f"dates with first breakout: {n_break}")
    print(f"  pass filters (RVOL+ATR): {n_filt}")
    print(f"  pass cutoff (<15:00): {n_cutoff}")
    print(f"  pass sizing (>=1 contract): {n_size}")
    print(f"  have next-bar open entry: {n_entry}")
    print(f"  => trade count (from runner): {n_entry}")


if __name__ == "__main__":
    main()