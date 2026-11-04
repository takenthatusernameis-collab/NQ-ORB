# Initial Task for Next Agent

## Status (session 2026-11-04 — maintenance re-verification pass COMPLETE)

- Branch main; HEAD c2b15e1 (chore(kilo): checkpoint agent session); working tree clean (`git status --short` empty); fetched origin --prune; up to date with origin/main. Recent commits: c2b15e1, c9861f3, 619dc61, e240cc5, eda9f46, 57e79a4, 55222fb.
- SHA-256 verified from disk (2026-11-04): all six tracked file hashes match recorded values (STRATEGY_RULES.txt, config/orb_mnq_15m_showcase.yaml, raw/MNQ_15min.csv, raw/MNQ_1min.csv, raw/MNQ_1min_frontmonth.csv, raw/MNQ_15min_frontmonth.csv).
- Tests: pandas + pytest installed for verification; full suite `python3 -m pytest tests/` = 71 passed, 0 failed (30 orb strategy tests + 41 controller/workflow tests).
- Artifacts: 20 JSON files in artifacts/ parse cleanly (README.md present); walk-forward: axb0306 3/3 test windows negative; Kaggle 8/8 test windows negative.
- Baselines re-verified reproducible from scratch (runner re-run, recheck copies removed after comparison): axb0306 net -$31,637.98, 60 trades; Kaggle front-month net -$626,525.96, 688 trades (all key metrics match canonical artifacts exactly).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data re-scan unchanged: no new genuinely free MNQ 1min/15min source. axb0306 ends 2026-04-15 (stale); Kaggle front-month ends 2025-11-12 (CC BY 4.0). All other candidates paid/key-gated/limited (MarketParquet $79 one-time full archive; free = daily-only + 1-week sample; FirstRateData $99.95/yr; HistoricalFuturesData paid; Kibot $520-$820; Portara paid; Databento key-gated; Yahoo 30-day 1min/daily-only; GetData $49.99 once; investing.com daily-only; CME DataMine sample-only/paid; Barchart Premier intraday; TickTradingData €200/instrument; FinzData $49 one-time; thinridge.io paid upstream; quantnet not free; getdata.finance NQ/NAS100 CFD not MNQ).

## Tasks (maintenance only)

1. **Re-verify** repo state (`git status`/`git log`/`git fetch origin --prune`), file hashes vs recorded values (the six tracked files listed in HANDOFF.md), canonical artifacts parseable, walk-forward present and all test windows negative. Run tests (`python3 -m pytest tests/`) if available.
2. **Optional reproducibility**: re-run both baselines from scratch (`python3 src/orb/runner.py --source axb0306 --prefix <name>` and `--source kaggle --prefix <name>`) and confirm metrics/trades match canonical artifacts. Remove any copies after comparison.
3. **Data monitoring**: watch for a new genuinely free MNQ 1min/15min source. If found, record source/license/access constraints, retrieval time, contract symbols/months, session timezone, bar timestamps, gaps, roll rules, adjustment method, and SHA-256 before any use. Known free: axb0306 (stale, ends 2026-04-15) and Kaggle front-month (ends 2025-11-12). All other candidates paid/key-gated/limited (see status above).
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
