# Initial Task for Next Agent

## Status (session 2026-11-03 — maintenance re-verification, one-hundred-thirty-sixth pass, COMPLETE)
- Branch main; working tree clean; up to date with origin/main (verified via `git fetch origin`: local HEAD 138716c == origin/main 138716c). HEAD advanced to 138716c from 1b7a6a2; that commit is docs-only (HANDOFF.md, INITIAL_TASK_FOR_NEXT_AGENT.md), no code/data/config/artifact changes.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1, config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4, raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37, raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99, raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7, raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Canonical artifacts present + parseable, SHA-256 identical to recorded: artifacts/metrics_axb0306.json (e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f), artifacts/metrics_kaggle.json (a6ae100685ea30aa2392122fdf9830ccbaad5d25a22039db7e7521a0b12c1af1). Trade ledger identical (axb0306 ce389da2488474a6d0d994cf99bb1e6509761d80f85986f1f8da3e1738b6a364, kaggle 7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5). Walk-forward identical (axb0306 a91cf29d4dd64ff3e690bba742c3c8e0f17079f0658bd4622cae67d4a73fff79/3 windows, kaggle cf8419973d2dbbeaea6b855ea6f483a4b469e61874334fbf3dfdebb4c7cda1a7/8 windows). All parse cleanly.
- Walk-forward: axb0306 all 3 test windows negative (net -$10,053.14, -$21,922.10, -$23,058.98); Kaggle all 8 test windows negative (net -$178,375.24 to -$114,820.72, final test window 2025-01-03..2025-08-28).
- Raw date ranges unchanged: axb0306 ends 2026-04-15; Kaggle front-month ends 2025-11-12.
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src /tmp/controller-tests-venv/bin/python -m pytest tests -q` -> 71 passed in 0.87s.
- Frozen baseline preserved; no code/strategy/parameter changes; working tree clean.
- Free-data monitoring 2026-11-03: no new genuinely free MNQ 1min/15min source found. No purchase/credentials. axb0306 last commit 60abd3fb dated 2026-04-15T23:34:55Z (unchanged); Kaggle brandenmorris both datasets "Updated a year ago", coverage ends 2025-11-12 (unchanged).

## Tasks (maintenance only)
1. **Re-verify** repo state (git status/log/fetch), file hashes vs recorded values, canonical artifacts parseable, walk-forward present and all test windows negative. Run tests if available.
2. **Data monitoring**: watch for a new genuinely free MNQ 1min/15min source. If found, record source/license/access constraints, retrieval time, contract symbols/months, session timezone, bar timestamps, gaps, roll rules, adjustment method, and SHA-256 before any use. Known free: axb0306 (single-contract MNQ.M26, unadjusted) and Kaggle front-month (unadjusted). Do not purchase data; never store credentials.
3. **No experiments without approval**: no parameter/strategy/rule changes without separately named, versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0.
4. **Update docs**: update HANDOFF.md and this file with concrete evidence if anything changes.

## Hard boundaries (AGENTS.md)
- Historical research and simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work
- Research blocked on data depth; both baselines negative under full costs; all walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- axb0306 roll/adjustment: single-contract MNQ.M26, no roll inside sample; repo update script hard-codes one contract ID — re-verify hash/continuity before re-downloading.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.

## Why this task
Maintenance/re-verification only. Do NOT tune stops/targets/filters/sizing/session times — STRATEGY_RULES.txt v1.0 frozen. Only (a) verify frozen baseline intact/reproducible, (b) watch for genuinely free MNQ 1min/15min data (provenance+SHA256 before use), (c) refresh HANDOFF.md/this file.

## Tasks (maintenance only)
1. **Re-verify** repo state (git status/log/fetch), file hashes vs recorded values, canonical artifacts parseable, walk-forward present and all test windows negative. Run tests if available.
2. **Data monitoring**: watch for a new genuinely free MNQ 1min/15min source. If found, record source/license/access constraints, retrieval time, contract symbols/months, session timezone, bar timestamps, gaps, roll rules, adjustment method, and SHA-256 before any use. Known free: axb0306 (single-contract MNQ.M26, unadjusted) and Kaggle front-month (unadjusted). Do not purchase data; never store credentials.
3. **No experiments without approval**: no parameter/strategy/rule changes without separately named, versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0.
4. **Update docs**: update HANDOFF.md and this file with concrete evidence if anything changes.

## Hard boundaries (AGENTS.md)
- Historical research and simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work
- Research blocked on data depth; both baselines negative under full costs; all walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- axb0306 roll/adjustment: single-contract MNQ.M26, no roll inside sample; repo update script hard-codes one contract ID — re-verify hash/continuity before re-downloading.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.

## Why this task
Maintenance/re-verification only. Do NOT tune stops/targets/filters/sizing/session times — STRATEGY_RULES.txt v1.0 frozen. Only (a) verify frozen baseline intact/reproducible, (b) watch for genuinely free MNQ 1min/15min data (provenance+SHA256 before use), (c) refresh HANDOFF.md/this file.

(End of file - total 32 lines)
