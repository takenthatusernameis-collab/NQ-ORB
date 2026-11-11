# Initial task for next agent

**Session:** 2026-11-11T19:11Z (maintenance re-verification)
**HEAD:** `b46cb99` (`main...origin/main`, clean working tree at verification start, up to date with origin; `b46cb99` advances `6ea1b33` via handoff-only checkpoint commit, `git diff --stat 6ea1b33 b46cb99` → HANDOFF.md + INITIAL_TASK_FOR_NEXT_AGENT.md only, 13 insertions/10 deletions). Handoff/initial-task edits committed this session as handoff-only checkpoint.
**Tests:** 75 passed in 0.72s. Command: `/tmp/kilo-verify-venv/bin/python -m pytest tests/ -q` (existing throwaway venv `/tmp/kilo-verify-venv` with `pytest` 8.x + `pandas` 3.1.1).
**SHA-256:** all 20 manifest hashes in HANDOFF.md recomputed and verified — all match (2026-11-11T19:11Z).
**Monitor/automation:** `research_state/free_data_monitor_20261108T060017Z.json` unchanged (`checked_at_utc` 2026-11-08T06:00:17.980919+00:00, SHA `3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f`); user crontab empty; `/etc/cron.d/` OS defaults only; `systemctl list-timers --all` OS timers only; only `.github/workflows/main.yml`; observed processes limited to OS/runner daemons (waagent, networkd-dispatcher) and this session's kilo idle-timeout wrapper.

## Prior task (completed)
Maintenance re-verification at HEAD `b46cb99`. Inspected `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `STRATEGY_RULES.txt`, `PROMPT.md`, `AGENTS.md`; confirmed clean tree at start; ran full tests (**75 passed in 0.72s**); recomputed and confirmed all 20 manifest SHA-256 hashes match (incl. audits `2773463...`/`3aac07d...`, monitor `3f90bc1...`); confirmed monitor file/`checked_at_utc`/SHA unchanged and 06:00Z loop stopped; confirmed no crontab, no research timers, single workflow, no duplicate research processes. **No drift** in frozen strategy/config/raw/canonical artifacts or monitor. Handoff/initial-task updated and committed (handoff-only checkpoint).

## Research status (frozen — no further work planned)
- **Strategy**: `STRATEGY_RULES.txt` v1.0 (MNQ 15-min ORB showcase). Baseline results are negative net and must not be presented as profitable: axb0306 net -$31,637.98 (60 trades, PF 0.492); kaggle net -$626,525.96 (688 trades, PF 0.227). Date-based WF OOS tests negative net. Do not present as profitable.
- **Data**: axb0306 MNQ (2026-01-20..2026-04-15, 60 complete days) and kaggle front-month proxy (2022-11-16..2025-11-12, 688 days). 1-min audits in `research_state/1m_audit_{axb0306,kaggle}.json`. Free-data search exhausted (`data/FEASIBILITY_REPORT.md`); 06:00Z monitor stopped.

## Next task
Continue in **maintenance/read-only verification mode**.
1. Inspect `HANDOFF.md` and `STRATEGY_RULES.txt`.
2. Verify state: `git status --short --branch`; run full tests (`/tmp/kilo-verify-venv/bin/python -m pytest tests/ -q` in a throwaway venv with `pytest`+`pandas`); recompute the SHA-256 hashes in `HANDOFF.md` manifest table.
3. Confirm `research_state/free_data_monitor_20261108T060017Z.json` and its `checked_at_utc`/SHA are unchanged and the 06:00Z loop remains stopped (check crontab, `/etc/cron.d/`, `systemctl list-timers --all`, workflows/processes).
4. If any drift is detected (dirty tree beyond handoff files, test failure, hash mismatch, monitor activity), investigate and document in `HANDOFF.md` with concrete evidence. Do **not** mutate frozen files to "fix" drift without explicit authorization and a separately versioned maintenance record.
5. Update `HANDOFF.md` and this file with exact results (HEAD, test output, hashes/manifest status, monitor state, blockers, next step). Commit handoff updates as a handoff-only checkpoint only if explicitly authorized.

**Constraints:** Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Do not restart the 06:00Z loop or launch nested/duplicate workflows. Keep session changes to handoff/initial-task files unless explicitly authorized for a separately versioned experiment.