# Initial Task for Next Agent

## Verified context (2026-11-09T20:16Z, this session)
- Repo: HEAD `d10ce83` (`## main...origin/main`); `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` edited this session (uncommitted). No other changes.
- Full suite: **75 passed in 0.60s** (`PYTHONPATH=/tmp/pytest_env python3 -m pytest tests/ -q`; system python3.12 lacks pytest/pandas/numpy — `/tmp/pytest_env` provides deps).
- **20/20 key files SHA-256 verified** (all match `HANDOFF.md` manifest).
- Monitor unchanged: `research_state/free_data_monitor_20261108T060017Z.json` (`checked_at_utc` `2026-11-08T06:00:17.980919+00:00`, SHA `3f90bc…776f`); axb0306 coverage ends 2026-04-15; no monitor writes after 2026-11-08T06:00:17Z; 06:00Z loop stopped.

## Completed work (2026-11-09T20:16Z, this session)
Maintenance re-verification independently completed:
- `git status --short --branch` → `## main...origin/main` (clean at start; handoff files edited now).
- 20/20 key SHA-256 recomputed and verified against `HANDOFF.md` manifest.
- `PYTHONPATH=/tmp/pytest_env python3 -m pytest tests/ -q` → **75 passed in 0.60s**.
- Monitor `checked_at_utc` unchanged (2026-11-08T06:00:17.980919+00:00); 06:00Z loop stopped.
- No code/strategy/config/raw/artifact/workflow changes.

## Next concrete task
None pending beyond standing maintenance. At next session start:
1. **Maintenance re-verification**: `git status --short --branch`; recompute SHA-256 for 20 manifest files vs `HANDOFF.md`; run `PYTHONPATH=/tmp/pytest_env python3 -m pytest tests/ -q` (or equivalent with deps) → expect 75 passed; confirm monitor `checked_at_utc` unchanged. Update handoff/this file with evidence.
2. **OR** (if explicitly authorized): proceed with a separately named, versioned experiment with explicit diff from frozen baseline (`STRATEGY_RULES.txt` v1.0). Do not optimize thresholds, stops, targets, entry rules, or session times without authorization. Any data/code changes must follow `AGENTS.md`/`PROMPT.md` constraints.
3. Commit `HANDOFF.md`/`INITIAL_TASK_FOR_NEXT_AGENT.md` updates if the workflow permits.

## Standing blocker (report honestly)
Limited free MNQ history (~3 months axb0306 2026-01-20..2026-04-15, 60 complete days; ~3 years kaggle front-month proxy 2022-11-16..2025-11-12, 688 days) restricts robust walk-forward/OOS inference. Both frozen baselines **negative net after costs** (axb0306 net -$31,637.98, 60 trades, PF 0.492; kaggle net -$626,525.96, 688 trades, PF 0.227; date-based WF OOS also negative net). Evidence, not edge. Do not present as profitable or use synthetic results as market evidence. Free-data search exhausted; 06:00Z monitor stopped.