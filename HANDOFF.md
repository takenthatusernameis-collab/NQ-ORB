# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification COMPLETE — 2026-11-05T22:56Z, this session)

- Session verification (2026-11-05T22:56Z, this session, repo HEAD at verification `0d6e934dbd8f3bdb4b0dab6301512447a80118c6`; working tree clean before durable-doc edits): `git status --short` **clean** (exit 0). All 6 tracked SHA-256 hashes **MATCH** (full): `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`. 24 `artifacts/*.json`, 0 parse errors. `artifacts/metrics_axb0306.json` SHA-256 unchanged `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f`. `python3 -m pytest -q` **71 passed, 0 failed** (0.73s). No code/strategy/data/raw/artifact changes.
- Free-data monitoring (GitHub API/urllib + bounded web search, 2026-11-05T22:56Z): `axb0306/cme-futures-ohlc` `MNQ/` latest commit unchanged `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` (2026-04-15T23:34:55Z). Blobs unchanged — `MNQ_1min_20260120_20260415.csv` `946c6b76d68548e5b1fe584b6e16de0f19f6d0d4` (4904282), `MNQ_15min_20260120_20260415.csv` `7df047964034b648ad7d8639515b6c9a92998af0` (333668). Bounded web search: **no genuinely free MNQ 1min/15min full-history CSV extension beyond 2026-04-15 observed**. Candidates assessed (not used/purchased; paid/limited/key-gated/sample-only/unverified): MarketParquet full archive paid + limited free (daily ~365d + intraday sample week Apr 6-10 2026), Databento signup credits (6-month expiry) + key-gated, FirstRateData sample paid/$99.95/yr updates, PortaraCQG paid, historicalfuturesdata limited free samples (MNQ monthly bars; 10s sample) / $59+yr, Kibot $820 one-time, Barchart Premier intraday, CME DataMine priced, getdata.finance NQ CFD/cash-style (not MNQ CME futures), broker/demo/platform exports restricted, Kaggle/GitHub trading repos unverified provenance/license/coverage (not open full-history futures CSV). No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified artifacts): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L.
- Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

## Prior session evidence (condensed)

- 2026-11-05T22:54Z (HEAD `02cddfdd`): 6/6 hashes MATCH, 24/24 parse, 71 passed/0 failed (0.63s), metrics hash unchanged, axb0306 blobs/commit unchanged; no free extension beyond 2026-04-15.
- 2026-11-05T22:53Z/22:50Z/22:49Z (HEADs `1019b02`, `6794085`, `ecb57cf`/`73aaa31`): same maintenance results; earlier same-minute HEAD recording corrected in history.
- 2026-11-05T22:08Z–18:37Z: repeated bounded re-verifications; 6/6 hashes MATCH, 24/24 parse, pytest 71/0 when available (runner drift noted in some sessions). No code/strategy/parameter/data changes. See git history for per-session evidence.

## Blockers / durable constraints

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through 2026-04-15 (re-verified 2026-11-05T22:08Z via GitHub API/urllib; blobs + latest MNQ commit unchanged).
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- Runner note (2026-11-05T22:08Z): `pytest` available this session — **71 passed, 0 failed** (0.66s). Prior sessions observed runner drift (pytest unavailable); treat as runner-dependent.
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
