# Initial task for the next Kilo worker — NQ ORB

Read `AGENTS.md`, `STRATEGY_RULES.txt`, `PROMPT.md`, and `HANDOFF.md` before making changes.

## Current state (steady state, session 2026-10-31m verified)
- Frozen baseline preserved: `STRATEGY_RULES.txt` v1.0 and `config/orb_mnq_15m_showcase.yaml` unchanged. No parameter/strategy changes.
- Free-data feasibility complete. Sources:
  - axb0306/cme-futures-ohlc: MNQ 1min/15min 2026-01-20..2026-04-15, single-contract MNQ.M26, no roll, no back-adjustment (roll method documented in data/FEASIBILITY_REPORT.md).
  - Kaggle brandenmorris Databento MNQ front-month: 2022-11-16..2025-11-12, unadjusted front-month by max volume, no roll adjustment.
- Baselines (cost-aware, commission $2.25 + fee $0.62 per side, 1-tick adverse slippage):
  - axb0306: 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.492, max DD $37,491.80.
  - Kaggle front-month: 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.227, max DD ~$626,994.56.
  - Both negative under full costs on available samples; costs dominate.
- Required performance reporting complete in artifacts/metrics_axb0306.json and artifacts/metrics_kaggle.json: avg win/loss R & USD, CAGR (null, net loss), Sharpe/Sortino annualized per-trade R, worst/best day, monthly/yearly breakdown, exposure_pct, signal_close_entry_sensitivity, cost-sensitivity grid, chronological train/val/test splits.
- Tests: `python -m pytest tests -q` -> 63 passed. Deterministic tests cover OR construction, first-breakout-only, both filters, both directions, stop/target (0.4R), tick rounding, sizing, one-trade-per-day, 15:00 cutoff, 15:55 flatten via 1min, wick-without-close, DST spring/fall, ambiguous intrabar touch (stop-first), contract-roll edge cases, config fields, RVOL denominator exclusion.
- Artifacts saved: trades + metrics ledgers for both samples in artifacts/. Raw data in raw/ with SHA-256 hashes in data/FEASIBILITY_REPORT.md.
- Free-data search exhausted (GitHub/Kaggle/Yahoo daily only); no new free MNQ 1min/15min source beyond the two above. No data purchased.
- Hashes verified unchanged (MNQ_15min f417f22d..., MNQ_1min 129623f4...).

## Priority tasks (next bounded task)
1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes before use.
2. No parameter/strategy changes without a separately versioned experiment (frozen baseline preserved).
3. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods.
4. Keep FEASIBILITY_REPORT.md, HANDOFF.md, and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.

## Constraints
- No parameter optimization, no strategy-rule changes, no broker integration, no live/paper orders.
- Historical research/simulation only. Do not purchase data or use paid/proprietary services.
- Do not present synthetic results as market evidence; distinguish implementation tests from empirical evaluation.
- Update `HANDOFF.md` with evidence, commands, results, blockers, next task.

## Verification command
`PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q`  (expect 63 passed)
