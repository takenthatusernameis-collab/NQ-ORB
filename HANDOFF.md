# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification COMPLETE — 2026-11-05T17:45Z, this session)

- Session verification (2026-11-05T17:45Z): `git status --short` clean before handoff edits (exit 0); no drift. All 6 tracked SHA-256 hashes **MATCH**; 24 `artifacts/*.json`, 0 parse errors; `python3 -m pytest -q` → **71 passed, 0 failed** (0.60s). `artifacts/metrics_axb0306.json` SHA-256/size unchanged `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f` (9055 bytes). Local `raw/MNQ_1min.csv` range verified 2026-01-20T13:27:00..2026-04-15T23:29:00 (84077 data rows).
- Free-data monitoring (GitHub API, 2026-11-05T17:45Z): `axb0306/cme-futures-ohlc` `MNQ/` unchanged — 8 files. `MNQ_1min_20260120_20260415.csv` 4904282 blob `946c6b76d68548e5b1fe584b6e16de0f19f6d0d4`; `MNQ_15min_20260120_20260415.csv` 333668 blob `7df047964034b648ad7d8639515b6c9a92998af0`; `MNQ_tick_20260309_20260415.csv` 29979112 blob `d9a91eea5dcd13c4b1af8ea3248937f61db18cce` (2026-03-09..2026-04-15 only, not sufficient as full-history 1min/15min extension). Latest MNQ commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z`. Bounded unauthenticated GitHub code search for alternative free MNQ 1min CSVs returned HTTP 401 (not usable without credentials); no credentials requested/stored. **No 1min/15min extension beyond 2026-04-15.** No data purchased; no code/strategy/parameter changes.
- SHA-256 re-verified from disk (all **MATCH**):
  - `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (126 lines)
  - `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4` (77 lines)
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37` (5609 lines)
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99` (84078 lines)
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7` (1059205 lines)
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4` (70615 lines)
- Baselines unchanged (verified artifacts): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L.
- Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter changes.

## Prior session log (compact)

- 2026-11-05T17:45Z: maintenance re-verification (clean, 6/6 MATCH, 24 artifacts parse clean, 71 passed). GitHub API: axb0306 MNQ 1min/15min blobs/sizes unchanged; latest MNQ commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z`; tick limited to 2026-03-09..2026-04-15. Bounded unauth GitHub code search returned HTTP 401 (no credentials used). No 1min/15min extension beyond 2026-04-15.
- 2026-11-05T17:42Z: maintenance re-verification (clean, 6/6 MATCH, 24 artifacts parse clean, 71 passed). GitHub API: axb0306 MNQ 1min/15min blobs/sizes unchanged; latest MNQ commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z`; tick limited to 2026-03-09..2026-04-15. No 1min/15min extension beyond 2026-04-15.
- 2026-11-05T17:40Z: maintenance re-verification (clean, 6/6 MATCH, 24 artifacts parse clean, 71 passed). GitHub API: axb0306 MNQ 1min/15min blobs/sizes unchanged; latest MNQ commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z`; tick limited to 2026-03-09..2026-04-15. No 1min/15min extension beyond 2026-04-15.
- 2026-11-05T17:34Z–17:37Z: repeated re-verifications (clean, 6/6 MATCH, 24 artifacts parse clean, 71 passed). GitHub API: 1min/15min blobs/sizes unchanged; latest MNQ commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z`; tick limited to 2026-03-09..2026-04-15. No 1min/15min extension beyond 2026-04-15.
- 2026-11-05T16:34Z–17:31Z: maintenance re-verifications and bounded free-source sweeps (paid/limited/intraday-inadequate sources identified in prior context; none used/purchased). No data purchased/credentials/code/strategy/parameter changes.

## Blockers / durable constraints

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through 2026-04-15 (re-verified 2026-11-05T17:41Z).
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- Carried-forward bounded sweep context (not used/purchased): MarketParquet ($79 full / free limited), FirstRate ($99.95/yr), Kibot ($69.83/5yr), Portara/Databento/Infoway paid/credits/unverified; Yahoo/Barchart free/Kaggle samples intraday-inadequate or non-matching; `getdata-finance` NQ equity cash/extended sessions, not MNQ futures.

## Next agent (immediate)

Maintenance/re-verification only:
1. Re-verify repo state: `git status --short` (clean), all 6 tracked SHA-256 hashes, `ls artifacts/*.json | wc -l` (24, 0 parse errors), `python3 -m pytest -q` (71 passed, 0 failed). Record any drift with concrete evidence.
2. Bounded free-data monitoring for a genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 (current latest free coverage); **record provenance + SHA-256 before use**. Do not purchase data or bypass access controls/terms.
3. No experiments/tuning without explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0.
4. Update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence if anything changes (hashes, test counts, artifacts, new data candidates, blockers).

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

(End of file)
