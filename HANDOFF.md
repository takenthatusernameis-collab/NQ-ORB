# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (verified 2026-11-04 — maintenance re-verification, 235th pass, COMPLETE)

- Branch: main. Working tree clean (`git status --short` empty). HEAD: c1ad4ed (chore(kilo): checkpoint agent session, in sync with origin/main after `git fetch origin --prune`). Prior recorded HEAD 2ab601c superseded by new checkpoint commit c1ad4ed.
- SHA-256 (recomputed from disk): STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4.
- Canonical artifacts (present + parseable): 21 JSON files in artifacts/ validated parse cleanly.
- Walk-forward detail (test windows): axb0306 — all 3 test windows negative (test net -$10,053.14, -$21,922.10, -$23,058.98). Kaggle — all 8 test windows negative (test net_pnl -$178,375.24, -$173,264.64, -$168,315.48, -$134,617.64, -$122,071.62, -$70,637.24, -$104,755.42, -$114,820.72). Final test window untouched by parameter selection.
- Baselines re-confirmed from canonical artifacts: axb0306 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.492, max DD $37,491.80, Sharpe -1.06, Sortino -0.67, expectancy -$527.30/trade. Kaggle front-month 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.227, max DD ~$626,994.56, Sharpe -1.68, Sortino -1.04, expectancy -$910.65/trade.
- Raw date ranges unchanged: axb0306 ends 2026-04-15 (1min last 2026-04-15T23:29, 15min last 2026-04-15T23:15); Kaggle front-month ends 2025-11-12 (1min 2025-11-12T23:59, 15min 2025-11-12T23:45).
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed in 0.93s.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no data purchased; no credentials requested/stored. Free-data monitoring re-sweep (2026-11-04): no new genuinely free MNQ 1min/15min source found. Paid/proprietary only: MarketParquet ($79 one-time archive, free = ~1yr daily + 1-week intraday sample pack), FirstRate Data (sample only), Kibot ($820 one-time), FinzData ($29 one-time; free = last 30 days daily), Portara (paid), CME DataMine (paid, requires SSO/license). Free-limited: Databento ($125 signup credit, expires 6 months — treated as paid, not free archive), historicalfuturesdata.com free account (MNQ limited to ~3 months, no full history), Yahoo Finance (MNQ=F daily only; 1-min only last 30 days). Kaggle `tgtanalytics/nq-futures-1min-bar-2022-2025` (Apache 2.0, ~1.05M rows, NQ E-mini not MNQ, 2022-12-26..2025-12-11) is a different instrument — not adopted. Known free unchanged: axb0306 (~3 months, single-contract MNQ.M26, unadjusted) and Kaggle front-month (~3 years, unadjusted, ends 2025-11-12, CC BY 4.0). Do not purchase data; never store credentials.

## Prior task

235th pass maintenance re-verification (this session): `git status` clean (HEAD c1ad4ed, in sync with origin/main after fetch/prune). All six file hashes recomputed from disk match recorded values exactly. 21 canonical artifacts parse cleanly. Walk-forward test windows confirmed all negative (axb0306 3/3, Kaggle 8/8). Baselines re-confirmed from canonical artifacts. Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed in 0.98s. Free-data monitoring re-swept (2026-11-04): no new genuinely free MNQ 1min/15min source found. Re-confirmed paid/proprietary only: MarketParquet ($79 one-time), FirstRate Data (sample only), Kibot ($820 one-time for MNQ continuous), FinzData ($29 one-time; free = last 30 days daily), Portara (paid), CME DataMine (paid). Free-limited unchanged: Databento ($125 credit, expires 6 months), historicalfuturesdata.com (~3 months MNQ only), Yahoo Finance (MNQ=F daily only). No code/strategy/parameter changes made; working tree clean.

## Next agent (immediate)

See INITIAL_TASK_FOR_NEXT_AGENT.md. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available, monitor for genuinely free MNQ 1min/15min data (record provenance+hash before use), do not tune/change strategy without separately named versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0. Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence.

## Free-data monitoring log (2026-11-04, 233rd pass)

Two web searches executed: "free MNQ micro e-mini nasdaq 100 futures 1 minute 15 minute historical data download csv" and "free nasdaq 100 futures intraday historical data 1min 15min open source dataset 2026". Result: no new genuinely free MNQ 1min/15min source. All candidates re-classified:

- **Paid/proprietary (rejected)**: Portara (MNQ intraday 1-min from 2019, paid), FirstRate Data (MNQ continuous from 2019-05-05, paid; free sample only), Kibot (MNQ continuous 1-min $520 / 15-min $150 one-time, paid), FinzData (MNQ full history $29 one-time; free = last 30 days daily only), MarketParquet (MNQ archive $79 one-time; free = ~1yr daily + 1-week intraday sample pack), CME DataMine (paid, SSO/license required).
- **Free-limited (rejected)**: Databento ($125 signup credit, expires 6 months — not a free archive), historicalfuturesdata.com (MNQ free account limited to ~3 months, no full history), Yahoo Finance (MNQ=F daily only; 1-min only last 30 days).
- **Wrong instrument (rejected)**: Kaggle `youneseloiarm/nasdaq-cme-future-nq` (CC0, NQ E-mini not MNQ), Kaggle `tgtanalytics/nq-futures-1min-bar-2022-2025` (NQ E-mini not MNQ), HF Data Library (US equities/ETFs 1-min only, no futures).
- **Known free (retained, unchanged)**: axb0306/cme-futures-ohlc (single-contract MNQ.M26, unadjusted, ~3 months, ends 2026-04-15); Kaggle front-month (CC BY 4.0, unadjusted, ~3 years, ends 2025-11-12).
