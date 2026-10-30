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
- **Implementation (scaffold)**: Created `src/orb/` modules (`data_loader.py`, `indicators.py`, `orb_logic.py`, `backtest.py`, `runner.py`), config `config/orb_mnq_15m_showcase.yaml`, artifacts dir.
- **Baseline run**: Ran `python src/orb/runner.py` on the sample. Found **60 trades** with frozen rules (first breakout only, both filters RVOL>=1.0 and ATR% 0.10-0.60%, ATR(14) Wilder stop 0.4x, target 0.4R, next-bar-open entry, $3000 risk, MNQ $2/pt, one trade/day). Sample trades saved to `artifacts/trades_baseline.json`.
- **Tests**: Added `tests/orb/test_orb_logic.py` (basic indicator/config tests). `python -m unittest tests.orb.test_orb_logic` passes (2 tests).

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
- **Costs**: Commission/fees/slippage assumptions not yet applied to PnL; need full cost model.
- **Reproducibility**: Need data hashes, full trade ledger with exits, and metrics.

## Next bounded task
1. **Extend data coverage**: Search for longer free MNQ history (other GitHub repos, Kaggle with MNQ, or alternative free sources). Document each attempt.
2. **Implement full execution model**: Use 1min bars for intrabar stop/target/flatten evaluation with stop-first on ambiguity, apply commissions/exchange fees/slippage per side, compute gross/net PnL, R-multiples.
3. **Add deterministic tests**: Opening range, first-break, filters, sizing, cutoffs (15:00 no entry, 15:55 flatten), DST, one-trade-per-day.
4. **Validation**: Chrono splits, long/short separate, sensitivity to costs, report trade count/win rate/avg R/expectancy/gross-net/max DD etc. Do not optimize.
5. **Update handoff** with full evidence.

Do not change frozen rules, buy data, add credentials, or enable live trading.
