# Initial Task for Next Agent

## Verified context (2026-11-09T07:32Z, this session)
- Repo: **clean** (`## main...origin/main`), HEAD `0000294 chore(kilo): checkpoint agent session`, no untracked files.
- Full suite: **75 passed in 0.89s** (`python3 -m pytest tests/ -q`, 2026-11-09T07:32Z).
- Tracked SHA-256 re-verified MATCH (16 files via `sha256sum`): `STRATEGY_RULES.txt` `6d3258c3...ad2b1`, `config/orb_mnq_15m_showcase.yaml` `2a6c5ff8...91e4`, `config/orb_mnq_1m_wf_v1.yaml` `ad745900...845b`, `raw/MNQ_15min.csv` `f417f22d...ce37`, `raw/MNQ_1min.csv` `129623f4...ea99`, `raw/MNQ_1min_frontmonth.csv` `edbadc73...13e7`, `raw/MNQ_15min_frontmonth.csv` `7e129ae3...9ef4`, `research_state/free_data_monitor_20261108T060017Z.json` `3f90bc19...776f`. Canonical artifacts match: `metrics_axb0306.json` `e06f9dd0...f93f`, `metrics_kaggle.json` `a6ae1006...1af1`, `trades_axb0306.json` `ce389da2...a364`, `trades_kaggle.json` `7251e4a9...8aa5`. Dated WF: `walk_forward_date_60_20_20_axb0306.json` `f05c44b0...5546`, `walk_forward_date_60_20_20_kaggle.json` `eac749dc...1355`. 1m audit ledgers: `1m_audit_axb0306.json` `3aac07d2...a706`, `1m_audit_kaggle.json` `27734632...4041`.
- This session's re-verification **complete**: git clean, all tracked hashes MATCH, canonical artifact hashes match, pytest 75/75 passed, free-data monitor unchanged (`checked_at_utc` `2026-11-08T06:00:17.980919+00:00`, axb0306/cme-futures-ohlc sha `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264`, latest bar `2026-04-15T23:34:55Z`, no extension). **No strategy/parameter changes to the frozen baseline.**
- Free-data search exhausted per `data/FEASIBILITY_REPORT.md`; 06:00Z maintenance loop stopped. Sources: axb0306 (2026-01-20..2026-04-15, single-contract MNQ.M26 unadjusted, 60 complete days) and kaggle front-month (2022-11-16..2025-11-12, unadjusted front-month by max volume, 688 trading days).

## Next task (maintenance re-verification; no feature work pending)
There is no pending feature work. The frozen baseline (`STRATEGY_RULES.txt` v1.0) is evaluated and reported; all concrete prior-task items are done. Re-verify durable state and keep the handoff honest:

1. **Re-verify durable handoff state at session start:** `git status --short --branch` must be clean (`## main...origin/main`), no untracked files. Recompute the tracked SHA-256 hashes with `sha256sum`; all must MATCH. Confirm canonical artifact hashes match HANDOFF.md.
2. **Run `python3 -m pytest tests/ -q`:** expect **75 passed**. Investigate any failure before declaring the session healthy; distinguish implementation tests from empirical evidence.
3. **Confirm the free-data monitor is unchanged:** `research_state/free_data_monitor_20261108T060017Z.json` hash matches; latest bar still `2026-04-15T23:34:55Z` (no extension); 06:00Z maintenance loop remains stopped. Do not restart it or launch additional scheduled workflows (AGENTS.md hard boundary).
4. **Do NOT modify** `STRATEGY_RULES.txt`, either config, raw data, or canonical artifacts. No threshold/stop/target/entry/session optimization; no broker/live/paid-data work; no credentials. If new work is requested, it must be a separately named, versioned experiment with an explicit diff from the frozen baseline (AGENTS.md #10).
5. **Update HANDOFF.md and this file** after any work, recording exact completed work, test command/results, blockers, and the next concrete task.

## Standing blocker (report honestly, do not overstate)
Limited free MNQ history (~3 months axb0306; ~3 years kaggle front-month proxy) restricts robust walk-forward/out-of-sample inference. Both baselines are negative net after costs (axb0306 net -$31,637.98, 60 trades, PF 0.492; kaggle net -$626,525.96, 688 trades, PF 0.227; date-based WF OOS tests also negative net). This is evidence, not a claim of edge. Do not present synthetic results as market evidence, and do not describe the strategy as profitable without reproducible, cost-aware, out-of-sample evidence.

## Deliverables (if any work is done)
Updated HANDOFF.md entry + this file; test command/results; blockers; no new artifacts unless a new experiment is explicitly authorized.