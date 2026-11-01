# Initial Task for Next Agent

## Status (session 2026-11-01 — prior task completed + live free-data sweep + handoff refresh, COMPLETE)
- Prior agent task read from HANDOFF.md + INITIAL_TASK_FOR_NEXT_AGENT.md; re-derived evidence rather than trusting prior claims.
- `git status`: working tree clean (branch main, HEAD 220ba42).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed.
- SHA-256 hashes verified unchanged and match HANDOFF.md exactly (all six files):
  - STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1
  - config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4
  - raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37
  - raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99
  - raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7
  - raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4
- Canonical artifacts verified from disk: axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80 (trades sha256 ce389da2488474a6d0d994cf99bb1e6509761d80f85986f1f8da3e1738b6a364); Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD ~$626,994.56 (trades sha256 7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5).
- Ledger integrity re-verified: zero multi-trade days on both samples; latest exit 10:00 ET (<= 15:55 ET); risk_points == 0.4*atr14 to within 0.0001 ticks on all 748 trades; atr_pct within [0.10, 0.60] on every trade; rvol >= 1.0 on every trade; exit-reason splits axb0306 42/12/6, kaggle 478/130/80; long/short axb0306 33/27, kaggle 359/329.
- Walk-forward re-derived and byte-diffed: `git diff --stat` EMPTY. axb0306 3 windows all negative net (-$10,053.14 .. -$23,058.98); kaggle 8 windows all negative net (-$70,637.24 .. -$134,617.64).
- Bounded free-data re-sweep (live, 2026-11-01): GitHub axb0306/cme-futures-ohlc MNQ path latest commit still `60abd3fb…` 2026-04-15T23:34:55Z (unchanged, 8 files, no intraday extension). Live websearch re-scan: FinzData ($29 one-time MNQ), FirstRate Data ($99.95/yr), MarketParquet ($79 one-time; free tier = ~1yr daily + small intraday sample pack only), Portara (£330–£1,500 paid), historicalfuturesdata.com ($59/yr, free 10s sample only), Databento (key-gated + credit-based), Barchart (Premier only for intraday), Yahoo daily-only, Kaggle (only already-ingested brandenmorris MNQ + NQ big-contract $20/point excluded; tgtanalytics NQ 1min 2022-2025 is the big NQ contract, not MNQ). No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; working tree clean.

## Bounded next task
1. **Maintenance only (default).** Re-verify repo state (git status, tests, hashes, artifacts, walk-forward) against HANDOFF.md. Do not change strategy/params/code.
2. **Data monitoring.** If a new genuinely free MNQ 1min/15min source appears, record provenance/hashes (source, URL, retrieval date, symbol/contract, timezone, roll/adjustment method, gaps, SHA-256) before use.
3. **No experiments without approval.** No parameter/strategy changes without a separately named, versioned experiment with an explicit diff from frozen baseline (STRATEGY_RULES.txt v1.0).
4. **Update docs.** If anything changes, update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with evidence.
5. **Blockers:** Research blocked on data depth (axb0306 ~3mo, Kaggle ~3yr front-month) — both negative under full costs; all walk-forward windows negative.

## Test command
- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` (71 passed)

## Hard boundaries (AGENTS.md)
- Historical research and simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.