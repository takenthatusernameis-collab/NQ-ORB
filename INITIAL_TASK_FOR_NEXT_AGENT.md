# Initial Task for Next Agent

## Verified context (2026-11-09T13:50Z, this session)
- Repo: **clean** (`## main...origin/main`), no untracked files (`git ls-files --others --exclude-standard` empty). HEAD at `f8e436b chore(kilo): checkpoint agent session` (main, tracking `origin/main`) — no code/strategy/data/raw/artifact/workflow changes made by this session (only `HANDOFF.md`/`INITIAL_TASK_FOR_NEXT_AGENT.md` updated).
- Full suite: **75 passed in 0.90s** (`python3 -m pytest tests/ -q`, 2026-11-09T13:50Z).
- All 16 tracked SHA-256 **MATCH** (recomputed via `sha256sum`): `STRATEGY_RULES.txt` `6d3258c3...`, `config/orb_mnq_15m_showcase.yaml` `2a6c5ff8...`, `config/orb_mnq_1m_wf_v1.yaml` `ad745900...`, `raw/MNQ_15min.csv` `f417f22d...`, `raw/MNQ_1min.csv` `129623f4...`, `raw/MNQ_1min_frontmonth.csv` `edbadc73...`, `raw/MNQ_15min_frontmonth.csv` `7e129ae3...`, `research_state/free_data_monitor_20261108T060017Z.json` `3f90bc19...`, `artifacts/metrics_axb0306.json` `e06f9dd0...`, `artifacts/metrics_kaggle.json` `a6ae1006...`, `artifacts/trades_axb0306.json` `ce389da2...`, `artifacts/trades_kaggle.json` `7251e4a9...`, `artifacts/walk_forward_date_60_20_20_axb0306.json` `f05c44b0...`, `artifacts/walk_forward_date_60_20_20_kaggle.json` `eac749dc...`, `research_state/1m_audit_axb0306.json` `3aac07d2...`, `research_state/1m_audit_kaggle.json` `27734632...`.
- Free-data monitor unchanged: `checked_at_utc` `2026-11-08T06:00:17.980919+00:00`; axb0306 coverage ends 2026-04-15 (`MNQ_15min` last 2026-04-15T23:15:00, `MNQ_1min` last 2026-04-15T23:29:00). 06:00Z maintenance loop remains stopped. No strategy/parameter changes.

## Next task (maintenance re-verification; no feature work pending)
No pending feature work. Frozen baseline (`STRATEGY_RULES.txt` v1.0) evaluated and reported (negative net; evidence not edge).

1. **Re-verify at session start:** `git status --short --branch` clean (`## main...origin/main`), no untracked files. Recompute 16 tracked SHA-256 hashes with `sha256sum`; all must MATCH HANDOFF.md.
2. **Run `python3 -m pytest tests/ -q`:** expect **75 passed**. Investigate failures before declaring healthy; distinguish implementation tests from empirical evidence.
3. **Confirm monitor unchanged:** `research_state/free_data_monitor_20261108T060017Z.json` hash/`checked_at_utc` unchanged; axb0306 coverage ends 2026-04-15. Do not restart 06:00Z maintenance loop or launch nested/duplicate workflows (AGENTS.md hard boundary).
4. **Do NOT modify** `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No threshold/stop/target/entry/session optimization; no broker/live/paid-data work; no credentials. Any new work must be a separately named, versioned experiment with explicit diff from frozen baseline.
5. **Update `HANDOFF.md` and this file** after any work, recording exact completed work, test command/results, blockers, and next concrete task. Keep HANDOFF.md compact.

## Completed work (2026-11-09T13:50Z, this session)
Maintenance re-verification per prior task. All checks passed; no code/strategy/data/raw/artifact/workflow changes. Only `HANDOFF.md` and this file updated.

- `git status --short --branch` → `## main...origin/main`, clean; no untracked files.
- HEAD: `f8e436b chore(kilo): checkpoint agent session`.
- 16/16 tracked SHA-256 MATCH (via `sha256sum`).
- `python3 -m pytest tests/ -q` → **75 passed in 0.90s**.
- Monitor unchanged (`3f90bc...776f`, `checked_at_utc` 2026-11-08T06:00:17.980919+00:00; raw ends 2026-04-15). 06:00Z loop stopped.

## Next concrete task
None pending. Repeat maintenance re-verification at next session start, or await an explicitly authorized new experiment (separately named, versioned, diffed from frozen baseline).

## Standing blocker (report honestly)
Limited free MNQ history (~3 months axb0306; ~3 years kaggle front-month proxy) restricts robust walk-forward/out-of-sample inference. Both baselines negative net after costs (axb0306 net -$31,637.98, 60 trades, PF 0.492; kaggle net -$626,525.96, 688 trades, PF 0.227; date-based WF OOS tests also negative net). Evidence, not edge. Do not present as profitable or use synthetic results as market evidence.

## Deliverables (if work done)
Updated `HANDOFF.md` + this file; test command/results; blockers; no new artifacts unless a new experiment is explicitly authorized.