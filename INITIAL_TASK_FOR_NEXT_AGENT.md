# Initial Task for Next Agent

## Status (session 2026-11-04 — maintenance re-verification pass COMPLETE)

- Branch main; HEAD 7f6a2cd (chore(kilo): checkpoint agent session); working tree clean; local HEAD matches origin/main; `git fetch origin --prune` up to date. Recent commits: 7f6a2cd, 9e41da0, f27590e.
- SHA-256 verified from disk: all six hashes match recorded values.
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed in 0.91s.
- Artifacts: 17 entries in artifacts/ parse cleanly (README.md + JSONs). Walk-forward: walk_forward_axb0306.json 3 windows all negative; walk_forward_kaggle.json 8 windows all negative.
- Frozen baseline preserved; no code/strategy/parameter changes.

## Tasks (maintenance only)

1. **Re-verify** repo state (`git status`/`git log`/`git fetch origin --prune`), file hashes vs recorded values, canonical artifacts parseable, walk-forward present and all test windows negative. Run tests if available.
2. **Optional reproducibility**: re-run both baselines from scratch (`python3 src/orb/runner.py --source axb0306 --prefix <name>` and `--source kaggle --prefix <name>`) and confirm metrics/trades match canonical artifacts. Remove any `_verify` copies after comparison.
3. **Data monitoring**: watch for a new genuinely free MNQ 1min/15min source. If found, record source/license/access constraints, retrieval time, contract symbols/months, session timezone, bar timestamps, gaps, roll rules, adjustment method, and SHA-256 before any use. Known free: axb0306 (stale, ends 2026-04-15) and Kaggle front-month (ends 2025-11-12). All other candidates paid/key-gated/limited (MarketParquet $79 one-time full archive; free = daily-only + 1-week sample; FirstRateData $99.95/yr; HistoricalFuturesData paid; Kibot $520-$820; Portara paid; Databento key-gated; Yahoo 30-day 1min; GetData $49.99 once; investing.com daily-only).
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
