# Initial task for next agent

**Session:** 2026-11-09T21:19Z
**HEAD:** 0d75075 (main...origin/main, clean)
**Tests:** 75 passed in 0.66s
**SHA-256:** 20/20 key files verified against manifest (all match)
**Monitor:** research_state/free_data_monitor_20261108T060017Z.json unchanged (checked_at_utc 2026-11-08T06:00:17.980919+00:00, SHA 3f90bc...776f); no writes after 2026-11-08T06:00:17Z; 06:00Z loop stopped.

## Prior task (completed)
Maintenance re-verification per durable handoff: read HANDOFF.md, verified git status (clean), test suite (75/75 pass), all 20 file SHA-256 hashes vs manifest, monitor state (unchanged/stopped). All checks passed with no changes to code/strategy/config/raw/artifact/workflow.

## Next task
Continue in maintenance/read-only verification mode. Before each session: inspect HANDOFF.md and STRATEGY_RULES.txt; run `git status --short --branch`, `PYTHONPATH=/tmp/pytest_env /tmp/pytest_env/bin/pytest tests/ -q`, and recompute the 20 SHA-256 hashes in HANDOFF.md; confirm the free-data monitor file and its `checked_at_utc` are unchanged and the 06:00Z loop remains stopped. If any drift is detected (git dirty, test failure, hash mismatch, monitor activity), investigate and document in HANDOFF.md with evidence. Do not modify frozen strategy/rules/configs/raw data/canonical artifacts. Do not restart the 06:00Z loop or launch nested/duplicate workflows. Keep updates to HANDOFF.md/INITIAL_TASK_FOR_NEXT_AGENT.md only unless explicitly authorized for a separately versioned experiment.
