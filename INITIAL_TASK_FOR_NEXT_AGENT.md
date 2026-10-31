# Initial task for the next Kilo worker — NQ ORB

Read `AGENTS.md`, `STRATEGY_RULES.txt`, `PROMPT.md`, and `HANDOFF.md` before making changes.

## Current state
- Free-data feasibility done (axb0306 MNQ 1min/15min Jan-Apr 2026; Kaggle Databento MNQ front-month May-Nov 2025). Roll methods documented in FEASIBILITY_REPORT. Baseline cost-aware run: 60 trades, net -$31637.98. Tests pass (52). Hashes verified.

## Priority tasks
1. Run baseline on Kaggle front-month sample and compare to axb0306 sample; document differences.
2. Add contract-roll edge-case tests with synthetic data.
3. Update FEASIBILITY_REPORT with baseline comparison and any new hashes.
4. Update HANDOFF and INITIAL_TASK with evidence.

## Constraints
No parameter optimization, no strategy-rule changes, no broker integration, no live/paper orders. Update `HANDOFF.md` with evidence, commands, results, blockers, next task.
