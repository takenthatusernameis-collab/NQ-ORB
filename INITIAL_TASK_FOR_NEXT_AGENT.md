# Initial task for the next Kilo worker — NQ ORB

Read `AGENTS.md`, `STRATEGY_RULES.txt`, `PROMPT.md`, and `HANDOFF.md` before making changes.

## Current state
- Free-data feasibility done (axb0306/cme-futures-ohlc MNQ 1min/15min, 2026-01-20 to 2026-04-15). 15:55 flatten implemented with 1min data and stop-first on ambiguity. Full execution engine with costs/slippage in place. Baseline cost-aware run done (60 trades on sample) - see `data/FEASIBILITY_REPORT.md`, `artifacts/trades_full.json`, `artifacts/metrics.json`. Splits and cost sensitivity added. Tests pass (51 tests). Hashes verified.

## Priority tasks
1. **Continuous contract/rolls**: Inspect axb0306 repo update scripts/config to document roll/adjustment method. Record exact contract months/roll rules. Do not purchase data.
2. **Harden execution & tests**: Add ambiguous intrabar touch tests with synthetic 1min data; validate flatten logic. Add contract-roll edge cases.
3. **Metrics & validation**: Keep chronological splits and cost sensitivity; add year/regime splits if more data becomes available.
4. **Data provenance**: Compute hashes for any new raw CSVs; update FEASIBILITY_REPORT.
5. **Update handoff**: Update `HANDOFF.md` with evidence, commands, results, blockers, next task.

## Constraints
No parameter optimization, no strategy-rule changes, no broker integration, no live/paper orders. Update `HANDOFF.md` with evidence, commands, results, blockers, next task.