# Initial task for the next Kilo worker — NQ ORB

Read `AGENTS.md`, `STRATEGY_RULES.txt`, `PROMPT.md`, and `HANDOFF.md` before making changes.

## Current state (steady state, session 2026-10-31q verified)
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

## Reproducibility re-verified (session 2026-10-31q)
- Both baselines match stored canonical artifacts field-by-field (trade_count, win_rate, gross/net P&L, costs, avg R, expectancy, PF, max DD, Sharpe, Sortino, exposure, cost grid). Determinism confirmed.
- Independent signal-funnel cross-check (`scripts/diag_signal_funnel.py`) reproduces engine trade counts exactly: Kaggle 932 dates -> 771 OR days -> 765 first breakouts -> 688 pass filters -> 688 trades; axb0306 61 OR days -> 61 breakouts -> 60 pass filters -> 60 trades.
- Ledger integrity audit: zero exits past 15:55 ET, zero days with >1 trade, stop/target within 0.125 index points (<= half tick) of the exact 0.4R formula (residual is tick rounding per spec).
- `artifacts/README.md` documents canonical vs verification vs historical artifact files; nothing deleted.

## Initial task (next bounded task)
1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes before use.
2. No parameter/strategy changes without a separately versioned experiment (frozen baseline preserved).
3. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods.
4. Keep FEASIBILITY_REPORT.md, HANDOFF.md, and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.

## Constraints
- No parameter optimization, no strategy-rule changes, no broker integration, no live/paper orders.
- Historical research/simulation only. Do not purchase data or use paid/proprietary services.
- Do not present synthetic results as market evidence; distinguish implementation tests from empirical evaluation.
- Update HANDOFF.md with evidence, commands, results, blockers, next task.

## Verification command
`PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` (expect 63 passed)

## Unresolved blockers (documented, not actionable without new data)
- History depth: axb0306 ~3 months (single-contract MNQ.M26, unadjusted); Kaggle front-month ~3 years (unadjusted front-month by max volume). No multi-year free MNQ 1min/15min beyond these; insufficient for robust walk-forward/OOS.
- Results negative under full costs on both available samples (costs dominate).
- Splits computed on limited samples; OOS interval is short.
