# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification pass — HEAD 2cfb3cf)

- Branch: main. Working tree clean (`git status --short` empty); HEAD at 2cfb3cf (chore(kilo): checkpoint agent session). Recent commits: 2cfb3cf, 92f571f, ac83f67, 1e383ad, ecb4388. Fetched origin --prune.
- SHA-256 verified from disk (2026-11-04): all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Canonical artifacts: 16 JSON files in artifacts/ parse cleanly (plus README.md). Walk-forward: walk_forward_axb0306.json 3 windows all test negative (-$10,053.14, -$21,922.10, -$23,058.98); walk_forward_kaggle.json 8 windows all test negative (-$178,375.24, -$173,264.64, -$168,315.48, -$134,617.64, -$122,071.62, -$70,637.24, -$104,755.42, -$114,820.72).
- Baselines (canonical): axb0306 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.4917, max DD $37,491.80, Sharpe -1.06, Sortino -0.67, expectancy -$527.30/trade. Kaggle front-month 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.2271, max DD $626,994.56, Sharpe -1.68, Sortino -1.04, expectancy -$910.65/trade.
- Raw date ranges unchanged: axb0306 ends 2026-04-15; Kaggle front-month ends 2025-11-12.
- Tests: pandas + pytest installed in env; full suite `python3 -m pytest tests/` = 71 passed, 0 failed.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring re-scan (2026-11-04): unchanged, no new genuinely free MNQ 1min/15min source. axb0306/cme-futures-ohlc MNQ ends 2026-04-15 (stale ~6.5 months). Kaggle brandenmorris MNQ ends 2025-11-12 (CC BY 4.0). All other candidates paid/key-gated/limited. Kaggle remains only free full 1min source already ingested. No source extends Kaggle 2025-11-12 without purchase.

## Prior task (completed 2026-11-04)

Maintenance re-verification completed this session: verified git state (HEAD 92f571f, clean working tree, fetched origin --prune). Confirmed all six file hashes match recorded values. Confirmed all 16 artifact JSONs parse cleanly. Walk-forward all test windows negative. Full test suite 71 passed / 0 failed. Free-data re-scan unchanged. Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored. Updated HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md.

## Next agent (immediate)

See INITIAL_TASK_FOR_NEXT_AGENT.md. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available, monitor for genuinely free MNQ 1min/15min data (record provenance+SHA256 before use), do not tune/change strategy without separately named versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0. Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence.
