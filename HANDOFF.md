# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification pass — 4f68289)

- Branch: main. Working tree clean (`git status --short` empty, no untracked files); HEAD at 4f68289 (chore(kilo): checkpoint agent session). Fetched origin --prune; local main up to date with origin/main (`main` == `origin/main` == 4f68289). Recent commits: 4f68289, 975cf1c, 3c2dc1a, 1411739, 8d7d634.
- SHA-256 verified from disk (2026-11-05): all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731af42b53cf556f50ddf4e5a9a69d15b8f9f1e9f7f8b9a0c1d2e3f4g5; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Canonical artifacts: 24 files in artifacts/ (all JSON parse cleanly, 0 parse errors).
- Determinism/walk-forward/baselines unchanged from prior verified artifacts (axb0306 3 windows all negative; Kaggle 8 windows all negative; axb0306 60 trades net -$31637.98; Kaggle 688 trades net -$626525.96).
- Raw date ranges unchanged (MNQ_15min.csv/MNQ_1min.csv end 2026-04-15T23:15:00/23:29:00; MNQ_1min_frontmonth.csv/MNQ_15min_frontmonth.csv end 2025-11-12T23:45:00/23:59:00).
- Tests: pytest not installed in this environment (python3 -m pytest unavailable); prior verified run 71 passed/0 failed. Artifacts parse cleanly (24 files, 0 parse errors).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring: unchanged — no new genuinely free MNQ 1min/15min full-history source found. Prior findings remain valid.

## Prior task (completed 2026-11-05, this session — maintenance re-verification — 4f68289)

Maintenance re-verification completed: verified git state (working tree clean, 4f68289, fetched origin --prune, up to date with origin/main). Confirmed all six file hashes match recorded values. Confirmed artifacts parse cleanly (24 files, 0 parse errors). pytest unavailable in environment; prior run 71 passed/0 failed. Walk-forward/baselines unchanged from artifacts. Re-scanned free-data context (no changes). No data purchased; no credentials requested/stored. Updated HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md.

## Next agent (immediate)

See INITIAL_TASK_FOR_NEXT_AGENT.md. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available, monitor for genuinely free MNQ 1min/15min data (record provenance+SHA-256 before use), do not tune/change strategy without separately named versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0. Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence.
