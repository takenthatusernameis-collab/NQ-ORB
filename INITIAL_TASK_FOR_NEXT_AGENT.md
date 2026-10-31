# Initial task for the next Kilo worker — NQ ORB

Read `AGENTS.md`, `STRATEGY_RULES.txt`, `PROMPT.md`, and `HANDOFF.md` before making changes.

## Current state
- Free-data feasibility done. Sources: axb0306 MNQ 1min/15min 2026-01-20..2026-04-15 (unverified continuous) and Kaggle brandenmorris Databento MNQ front-month 2022-11-16..2025-11-12 (unadjusted front-month by max volume). Roll methods documented in data/FEASIBILITY_REPORT.md with hashes.
- Baselines (cost-aware): axb0306 60 trades net -$31,637.98; Kaggle front-month 688 trades net -$626,525.96. Both negative under full costs on available samples. Chrono splits/cost sensitivity present.
- Tests pass (54). Artifacts saved (trades/metrics for both samples). Added ambiguous intrabar/roll/DST tests.

## Priority tasks
1. Continue free-data search if new sources appear; document provenance/hashes; do not purchase data.
2. If longer history found, run chronological splits and cost sensitivity across full periods; else document limitations clearly.
3. Add more intrabar ambiguity/roll edge-case tests as data/logic allow (keep deterministic/synthetic).
4. Update FEASIBILITY_REPORT, HANDOFF, and INITIAL_TASK with evidence.

## Constraints
No parameter optimization, no strategy-rule changes, no broker integration, no live/paper orders. Update `HANDOFF.md` with evidence, commands, results, blockers, next task.
