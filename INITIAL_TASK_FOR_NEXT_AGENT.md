# Initial task for next agent

**Session:** 2026-11-09T23:22Z
**HEAD:** `4ac7f74` (`main...origin/main`, clean working tree)
**Tests:** 75 passed in 0.69s (`PYTHONPATH=/tmp/pytest_env /tmp/pytest_env/bin/pytest tests/ -q`)
**SHA-256:** 20/20 key files verified against `HANDOFF.md` manifest (all match; recomputed this session). 20th file `artifacts/walk_forward_date_60_20_20_kaggle.json` = `eac749dc112a31df57e366203efa378e0ba5528ac6c4ee878a22bf0557781355`.
**Monitor:** `research_state/free_data_monitor_20261108T060017Z.json` unchanged (`checked_at_utc` 2026-11-08T06:00:17.980919+00:00, mtime 2026-11-09 20:08:32.132968865 +00:00, size 3538, SHA `3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f`); no writes after 2026-11-08T06:00:17Z; user crontab empty; 06:00Z loop stopped; only `.github/workflows/main.yml` present, no duplicate workflows/processes.

## Prior task (completed)
Maintenance re-verification per durable handoff (2026-11-09T23:22Z): read `HANDOFF.md`/`STRATEGY_RULES.txt`/prior task; confirmed `git status --short --branch` clean at HEAD `4ac7f74` (only handoff files changed vs `f8c814e`); ran full test suite (75/75 pass, 0.69s); recomputed all 20 manifest SHA-256 hashes via script (all match); confirmed monitor unchanged and 06:00Z loop stopped (crontab empty); confirmed no duplicate workflows/processes. No drift detected. No code, strategy, config, raw data, or canonical artifact changes.

## Next task
Continue in **maintenance/read-only verification mode**.

1. Inspect `HANDOFF.md` and `STRATEGY_RULES.txt`.
2. Verify state: `git status --short --branch`; run `PYTHONPATH=/tmp/pytest_env /tmp/pytest_env/bin/pytest tests/ -q`; recompute the 20 SHA-256 hashes in `HANDOFF.md`.
3. Confirm `research_state/free_data_monitor_20261108T060017Z.json` and its `checked_at_utc`/SHA are unchanged and the 06:00Z loop remains stopped.
4. If any drift is detected (dirty tree beyond handoff files, test failure, hash mismatch, monitor activity), investigate and document in `HANDOFF.md` with concrete evidence. Do **not** mutate frozen files to "fix" drift without explicit authorization and a separately versioned maintenance record.
5. Update `HANDOFF.md` and this file with exact results (HEAD, test output, hashes/manifest status, monitor state, blockers, next step).

**Constraints:** Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Do not restart the 06:00Z loop or launch nested/duplicate workflows. Keep session changes to handoff/initial-task files unless explicitly authorized for a separately versioned experiment.