# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification COMPLETE — 2026-11-05T21:57Z, this session)

- Session verification (2026-11-05T21:54Z, repo HEAD before durable-doc edit `cf1aa03bce218c515744dc714cc504ab97057866` 2026-11-05T21:53:48Z "chore(kilo): maintenance re-verify 2026-11-05T21:51Z"): `git status --short` **clean** (exit 0). All 6 tracked SHA-256 hashes **MATCH**: `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`. 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed, 0 failed** (0.70s, 2026-11-05T21:54Z). `artifacts/metrics_axb0306.json` SHA-256 unchanged `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f`. No code/strategy/data/raw/artifact changes.
- Free-data monitoring (GitHub API + bounded web search, 2026-11-05T21:54Z): `axb0306/cme-futures-ohlc` `MNQ/` re-fetched via GitHub API (HTTP 200) — all 8 blobs **unchanged**: `MNQ_15min_20260120_20260415.csv` `7df047964034b648ad7d8639515b6c9a92998af0` (333668); `MNQ_1h_20250321_20260415.csv` `79ef8f14354734f9b83ee8c6fe4af3c1a31d546e`; `MNQ_1min_20260120_20260415.csv` `946c6b76d68548e5b1fe584b6e16de0f19f6d0d4` (4904282); `MNQ_30min_20260120_20260415.csv` `b7dd7049010b794ef1b1eaf655031db79ef55c51`; `MNQ_4h_20250321_20260415.csv` `7a3c229ebda8d4c7137eab090fa432f0045c7ebb`; `MNQ_5min_20260120_20260415.csv` `079f0e098b63fcecee9231831185debf11f90b0e`; `MNQ_daily_20250324_20260414.csv` `c13eac543793037758a4ce99300d498cdb3962c1`; `MNQ_tick_20260309_20260415.csv` `d9a91eea5dcd13c4b1af8ea3248937f61db18cce`. Latest MNQ commit **unchanged** `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` ("Update 2026-04-15: 368 files updated"). Bounded web search: **no genuinely free MNQ 1min/15min full-history CSV extension beyond 2026-04-15 observed**. Candidates assessed (not used/purchased): FinzData $49 one-market/$295 complete; FirstRate paid ($99.95/yr updates, sample); Portara paid intraday/tick; Kibot $520 continuous-intraday; historicalfuturesdata $59/yr bars (limited free monthly samples); MarketParquet $79 full archive (limited free daily+sample week); Databento API-key/credits ($125 signup, not open full-history CSV) and dbn-cache key-gated; Kaggle provenance/license/coverage unverified; getdata NQ equity (cash/extended sessions), not MNQ futures; broker/demo/API-key sources not open CSV. No data purchased; no credentials requested/stored.
- Baselines unchanged (verified artifacts): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L.
- Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

## Prior session log (compact)

