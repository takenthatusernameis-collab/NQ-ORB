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

## Completed work (verification session 2026-10-31)
- Re-verified raw data hashes: MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99.
- Ran full test suite: `python -m pytest tests -q` -> 45 passed.
- Baseline metrics (cost-aware, sample 2026-01-20..2026-04-15): 60 trades, WR 70%, gross -$7,662.00, net -$31,637.98, avg R -0.043, expectancy -$527.30/trade, PF 0.492, max DD $37,491.80, longs 33 (-$17,601.84), shorts 27 (-$14,036.14). Artifacts: artifacts/trades_full.json, artifacts/metrics.json.
- Data coverage search: no additional free longer MNQ 1min/15min source located beyond axb0306/cme-futures-ohlc in this session; documented in data/FEASIBILITY_REPORT.md. History remains ~3 months, insufficient for walk-forward/OOS.

## Unresolved blockers
- History depth ~3 months only; no multi-year free MNQ 1min/15min found.
- Continuous contract/roll adjustment method still undocumented.
- No chronological train/val/test splits yet due to sample size.

## Next bounded task
1. Search additional free MNQ sources (Kaggle MNQ 1min, other public repos) and document provenance/hashes; do not purchase.
2. Implement chronological split reporting on available sample and cost sensitivity.
3. Add deterministic tests for DST transitions, contract rolls, ambiguous intrabar touches, cutoff/flatten.
4. Update FEASIBILITY_REPORT and HANDOFF with evidence.
## Completed work (verification session 2026-10-31b)
- Re-ran full test suite: `python -m pytest tests -q` -> 45 passed.
- Confirmed baseline metrics unchanged in artifacts/metrics.json.
- No code changes required; handoff/next-task refreshed.


## Completed work (verification session 2026-10-31c)
- Searched for additional free MNQ history sources; no longer history found beyond axb0306/cme-futures-ohlc (still ~3 months Jan 20 - Apr 15 2026). Documented.
- Added chronological split reporting (train/val/test) and cost sensitivity to artifacts/metrics.json.
- Added deterministic tests for cutoff time, risk sizing, config fields.
- Full test suite: 48 passed.
- Baseline cost-aware unchanged (60 trades, net -$31637.98).

## Unresolved blockers
- History depth ~3 months only; no multi-year free MNQ 1min/15min found.
- Continuous contract/roll adjustment method still undocumented.
- Splits computed on limited sample.

## Completed work (verification session 2026-10-31d)
- Added deterministic DST conversion tests (spring forward 2026-03-09, fall back 2026-11-01) and tick-size check.
- Full test suite: 51 passed.
- No longer free MNQ 1min/15min history found beyond axb0306 (still ~3 months). Documented.
- Baseline unchanged: 60 trades, net -$31637.98.

## Unresolved blockers
- History depth ~3 months only; no multi-year free MNQ 1min/15min found.
- Continuous contract/roll adjustment method still undocumented.
- Splits computed on limited sample.

## Next bounded task
1. Document continuous contract/roll adjustment method from axb0306 repo (inspect update scripts/config).
2. Add ambiguous intrabar touch scenario tests with synthetic 1min data.
3. Update FEASIBILITY_REPORT with roll-method findings and any new hashes.
4. Update HANDOFF and INITIAL_TASK with evidence.

## Completed work (verification session 2026-10-31f)
- Ran baseline on Kaggle front-month sample (unadjusted front-month by max volume, Databento-derived): 688 trades, net -$626,525.96 (cost-aware). Compared to axb0306 (60 trades, net -$31,637.98). Documented differences in data/FEASIBILITY_REPORT.md.
- Documented continuous contract/roll methods for both sources; added hashes for Kaggle front-month CSVs.
- Added deterministic contract-roll edge-case tests (2 tests). Added ambiguous intrabar touch test previously; DST/tick/cutoff/risk sizing tests present.
- Full test suite: 53 passed.
- Baselines unchanged in recorded artifacts.

## Unresolved blockers
- History depth: axb0306 ~3 months (unverified continuous), Kaggle front-month ~7 months (May-Nov 2025, unadjusted front-month) - still limited vs multi-year needed for robust walk-forward/OOS.
- axb0306 roll/adjustment method undocumented (unverified continuous).
- No multi-year free MNQ 1min/15min found; results remain negative under full costs on available samples.

## Next bounded task
1. Expand free-data search for longer MNQ history (other public repos/Kaggle sources) with provenance/hashes; do not purchase.
2. If longer free history found, run chronological splits and cost sensitivity across full periods; else document limitations clearly.
3. Add more intrabar ambiguity tests and edge cases around roll transitions if data allows.
4. Update FEASIBILITY_REPORT/HANDOFF/INITIAL_TASK with evidence.
