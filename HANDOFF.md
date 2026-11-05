# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification pass — HEAD 3f19249)

- Branch: main. Working tree clean (`git status --short` empty, no untracked files); HEAD at 3f19249 (chore(kilo): checkpoint agent session). Fetched origin --prune; local main up to date with origin/main (`main` == `origin/main` == 3f19249). Recent commits: 3f19249, 6e71e87, 55f9677, 7f2ad6e, 36be7a0, 9f0eb8e, a7c4c55.
- HEAD advanced past 6e71e87/55f9677 (checkpoint doc-bumps). No code/strategy/data changes in this session.
- SHA-256 verified from disk (2026-11-05): all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Canonical artifacts: 21 files in artifacts/ (README.md + 20 JSON); all JSON parse cleanly (0 parse errors).
- Walk-forward verified from artifacts: axb0306 3 windows, all test_net_pnl negative (-$10053.14, -$21922.10, -$23058.98). Kaggle 8 windows, all test_net_pnl negative (-$178375.24, -$173264.64, -$168315.48, -$134617.64, -$122071.62, -$70637.24, -$104755.42, -$114820.72).
- Baselines verified: axb0306 60 trades, 70.0% WR, net -$31637.98 (artifacts/metrics_axb0306_full.json); Kaggle front-month 688 trades, 64.8256% WR, net -$626525.96 (artifacts/metrics_kaggle.json).
- Raw date ranges unchanged (MNQ_15min.csv/MNQ_1min.csv end 2026-04-15T23:15:00/23:29:00; MNQ_1min_frontmonth.csv/MNQ_15min_frontmonth.csv end 2025-11-12T23:59:00/23:45:00).
- Tests: `python3 -m pytest tests/` = 71 passed, 0 failed (pytest 9.2.0 available this session).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring re-scan (2026-11-05): unchanged — no new genuinely free MNQ 1min/15min full-history source found. MarketParquet offers only a limited free MNQ intraday sample pack (Apr 6-10 2026, 1min-1h, no account) plus ~365 days of daily bars with a free account; full intraday archive is paid ($79). Databento MNQ OHLCV-1m requires paid credits. Kaggle MNQ returns only brandenmorris/mnq-1-minute-data-5132025-11122025 (ends 2025-11-12, already ingested) and its byte-identical duplicate; all other hits are NQ big contract ($20/point), excluded per STRATEGY_RULES.txt. No data purchased; no credentials requested or stored.

## Prior task (completed 2026-11-05, this session — maintenance re-verification — HEAD 3f19249)

Maintenance re-verification completed this session: verified git state (working tree clean, HEAD 3f19249, fetched origin --prune, up to date with origin/main). Confirmed 3f19249 is a pure checkpoint over prior checkpoints (no code/strategy/data changes). Confirmed all six file hashes match recorded values. Confirmed artifacts parse cleanly (21 files: README.md + 20 JSON, 0 parse errors). Walk-forward structures verified (axb0306 3 windows all negative, test_net_pnl=[-10053.14, -21922.10, -23058.98]; Kaggle 8 windows all negative). Verified baselines (axb0306_full: 60 trades, 70.0% WR, net -$31637.98; Kaggle: 688 trades, 64.8256% WR, net -$626525.96) and raw date ranges (MNQ_15min/MNQ_1min end 2026-04-15T23:15:00/23:29:00; front-month end 2025-11-12T23:59:00/23:45:00). Re-ran tests (71 passed/0 failed, pytest 9.2.0). Re-ran free-data monitoring sweep (MarketParquet limited free sample only; Kaggle MNQ only the already-ingested brandenmorris dataset + byte-identical duplicate; NQ big-contract hits excluded; no new free full-history MNQ 1min/15min source). No data purchased; no credentials requested or stored. Updated HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md.

## Next agent (immediate)

See INITIAL_TASK_FOR_NEXT_AGENT.md. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available, monitor for genuinely free MNQ 1min/15min data (record provenance+SHA-256 before use), do not tune/change strategy without separately named versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0. Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence.

(End of file)
