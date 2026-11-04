# Initial Task for Next Agent

## Status (session 2026-11-04 — maintenance re-verification pass COMPLETE)

- Branch main; HEAD 2bfcdc6 (checkpoint); working tree clean; local HEAD matches origin/main (2bfcdc6); `git fetch origin --prune` up to date.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3...; config/orb_mnq_15m_showcase.yaml 2a6c5ff8...; raw/MNQ_15min.csv f417f22d...; raw/MNQ_1min.csv 129623f4...; raw/MNQ_1min_frontmonth.csv edbadc73...; raw/MNQ_15min_frontmonth.csv 7e129ae3...).
- Canonical artifacts present + parseable: 16 JSON artifacts in artifacts/ parse cleanly. Walk-forward axb0306: 3 windows all test negative (-$10,053.14, -$21,922.10, -$23,058.98). Walk-forward Kaggle: 8 windows all test negative (-$178,375.24 ... -$114,820.72).
- Baselines from canonical artifacts: axb0306 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.4917, max DD $37,491.80, Sharpe -1.06, Sortino -0.67, expectancy -$527.30/trade. Kaggle front-month 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.2271, max DD ~$626,994.56, Sharpe -1.68, Sortino -1.04, expectancy -$910.65/trade.
- Raw date ranges unchanged: axb0306 ends 2026-04-15; Kaggle front-month ends 2025-11-12.
- Optional reproducibility re-run (this pass): both baselines re-run from scratch reproduced canonical metrics exactly — axb0306 (60 trades, gross -$7,662.00, net -$31,637.98, PF 0.49167, max DD $37,491.80, Sharpe -1.056, Sortino -0.668, expectancy -$527.30, WR 70.0%) and kaggle (688 trades, gross -$140,899.00, net -$626,525.96, PF 0.2271, max DD $626,994.56, Sharpe -1.68, Sortino -1.04, expectancy -$910.65, WR 64.83%); per-trade ledgers identical for both. `_verify` copies removed after comparison.
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed in 0.99s.
- Frozen baseline preserved; no code/strategy/parameter changes. No leftover `_verify` copies.
- Free-data monitoring (2026-11-04): no new genuinely free MNQ 1min/15min source found. All candidates paid. Kaggle remains the only free full 1min source (already ingested).

## Tasks (maintenance only)

1. **Re-verify** repo state (`git status`/`git log`/`git fetch origin --prune`), file hashes vs recorded values, canonical artifacts parseable, walk-forward present and all test windows negative. Run tests if available.
2. **Optional reproducibility**: re-run both baselines from scratch (`python3 src/orb/runner.py --source axb0306 --prefix <name>` and `--source kaggle --prefix <name>`) and confirm metrics/trades match canonical artifacts. Remove any `_verify` copies after comparison.
3. **Data monitoring**: watch for a new genuinely free MNQ 1min/15min source. If found, record source/license/access constraints, retrieval time, contract symbols/months, session timezone, bar timestamps, gaps, roll rules, adjustment method, and SHA-256 before any use. Known free: axb0306 and Kaggle front-month.
4. **No experiments without approval**: no parameter/strategy/rule changes without separately named, versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0.
5. **Update docs**: update HANDOFF.md and this file with concrete evidence if anything changes.

## Hard boundaries (AGENTS.md)

- Historical research and simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both baselines negative under full costs; all walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- axb0306 roll/adjustment: single-contract MNQ.M26, no roll inside sample; verify hash/continuity before re-downloading.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.

## Why this task

Maintenance/re-verification only. Do NOT tune stops/targets/filters/sizing/session times — STRATEGY_RULES.txt v1.0 frozen. Only (a) verify frozen baseline intact/reproducible, (b) watch for genuinely free MNQ 1min/15min data (provenance+SHA256 before use), (c) refresh HANDOFF.md/this file.
