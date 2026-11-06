# Initial Task for Next Agent

## Status (maintenance re-verification — 2026-11-06T0900Z, this session)

- `git status --short` **clean** (exit 0) before durable-doc edits. Repo HEAD at verification `7ba8914`.
- Verification (2026-11-06T09:00Z): all 6 tracked SHA-256 hashes **MATCH** (STRATEGY_RULES `6d3258c3...`, config `2a6c5ff8...`, `raw/MNQ_15min.csv` `f417f22d...`, `raw/MNQ_1min.csv` `129623f4...`, `raw/MNQ_1min_frontmonth.csv` `edbadc73...`, `raw/MNQ_15min_frontmonth.csv` `7e129ae3...`). 24 `artifacts/*.json`, 0 parse errors. `artifacts/metrics_axb0306.json` SHA-256 **MATCH** `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f` (`net_pnl` -31637.98, `win_rate` 0.7, `profit_factor` 0.491672798902303). `python3 -m pytest -q` **71 passed / 0 failed** (exit 0, 0.89s; deps installed: `pytest`, `pandas`, `numpy`). No strategy/code/data/raw/artifact drift.
- Free-data monitoring (2026-11-06T08:30:51Z, `scripts/free_data_monitor.py`): ledger `research_state/free_data_monitor_2026-11-06T0900Z.json` (checked_at_utc `2026-11-06T08:30:51.057788+00:00`, 14 candidates, SHA-256 `c4de5a9b7be28c5e583e47317856211bc4de0b4dd43463f6277400ce1095284c`). `axb0306/cme-futures-ohlc` verdict `free`, latest MNQ 1min/15min coverage ends **2026-04-15** (repo HEAD commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264`, date `2026-04-15T23:34:55Z`, message "Update 2026-04-15: 368 files updated"; no extension observed). **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified artifacts): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

## Tasks (maintenance only — do in order)

1. **Re-verify repo state.** Run `git status --short` (expect clean before edits), re-compute all 6 tracked SHA-256 hashes against values in `HANDOFF.md`, confirm `ls artifacts/*.json | wc -l` = 24 and 0 parse errors, and run `python3 -m pytest -q` (expected **71 passed / 0 failed**). Install missing deps if needed (`pip install pytest pandas numpy`) and record outcome. Record any drift with concrete evidence.
2. **Bounded free-data monitoring.** Check for a genuinely free MNQ 1min/15min full-history source extending beyond **2026-04-15** (current latest free coverage in `axb0306/cme-futures-ohlc`). **Record provenance + SHA-256 before use.** Do not purchase data or bypass access controls/terms. Run `python3 scripts/free_data_monitor.py > research_state/free_data_monitor_<UTCstamp>.json` and summarize findings (checked_at, candidate count, ledger SHA-256, axb0306 MNQ max end).
3. **No experiments/tuning.** Do not optimize thresholds, stops, targets, entry rules, or session times. Any change requires explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0.
4. **Update handoff files.** Update `HANDOFF.md` and this file with concrete evidence if anything changes (hashes, test counts, artifacts, new data candidates, blockers). Commit durably.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` MNQ 1min/15min free coverage ends **2026-04-15** (re-verified 2026-11-06T08:28Z; ledger `research_state/free_data_monitor_2026-11-06T0828Z.json`, SHA-256 `f37c31e38d3b23dbd7776f461935ce55bfa522260d89de3040aaad741c88d7e7`; axb0306 repo HEAD commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z`). Kaggle front-month ends 2025-11-12 (untouched OOS ~2.9 months). No free extension found without purchase.
- If a genuinely free MNQ 1min/15min source with longer history is found (**record provenance + SHA-256 before use**), the next concrete task is a re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning. Recompute metrics independently from the trade ledger and store configs/hashes/ledger/summary/validation artifacts.
