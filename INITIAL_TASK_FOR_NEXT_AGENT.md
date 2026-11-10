# Initial task for next agent

**Session:** 2026-11-10T02:56Z
**HEAD:** `dd4d5a1` (`main...origin/main`; clean). HEAD advanced from prior handoff's cited `ee81e34` via `dd4d5a1` touching only `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` — no code/strategy/config/raw/artifact drift.
**Tests:** 75 passed in 0.92s. Command: `/tmp/kilo-tests-venv/bin/python -m pytest tests/ -q` (throwaway venv at `/tmp/kilo-tests-venv` with pytest/numpy/requests/pandas; matches `.github/workflows/main.yml` controller-tests step).
**SHA-256:** 20/20 key files verified against `HANDOFF.md` manifest (all match exactly).
**Monitor:** `research_state/free_data_monitor_20261108T060017Z.json` unchanged (`checked_at_utc` 2026-11-08T06:00:17.980919+00:00, file SHA `3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f`); user crontab empty (`no crontab for runner`); `/etc/cron.d/` OS-defaults only (e2scrub_all, php, sphinxsearch, sysstat); `systemctl list-timers` shows only OS timers — no research timers; only `.github/workflows/main.yml` present; no duplicate research workflows/processes.

## Prior task (completed)

Maintenance re-verification per durable handoff (2026-11-10T02:56Z): inspected `HANDOFF.md`/`STRATEGY_RULES.txt`/`PROMPT.md`/`AGENTS.md`; verified clean tree at HEAD `dd4d5a1` (diff vs prior cited `ee81e34` = handoff files only via commit `dd4d5a1`); ran full test suite (**75/75 passed, 0.92s**); recomputed all 20 manifest SHA-256 hashes (**all match**); confirmed monitor unchanged and 06:00Z loop stopped; confirmed no duplicate workflows/processes. **No drift detected.** No code, strategy, config, raw data, or canonical artifact changes.

## Research status (frozen — no further work planned)

- **Strategy**: `STRATEGY_RULES.txt` v1.0 (MNQ 15-min ORB showcase). Baseline results are negative net and must not be presented as profitable: axb0306 net -$31,637.98 (60 trades, PF 0.492); kaggle net -$626,525.96 (688 trades, PF 0.227). Date-based WF OOS tests negative net.
- **Data**: axb0306 MNQ (2026-01-20..2026-04-15, 60 complete days; raw `MNQ_{15min,1min}.csv`) and kaggle front-month proxy (2022-11-16..2025-11-12, 688 days; raw `MNQ_{15min,1min}_frontmonth.csv`). 1-min audits: `research_state/1m_audit_{axb0306,kaggle}.json`. Free-data search exhausted (`data/FEASIBILITY_REPORT.md`); 06:00Z monitor stopped.
- **Standing constraints**: Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Do not restart the 06:00Z loop or launch nested/duplicate workflows.

## Next task

Continue in **maintenance/read-only verification mode**.

1. Inspect `HANDOFF.md` and `STRATEGY_RULES.txt`.
2. Verify state: `git status --short --branch`; run the full test suite (`/tmp/kilo-tests-venv/bin/python -m pytest tests/ -q` or derive from `.github/workflows/main.yml` controller-tests step with a throwaway venv if `/tmp/kilo-tests-venv` is absent); recompute the 20 SHA-256 hashes in `HANDOFF.md`.
3. Confirm `research_state/free_data_monitor_20261108T060017Z.json` and its `checked_at_utc`/SHA are unchanged and the 06:00Z loop remains stopped.
4. If any drift is detected (dirty tree beyond handoff files, test failure, hash mismatch, monitor activity), investigate and document in `HANDOFF.md` with concrete evidence. Do **not** mutate frozen files to "fix" drift without explicit authorization and a separately versioned maintenance record.
5. Update `HANDOFF.md` and this file with exact results (HEAD, test output, hashes/manifest status, monitor state, blockers, next step). Commit handoff updates as a handoff-only checkpoint only if explicitly authorized.

**Constraints:** Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Do not restart the 06:00Z loop or launch nested/duplicate workflows. Keep session changes to handoff/initial-task files unless explicitly authorized for a separately versioned experiment.
