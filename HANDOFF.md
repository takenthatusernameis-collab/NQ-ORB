# Handoff

## Current durable state (maintenance re-verification — 2026-11-06T07:50Z, this session)

- Session verification (2026-11-06T07:50Z, repo HEAD at verification `581732e`, 2026-11-06T07:50:07Z): `git status --short` **clean** before durable-doc edits (exit 0). All 6 tracked SHA-256 hashes **MATCH** (full): `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`. 24 `artifacts/*.json`, 0 parse errors. `artifacts/metrics_axb0306.json` SHA-256 **MATCH** `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f` (`net_pnl` -31637.98, `win_rate` 0.7, `profit_factor` 0.491672798902303). `python3 -m pytest -q` **71 passed, 0 failed** (exit 0, 0.91s). No code/strategy/data/raw/artifact changes.
- Free-data monitoring (2026-11-06T07:50Z, `scripts/free_data_monitor.py`): new ledger `research_state/free_data_monitor_2026-11-06T0750Z.json` (checked_at_utc `2026-11-06T07:50:58.190796+00:00`, 14 candidates, SHA-256 `ae279a893dcbd060e7fe84d66213811925ff598146990c0ffe09c1e9d7a20580`). `axb0306/cme-futures-ohlc` verdict `free`, latest MNQ 1min/15min coverage ends **2026-04-15** (re-verified; no extension observed). **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified artifacts): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Prior session evidence (condensed)

- 2026-11-06T07:47Z (HEAD `80c9c8b`): clean pre-edit, 6/6 hashes MATCH, 24/24 artifacts parse, metrics `e06f9dd0...` MATCH (`net_pnl` -31637.98, `win_rate` 0.7, `profit_factor` 0.491672798902303), pytest **71 passed/0 failed** (0.89s), monitor `free_data_monitor_2026-11-06T0746Z.json` (14 candidates, SHA-256 `ae6cd5ff...`, checked `2026-11-06T07:47:03Z`), axb0306 ends 2026-04-15. No drift.
- Repeated bounded maintenance re-verifications (2026-11-06T00:58Z–07:48Z): 6/6 hashes MATCH, 24/24 artifacts parse, metrics hash `e06f9dd0...` unchanged, `axb0306/cme-futures-ohlc` MNQ coverage ends 2026-04-15, no genuinely free MNQ 1min/15min full-history extension beyond 2026-04-15. Pytest **71 passed / 0 failed** in pytest-capable envs; earlier "unavailable" reports were missing deps (resolved 2026-11-06T05:57Z by installing `pytest`/`pandas`/`numpy` into runner-local env). No code/strategy/parameter/data/raw/artifact changes.

## Blockers / durable constraints

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through **2026-04-15** (re-verified 2026-11-06T07:50Z via monitor ledger `free_data_monitor_2026-11-06T0750Z.json`, SHA-256 `ae279a893dcbd060e7fe84d66213811925ff598146990c0ffe09c1e9d7a20580`; no extension observed).
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- Carried-forward bounded sweep context (not used/purchased): FinzData ($49+), FirstRate ($99.95/yr), Portara, Kibot ($520–$820), historicalfuturesdata ($59–$129), MarketParquet ($79), Databento API-key/credits (key-gated), Kaggle unverified provenance/license/coverage, `getdata-finance` NQ equity cash/extended (not MNQ futures), `infoway` unverified (sample prices off MNQ scale; not ingested), `s-k-28/nq-es-trader-5k-payout` third-party repo artifacts (loader.py sources Yahoo/synthetic; not authoritative; not ingested).

## Next agent (immediate)

Maintenance/re-verification only — **completed 2026-11-06T07:50Z** (see "Current durable state"). Repeat the same bounded loop:
1. Re-verify repo state: `git status --short` (clean), all 6 tracked SHA-256 hashes, `ls artifacts/*.json | wc -l` (24, 0 parse errors), `python3 -m pytest -q` (71 passed, 0 failed; install missing deps if needed: `pip install pytest pandas numpy`).
2. Bounded free-data monitoring for a genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 (latest observed `axb0306/cme-futures-ohlc`). **Record provenance + SHA-256 before use.** Do not purchase data or bypass access controls/terms. Run `python3 scripts/free_data_monitor.py > research_state/free_data_monitor_<UTCstamp>.json` each session.
3. No experiments/tuning without explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0.
4. Update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence if anything changes. Commit durably.

## Next concrete work (if a genuinely free MNQ 1min/15min source with longer history is found)

Re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning. Recompute metrics independently from the trade ledger and store configs/hashes/ledger/summary/validation artifacts. Record provenance + SHA-256 before use.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
