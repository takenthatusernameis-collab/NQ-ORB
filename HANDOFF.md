# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification COMPLETE — 2026-11-05T18:50Z, this session)

- Session verification (2026-11-05T18:50Z, repo `946a6e0` before handoff edits): `git status --short` clean (exit 0); no drift. All 6 tracked SHA-256 hashes **MATCH**; 24 `artifacts/*.json`, 0 parse errors; `python3 -m pytest -q` → **71 passed, 0 failed** (0.63s). `artifacts/metrics_axb0306.json` SHA-256 unchanged `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f`.
- Free-data monitoring (GitHub API + bounded web search, 2026-11-05T18:50Z): `axb0306/cme-futures-ohlc` `MNQ/` directory listing re-fetched — all 8 blobs **unchanged**: `MNQ_15min_20260120_20260415.csv` `7df047964034b648ad7d8639515b6c9a92998af0` (333668); `MNQ_1h_20250321_20260415.csv` `79ef8f14354734f9b83ee8c6fe4af3c1a31d546e`; `MNQ_1min_20260120_20260415.csv` `946c6b76d68548e5b1fe584b6e16de0f19f6d0d4` (4904282); `MNQ_30min_20260120_20260415.csv` `b7dd7049010b794ef1b1eaf655031db79ef55c51`; `MNQ_4h_20250321_20260415.csv` `7a3c229ebda8d4c7137eab090fa432f0045c7ebb`; `MNQ_5min_20260120_20260415.csv` `079f0e098b63fcecee9231831185debf11f90b0e`; `MNQ_daily_20250324_20260414.csv` `c13eac543793037758a4ce99300d498cdb3962c1`; `MNQ_tick_20260309_20260415.csv` `d9a91eea5dcd13c4b1af8ea3248937f61db18cce`. Latest MNQ commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` — **unchanged**. Bounded web search (2026-11-05T18:50Z): **no genuinely free MNQ 1min/15min full-history extension beyond 2026-04-15 observed**. Re-confirmed paid/limited/gated/unverified: FinzData ($49, last-30-days daily free only); MarketParquet (free daily ~365d + limited intraday sample; full archive paid); historicalfuturesdata.com (paid/limited samples); Databento GLBX.MDP3 MNQ (API-key/credit-gated); FirstRate ($99.95/yr); Portara/Kibot paid; Infoway (free API key required, unverified MNQ futures depth); `azizuysal/dbn-cache`/`charlesbx/futures-backtester` require Databento data. Kaggle `brandenmorris` MNQ still ends 2025-11-12 (unchanged). `tgtanalytics`/`youneseloiarm`/`tzamrik`/`getdata-finance` are NQ equity/cash or big-contract, excluded per `STRATEGY_RULES.txt`. No data purchased; no credentials requested/stored.
- SHA-256 re-verified from disk (all **MATCH**): `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`.
- Baselines unchanged (verified artifacts): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L.
- Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter changes.

## Prior session log (compact)

- 2026-11-05T18:50Z (this session, `946a6e0`): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse, 71 passed). GitHub API: axb0306 MNQ/ blobs unchanged; latest MNQ commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` unchanged. Bounded web search: **no genuinely free MNQ 1min/15min full-history extension beyond 2026-04-15** (FinzData/MarketParquet/historicalfuturesdata.com/Databento/FirstRate/Portara/Kibot/Infoway/dbn-cache/charlesbx paid/limited/key-gated or Databento-dependent; Kaggle brandenmorris ends 2025-11-12; NQ equity/big-contract sources excluded). No data purchased; no code/strategy/parameter changes.
- 2026-11-05T18:46Z (`ed797b1`): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse, 71 passed). axb0306 unchanged; no free extension beyond 2026-04-15.
- 2026-11-05T18:45Z (this session, `905101d`): maintenance re-verification (clean, 6/6 MATCH, 24 artifacts parse clean, 71 passed). GitHub API: axb0306 MNQ blobs unchanged; latest MNQ commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` unchanged. Bounded web search: FinzData/MarketParquet/historicalfuturesdata.com/Databento/FirstRate/Portara/Kaggle/dbn-cache/charlesbx — **no genuinely free MNQ 1min/15min full-history extension beyond 2026-04-15** (paid/limited/samples/credits/Databento-dependent). No data purchased; no code/strategy/parameter changes.
- 2026-11-05T18:42Z (`dbbc35e`): maintenance re-verification (clean, 6/6 MATCH, 24/71). axb0306 unchanged; no free extension beyond 2026-04-15.
- 2026-11-05T18:42Z (`827cfcd`): maintenance re-verification (clean, 6/6 MATCH, 24/71). axb0306 unchanged; no free extension beyond 2026-04-15.
- 2026-11-05T18:37Z (`7d6a856`): maintenance re-verification (clean, 6/6 MATCH, 24/71). axb0306 unchanged; no free extension beyond 2026-04-15.
- 2026-11-05T18:35Z (`a32f9a7`): maintenance re-verification (clean, 6/6 MATCH, 24/71). axb0306 unchanged; no free extension beyond 2026-04-15.
- 2026-11-05T18:33Z–17:45Z: repeated maintenance re-verifications (clean, 6/6 MATCH, 24/71). axb0306 unchanged; no free extension beyond 2026-04-15.
- 2026-11-05T16:34Z–17:42Z: maintenance re-verifications and bounded free-source sweeps (paid/limited/intraday-inadequate; none used/purchased). No code/strategy/parameter changes.

## Blockers / durable constraints

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through 2026-04-15 (re-verified 2026-11-05T18:50Z).
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
