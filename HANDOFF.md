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
- **Data feasibility audit**: Created `data/FEASIBILITY_REPORT.md`. Found free MNQ 1min/15min data via public GitHub repo `axb0306/cme-futures-ohlc` (TopstepX-sourced), UTC timestamps, covers 2026-01-20 to 2026-04-15 (~3 months). 1min data exists so 15:55 ET flatten/intrabar ordering is testable in principle. Limited history and continuous/adjustment method need care.
- **Downloaded free sample**: Saved `raw/MNQ_15min.csv` and `raw/MNQ_1min.csv`.
- **Full execution engine**: Extended `backtest.py` to use 1min bars for intrabar stop/target evaluation with stop-first on ambiguous bars, enforce 15:55 flatten, apply commissions+fees per side ($2.25+$0.62) and slippage (1 tick adverse), compute gross/net PnL, track exit reasons/times.
- **Baseline run (cost-aware)**: Ran backtest on the sample. Found **60 trades**, 42 wins/18 losses (70% win rate). Gross PnL -$7662.00, net PnL -$31637.98 (total costs ~$23976). Avg R -0.043, expectancy -$527.30/trade. Max DD ~$37492. Longs/shorts both negative in sample. Results saved to `artifacts/trades_full.json` and `artifacts/metrics.json`.
- **Tests**: Expanded `tests/orb/test_orb_logic.py` with additional tests for DST, flatten time, ambiguity. All orb logic tests pass (9 tests). Also verified controller/workflow tests pass.
- **Data provenance**: SHA-256 hashes computed for raw CSVs and recorded in `data/FEASIBILITY_REPORT.md` (MNQ_15min.csv f417..., MNQ_1min.csv 1296...).

## Source/data provenance (recorded)
- Source: https://github.com/axb0306/cme-futures-ohlc (MNQ files)
- Files: MNQ_15min_20260120_20260415.csv, MNQ_1min_20260120_20260415.csv
- Format: datetime,open,high,low,close,volume (UTC per repo README)
- Retrieved: 2026-10-30
- Coverage: 2026-01-20 to 2026-04-15 (~3 months). TZ/DST: UTC converted to America/New_York.
- Contract: MNQ (micro) $2/pt per rules. Continuous series as provided by repo (adjustment method not fully inspected - documented as gap).
- Hashes: See data/FEASIBILITY_REPORT.md

## Commands executed
- pip installed pandas numpy pyyaml pytest
- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python src/orb/runner.py` (generated 60 trades)
- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m unittest tests.orb.test_orb_logic` (OK)
- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests/test_workflow_diagnostics_scanner.py tests/test_controller_progress_accounting.py` (all passed)

## Unresolved blockers / uncertainty
- **History depth**: Only ~3 months of free 1min/15min MNQ - insufficient for walk-forward/OOS per validation protocol. Need longer free history.
- **Continuous contract/rolls**: Repo uses TopstepX data; roll/adjustment method needs explicit documentation/verification.
- **15:55 flatten & intrabar ordering**: Implemented with stop-first on ambiguity; edge cases around DST/rolls need more testing.
- **Reproducibility**: Trade ledger and metrics saved; data hashes recorded.

## Next bounded task
1. **Extend data coverage**: Search for longer free MNQ history (other GitHub repos, Kaggle with MNQ, or alternative free sources). Document each attempt with provenance/hashes. Do not purchase data.
2. **Harden execution**: Add tests for DST transitions, contract rolls, ambiguous intrabar touches, cutoff times. Validate flatten logic more thoroughly.
3. **Metrics & validation**: Compute full required metrics with chronological splits (train/val/test), long/short splits, year/regime if possible. Run sensitivity to costs (slippage/fees). Report uncertainty and data limitations.
4. **Data provenance**: Compute hashes (sha256) for raw CSVs in `raw/`, update FEASIBILITY_REPORT with details.
5. **Update handoff** with full evidence.

Do not change frozen rules, buy data, add credentials, or enable live trading.
