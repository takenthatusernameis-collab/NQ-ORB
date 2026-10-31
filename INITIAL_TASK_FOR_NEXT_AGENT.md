# Initial task for the next Kilo worker — NQ ORB

Read `AGENTS.md`, `STRATEGY_RULES.txt`, `PROMPT.md`, and `HANDOFF.md` before making changes.

## Current state
- Free-data feasibility done. Sources: axb0306 MNQ 1min/15min 2026-01-20..2026-04-15 (unverified continuous) and Kaggle brandenmorris Databento MNQ front-month 2022-11-16..2025-11-12 (unadjusted front-month by max volume). Roll methods documented in data/FEASIBILITY_REPORT.md with hashes.
- Baselines (cost-aware): axb0306 60 trades net -$31,637.98; Kaggle front-month 688 trades net -$626,525.96. Both negative under full costs on available samples. Chrono splits/cost sensitivity present.
- Tests pass (60). Artifacts saved (trades/metrics for both samples). Added ambiguous intrabar/roll/DST tests.
- Free-data search re-run 2026-10-31i: no new free MNQ 1min/15min source found (Yahoo only daily). No data purchased.

## Priority tasks
1. Maintain documentation; if a new free MNQ source appears, record provenance/hashes before use.
2. Add intrabar ambiguity/roll-transition tests only where deterministic synthetic fixtures are available.
3. If longer history is obtained (free only), run chronological splits and cost sensitivity across full periods.
4. Update FEASIBILITY_REPORT, HANDOFF, and INITIAL_TASK with evidence.

## Constraints
No parameter optimization, no strategy-rule changes, no broker integration, no live/paper orders. Update `HANDOFF.md` with evidence, commands, results, blockers, next task.
