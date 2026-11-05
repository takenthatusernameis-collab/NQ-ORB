# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification pass — HEAD 6326f53)
- Branch: main. Working tree clean (`git status --short` empty); HEAD at 6326f53 (chore: capture completed workflow run diagnostics). Fetched origin --prune; local main up to date with origin/main. Recent commits: 6326f53, 7c9a762, 0b6435f, cb67d10, b76d3f8.
- SHA-256 verified from disk (2026-11-05): all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Canonical artifacts: 17 files in artifacts/ (README.md + 16 JSON); all JSON parse cleanly (0 parse errors).
- Walk-forward verified from artifacts: axb0306 3 windows, all test_net_pnl negative (-$10053.14, -$21922.10, -$23058.98). Kaggle 8 windows, all test_net_pnl negative (-$178375.24, -$173264.64, -$168315.48, -$134617.64, -$122071.62, -$70637.24, -$104755.42, -$114820.72).
- Raw date ranges unchanged (MNQ_15min.csv/MNQ_1min.csv end 2026-04-15; MNQ_1min_frontmonth.csv/MNQ_15min_frontmonth.csv end 2025-11-12).
- Tests: pytest not installed in current environment; repository test files present (tests/orb/*, test_walk_forward.py, etc.). Cannot run full `python3 -m pytest tests/` here; test suite state was last recorded as 71 passed, 0 failed in prior sessions.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring re-scan (2026-11-05): unchanged — no new genuinely free MNQ 1min/15min source found. Kaggle brandenmorris MNQ (CC BY 4.0) remains capped 2025-11-12; axb0306 remains stale at 2026-04-15; other candidates remain paid/key-gated/limited.

## Prior task (completed 2026-11-05, this session — maintenance re-verification — HEAD 6326f53)

Maintenance re-verification completed this session: verified git state (working tree clean, HEAD 6326f53, fetched origin --prune, up to date with origin/main). Confirmed all six file hashes match recorded values. Confirmed artifacts parse cleanly (17 files; 0 JSON parse errors). Walk-forward structures verified (axb0306 3 windows all negative; Kaggle 8 windows all negative). Confirmed raw date ranges unchanged. Reviewed prior test status (71 passed/0 failed recorded previously). Re-ran free-data monitoring sweep; no new genuinely free MNQ 1min/15min source found. Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored. Updated HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md.

## Next agent (immediate)

See INITIAL_TASK_FOR_NEXT_AGENT.md. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available, monitor for genuinely free MNQ 1min/15min data (record provenance+SHA256 before use), do not tune/change strategy without separately named versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0. Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence.
