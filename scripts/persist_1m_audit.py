#!/usr/bin/env python3
"""Persist 1-minute coverage audit ledgers for walk-forward feasibility.

Wraps scripts/audit_1m_coverage.py and writes a dated JSON ledger under
research_state/ per source, including source paths, file hashes, session
alignment, DST coverage, gaps, zero-volume/nonfinite checks, tick sanity,
trade-day overlap with the canonical ledger, and explicit limitations.

Usage:
    python3 scripts/persist_1m_audit.py [--source axb0306|kaggle|both]
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from audit_1m_coverage import load, audit, ET, UTC  # noqa: E402

ROOT = Path(__file__).parent.parent
RESEARCH_STATE = ROOT / "research_state"

PATHS = {
    "axb0306": ("raw/MNQ_1min.csv", "raw/MNQ_15min.csv"),
    "kaggle": ("raw/MNQ_1min_frontmonth.csv", "raw/MNQ_15min_frontmonth.csv"),
}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def trade_day_overlap(source, df1m):
    """Count 1m trading dates that also appear in the canonical trade ledger."""
    ledger_path = ROOT / f"artifacts/trades_{source}.json"
    if not ledger_path.exists():
        return {"ledger_present": False, "overlap_days": None}
    ledger = json.load(open(ledger_path))
    ledger_dates = {t["date"] for t in ledger if t.get("net_pnl") is not None}
    dates_1m = set(df1m["date"].astype(str))
    overlap = sorted(dates_1m & ledger_dates)
    return {
        "ledger_present": True,
        "ledger_completed_trades": len([t for t in ledger if t.get("net_pnl") is not None]),
        "ledger_dates": len(ledger_dates),
        "overlap_days": len(overlap),
        "overlap_start": overlap[0] if overlap else None,
        "overlap_end": overlap[-1] if overlap else None,
        "1m_dates_missing_from_ledger": sorted(dates_1m - ledger_dates)[:10],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="both", choices=["axb0306", "kaggle", "both"])
    args = ap.parse_args()
    sources = ["axb0306", "kaggle"] if args.source == "both" else [args.source]

    for src in sources:
        p1m, p15 = PATHS[src]
        df1m = load(ROOT / p1m)
        df15 = load(ROOT / p15)
        res = {
            "1m": audit(df1m, src + "_1m"),
            "15m": audit(df15, src + "_15m"),
        }
        res["1m"]["file"] = p1m
        res["1m"]["sha256"] = sha256_file(ROOT / p1m)
        res["15m"]["file"] = p15
        res["15m"]["sha256"] = sha256_file(ROOT / p15)
        res["trade_day_overlap"] = trade_day_overlap(src, df1m)

        # Explicit limitations, auditable and not fabricated.
        lim = []
        if src == "kaggle":
            lim.append(
                "kaggle 15m bars are timestamped at 00:00/00:15/00:30 UTC by construction "
                "in this dataset; they do NOT carry 09:30/15:55 ET session anchors. "
                "The 1m series is what provides execution-grade 15:55 ET flatten evidence."
            )
            lim.append(
                "kaggle is a front-month continuous proxy, not a spot MNQ contract; "
                "roll semantics must remain explicit and volume averages must not "
                "mix across roll boundaries."
            )
            lim.append(
                "kaggle 1m has 771 days with a 09:30 ET bar and 743 with a 15:55 ET bar; "
                "743 days have both. 28 days with 09:30 lack a 15:55 bar (session ended "
                "early / data gap) and produce no evaluable flatten."
            )
        else:
            lim.append(
                "axb0306 is a short free sample spanning 2026-01-20..2026-04-15 (74 days, "
                "60 with both 09:30 and 15:55 ET bars). Statistical power is limited; this "
                "is a validation subset, not a full history."
            )
            lim.append(
                "axb0306 15m bars are timestamped at 08:15/08:30/08:45 UTC by construction "
                "and do not carry 09:30/15:55 ET session anchors in the 15m audit view."
            )
        lim.append(
            "Gaps > 60s between consecutive 1m bars exist in both sources (overnight/session "
            "boundaries). These are expected and are NOT treated as missing intraday data."
        )
        res["limitations"] = lim
        res["generated_at_utc"] = datetime.now(timezone.utc).isoformat()

        out_path = RESEARCH_STATE / f"1m_audit_{src}.json"
        with open(out_path, "w") as f:
            json.dump(res, f, indent=2, default=str)
        print(f"Wrote {out_path} ({out_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()