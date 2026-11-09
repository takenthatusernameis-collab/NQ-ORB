# Initial Task for Next Agent

## Verified context (2026-11-09T20:25Z, this session)
- Repo: HEAD `e502726` (`## main...origin/main`); `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` updated this session — changes left **uncommitted** in the working tree for review (commit when the workflow permits).
- Full suite: **75 passed in 0.63s** (`PYTHONPATH=/tmp/pytest_env /tmp/pytest_env/bin/pytest tests/ -q`; system python3.12 lacks pytest/pandas/numpy — `/tmp/pytest_env` provides deps; note: `/tmp/pytest_env/bin/python3` does not exist, use `/tmp/pytest_env/bin/pytest` directly).
- **20/20 key files SHA-256 verified** (full 64-char hashes recomputed this session; all match `HANDOFF.md` manifest).
- Monitor unchanged: `research_state/free_data_monitor_20261108T060017Z.json` (`checked_at_utc` `2026-11-08T06:00:17.980919+00:00`, file SHA `3f90bc19548bb0d3…977c776f`); axb0306 coverage ends 2026-04-15; no monitor writes after 2026-11-08T06:00:17Z; 06:00Z loop stopped.

## Completed work (2026-11-09T20:25Z, this session)
Maintenance re-verification completed:
- `git status --short --branch` → `## main...origin/main` (clean working tree; HEAD `e502726`).
- 20/20 key SHA-256 recomputed and verified against `HANDOFF.md` manifest (all 20 full hashes match; full hashes recorded in `HANDOFF.md`).
- `PYTHONPATH=/tmp/pytest_env /tmp/pytest_env/bin/pytest tests/ -q` → **75 passed in 0.63s**.
- Monitor `checked_at_utc` unchanged (2026-11-08T06:00:17.980919+00:00); 06:00Z loop stopped.
- No code/strategy/config/raw/artifact/workflow changes (only handoff files updated this session).

## Next concrete task
At next session start:
1. **Maintenance re-verification**: `git status --short --branch`; recompute SHA-256 for the 20 manifest files vs `HANDOFF.md`; run `PYTHONPATH=/tmp/pytest_env /tmp/pytest_env/bin/pytest tests/ -q` → expect 75 passed; confirm monitor `checked_at_utc` unchanged. Update handoff/this file with evidence.
2. **OR** (if explicitly authorized): proceed with a separately named, versioned experiment with an explicit diff from the frozen baseline (`STRATEGY_RULES.txt` v1.0). Do not optimize thresholds, stops, targets, entry rules, or session times without authorization. Any data/code changes must follow `AGENTS.md`/`PROMPT.md` constraints.
3. Commit `HANDOFF.md`/`INITIAL_TASK_FOR_NEXT_AGENT.md` updates if the workflow permits.

## Standing blocker (report honestly)
Limited free MNQ history (~3 months axb0306 2026-01-20..2026-04-15, 60 complete days; ~3 years kaggle front-month proxy 2022-11-16..2025-11-12, 688 days) restricts robust walk-forward/OOS inference. Both frozen baselines **negative net after costs** (axb0306 net -$31,637.98, 60 trades, PF 0.492; kaggle net -$626,525.96, 688 trades, PF 0.227; date-based WF OOS also negative net). Evidence, not edge. Do not present as profitable or use synthetic results as market evidence. Free-data search exhausted (`data/FEASIBILITY_REPORT.md`); 06:00Z monitor stopped.
