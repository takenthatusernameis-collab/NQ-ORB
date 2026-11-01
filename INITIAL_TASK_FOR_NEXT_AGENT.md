# Initial Task for Next Agent

## Status (session 2026-11-01 — maintenance re-verification + live free-data re-sweep, COMPLETE)
- Prior agent task read from HANDOFF.md + INITIAL_TASK_FOR_NEXT_AGENT.md; re-derived evidence rather than trusting prior claims.
- `git status`: working tree clean (branch main, up to date with origin/main, HEAD 82b1553).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed.
- SHA-256 recomputed from disk; all six match recorded values exactly (STRATEGY_RULES.txt 6d3258c3…, config 2a6c5ff8…, raw/MNQ_15min.csv f417f22d…, raw/MNQ_1min.csv 129623f4…, raw/MNQ_1min_frontmonth.csv edbadc73…, raw/MNQ_15min_frontmonth.csv 7e129ae3…).
- Canonical artifacts verified: axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80 (trades sha256 ce389da2…); Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD ~$626,994.56 (trades sha256 7251e4a9…). Walk-forward: all windows negative on both sources.
- Verify artifacts committed and byte-identical to canonical (metrics_verify_axb/kag, trades_verify_axb/kag, walk_forward.json == walk_forward_kaggle.json).
- Live free-data re-sweep (2026-11-01): GitHub axb0306/cme-futures-ohlc MNQ path latest commit still `60abd3fb…` 2026-04-15T23:34:55Z, 8 files unchanged. Live websearch re-scan of FinzData ($49 one-time MNQ intraday from 2019-05-05), MarketParquet ($79 one-time continuous MNQ 1min 2019-05-06..2026-10-23; free tier = ~1yr daily + Apr 6-10 2026 intraday sample pack only), FirstRate Data ($99.95/yr), Portara (paid), historicalfuturesdata.com ($59/yr, free 10s sample + 3 months MNQ), Databento (key-gated + $125 credit expiring; continuous unadjusted, UTC), Barchart (Premier only for intraday), Yahoo Finance (daily only), CME DataMine (priced per dataset), Kaggle brandenmorris MNQ unchanged (CC BY 4.0, already ingested). No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; working tree clean.

## Bounded next task
1. **Maintenance only (default).** Re-verify repo state (git status, tests, hashes, artifacts, walk-forward) against HANDOFF.md. Do not change strategy/params/code.
2. **Data monitoring.** If a new genuinely free MNQ 1min/15min source appears, record provenance/hashes (source, URL, retrieval date, symbol/contract, timezone, roll/adjustment method, gaps, SHA-256) before use.
3. **No experiments without approval.** No parameter/strategy changes without a separately named, versioned experiment with an explicit diff from frozen baseline (STRATEGY_RULES.txt v1.0).
4. **Update docs.** If anything changes, update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with evidence.
5. **Blockers:** Research blocked on data depth (axb0306 ~3mo, single-contract MNQ.M26, no roll; Kaggle ~3yr front-month, unadjusted) — both negative under full costs; all walk-forward windows negative. Highest-value action remains a bounded free-data re-sweep, not parameter fitting.

## Test command
- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` (71 passed)

## Hard boundaries (AGENTS.md)
- Historical research and simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.