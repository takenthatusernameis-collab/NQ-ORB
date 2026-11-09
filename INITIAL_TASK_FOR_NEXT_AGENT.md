# Initial Task for Next Agent

## Verified context (2026-11-09T15:03Z, this session)
- Repo: **clean** (`## main...origin/main`), no untracked. HEAD `8d1dfe2`. No code/strategy/data/raw/artifact/workflow changes; only `HANDOFF.md`/`INITIAL_TASK_FOR_NEXT_AGENT.md` updated.
- Full suite: **75 passed in 0.92s** (`python3 -m pytest tests/ -q`, 2026-11-09T15:03Z).
- **20/20 key files SHA-256 verified** (manifest in `HANDOFF.md`, full `prefix…suffix` entries recomputed and matched).
- Monitor unchanged: `research_state/free_data_monitor_20261108T060017Z.json` (`checked_at_utc` `2026-11-08T06:00:17.980919+00:00`); axb0306 coverage ends 2026-04-15. 06:00Z loop stopped.
- **Note:** prior "16 tracked SHA-256" set cited non-existent paths (e.g. `config/baseline_mnq_showcase.yaml`, `raw/README.md`, `research_state/*_mnq*.json`/`baseline_*`/`data_availability_monitor_*`, `artifacts/data_availability_report.*`). Use the 20-file manifest in `HANDOFF.md`. Do not delete/rewrite evidence; align naming only if explicitly authorized as separately versioned maintenance.

## Completed work (2026-11-09T15:03Z, this session)
Maintenance re-verification independently completed and confirmed:
- `git status --short --branch` → `## main...origin/main`, clean; no untracked. HEAD `8d1dfe2`.
- 20/20 key SHA-256 verified present and matched (`HANDOFF.md` manifest).
- `python3 -m pytest tests/ -q` → **75 passed in 0.92s**.
- Monitor unchanged (`checked_at_utc` 2026-11-08T06:00:17.980919+00:00; axb0306 coverage ends 2026-04-15). 06:00Z loop stopped.

## Next concrete task
None pending beyond standing maintenance. At next session start, repeat the maintenance re-verification (git status, 20/20 SHA-256 vs `HANDOFF.md` manifest, `python3 -m pytest tests/ -q` → 75 passed, monitor unchanged) OR proceed with an explicitly authorized new experiment that is separately named, versioned, and diffed from the frozen baseline (`STRATEGY_RULES.txt` v1.0). Do not optimize thresholds, stops, targets, entry rules, or session times without authorization.

## Standing blocker (report honestly)
Limited free MNQ history (~3 months axb0306; ~3 years kaggle front-month proxy) restricts robust walk-forward/OOS inference. Both baselines negative net after costs (axb0306 net -$31,637.98, 60 trades, PF 0.492; kaggle net -$626,525.96, 688 trades, PF 0.227; date-based WF OOS also negative net). Evidence, not edge. Do not present as profitable or use synthetic results as market evidence.
