# Handoff
## Current durable state (maintenance re-verification — 2026-11-06T21:33Z, this session)

- Session verification (2026-11-06T21:33Z): `git status --short` **clean** (exit 0). All 6 tracked SHA-256 hashes **MATCH** (STRATEGY_RULES.txt `6d3258c3...`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff8...`; `raw/MNQ_15min.csv` `f417f22d...`; `raw/MNQ_1min.csv` `129623f4...`; `raw/MNQ_1min_frontmonth.csv` `edbadc73...`; `raw/MNQ_15min_frontmonth.csv` `7e129ae3...`). 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed, 0 failed** (exit 0, 0.91s). `python3 scripts/free_data_monitor.py` -> ledger `research_state/free_data_monitor_20261106T213346Z.json` (file SHA-256 `06c7e10976d5f1d6598accab2912a83b462fa652d520a470dcb11dc89a01b258`, checked_at_utc `2026-11-06T21:33:46.095344+00:00`, 14 candidates, JSON valid). axb0306 latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264`, dated `2026-04-15T23:34:55Z`; MNQ 1min/15min coverage ends 2026-04-15, no extension observed. No code/strategy/data/raw/artifact changes.
- Session verification (2026-11-06T21:11Z): `git status --short` **clean** (exit 0). All 6 tracked SHA-256 hashes **MATCH** (STRATEGY_RULES.txt `6d3258c3...`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff8...`; `raw/MNQ_15min.csv` `f417f22d...`; `raw/MNQ_1min.csv` `129623f4...`; `raw/MNQ_1min_frontmonth.csv` `edbadc73...`; `raw/MNQ_15min_frontmonth.csv` `7e129ae3...`). 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed, 0 failed** (exit 0, 0.94s). `python3 scripts/free_data_monitor.py` -> ledger `research_state/free_data_monitor_20261106T211152Z.json` (file SHA-256 `5cee0bc1f5911b64ad47c66e68ecf8381e5f66f396dafe6e2b5f17def436ab35`, checked_at_utc `2026-11-06T21:11:52.013146+00:00`, 14 candidates, JSON valid). axb0306 latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264`, dated `2026-04-15T23:34:55Z`; MNQ 1min/15min coverage ends 2026-04-15, no extension observed. No code/strategy/data/raw/artifact changes.
- Session verification (2026-11-06T20:57Z): `git status --short` **clean** (exit 0). All 6 tracked SHA-256 hashes **MATCH**. 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed, 0 failed** (exit 0, 0.90s). `python3 scripts/free_data_monitor.py` re-run; latest ledger remained `research_state/free_data_monitor_20261106T2031Z.json` (checked_at_utc `2026-11-06T20:31:28.534928+00:00`, SHA-256 `771a9137a9e14c09c2f8e49cc2c0c124a212e42efad587efea7f9c21726f14a6`, 14 candidates, JSON valid). axb0306 latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264`, dated `2026-04-15T23:34:55Z`; MNQ 1min/15min coverage ends 2026-04-15, no extension observed. No code/strategy/data/raw/artifact changes.
- Baselines unchanged: axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0).

## Next agent (immediate)

Repeat the same bounded maintenance loop (re-verify state, run `scripts/free_data_monitor.py`, record evidence, no tuning). Latest completed: **2026-11-06T21:35Z** (ledger `research_state/free_data_monitor_20261106T213513Z.json`, file SHA-256 `c5441e814a63a9c643fd6ab50db065673c99dc33d9b3b7dafc8cdb32df227771`, checked `2026-11-06T21:35:13.282873+00:00`, 14 candidates; axb0306 MNQ 1min/15min ends 2026-04-15, no extension observed).

## Prior maintenance verifications (evidence preserved)

- 2026-11-06T21:35Z: ledger `research_state/free_data_monitor_20261106T213513Z.json` SHA-256 `c5441e814a63a9c643fd6ab50db065673c99dc33d9b3b7dafc8cdb32df227771` (checked `2026-11-06T21:35:13.282873+00:00`), pytest unavailable in env (prior verified 71 passed), axb0306 ends 2026-04-15.
- 2026-11-06T21:14Z: ledger `research_state/free_data_monitor_20261106T211412Z.json` SHA-256 `5cee0bc1f5911b64ad47c66e68ecf8381e5f66f396dafe6e2b5f17def436ab35` (checked `2026-11-06T21:14:12.640614+00:00`), 71 passed, axb0306 ends 2026-04-15.
- 2026-11-06T21:11Z: ledger `research_state/free_data_monitor_20261106T211152Z.json` SHA-256 `5cee0bc1f5911b64ad47c66e68ecf8381e5f66f396dafe6e2b5f17def436ab35` (checked `2026-11-06T21:11:52.013146+00:00`), 71 passed, axb0306 ends 2026-04-15.
- 2026-11-06T20:57Z: ledger `research_state/free_data_monitor_20261106T2031Z.json` SHA-256 `771a9137a9e14c09c2f8e49cc2c0c124a212e42efad587efea7f9c21726f14a6` (checked `2026-11-06T20:31:28.534928+00:00`), 71 passed, axb0306 ends 2026-04-15.

## Blockers / durable constraints

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through **2026-04-15**.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
