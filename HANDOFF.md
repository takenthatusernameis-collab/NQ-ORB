## Durable state (authoritative snapshot)
- **2026-11-10T03:47Z (this session)**: maintenance re-verification completed. HEAD `074ec7c` (`main...origin/main`, clean working tree). HEAD advanced from prior handoff's cited `d43b4c4` via checkpoint commits `9b4e59b` and `074ec7c` (`chore(kilo): checkpoint agent session`), each touching only `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` — no code/strategy/config/raw/artifact drift (`git show --name-only --oneline HEAD` confirms handoff files only; `git diff d43b4c4 074ec7c` = handoff files only). Verified: `git status --short --branch` → clean; full suite **75 passed in 0.89s** (`/tmp/kilo-tests-venv/bin/python -m pytest tests/ -q`; throwaway venv with pytest/numpy/requests/pandas per `.github/workflows/main.yml` controller-tests step); **20/20 key files SHA-256 recomputed and verified** against manifest (all match exactly); monitor `research_state/free_data_monitor_20261108T060017Z.json` unchanged (`checked_at_utc` `2026-11-08T06:00:17.980919+00:00`, file SHA `3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f` matches); user crontab empty (`no crontab for runner`); `/etc/cron.d/` contains only OS defaults (e2scrub_all, php, sphinxsearch, sysstat) — no research cron; `systemctl list-timers` shows only OS timers (systemd-tmpfiles-clean, sysstat-collect, phpsessionclean, fstrim, motd-news, man-db, dpkg-db-backup, logrotate, sysstat-summary, podman-auto-update, update-notifier-*, e2scrub_all, apport-autoreport, fwupd-refresh, snapd.snap-repair, ua-timer) — no matching research timers; only `.github/workflows/main.yml` present; no duplicate research workflows/processes. No code/strategy/config/raw/artifact changes. `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` updated this session.
- **2026-11-10T02:56Z (prior session)**: maintenance re-verification at HEAD `dd4d5a1` (clean). Handoff-only diff vs prior cited `ee81e34`; 75 passed (0.92s); 20/20 SHA-256 verified; monitor unchanged/stopped. No drift.
- **2026-11-10T02:52Z (prior session)**: maintenance re-verification at HEAD `3170414` (clean). Handoff-only diff vs prior cited `3cf3f29`; 75 passed (0.92s); 20/20 SHA-256 verified; monitor unchanged/stopped. No drift.
- **2026-11-10T01:38Z (prior session)**: maintenance re-verification at HEAD `a7b00cc` (clean); checkpoint commit, no code/strategy/config/raw/artifact drift. 75 passed (0.69s); 20/20 SHA-256 verified; monitor unchanged/stopped.
- **2026-11-10T01:27Z–01:16Z (prior sessions)**: repeated maintenance re-verifications (handoff-only checkpoints `fca329d`, `5a1bd00`, `3f6ce4c`, `3d76d32` et al.); each: clean or handoff-only, 75 passed (0.59–0.69s), 20/20 SHA-256 verified, monitor unchanged/stopped. No drift.
- **Prior sessions (2026-11-09T14:56Z and earlier)**: repeated maintenance re-verifications; monitor loop stopped at `research_state/free_data_monitor_20261108T060017Z.json`. Note: some older handoff text cited a stale 16-file SHA set with paths absent in current tree; discrepancy not mutated — 20-file manifest below is authoritative.

## Research status (frozen)
- **Strategy**: `STRATEGY_RULES.txt` v1.0 (MNQ 15-min ORB showcase, 09:30–09:45 ET OR, first-breakout-only, RVOL>=1.0 + ATR% 0.10–0.60%, 0.4×ATR stop, 0.4R target, $3000 risk, 15:00 ET cutoff, 15:55 ET flatten, 1 trade/day). No parameter changes.
- **Data**: axb0306 MNQ (2026-01-20..2026-04-15, 60 complete days; raw `MNQ_{15min,1min}.csv`) and kaggle front-month proxy (2022-11-16..2025-11-12, 688 days; raw `MNQ_{15min,1min}_frontmonth.csv`). 1-min audits: `research_state/1m_audit_{axb0306,kaggle}.json`. Free-data search exhausted (`data/FEASIBILITY_REPORT.md`); 06:00Z monitor stopped.
- **Results (negative net, evidence not edge)**: axb0306 net -$31,637.98 (60 trades, PF 0.492); kaggle net -$626,525.96 (688 trades, PF 0.227). Date-based WF OOS tests negative net. Do not present as profitable.

## SHA-256 manifest (20 key files, verified 2026-11-10T02:57Z and re-verified 2026-11-10T03:44Z, 2026-11-10T03:45Z, and 2026-11-10T03:47Z — all match)
| File | SHA-256 |
|---|---|
| STRATEGY_RULES.txt | 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1 |
| config/orb_mnq_15m_showcase.yaml | 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4 |
| config/orb_mnq_1m_wf_v1.yaml | ad745900a1b9adf2ef65a591eb24aa435670ac797525077d58775e53618f845b |
| data/FEASIBILITY_REPORT.md | a0a0f88eaeb0b63882d00557d6b740bb732a41b30e56ab4c5f45ce73e79bab1b |
| raw/MNQ_15min.csv | f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37 |
| raw/MNQ_15min_frontmonth.csv | 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4 |
| raw/MNQ_1min.csv | 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99 |
| raw/MNQ_1min_frontmonth.csv | edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7 |
| research_state/1m_audit_axb0306.json | 3aac07d224662c7ef514cc0e7df4a1236bcb5be312b5dc88f70a74533cb8a706 |
| research_state/1m_audit_kaggle.json | 277346323e2375485abd053d3587736778eaaae64e0b12494ae71eeb588f6041 |
| research_state/free_data_monitor_20261108T060017Z.json | 3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f |
| artifacts/README.md | 90792fb6b81103641187aad1e00dd8828446c6c62a1d192d2204f913e619552f |
| artifacts/metrics_axb0306_full.json | dddaefa2aaa23df2f34b10d5dee0220a08d6cfe6e86f9e39a19e6f912ee22f8f |
| artifacts/metrics_kaggle.json | a6ae100685ea30aa2392122fdf9830ccbaad5d25a22039db7e7521a0b12c1af1 |
| artifacts/trades_axb0306_full.json | 43672bbfe6e1198e24f412cc5c0c3bd1a7287253af493390ea1977fb12d7f115 |
| artifacts/trades_kaggle.json | 7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5 |
| artifacts/walk_forward_axb0306.json | a91cf29d4dd64ff3e690bba742c3c8e0f17079f0658bd4622cae67d4a73fff79 |
| artifacts/walk_forward_kaggle.json | cf8419973d2dbbeaea6b855ea6f483a4b469e61874334fbf3dfdebb4c7cda1a7 |
| artifacts/walk_forward_date_60_20_20_axb0306.json | f05c44b0b129ef96118e2f57b3a4a41531292efd3976ac0394bb6b8b948a5546 |
| artifacts/walk_forward_date_60_20_20_kaggle.json | eac749dc112a31df57e366203efa378e0ba5528ac6c4ee878a22bf0557781355 |

## Standing constraints
- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change must be a separately named, versioned experiment with explicit diff from baseline.
- 06:00Z maintenance loop remains stopped. Do not restart or launch nested/duplicate workflows.

(End of file - total 43 lines)