# Initial Task for Next Agent

## Status (maintenance re-verification COMPLETE — 2026-11-05T22:03Z, this session)
- `git status --short` **clean** (exit 0) before durable-doc edits. Repo HEAD at verification `0109f0ed23adc48a1abcfc5a2919d82608b60298` (2026-11-05T21:59Z). This-session verification (2026-11-05T22:03Z): all 6 tracked SHA-256 hashes **MATCH** (short form): `STRATEGY_RULES.txt` `6d3258c3...`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff8...`; `raw/MNQ_15min.csv` `f417f22d...`; `raw/MNQ_1min.csv` `129623f4...`; `raw/MNQ_1min_frontmonth.csv` `edbadc73...`; `raw/MNQ_15min_frontmonth.csv` `7e129ae3...` (full values in HANDOFF.md §7). 24 `artifacts/*.json`, 0 parse errors; `artifacts/metrics_axb0306.json` SHA-256 unchanged `e06f9dd0...`. `python3 -m pytest -q` **71 passed, 0 failed** (0.69s). No strategy/code/data/raw/artifact drift observed.
- Free-data monitoring (GitHub API + bounded web search, 2026-11-05T22:03Z): `axb0306/cme-futures-ohlc` `MNQ/` unchanged (HTTP 200) — `MNQ_1min_20260120_20260415.csv` `946c6b76d68548e5b1fe584b6e16de0f19f6d0d4` (4904282); `MNQ_15min_20260120_20260415.csv` `7df047964034b648ad7d8639515b6c9a92998af0` (333668). Latest MNQ commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` unchanged. Bounded web search: **no genuinely free MNQ 1min/15min full-history CSV extension beyond 2026-04-15 observed** (FinzData/FirstRate/Portara/Kibot/historicalfuturesdata/MarketParquet paid or limited; Databento API-key/credits + dbn-cache key-gated; Kaggle provenance/license unverified; Yahoo/Barchart/broker/demo restricted; getdata NQ equity not MNQ futures). No data purchased; no credentials requested/stored.
- Baselines unchanged (verified artifacts): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L.
- Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

## Tasks (maintenance only — do in order)

1. **Re-verify repo state.** Run `git status --short` (expect clean before edits), re-compute all 6 tracked SHA-256 hashes against values above, confirm `ls artifacts/*.json | wc -l` = 24 and 0 parse errors, and run `python3 -m pytest -q` (expected **71 passed / 0 failed** in a pytest-capable environment). If `pytest` is unavailable, record the runner constraint with concrete evidence and do not claim pass/fail. Record any drift with concrete evidence.
2. **Bounded free-data monitoring.** Check for a genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 (current latest free coverage in `axb0306/cme-futures-ohlc`). **Record provenance + SHA-256 before use.** Do not purchase data or bypass access controls/terms.
3. **No experiments/tuning.** Do not optimize thresholds, stops, targets, entry rules, or session times. Any change requires explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0.
4. **Update handoff files.** Update `HANDOFF.md` and this file with concrete evidence if anything changes (hashes, test counts, artifacts, new data candidates, blockers, runner/test constraints).

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through 2026-04-15 (re-verified 2026-11-05T21:54Z).
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- Runner note (2026-11-05T21:54Z): `pytest` available this session — **71 passed, 0 failed** (0.70s). Prior sessions observed runner drift (pytest unavailable); treat as runner-dependent.
- If a genuinely free MNQ 1min/15min source with longer history is found (**record provenance + SHA-256 before use**), the next concrete task is a re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning. Recompute metrics independently from the trade ledger and store configs/hashes/ledger/summary/validation artifacts.
