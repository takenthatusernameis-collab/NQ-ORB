# Initial task for the next Kilo worker — NQ ORB

Read `AGENTS.md`, `STRATEGY_RULES.txt`, `PROMPT.md`, and `HANDOFF.md` before making changes.

## Current state
- Free-data feasibility done (axb0306/cme-futures-ohlc MNQ 1min/15min, 2026-01-20 to 2026-04-15). 15:55 flatten implemented with 1min data and stop-first on ambiguity. Full execution engine with costs/slippage in place. Baseline cost-aware run done (60 trades on sample) - see `data/FEASIBILITY_REPORT.md`, `artifacts/trades_full.json`, `artifacts/metrics.json`. Tests pass (orb logic + controller/workflow tests).

## Priority tasks
1. **Data coverage**: Find longer free MNQ history. Try other public repos, Kaggle (check MNQ specifically), or other legitimate free sources. Record provenance/hashes for any new data. Do not purchase data.
2. **Harden execution & tests**: Add tests for DST transitions, contract rolls, ambiguous intrabar touches, cutoff times. Validate flatten logic more thoroughly.
3. **Metrics & validation**: Compute full required metrics with chronological splits (train/val/test), long/short splits, year/regime if possible. Run sensitivity to costs (slippage/fees). Report uncertainty and data limitations.
4. **Data provenance**: Compute hashes (sha256) for raw CSVs in `raw/`, update FEASIBILITY_REPORT with details.
5. **Update handoff**: Update `HANDOFF.md` with evidence, commands, results, blockers, next task.

## Constraints
No parameter optimization, no strategy-rule changes, no broker integration, no live/paper orders. Update `HANDOFF.md` with evidence, commands, results, blockers, next task.
