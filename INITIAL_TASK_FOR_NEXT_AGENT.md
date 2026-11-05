# Initial Task for Next Agent

## Status (maintenance re-verification COMPLETE — 2026-11-05T15:37Z, this session)

- Branch `main`; HEAD `e10dccc` at session start (checkpoint drift only; no strategy/code/data drift). `git status --short` clean before edits.
- Session re-verification completed at 2026-11-05T15:37Z with **no drift**: git clean, all 6 hashes MATCH (below), 24 artifacts parse clean (0 errors), `python3 -m pytest -q` → **71 passed, 0 failed** (0.70s), `metrics_axb0306.json` SHA-256 unchanged `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f` (9055 bytes), free-data coverage unchanged (no extension beyond 2026-04-15).
- SHA-256 re-verified (all **MATCH**): `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (126); `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4` (77); `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37` (5609); `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99` (84078); `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7` (1059205); `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4` (70615).
- Artifacts: **24** JSON files parse cleanly (0 parse errors). `artifacts/metrics_axb0306.json` SHA-256 unchanged `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f` (9055 bytes).
- Tests: `python3 -m pytest -q` → **71 passed, 0 failed** (0.70s, 2026-11-05T15:37Z).
- Baselines unchanged (verified artifacts): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L.
- Free-data monitoring (2026-11-05T15:37Z): GitHub API `axb0306/cme-futures-ohlc` MNQ path latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z`; GitHub contents shows `MNQ_1min_20260120_20260415.csv` (4904282, blob `946c6b76...`) and `MNQ_15min_20260120_20260415.csv` (333668, blob `7df04796...`) — **no extension beyond 2026-04-15**. A `MNQ_tick_20260309_20260415.csv` tick file (29979112 bytes, blob `d9a91eea...`, 2026-03-09..2026-04-15) is present — 1-minute-or-better but only a ~1-month window ending 2026-04-15, so it does **not** satisfy the full-history-extension criterion and is not used as evidence. Bounded sweep: paid/proprietary sources remain paid — **not used/purchased**. Free intraday-inadequate/non-matching sources unchanged — **not used as evidence**. **No genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 found.** No data purchased; no credentials; no code/strategy/parameter changes.
- Frozen baseline preserved.

## Tasks (maintenance only — do in order)

1. **Re-verify repo state.** Run `git status --short` (expect clean before your edits), re-compute all 6 tracked SHA-256 hashes against values above, confirm `ls artifacts/*.json | wc -l` = 24 and `python3 -m pytest -q` = 71 passed / 0 failed. Record any drift with concrete evidence.
2. **Bounded free-data monitoring.** Check for a genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 (current latest free coverage observed in `axb0306/cme-futures-ohlc`). **Record provenance + SHA-256 before use.** Do not purchase data or bypass access controls/terms.
3. **No experiments/tuning.** Do not optimize thresholds, stops, targets, entry rules, or session times. Any change requires explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0.
4. **Update handoff files.** Update `HANDOFF.md` and this file with concrete evidence if anything changes (hashes, test counts, artifacts, new data candidates, blockers).

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through 2026-04-15.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- If a genuinely free MNQ 1min/15min source with longer history is found (**record provenance + SHA-256 before use**), the next concrete task is a re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning. Recompute metrics independently from the trade ledger and store configs/hashes/ledger/summary/validation artifacts.

(End of file)
