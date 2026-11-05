# Initial Task for Next Agent

## Status (maintenance re-verification COMPLETE — 2026-11-05 07:34–07:36 UTC)

- Branch `main`; HEAD at verification `30223432adb34ab1fb3bdd0b88498bef9df9e9e3` (2026-11-05 07:33:53 +0000, `chore(kilo): checkpoint agent session`). Working tree clean at verification start.
- SHA-256 re-verified from disk (all 6 match): `STRATEGY_RULES.txt` `6d3258c3…ad2b1`, `config/orb_mnq_15m_showcase.yaml` `2a6c5ff8…91e4`, `raw/MNQ_15min.csv` `f417f22d…ce37`, `raw/MNQ_1min.csv` `129623f4…ea99`, `raw/MNQ_1min_frontmonth.csv` `edbadc73…13e7`, `raw/MNQ_15min_frontmonth.csv` `7e129ae3…9ef4`.
- Artifacts: 24 JSON files parse cleanly (0 parse errors).
- Baselines unchanged (`metrics_*_full.json` / `metrics_verify_*`): `axb0306` 60 trades, net `-$31637.98`, win rate `70%`, profit factor `0.4917`; Kaggle 688 trades, net `-$626525.96`, win rate `64.8%`, profit factor `0.2271`. Prior verified walk-forward: `axb0306` 3 windows all negative; Kaggle 8 windows all negative.
- Raw rows unchanged: `MNQ_15min` 5609; `MNQ_1min` 84078; `MNQ_1min_frontmonth` 1059205; `MNQ_15min_frontmonth` 70615 (total 1219507).
- Tests: `python3 -m pytest -q` → **71 passed, 0 failed** (0.89s, 2026-11-05 07:35 UTC).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring (2026-11-05 sweep): axb0306/cme-futures-ohlc MNQ intraday files still `20260120_20260415` (no extension). Kaggle-brand MNQ 1m sources still end 2025-11-12 / overlap existing coverage; no extension. MarketParquet (daily free + 1-week intraday sample; full archive paid), FirstRate (paid/subscription), Kibot ($520 paid), Databento (key-gated/credit-based), Yahoo (daily/limited intraday), Barchart/CME/other portals paid or insufficient. NQ-only datasets excluded per `STRATEGY_RULES.txt`. **No new genuinely free MNQ 1min/15min full-history source located.**

## Tasks (maintenance only)

1. Re-verify repo state, file hashes, artifacts, and run tests if available (`python3 -m pytest -q`). Record any drift with concrete evidence.
2. Bounded free-data monitoring for a genuinely free MNQ 1min/15min full-history source that extends beyond 2025-11-12 (front-month) and/or provides longer MNQ.M26 context; **record provenance + SHA-256 before use**. Do not purchase data or bypass access controls/terms.
3. No experiments/tuning without explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0. Do not optimize thresholds, stops, targets, entry rules, or session times.
4. Update `HANDOFF.md` and this file with concrete evidence if anything changes (hashes, test counts, artifacts, new data candidates, blockers).

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15).
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- If a genuinely free MNQ 1min/15min source with longer history is found (**record provenance + SHA-256 before use**), the next concrete task is a re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning. Recompute metrics independently from the trade ledger and store configs/hashes/ledger/summary/validation artifacts.
