#!/usr/bin/env python3
"""Bounded free-data monitoring for NQ/MNQ 1min/15min full-history sources.

Records provenance evidence for every candidate checked, with the verdict
(genuinely-free full-history extension vs excluded) and the reason.
Used by the maintenance/re-verification loop in HANDOFF.md.

No data is downloaded, purchased, or persisted here. This is a ledger of
candidate checks, not a data acquisition tool.
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from typing import Any


def gh_commit_latest(repo: str, path: str = "") -> dict[str, Any]:
    """Return latest commit metadata for a repo path via GitHub API (unauthenticated).

    Falls back to ``git ls-remote`` (which does not consume REST API rate limit)
    when the unauthenticated API call fails or is rate-limited.
    """
    url = f"https://api.github.com/repos/{repo}/commits?path={path}&per_page=1"
    try:
        out = subprocess.run(
            ["curl", "-s", "--max-time", "20", url],
            check=False, capture_output=True, text=True,
        )
        data = json.loads(out.stdout or "{}")
    except Exception as e:  # noqa: BLE001
        data = {"_parse_error": str(e)}
    if not data:
        return {"ok": False, "error": "empty response"}
    if isinstance(data, dict):
        # GitHub returns a dict with a "message" key on errors (e.g. rate limit)
        return {"ok": False, "error": str(data.get("message", data)),
                "fallback": "git_ls_remote"}
    c = data[0]
    return {
        "ok": True,
        "sha": c["sha"],
        "date": c["commit"]["author"]["date"],
        "message": c["commit"]["message"].splitlines()[0][:80],
    }


def gh_ls_remote_head(repo: str) -> dict[str, Any]:
    """Return HEAD commit SHA for a repo via ``git ls-remote`` (no API rate limit)."""
    try:
        out = subprocess.run(
            ["git", "ls-remote", f"https://github.com/{repo}.git"],
            check=False, capture_output=True, text=True, timeout=30,
        )
        head_sha = ""
        main_sha = ""
        for line in (out.stdout or "").strip().splitlines():
            parts = line.split()
            if len(parts) < 2:
                continue
            sha, ref = parts[0], parts[1]
            if ref == "HEAD":
                head_sha = sha
            elif ref in ("refs/heads/main", "refs/heads/master"):
                main_sha = sha
        sha = head_sha or main_sha
        if sha:
            return {"ok": True, "sha": sha, "method": "git_ls_remote"}
        return {"ok": False, "error": f"no head ref: {out.stderr[:200]}"}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "error": str(e)}


def main() -> int:
    ts = datetime.now(timezone.utc).isoformat()
    evidence: dict[str, Any] = {
        "checked_at_utc": ts,
        "axb0306_cme_futures_ohlc": gh_commit_latest("axb0306/cme-futures-ohlc", "MNQ"),
        "axb0306_head_sha_fallback": gh_ls_remote_head("axb0306/cme-futures-ohlc"),
        "candidates": [
            {
                "name": "axb0306/cme-futures-ohlc",
                "url": "https://github.com/axb0306/cme-futures-ohlc",
                "verdict": "free",
                "note": "Latest MNQ 1min/15min coverage ends 2026-04-15. Re-verified each session; no extension observed.",
            },
            {
                "name": "finzdata",
                "url": "https://finzdata.com/futures/mnq",
                "verdict": "paid",
                "note": "Full MNQ 1min/15min history is $49 one-time; last 30 days daily free. Not a free full-history source.",
            },
            {
                "name": "historicalfuturesdata.com",
                "url": "https://historicalfuturesdata.com/browse/MNQ",
                "verdict": "paid",
                "note": "Annual 1m bars $59/year; only 10s monthly samples + 3 free months require free verified account. Not free full history.",
            },
            {
                "name": "marketparquet",
                "url": "https://marketparquet.com/data/futures/mnq",
                "verdict": "paid",
                "note": "Intraday archive (2007-12-31..) is paid; free tier is daily-only last ~365 days + a sample week.",
            },
            {
                "name": "firstratedata",
                "url": "https://firstratedata.com/i/futures/MNQ",
                "verdict": "paid",
                "note": "$99.95/yr after 1 month free updates. Not free full history.",
            },
            {
                "name": "portara",
                "url": "https://portara.org/portarashop/product/mnq/",
                "verdict": "paid",
                "note": "£330-£1,500. Not free.",
            },
            {
                "name": "databento",
                "url": "https://databento.com/catalog/cme/GLBX.MDP3/futures/MNQ",
                "verdict": "credits",
                "note": "$125 signup credit expires after 6 months; not a free open full-history CSV.",
            },
            {
                "name": "cme_datamine",
                "url": "https://www.cmegroup.com/datamine/datamine-api.html",
                "verdict": "paid",
                "note": "Full data priced per dataset; requires CME API ID + credentials. Excluded (no credentials, paid).",
            },
            {
                "name": "yahoo_finance",
                "url": "https://finance.yahoo.com/quote/MNQ=F/",
                "verdict": "inadequate",
                "note": "1m only last 30 days, 5m 60 days, 1h 730 days; not back-adjusted; insufficient for 15m full history.",
            },
            {
                "name": "barchart",
                "url": "https://barchart.com",
                "verdict": "inadequate",
                "note": "Free tier: 2y daily, 1 download/day; intraday 1m needs Premier (paid).",
            },
            {
                "name": "kaggle",
                "url": "https://www.kaggle.com/datasets?search=nq+futures+1min",
                "verdict": "unverified",
                "note": "Unknown provenance and license; roll handling and timezone must be checked. Not used without verification.",
            },
            {
                "name": "getdata_finance_nq",
                "url": "https://getdata.io/data-sources/132756-commodities-futures-prices-changes-trading-volume-daily-charts-yahoo-finance",
                "verdict": "excluded",
                "note": "NQ symbol feed describes US stocks cash & extended hours (equity/cash-style), not MNQ futures. Excluded per STRATEGY_RULES market definition.",
            },
            {
                "name": "s-k-28/nq-es-trader-5k-payout",
                "url": "https://github.com/s-k-28/nq-es-trader-5k-payout",
                "verdict": "excluded",
                "note": "Bundled data files are third-party repo artifacts (loader.py sources Yahoo/synthetic). Not an authoritative free MNQ full-history source; provenance unverified. Not ingested.",
            },
            {
                "name": "infoway",
                "url": "https://infoway.io/en/commodities-api/mnq",
                "verdict": "unverified",
                "note": "Free-API-key signup (no CC) offers MNQ OHLCV via data.infoway.io/common/v2/batch_kline, klineType 1..12 (1m..1y). Historical depth/roll-adjustment/tz undocumented; documented sample response prices (~298.62) are not on the MNQ point scale (~15k-26k) implying mapped/synthetic or non-futures provenance. Full history not demonstrated. Not ingested; no key created.",
            },
        ],
    }
    print(json.dumps(evidence, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())