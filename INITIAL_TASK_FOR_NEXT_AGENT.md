# Initial Task for Next Agent

## Status (session 2026-11-03 — maintenance re-verification, one-hundred-twenty-second pass, COMPLETE)
- Branch main; working tree clean; up to date with origin/main (verified via `git fetch origin`: local HEAD be3bf7f == origin/main be3bf7f).
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1, config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4, raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37, raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99, raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7, raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Canonical artifacts present + parseable: artifacts/metrics_axb0306.json (60 trades, 70.00% WR, gross -$7,662.00, net -$31,637.98, PF 0.49167), artifacts/metrics_kaggle.json (688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.22709). Trade ledger SHA-256 identical (axb0306 ce389da2488474a6d0d994cf99bb1e6509761d80f85986f1f8da3e1738b6a364, kaggle 7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5). Walk-forward: artifacts/walk_forward_axb0306.json (a91cf29d4dd64ff3e690bba742c3c8e0f17079f0658bd4622cae67d4a73fff79, 3 windows all negative), artifacts/walk_forward_kaggle.json (cf8419972d2dbbeaea6b855ea6f483a4b469e61874334fbf3dfdebb4c7cda1a7, 8 windows all negative). All artifact files parse cleanly.
- Raw date ranges unchanged: axb0306 ends 2026-04-15; Kaggle front-month ends 2025-11-12 (final ~2.9 months from 2025-08-29, ~38 trades, net -$21,472.00, preserved as untouched OOS).
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed in 0.75s.
- Frozen baseline preserved; no code/strategy/parameter changes; working tree clean.
- Free-data monitoring: no new genuinely free MNQ 1min/15min source found (FinzData/FirstRate/MarketParquet/Databento/Yahoo/daily-only/Portara/infoway excluded per no-purchase policy). Known free: axb0306 (single-contract MNQ.M26, unadjusted) and Kaggle front-month (unadjusted). Do not purchase data; never store credentials.

## Tasks (maintenance only)
1. **Re-verify** repo state (git status/log/fetch), file hashes vs recorded values, canonical artifacts parseable, walk-forward present and negative. Run tests if available.
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
- Research blocked on data depth; both baselines negative under full costs; all walk-forward windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- axb0306 roll/adjustment: single-contract MNQ.M26, no roll inside sample; repo update script hard-codes one contract ID — re-verify hash/continuity before re-downloading.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.

## Why this task
Maintenance/re-verification only. Do NOT tune stops/targets/filters/sizing/session times — STRATEGY_RULES.txt v1.0 frozen. Only (a) verify frozen baseline intact/reproducible, (b) watch for genuinely free MNQ 1min/15min data (provenance+SHA256 before use), (c) refresh HANDOFF.md/this file.
