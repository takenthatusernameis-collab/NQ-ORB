# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification pass — HEAD 2006d4d)

- Branch: main. Working tree clean (`git status --short` empty, no untracked files); HEAD at 2006d4d (chore(kilo): checkpoint agent session). Fetched origin --prune; local main up to date with origin/main (`main` == `origin/main` == 2006d4d). Recent commits: 2006d4d, e1a15ff, 20260c0, e39a863, 41d6d6a, 71c6da9, ee49188, d372430, b021d09, fe68455.
- HEAD advanced via checkpoints since prior verified state; no code/strategy/data changes in this session.
- SHA-256 verified from disk (2026-11-05): all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Canonical artifacts: 25 files in artifacts/ (all JSON parse cleanly, 0 parse errors).
- Determinism state unchanged from prior verified values (axb0306 trade-ledger axb0306 ce389da2488474a6d0d994cf99bb1e6509761d80f85986f1f8da3e1738b6a364; kaggle 7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5).
- Walk-forward verified from artifacts (prior): axb0306 3 windows, all test_net_pnl negative (-$10053.14, -$21922.10, -$23058.98). Kaggle 8 windows, all test_net_pnl negative (-$178375.24, -$173264.64, -$168315.48, -$134617.64, -$122071.62, -$70637.24, -$104755.42, -$114820.72).
- Baselines verified (prior): axb0306 60 trades, 70.0% WR, net -$31637.98 (artifacts/metrics_axb0306_full.json); Kaggle front-month 688 trades, 64.8256% WR, net -$626525.96 (artifacts/metrics_kaggle.json).
- Raw date ranges unchanged (MNQ_15min.csv/MNQ_1min.csv end 2026-04-15T23:15:00/23:29:00; MNQ_1min_frontmonth.csv/MNQ_15min_frontmonth.csv end 2025-11-12T23:45:00/23:59:00).
- Tests: `python3 -m pytest tests/` = 71 passed, 0 failed (pytest 9.2.0).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring: unchanged — no new genuinely free MNQ 1min/15min full-history source found. Prior findings remain valid.

## Prior task (completed 2026-11-05, this session — maintenance re-verification — HEAD 2006d4d)

Maintenance re-verification completed: verified git state (working tree clean, HEAD 2006d4d, fetched origin --prune, up to date with origin/main). Confirmed all six file hashes match recorded values. Confirmed artifacts parse cleanly (25 files, 0 parse errors). Re-ran tests (71 passed/0 failed). Walk-forward/baselines unchanged from artifacts. Re-scanned free-data context (no changes). No data purchased; no credentials requested/stored. Updated HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md.

## Next agent (immediate)

See INITIAL_TASK_FOR_NEXT_AGENT.md. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available, monitor for genuinely free MNQ 1min/15min data (record provenance+SHA-256 before use), do not tune/change strategy without separately named versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0. Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence.

## Maintenance re-verification pass — 2026-11-05 (HEAD 20260c0) [historical]

- Repo state: working tree clean; local main == origin/main == 20260c0. Determinism re-verified from fresh process (axb0306 net -$31,637.98, kaggle net -$626,525.96; trade-ledger SHA-256 byte-identical). Artifacts 21 files, all parse cleanly. Tests 71 passed/0 failed. Free-data re-scan confirmed no new genuinely free MNQ 1min/15min full-history source.

(End of file)
