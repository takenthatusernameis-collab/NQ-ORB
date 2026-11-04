# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (verified 2026-11-04 — 284th pass COMPLETE)

- Branch: main. Working tree clean of tracked changes (`git status --short` empty); HEAD at faf3d1e (checkpoint); local HEAD matches origin/main; `git fetch origin --prune` up to date.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Canonical artifacts: all 16 JSON files in artifacts/ parse cleanly (17 directory entries incl. README.md). Walk-forward (from artifacts): axb0306 3 windows all test negative (-$10,053.14, -$21,922.10, -$23,058.98); Kaggle 8 windows all test negative (-$178,375.24, -$173,264.64, -$168,315.48, -$134,617.64, -$122,071.62, -$70,637.24, -$104,755.42, -$114,820.72).
- Baselines: axb0306 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.4917, max DD $37,491.80, Sharpe -1.06, Sortino -0.67, expectancy -$527.30/trade. Kaggle front-month 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.2271, max DD $626,994.56, Sharpe -1.68, Sortino -1.04, expectancy -$910.65/trade.
- Raw date ranges unchanged: axb0306 ends 2026-04-15; Kaggle front-month ends 2025-11-12.
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed in 0.92s.
- Frozen baseline preserved; no code/strategy/parameter changes. No leftover `_verify` artifact copies found.
- Reproducibility re-confirmed this pass: both baselines re-run from scratch via `python3 src/orb/runner.py --source axb0306 --prefix verify` and `--source kaggle --prefix verify`; every metric matched canonical artifacts exactly (win_rate, gross_pnl, net_pnl, profit_factor, max_drawdown_usd, sharpe_r, sortino_r, expectancy_usd). Verify artifacts removed after comparison.
- Free-data monitoring (2026-11-04): no new genuinely free MNQ 1min/15min source found. All candidates paid — FinzData $49 one-time, HistoricalFuturesData $59/yr, FirstRateData $99.95, Databento $125 expiring credit, MarketParquet paid archive, Yahoo Finance limited to 30 days of 1min. Kaggle remains the only free full 1min source (already ingested).

## Prior task

284th pass maintenance re-verification (2026-11-04): verified git state (HEAD faf3d1e, clean working tree, up to date with origin), recomputed all six file hashes - all match recorded values. Confirmed all 16 JSON artifacts parse cleanly. Re-read walk-forward from artifacts - all 11 test windows negative (axb0306 3 windows all negative; Kaggle 8 windows all negative). Ran full test suite - 71 passed in 0.96s. Frozen baseline preserved; no code/strategy/parameter changes. No leftover `_verify` artifact copies found. Free-data monitoring: no new genuinely free MNQ 1min/15min source (all candidates paid). Updated HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md.

## Next agent (immediate)

See INITIAL_TASK_FOR_NEXT_AGENT.md. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available, monitor for genuinely free MNQ 1min/15min data (record provenance+hash before use), do not tune/change strategy without separately named versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0. Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence.