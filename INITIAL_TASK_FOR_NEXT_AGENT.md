# Initial Task for Next Agent

## Verified context (2026-11-09T14:58Z, this session)
- Repo: **clean** (`## main...origin/main`), no untracked. HEAD `9abd995`. No code/strategy/data/raw/artifact/workflow changes; only `HANDOFF.md`/`INITIAL_TASK_FOR_NEXT_AGENT.md` updated.
- Full suite: **75 passed in 0.90s** (`python3 -m pytest tests/ -q`, 2026-11-09T14:58Z).
- **20/20 key files SHA-256 verified** (manifest in `HANDOFF.md`): `STRATEGY_RULES.txt`, 2 configs, `data/FEASIBILITY_REPORT.md`, 4 raw CSVs, 2 1m audits, monitor, canonical metrics/trades/WF artifacts.
- Monitor unchanged: `research_state/free_data_monitor_20261108T060017Z.json` (`checked_at_utc` `2026-11-08T06:00:17.980919+00:00`, `3f90bc…776f`); axb0306 coverage ends 2026-04-15. 06:00Z loop stopped.
- **Note:** prior "16 tracked SHA-256" set cited non-existent paths (e.g. `config/baseline_mnq_showcase.yaml`, `raw/README.md`, `research_state/*_mnq*.json`/`baseline_*`/`data_availability_monitor_*`, `artifacts/data_availability_report.*`). Use the 20-file manifest in `HANDOFF.md`. Do not delete/rewrite evidence; align naming only if explicitly authorized as separately versioned maintenance.

## Next task (maintenance re-verification; no feature work pending)
No pending feature work. Frozen baseline (`STRATEGY_RULES.txt` v1.0) evaluated and reported (negative net; evidence not edge).

1. **Re-verify:** `git status --short --branch` clean (`## main...origin/main`), no untracked. Recompute SHA-256 for the 20 key files in `HANDOFF.md`; all must match. Investigate missing/mismatch before declaring healthy (no fabricate/overwrite).
2. **Run `python3 -m pytest tests/ -q`:** expect **75 passed**. Investigate failures; distinguish implementation tests from empirical evidence.
3. **Confirm monitor unchanged:** `research_state/free_data_monitor_20261108T060017Z.json` hash/`checked_at_utc` unchanged; axb0306 ends 2026-04-15. Do not restart 06:00Z loop or launch nested/duplicate workflows (AGENTS.md).
4. **Do NOT modify** `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No optimization; no broker/live/paid-data/credentials. Any new work = separately named, versioned experiment with explicit diff from frozen baseline.
5. **Update `HANDOFF.md` and this file** after work with exact completed work, test command/results, blockers, next concrete task.

## Completed work (2026-11-09T14:58Z, this session)
Maintenance re-verification per prior task. All checks passed; no code/strategy/data/raw/artifact/workflow changes. Only `HANDOFF.md` and this file updated.
- `git status --short --branch` → `## main...origin/main`, clean; no untracked. HEAD `9abd995`.
- 20/20 key SHA-256 verified present and matched (`HANDOFF.md` manifest).
- `python3 -m pytest tests/ -q` → **75 passed in 0.90s**.
- Monitor unchanged (`3f90bc…776f`, `checked_at_utc` 2026-11-08T06:00:17.980919+00:00; axb0306 coverage ends 2026-04-15). 06:00Z loop stopped.

## Next concrete task
None pending. Repeat maintenance re-verification at next session start, or await an explicitly authorized new experiment (separately named, versioned, diffed from frozen baseline).

## Standing blocker (report honestly)
Limited free MNQ history (~3 months axb0306; ~3 years kaggle front-month proxy) restricts robust walk-forward/OOS inference. Both baselines negative net after costs (axb0306 net -$31,637.98, 60 trades, PF 0.492; kaggle net -$626,525.96, 688 trades, PF 0.227; date-based WF OOS also negative net). Evidence, not edge. Do not present as profitable or use synthetic results as market evidence.
