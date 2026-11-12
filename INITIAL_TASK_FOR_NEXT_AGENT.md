# Initial task for next agent

**Session:** 2026-11-12T08:44:47Z (maintenance re-verification)
**HEAD (at verification):** `f09bdc3` (`main...origin/main`, clean; `git fetch --dry-run` no remote changes, `git diff origin/main --stat` empty). Working tree is handoff-only after this update.
**Tests:** 75 passed in 0.95s. Command: `/tmp/kilo-verify-venv/bin/python -m pytest tests/ -q` (throwaway venv `/tmp/kilo-verify-venv` with `pytest`+`pandas`).
**SHA-256:** 20/20 manifest hashes matched (known `artifacts/metrics_axb0306_full.json` historical manifest typo: on-disk `dddaefa…` authoritative/unchanged). Monitor SHA `3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f` unchanged.
**Automation/monitor:** `research_state/free_data_monitor_20261108T060017Z.json` unchanged (`checked_at_utc` 2026-11-08T06:00:17.980919+00:00, axb0306 CME OHLC capped at 2026-04-15). `crontab -l` empty; `/etc/cron.d/` OS defaults only (e2scrub_all, php, sphinxsearch, sysstat); `systemctl list-timers --all` OS timers only, no orb/kilo/research/data timers; only `.github/workflows/main.yml`; no matching research/monitor processes. 06:00Z loop remains stopped.

## Prior task (completed)
Maintenance re-verification at HEAD `f09bdc3` (clean `main...origin/main`, `git fetch --dry-run` no remote changes, `git diff origin/main --stat` empty). Inspected `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `STRATEGY_RULES.txt` (v1.0, 126 lines, unchanged), `PROMPT.md`, `AGENTS.md`; ran full tests (**75 passed in 0.95s**); recomputed manifest hashes — **20/20 matched** (known `metrics_axb0306_full.json` manifest typo only, on-disk unchanged); confirmed monitor file/`checked_at_utc`/SHA unchanged and 06:00Z loop stopped (crontab empty, OS-default cron.d/timers only, only `main.yml`, no duplicate processes). No frozen files modified. Handoff/initial-task updated (handoff-only, uncommitted).

## Research status (frozen — no further work planned)
- **Strategy**: `STRATEGY_RULES.txt` v1.0 (MNQ 15-min ORB showcase). Baseline results are negative net and must not be presented as profitable: axb0306 net -$31,637.98 (60 trades, PF 0.492); kaggle net -$626,525.96 (688 trades, PF 0.227). Date-based WF OOS tests negative net.
- **Data**: axb0306 MNQ (2026-01-20..2026-04-15, 60 complete days) and kaggle front-month proxy (2022-11-16..2025-11-12, 688 days). 1-min audits in `research_state/1m_audit_{axb0306,kaggle}.json`. Free-data search exhausted (`data/FEASIBILITY_REPORT.md`); 06:00Z monitor stopped.

## Next task
Continue in **maintenance/read-only verification mode**. The research baseline is frozen and complete; your job is to keep the repository provably intact and to report any change.

1. Inspect `HANDOFF.md` and `STRATEGY_RULES.txt` (v1.0, 126 lines — must be unchanged).
2. Verify state: `git status --short --branch` (expect clean `main...origin/main` before edits); run full tests (`/tmp/kilo-verify-venv/bin/python -m pytest tests/ -q` in a throwaway venv with `pytest`+`pandas`); recompute the 20 SHA-256 hashes in the `HANDOFF.md` manifest and confirm all match (known exception: `artifacts/metrics_axb0306_full.json` manifest typo in historical text — on-disk authoritative `dddaefa…`, not drift).
3. Confirm `research_state/free_data_monitor_20261108T060017Z.json` `checked_at_utc`/SHA unchanged and the 06:00Z loop stopped (crontab, `/etc/cron.d/`, `systemctl list-timers --all`, `.github/workflows/`, processes).
4. If drift is detected (dirty tree beyond handoff files, test failure, hash mismatch beyond the known typo, or monitor activity), investigate and document with concrete evidence. Do **not** mutate frozen files without explicit authorization and a separately versioned maintenance record.
5. Update `HANDOFF.md` and this file with exact results (HEAD, test output, hashes/manifest status, monitor state, blockers, next step). Commit handoff updates as a handoff-only checkpoint if appropriate/authorized.

**Constraints:** Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Do not restart the 06:00Z loop or launch nested/duplicate workflows. Keep session changes to handoff/initial-task files unless explicitly authorized for a separately versioned experiment.

**If you ever want to do real research work instead of maintenance:** the frozen baseline is negative-net and fully documented (`data/FEASIBILITY_REPORT.md`, `artifacts/`, `research_state/`). Any new experiment must be separately named/versioned with an explicit diff from `STRATEGY_RULES.txt` v1.0, must not overwrite frozen files, and must follow the guardrails in `AGENTS.md` (free data only, no optimization before the untouched baseline is reported, chronological splits, gross+net reporting). Start by re-reading `PROMPT.md` and `data/FEASIBILITY_REPORT.md`.

(End of file - total 29 lines)