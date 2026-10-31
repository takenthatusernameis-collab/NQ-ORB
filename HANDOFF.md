# NQ ORB — Durable Handoff
Date initialized: 2026-10-30
Repository: takenthatusernameis-collab/NQ-ORB
Status: Free-data feasibility audit complete; MNQ 15m/1m infrastructure implemented against a short free sample with baseline signals generated.

## Initial authoritative state
- `STRATEGY_RULES.txt` contains the user-specified NQ ORB rules and MNQ 15-minute showcase preset.
- `PROMPT.md` specifies the research workflow.
- `AGENTS.md` defines research, auditability, and no-live-trading constraints.
- `.github/workflows/main.yml` present (controller/workflow files as committed).
- No validated multi-year backtest yet; results are from short free sample only.

## Completed work (this session)
- **Data feasibility audit**: Created `data/FEASIBILITY_REPORT.md`. Found free MNQ 1min/15min data via public GitHub repo `axb0306/cme-futures-ohlc` (TopstepX-sourced), UTC timestamps, covers 2026-01-20 to 2026-04-15 (~3 months). 1min data exists so 15:55 ET flatten/intrabar ordering is testable in principle. Limited history and continuous/adjustment method need care; commercial sources exist but not free bulk.
- **Downloaded free sample**: Saved `raw/MNQ_15min.csv` (5609 lines) and `raw/MNQ_1min.csv` (84078 lines).
- **Full execution engine**: Extended `backtest.py` to use 1min bars for intrabar stop/target evaluation with stop-first on ambiguous bars, enforce 15:55 flatten, apply commissions+fees per side ($2.25+$0.62) and slippage (1 tick adverse), compute gross/net PnL, track exit reasons/times.
- **Baseline run (cost-aware)**: Ran `python src/orb/runner.py` on the sample. Found **60 trades**, 42 wins/18 losses (70% win rate). Gross PnL -$7662.00, net PnL -$31637.98 (total costs ~$23976). Avg R -0.043, expectancy -$527.30/trade. Max DD ~$37492. Longs/shorts both negative in sample. Results saved to `artifacts/trades_full.json` and `artifacts/metrics.json`.
- **Tests**: Expanded `tests/orb/test_orb_logic.py` (OR construction, config, cutoffs). `python -m unittest tests.orb.test_orb_logic` passes (5 tests).

## Source/data provenance (recorded)
- Source: https://github.com/axb0306/cme-futures-ohlc (MNQ files)
- Files: MNQ_15min_20260120_20260415.csv, MNQ_1min_20260120_20260415.csv
- Format: datetime,open,high,low,close,volume (UTC per repo README)
- Retrieved: 2026-10-30
- Coverage: 2026-01-20 to 2026-04-15 (~3 months). TZ/DST: UTC converted to America/New_York (confirmed 14:30Z -> 09:30 ET EST).
- Contract: MNQ (micro) $2/pt per rules. Continuous series as provided by repo (adjustment method not fully inspected - documented as gap).

## Commands executed
- Created dirs, wrote feasibility report, downloaded CSVs via curl
- pip installed pandas numpy pyyaml
- `python src/orb/runner.py` (generated 60 trades)
- `python -m unittest tests.orb.test_orb_logic` (OK)

## Unresolved blockers / uncertainty
- **History depth**: Only ~3 months of free 1min/15min MNQ - insufficient for walk-forward/OOS per validation protocol. Need longer free history.
- **Continuous contract/rolls**: Repo uses TopstepX data; roll/adjustment method needs explicit documentation/verification. Do not assume back-adjusted prices are directly executable without checking.
- **15:55 flatten & intrabar ordering**: 1min data exists, but full simulation of stop/target fills with proper ordering/slippage/fees not yet implemented in engine (trades logged but exits not simulated). Mark as partially implemented.
- **Reproducibility**: Trade ledger and metrics saved; need data hashes and full documentation of any new data sources.

- **Data provenance**: Added SHA-256 hashes for raw CSVs to `data/FEASIBILITY_REPORT.md` (MNQ_15min.csv f417..., MNQ_1min.csv 1296...).

## Next bounded task
1. **Extend data coverage**: Search for longer free MNQ history (other GitHub repos, Kaggle with MNQ, or alternative free sources). Document each attempt with provenance/hashes.
2. **Harden execution**: Validate flatten at exactly 15:55, add more edge case handling, ensure no lookahead. Add tests for DST/rolls/ambiguous touches.
3. **Validation**: Chrono splits (train/val/test), long/short separate, sensitivity to costs (slippage/fees), report all required metrics. Do not optimize.
4. **Data provenance**: Compute hashes for raw CSVs, document acquisition details.
5. **Update handoff** with full evidence.

Do not change frozen rules, buy data, add credentials, or enable live trading.
