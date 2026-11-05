# Initial Task for Next Agent

## Status (session 2026-11-05 — maintenance re-verification pass COMPLETE, HEAD 20260c0)

- Branch main; HEAD 20260c0 (chore(kilo): checkpoint agent session); working tree clean (`git status --short` empty, no untracked files). Fetched origin --prune; local main up to date with origin/main (`main` == `origin/main` == 20260c0). Recent commits: 20260c0, e39a863, 41d6d6a, 71c6da9, ee49188, d372430, b021d09, fe68455, b2c4da2, 70add8d, 2794b06, d2bd42b, bfd59c4.
- SHA-256 re-verified from disk (2026-11-05): all six tracked file hashes match recorded values.
- Determinism re-verified from fresh process: axb0306 net -$31,637.98; kaggle net -$626,525.96. Trade-ledger SHA-256 byte-identical: axb0306 `ce389da2488474a6d0d994cf99bb1e6509761d80f85986f1f8da3e1738b6a364`; kaggle `7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5`. Metrics files also byte-identical. Verify copies deleted after comparison.
- Artifacts: 21 files in artifacts/ (README.md + 20 JSON); all JSON parse cleanly (0 parse errors).
- Walk-forward verified from artifacts: axb0306 3 windows, all test_net_pnl negative ([-$10,053.14, -$21,922.10, -$23,058.98]). Kaggle 8 windows, all test_net_pnl negative ([-$178,375.24, -$173,264.64, -$168,315.48, -$134,617.64, -$122,071.62, -$70,637.24, -$104,755.42, -$114,820.72]).
- Baselines verified: axb0306_full 60 trades, 70.0% WR, net -$31,637.98; Kaggle front-month 688 trades, 64.8256% WR, net -$626,525.96.
- Raw date ranges unchanged: MNQ_15min.csv 2026-01-20T13:15 → 2026-04-15T23:15; MNQ_1min.csv 2026-01-20T13:27 → 2026-04-15T23:29; front-month files end 2025-11-12T23:45/23:59.
- Tests: `python3 -m pytest tests/` = 71 passed, 0 failed.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data re-scan (2026-11-05): no new genuinely free MNQ 1min/15min full-history source. Confirmed paid/key-gated: historicalfuturesdata.com ($59/yr per bar size), FinzData ($49 one-time), FirstRate ($99.95/yr), MarketParquet ($79 one-time; free tier daily-only), Kibot ($520), Portara (paid), Databento (key-gated + credit-based), Barchart (intraday needs Premier), Yahoo Finance (MNQ=F daily only; 1-min = last 30 days), investing.com (daily-only), CME DataMine (samples only). Kaggle MNQ hits remain brandenmorris (ends 2025-11-12, already ingested) + byte-identical duplicate; all other hits are NQ big contract ($20/point) or non-MNQ.

## Tasks (maintenance only)

1. Re-verify repo state, file hashes, artifacts, walk-forward, tests if available.
2. Data monitoring for genuinely free MNQ 1min/15min source; record provenance+SHA-256 before use.
3. No experiments without approval.
4. Update HANDOFF.md and this file with concrete evidence if anything changes.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both baselines negative under full costs; all walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- axb0306 roll/adjustment: single-contract MNQ.M26, no roll inside sample.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.

## Why this task

Maintenance/re-verification only. Do NOT tune stops/targets/filters/sizing/session times — STRATEGY_RULES.txt v1.0 frozen. Only (a) verify frozen baseline intact/reproducible, (b) watch for genuinely free MNQ 1min/15min data (provenance+SHA256 before use), (c) refresh HANDOFF.md/this file.

(End of file)
