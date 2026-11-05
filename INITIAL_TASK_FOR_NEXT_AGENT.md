# Initial Task for Next Agent

## Status (maintenance re-verification COMPLETE — 514b8b3, 2026-11-05 07:28 UTC)

- Branch `main`; HEAD `514b8b37c527dd6ba6b359b78852591da75116e1` (514b8b3); working tree clean at verification start.
- SHA-256 re-verified from disk: all 6 tracked hashes match recorded values (`STRATEGY_RULES.txt`, `config/orb_mnq_15m_showcase.yaml`, `raw/MNQ_{15min,1min,1min_frontmonth,15min_frontmonth}.csv`).
- Artifacts: 25 entries, 24 JSON files parse cleanly (0 parse errors).
- Walk-forward/baselines unchanged from prior verified artifacts (`axb0306` 3 windows all negative; Kaggle 8 windows all negative; `axb0306` 60 trades net `-$31637.98`, win rate `70%`, profit factor `0.4917`; Kaggle 688 trades net `-$626525.96`, win rate `64.8%`, profit factor `0.2271`; all walk-forward test windows negative net P&L).
- Raw row counts unchanged (`MNQ_15min` 5609; `MNQ_1min` 84078; `MNQ_1min_frontmonth` 1059205; `MNQ_15min_frontmonth` 70615).
- Tests: `python3 -m pytest -q` → **71 passed, 0 failed** (0.89s).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring (2026-11-05 sweep): MarketParquet/historicalfuturesdata, FirstRate Data, Portara, FinzData, Databento, Barchart, Yahoo Finance, Kibot/GetData/TestMax re-checked — paid, key-gated, restricted, or insufficient for free full MNQ 1min/15min history. Kaggle `brandenmorris/mnq-1-minute-data-5132025-11122025` (MNQ 1m, CC BY 4.0, 2025-05-13–2025-11-12) overlaps existing front-month end (2025-11-12) and does not extend verified history. **No new genuinely free MNQ 1min/15min full-history source located.**

## Tasks (maintenance only)

1. Re-verify repo state, file hashes, artifacts, and run tests if available.
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

- Research blocked on data depth; both baselines negative under full costs; all walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- If a genuinely free MNQ 1min/15min source with longer history is found (**record provenance + SHA-256 before use**), the next concrete task is a re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning.
