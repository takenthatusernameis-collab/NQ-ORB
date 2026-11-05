# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification pass — HEAD 41d6d6a)

- Branch: main. Working tree clean (`git status --short` empty, no untracked files); HEAD at e39a863 (chore(kilo): checkpoint agent session). Fetched origin --prune; local main up to date with origin/main (`main` == `origin/main` == e39a863). Recent commits: e39a863, 41d6d6a, ee49188, d372430, b021d09, fe68455, b2c4da2, 70add8d, 2794b06, d2bd42b, bfd59c4.
- HEAD advanced via checkpoints since prior verified state; no code/strategy/data changes in this session.
- SHA-256 verified from disk (2026-11-05): all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Canonical artifacts: 21 files in artifacts/ (README.md + 20 JSON); all JSON parse cleanly (0 parse errors).
- Determinism: prior verified byte-identical metrics and trade-ledger SHA-256 (axb0306 ce389da2488474a6d0d994cf99bb1e6509761d80f85986f1f8da3e1738b6a364; kaggle 7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5). State unchanged.
- Walk-forward verified from artifacts: axb0306 3 windows, all test_net_pnl negative (-$10053.14, -$21922.10, -$23058.98). Kaggle 8 windows, all test_net_pnl negative (-$178375.24, -$173264.64, -$168315.48, -$134617.64, -$122071.62, -$70637.24, -$104755.42, -$114820.72).
- Baselines verified: axb0306 60 trades, 70.0% WR, net -$31637.98 (artifacts/metrics_axb0306_full.json); Kaggle front-month 688 trades, 64.8256% WR, net -$626525.96 (artifacts/metrics_kaggle.json).
- Raw date ranges unchanged (MNQ_15min.csv/MNQ_1min.csv end 2026-04-15T23:15:00/23:29:00; MNQ_1min_frontmonth.csv/MNQ_15min_frontmonth.csv end 2025-11-12T23:59:00/23:45:00).
- Tests: `python3 -m pytest tests/` = 71 passed, 0 failed (pytest 9.2.0 available this session).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring re-scan (2026-11-05): unchanged — no new genuinely free MNQ 1min/15min full-history source found. axb0306/cme-futures-ohlc last MNQ-path commit still 60abd3fb dated 2026-04-15T23:34:55Z (stale ~6.5 months); live MNQ/ directory listing still exactly the same 8 files, no extension of intraday history. MarketParquet limited sample only; full archive paid. Kaggle MNQ only already-ingested brandenmorris dataset + byte-identical duplicate; NQ big-contract hits excluded.

## Prior task (completed 2026-11-05, this session — maintenance re-verification — HEAD 41d6d6a)

Maintenance re-verification completed this session: verified git state (working tree clean, HEAD d372430, fetched origin --prune, up to date with origin/main). Confirmed all six file hashes match recorded values. Confirmed artifacts parse cleanly (21 files: README.md + 20 JSON, 0 parse errors). Re-ran tests (71 passed/0 failed). Walk-forward/baselines unchanged from artifacts. Re-scanned free-data sources (no new genuinely free MNQ 1min/15min full-history; axb0306 MNQ path still at commit 60abd3fb dated 2026-04-15T23:34:55Z, stale ~6.5 months, no history extension). No data purchased; no credentials requested/stored. Updated HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md.

## Next agent (immediate)

See INITIAL_TASK_FOR_NEXT_AGENT.md. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available, monitor for genuinely free MNQ 1min/15min data (record provenance+SHA-256 before use), do not tune/change strategy without separately named versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0. Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence.

## Maintenance re-verification pass — 2026-11-05 (HEAD 20260c0)

- Repo state: working tree clean (`git status --short` empty, no untracked files); `git fetch origin --prune` clean; local main == origin/main == 20260c0. HEAD advanced via `chore(kilo): checkpoint agent session` commits since prior verified state (20260c0, e39a863, 41d6d6a); no code/strategy/data changes.
- SHA-256 re-verified from disk: all six tracked file hashes match recorded values (STRATEGY_RULES.txt 6d3258c3…; config/orb_mnq_15m_showcase.yaml 2a6c5ff8…; raw/MNQ_15min.csv f417f22d…; raw/MNQ_1min.csv 129623f4…; raw/MNQ_1min_frontmonth.csv edbadc73…; raw/MNQ_15min_frontmonth.csv 7e129ae3…).
- Determinism re-verified from fresh process (`python3 src/orb/runner.py --prefix verify_axb --source axb0306` / `--prefix verify_kag --source kaggle`): axb0306 net -$31,637.98 (matches recorded); kaggle net -$626,525.96 (matches recorded). Trade-ledger SHA-256 byte-identical: axb0306 `ce389da2488474a6d0d994cf99bb1e6509761d80f85986f1f8da3e1738b6a364`; kaggle `7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5`. Metrics files (`artifacts/metrics_verify_*.json`) also byte-identical. Verify copies deleted after comparison.
- Artifacts: 21 files (README.md + 20 JSON); all parse cleanly (0 parse errors). Walk-forward unchanged: axb0306 3 windows, all test_net_pnl negative ([-$10,053.14, -$21,922.10, -$23,058.98]); Kaggle 8 windows, all negative ([-$178,375.24, -$173,264.64, -$168,315.48, -$134,617.64, -$122,071.62, -$70,637.24, -$104,755.42, -$114,820.72]).
- Raw date ranges unchanged: MNQ_15min.csv 2026-01-20T13:15 → 2026-04-15T23:15; MNQ_1min.csv 2026-01-20T13:27 → 2026-04-15T23:29; front-month files end 2025-11-12T23:45/23:59.
- Tests: `python3 -m pytest tests/` = 71 passed, 0 failed.
- Free-data re-scan (2026-11-05): no new genuinely free MNQ 1min/15min full-history source. Confirmed paid/key-gated: historicalfuturesdata.com ($59/yr per bar size; free tier = latest-month 10s sample + daily for registered users), FinzData ($49 one-time; free tier = last 30 days daily only), FirstRate ($99.95/yr after 1 free month; sample ZIP only), MarketParquet ($79 one-time intraday archive; free tier daily-only ~365 days + 1-week sample pack), Kibot ($520 all-futures continuous 1-min), Portara (paid), Databento (key-gated + credit-based), Barchart (free = 2yr daily, 1 download/day; intraday needs Premier), Yahoo Finance (MNQ=F daily only; 1-min = last 30 days only), investing.com (daily-only), CME DataMine (samples only). Kaggle MNQ hits remain brandenmorris (ends 2025-11-12, already ingested) + byte-identical duplicate; all other hits are NQ big contract ($20/point, excluded per STRATEGY_RULES.txt) or non-MNQ. No data purchased; no credentials requested or stored.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.

(End of file)
