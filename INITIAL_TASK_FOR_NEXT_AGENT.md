# Initial Task for Next Agent

## Status (maintenance re-verification COMPLETE — 2026-11-05 07:35 UTC)

- Branch `main`; HEAD `0d9618d` (chore(kilo): checkpoint agent session; one commit ahead of the `650ae0a` referenced in the prior task text, same verified tree). Working tree clean at verification start.
- SHA-256 re-verified from disk (all 6 match): `STRATEGY_RULES.txt` `6d3258c3…ad2b1`, `config/orb_mnq_15m_showcase.yaml` `2a6c5ff8…91e4`, `raw/MNQ_15min.csv` `f417f22d…ce37`, `raw/MNQ_1min.csv` `129623f4…ea99`, `raw/MNQ_1min_frontmonth.csv` `edbadc73…13e7`, `raw/MNQ_15min_frontmonth.csv` `7e129ae3…9ef4`.
- Artifacts: 24 JSON files parse cleanly (0 parse errors; 25 entries total).
- Baselines unchanged (`metrics_*_full.json` / `metrics_verify_*`): `axb0306` 60 trades, net `-$31637.98`, win rate `70%`, profit factor `0.4917`; Kaggle 688 trades, net `-$626525.96`, win rate `64.8%`, profit factor `0.2271`. Prior verified walk-forward: `axb0306` 3 windows all negative; Kaggle 8 windows all negative.
- Raw rows unchanged: `MNQ_15min` 5609; `MNQ_1min` 84078; `MNQ_1min_frontmonth` 1059205; `MNQ_15min_frontmonth` 70615.
- Tests: `python3 -m pytest -q` → **71 passed, 0 failed** (0.88s, 2026-11-05 07:35 UTC).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring (2026-11-05 sweep): axb0306/cme-futures-ohlc MNQ path via GitHub API — exactly the same 8 files, latest MNQ-path commit `2026-04-15T23:34:55Z`, unchanged ~6.5 months, no extension of intraday history. Kaggle `brandenmorris/mnq-1-minute-data-5132025-11122025` "Updated a year ago", coverage still ends **2025-11-12** — no extension of the already-ingested front-month series; byte-identical duplicate `brandenmorris/mnq-1m-q4-2022-q4-2025-ts-ohlcv-sym` re-confirmed as no-new-history. All other Kaggle/GitHub MNQ hits are NQ ($20/point) or non-MNQ — excluded per STRATEGY_RULES.txt. MarketParquet/FirstRate/Portara/FinzData/Databento/Barchart/Yahoo/Kibot/investing.com/CME DataMine/thinridge.io all paid, key-gated, daily-only, or insufficient. **No new genuinely free MNQ 1min/15min full-history source located.**

## Tasks (maintenance only)

1. Re-verify repo state, file hashes, artifacts, and run tests if available (`python3 -m pytest -q`).
2. Bounded free-data monitoring for a genuinely free MNQ 1min/15min full-history source; **record provenance + SHA-256 before use**. Do not purchase data or bypass access controls/terms.
3. No experiments/tuning without explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0.
4. Update `HANDOFF.md` and this file with concrete evidence if anything changes.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- If a genuinely free MNQ 1min/15min source with longer history is found (**record provenance + SHA-256 before use**), the next concrete task is a re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning.
