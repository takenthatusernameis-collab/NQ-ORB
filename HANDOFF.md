# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification pass — HEAD 6cc0601)

- Branch: main. Working tree clean (`git status --short` empty); HEAD at 6cc0601 (chore(kilo): checkpoint agent session, controller-committed 2026-11-04T21:49:03Z). Fetched origin --prune; local main up to date with origin/main. Recent commits: 6cc0601, 7ab124e, 7287ad5, 4d00661, b007093.
- SHA-256 verified from disk (2026-11-04): all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Canonical artifacts: 21 files in artifacts/ including README.md; 20 JSON files parse cleanly. Walk-forward (axb0306): 3 windows, all test_net_pnl negative (-$10053.14, -$21922.10, -$23058.98). Walk-forward (kaggle): 8 windows, all test_net_pnl negative (-$178375.24, -$173264.64, -$168315.48, -$134617.64, -$122071.62, -$70637.24, -$104755.42, -$114820.72).
- Baselines confirmed from canonical artifacts: axb0306 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.4917, max DD $37,491.80, Sharpe -1.06, Sortino -0.67, expectancy -$527.30/trade. Kaggle front-month 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.2271, max DD $626,994.56, Sharpe -1.68, Sortino -1.04, expectancy -$910.65/trade.
- Raw date ranges unchanged: axb0306 ends 2026-04-15; Kaggle front-month ends 2025-11-12.
- Tests: pandas + pytest installed in env; full suite `python3 -m pytest tests/` = 71 passed, 0 failed (re-confirmed this session).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring re-scan (2026-11-04): unchanged — no new genuinely free MNQ 1min/15min source. axb0306 ends 2026-04-15 (stale). Kaggle brandenmorris MNQ (CC BY 4.0) confirmed still ends 2025-11-12 (no newer file on dataset page); final ~2.9 months remain untouched OOS. Paid/key-gated candidates unchanged as recorded. Kaggle remains the only free full 1min MNQ source already ingested. No free source extends Kaggle 2025-11-12 without purchase.

## Prior task (completed 2026-11-04, session at HEAD 7ab124e — maintenance re-verification)

Maintenance re-verification completed prior session: verified git state (working tree clean, HEAD 7ab124e, fetched origin --prune, up to date with origin/main). Confirmed all six file hashes match recorded values (STRATEGY_RULES.txt 6d3258c3...; config/orb_mnq_15m_showcase.yaml 2a6c5ff8...; raw/MNQ_15min.csv f417f22d...; raw/MNQ_1min.csv 129623f4...; raw/MNQ_1min_frontmonth.csv edbadc73...; raw/MNQ_15min_frontmonth.csv 7e129ae3...). Confirmed artifacts parse cleanly (21 files total; 20 JSON). Full test suite 71 passed / 0 failed. Walk-forward structures verified (axb0306 3 windows all test_net_pnl negative: -$10053.14, -$21922.10, -$23058.98; Kaggle 8 windows all test_net_pnl negative: -$178375.24, -$173264.64, -$168315.48, -$134617.64, -$122071.62, -$70637.24, -$104755.42, -$114820.72). Re-ran free-data monitoring sweep; no new genuinely free MNQ 1min/15min source found. Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored. Updated HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md (controller-committed as HEAD 6cc0601).

## Prior task (completed 2026-11-04, this session — maintenance re-verification — HEAD 6cc0601)

Maintenance re-verification completed this session: verified git state (working tree clean, HEAD 6cc0601, fetched origin --prune, up to date with origin/main; recent commits 6cc0601, 7ab124e, 7287ad5, 4d00661, b007093). Confirmed all six file hashes match recorded values (same six values as above). Confirmed raw date ranges unchanged from disk (MNQ_15min.csv/MNQ_1min.csv end 2026-04-15; MNQ_1min_frontmonth.csv/MNQ_15min_frontmonth.csv end 2025-11-12). Confirmed artifacts parse cleanly (21 files total; 20 JSON, 0 parse errors). Confirmed walk-forward structures from artifacts (axb0306 3 windows all negative; Kaggle 8 windows all negative; values as listed above). Full test suite `python3 -m pytest tests/` = 71 passed, 0 failed. Re-ran free-data monitoring sweep; no new genuinely free MNQ 1min/15min source found (Kaggle brandenmorris MNQ CC BY 4.0 still capped 2025-11-12; axb0306 stale at 2026-04-15; all other candidates paid/key-gated/limited). Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored. Updated HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md.

## Next agent (immediate)

See INITIAL_TASK_FOR_NEXT_AGENT.md. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available, monitor for genuinely free MNQ 1min/15min data (record provenance+SHA256 before use), do not tune/change strategy without separately named versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0. Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence.

(End of file)
