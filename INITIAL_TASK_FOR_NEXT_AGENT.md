# Initial Task for Next Agent

## Status (session 2026-11-04 — maintenance re-verification pass COMPLETE, HEAD 2f645b8)

- Branch main; HEAD 2f645b8 (chore(kilo): checkpoint agent session, controller-committed 2026-11-04T22:41:20Z); working tree clean (`git status --short` empty); fetched origin --prune; up to date with origin/main. Recent commits: 2f645b8, d66115c, 661fded, 6cc0601, 7ab124e.
- SHA-256 verified from disk (2026-11-04): all six tracked file hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Tests: pandas + pytest installed for verification; full suite `python3 -m pytest tests/` = 71 passed, 0 failed.
- Artifacts: 21 files in artifacts/ (README.md); 20 JSON parse cleanly. Walk-forward axb0306 3/3 test windows negative (-$10053.14, -$21922.10, -$23058.98). Walk-forward Kaggle 8/8 test windows negative (-$178375.24, -$173264.64, -$168315.48, -$134617.64, -$122071.62, -$70637.24, -$104755.42, -$114820.72).
- Baselines from canonical artifacts: axb0306 net -$31,637.98, 60 trades (70.0% WR); Kaggle front-month net -$626,525.96, 688 trades (64.83% WR).
- Raw date ranges unchanged: axb0306 ends 2026-04-15; Kaggle front-month ends 2025-11-12.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data re-scan (2026-11-04): Kaggle brandenmorris MNQ (CC BY 4.0) still capped at 2025-11-12 (no newer file on dataset page); final ~2.9 months remain untouched OOS. axb0306 ends 2026-04-15 (stale). Paid/key-gated candidates unchanged. No genuinely free MNQ 1min/15min source found to extend coverage.

## Status (session 2026-11-04 — maintenance re-verification pass COMPLETE, HEAD d66115c)

- Branch main; HEAD d66115c (chore(kilo): checkpoint agent session, controller-committed 2026-11-04T21:51:37Z); working tree clean (`git status --short` empty); fetched origin --prune; up to date with origin/main. Recent commits: d66115c, 661fded, 6cc0601, 7ab124e, 7287ad5.
- SHA-256 verified from disk (2026-11-04): all six tracked file hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Tests: pandas + pytest installed for verification; full suite `python3 -m pytest tests/` = 71 passed, 0 failed.
- Artifacts: 21 files in artifacts/ (README.md); 20 JSON parse cleanly. Walk-forward axb0306 3/3 test windows negative (-$10053.14, -$21922.10, -$23058.98). Walk-forward Kaggle 8/8 test windows negative (-$178375.24, -$173264.64, -$168315.48, -$134617.64, -$122071.62, -$70637.24, -$104755.42, -$114820.72).
- Baselines from canonical artifacts: axb0306 net -$31,637.98, 60 trades (70.0% WR); Kaggle front-month net -$626,525.96, 688 trades (64.83% WR).
- Raw date ranges unchanged: axb0306 ends 2026-04-15; Kaggle front-month ends 2025-11-12.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data re-scan (2026-11-04): Kaggle brandenmorris MNQ (CC BY 4.0) still capped at 2025-11-12 (no newer file on dataset page); final ~2.9 months remain untouched OOS. axb0306 ends 2026-04-15 (stale). Paid/key-gated candidates unchanged. No genuinely free MNQ 1min/15min source found to extend coverage.

- Branch main; HEAD 6cc0601 (chore(kilo): checkpoint agent session, controller-committed 2026-11-04T21:49:03Z); working tree clean (`git status --short` empty); fetched origin --prune; up to date with origin/main. Recent commits: 6cc0601, 7ab124e, 7287ad5, 4d00661, b007093.
- SHA-256 verified from disk (2026-11-04): all six tracked file hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Tests: pandas + pytest installed for verification; full suite `python3 -m pytest tests/` = 71 passed, 0 failed.
- Artifacts: 21 files in artifacts/ (README.md); 20 JSON parse cleanly. Walk-forward axb0306 3/3 test windows negative (-$10053.14, -$21922.10, -$23058.98). Walk-forward Kaggle 8/8 test windows negative (-$178375.24, -$173264.64, -$168315.48, -$134617.64, -$122071.62, -$70637.24, -$104755.42, -$114820.72).
- Baselines from canonical artifacts: axb0306 net -$31,637.98, 60 trades (70.0% WR); Kaggle front-month net -$626,525.96, 688 trades (64.83% WR).
- Raw date ranges unchanged: axb0306 ends 2026-04-15; Kaggle front-month ends 2025-11-12.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data re-scan (2026-11-04): Kaggle brandenmorris MNQ (CC BY 4.0) still capped at 2025-11-12 (no newer file on dataset page); final ~2.9 months remain untouched OOS. axb0306 ends 2026-04-15 (stale). Paid/key-gated candidates unchanged. No genuinely free MNQ 1min/15min source found to extend coverage.

## Tasks (maintenance only)

1. **Re-verify** repo state (`git status`/`git log`/`git fetch origin --prune`), file hashes vs recorded values (the six tracked files listed in HANDOFF.md), canonical artifacts parseable, walk-forward present and all test windows negative. Run tests (`python3 -m pytest tests/`) if available.
2. **Optional reproducibility**: re-run both baselines from scratch (`python3 src/orb/runner.py --source axb0306 --prefix <name>` and `--source kaggle --prefix <name>`) and confirm metrics/trades match canonical artifacts. Remove any copies after comparison.
3. **Data monitoring**: watch for a new genuinely free MNQ 1min/15min source. If found, record source/license/access constraints, retrieval time, contract symbols/months, session timezone, bar timestamps, gaps, roll rules, adjustment method, and SHA-256 before any use. Known free: axb0306 (stale, ends 2026-04-15) and Kaggle front-month (ends 2025-11-12). All other candidates paid/key-gated/limited.
4. **No experiments without approval**: no parameter/strategy/rule changes without separately named, versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0.
5. **Update docs**: update HANDOFF.md and this file with concrete evidence if anything changes.

## Hard boundaries (AGENTS.md)

- Historical research and simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both baselines negative under full costs; all walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- axb0306 roll/adjustment: single-contract MNQ.M26, no roll inside sample; verify hash/continuity before re-downloading.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.

## Why this task

Maintenance/re-verification only. Do NOT tune stops/targets/filters/sizing/session times — STRATEGY_RULES.txt v1.0 frozen. Only (a) verify frozen baseline intact/reproducible, (b) watch for genuinely free MNQ 1min/15min data (provenance+SHA256 before use), (c) refresh HANDOFF.md/this file.