- 2026-11-05T21:57Z (this session): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse, **71 passed/0 failed** 0.65s). All 6 tracked SHA-256 MATCH; 24 artifacts; `metrics_axb0306.json` unchanged `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f`. No free-data change; axb0306 unchanged; no code/strategy/parameter/raw/artifact changes. (clean, 6/6 MATCH, 24/24 parse, **71 passed/0 failed** 0.70s). Repo HEAD before durable-doc edit `cf1aa03bce218c515744dc714cc504ab97057866` (2026-11-05T21:53:48Z, "chore(kilo): maintenance re-verify 2026-11-05T21:51Z"). All 6 tracked SHA-256 MATCH; 24 artifacts; `metrics_axb0306.json` unchanged `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f`. GitHub API (HTTP 200): axb0306 latest MNQ commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` (2026-04-15T23:34:55Z) + all 8 blob SHAs unchanged. Bounded web search: no genuinely free MNQ 1min/15min full-history CSV extension beyond 2026-04-15. Candidates assessed: FinzData/FirstRate/Portara/Kibot/historicalfuturesdata/MarketParquet paid or limited; Databento API-key/credits + dbn-cache key-gated; Kaggle unverified; getdata NQ equity (not MNQ futures). No data purchased; no code/strategy/parameter/raw/artifact changes.
- 2026-11-05T21:51Z (prior session): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse, **71 passed/0 failed** 0.67s). Repo HEAD `04dca0a29d21cf927f478653721d777b1b1b5770`. axb0306 unchanged; no free extension beyond 2026-04-15.
- 2026-11-05T21:48Z (prior session): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse, **71 passed/0 failed** 0.73s). Repo HEAD `b74265e0041664449815aabb185a93a50730e771`. axb0306 unchanged; no free extension beyond 2026-04-15.
- 2026-11-05T21:04Z (prior session): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse, **71 passed/0 failed** 0.65s). Repo HEAD `1ff8b6f`. axb0306 unchanged.

- 2026-11-05T21:03Z (this session): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse, **71 passed/0 failed** 0.68s). Repo HEAD `8f0c45f` (2026-11-05T21:01:20Z, "chore(kilo): maintenance re-verify 2026-11-05T21:01Z"). All 6 tracked SHA-256 MATCH; 24 artifacts; metrics_axb0306 unchanged. No free-data change; axb0306 unchanged; no code/strategy/parameter changes.
- 2026-11-05T21:01Z (this session): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse, **71 passed/0 failed** 0.64s). Repo HEAD `da2274dae511496bf58b4062b66f1de83530b026` at verification; `git status --short` clean; all 6 tracked SHA-256 MATCH; 24 artifacts parse OK; `metrics_axb0306.json` unchanged. GitHub API: axb0306 MNQ blobs + latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` (2026-04-15T23:34:55Z) unchanged. Bounded web search: no genuinely free MNQ 1min/15min full-history CSV extension beyond 2026-04-15 (MarketParquet/FirstRate/Portara/Kibot paid or limited; Databento/Infoway API-key/credits/gated; Kaggle unverified). No data purchased; no code/strategy/parameter changes.
- 2026-11-05T21:02Z (`0ef4d38`): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse). `pytest` unavailable; last recorded 71 passed/0 failed (2026-11-05T18:50Z). axb0306 unchanged.
- 2026-11-05T20:54Z (`a4067cf`): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse). `pytest` unavailable; last recorded 71 passed/0 failed (2026-11-05T18:50Z). No free-data change.
- 2026-11-05T20:51Z (`4c0ead3`): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse). Runner drift: pytest unavailable. axb0306 unchanged; no free extension beyond 2026-04-15.
- 2026-11-05T18:50Z (`946a6e0`): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse, 71 passed). axb0306 unchanged.
- 2026-11-05T18:46Z (`ed797b1`): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse, 71 passed). axb0306 unchanged.
- 2026-11-05T18:45Z (`905101d`): maintenance re-verification (clean, 6/6 MATCH, 24/24 parse, 71 passed). No free extension beyond 2026-04-15.
- 2026-11-05T18:42Z (`dbbc35e`, `827cfcd`): maintenance re-verifications (clean, 6/6 MATCH, 24/71). axb0306 unchanged.
- 2026-11-05T18:37Z–16:34Z: repeated maintenance re-verifications/bounded sweeps (clean, 6/6 MATCH, 24/71 where pytest available). No code/strategy/parameter changes.

## Blockers / durable constraints

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through 2026-04-15 (re-verified 2026-11-05T21:54Z via GitHub API HTTP 200; blobs + latest MNQ commit unchanged).
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- No runner pytest constraint this session (pytest available; 71 passed/0 failed 2026-11-05T21:54Z). Prior sessions noted pytest unavailable in that runner — treat as runner-dependent.
- Carried-forward bounded sweep context (not used/purchased): FinzData ($49+), FirstRate ($99.95/yr), Portara, Kibot ($520), historicalfuturesdata ($59/yr, limited free samples), MarketParquet ($79 full / limited free), Databento API-key/credits (dbn-cache key-gated), Kaggle unverified provenance/license/coverage. `getdata-finance` NQ equity cash/extended sessions, not MNQ futures.


## Next agent (immediate)

Maintenance/re-verification only:
1. Re-verify repo state: `git status --short` (clean), all 6 tracked SHA-256 hashes, `ls artifacts/*.json | wc -l` (24, 0 parse errors), `python3 -m pytest -q` (expected 71 passed, 0 failed in a pytest-capable env). If `pytest` unavailable, record runner constraint as drift and do not claim pass/fail.
2. Bounded free-data monitoring for a genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 (current latest free coverage). **Record provenance + SHA-256 before use.** Do not purchase data or bypass access controls/terms.
3. No experiments/tuning without explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0.
4. Update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence if anything changes (hashes, test counts, artifacts, new data candidates, blockers). Commit durably.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

(End of file)
