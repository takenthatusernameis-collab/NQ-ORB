# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification — 2026-11-06T03:42Z, this session)

- Session verification (2026-11-06T03:42Z, repo HEAD at verification `68c31e0`):" `git status --short` **clean** before durable-doc edits (exit 0). All 6 tracked SHA-256 hashes **MATCH** (full): `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`. 24 `artifacts/*.json`, 0 parse errors. `artifacts/metrics_axb0306.json` SHA-256 unchanged `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f` (verified `net_pnl` -31637.98, `win_rate` 0.7, `profit_factor` 0.491672798902303). `python3 -m pytest -q` **unavailable in this runner** (`/usr/bin/python3: No module named pytest`, exit 1) — recorded as runner drift; prior pytest-capable session (2026-11-06T02:05Z) reported 71 passed, 0 failed. No code/strategy/data/raw/artifact changes.
- Free-data monitoring (2026-11-06T03:42Z, `scripts/free_data_monitor.py` + bounded GitHub API re-check): `scripts/free_data_monitor.py` ran (tail captured). Ledger produced: `research_state/free_data_monitor_2026-11-06T0342Z.json` (checked_at_utc `2026-11-06T03:42:27.311015+00:00`, 13 candidates). Direct GitHub API re-check of `axb0306/cme-futures-ohlc` latest repo commit: `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` (2026-04-15T23:34:55Z, "Update 2026-04-15: 368 files updated") — **unchanged**. `axb0306` verdict `free`, latest MNQ 1min/15min coverage ends **2026-04-15**. **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified artifacts): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L.
- Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

## Prior session evidence (condensed)

- Repeated bounded maintenance re-verifications (2026-11-06T00:58Z–02:46Z, plus earlier sessions): consistent results when run — 6/6 hashes MATCH, 24/24 artifacts parse, pytest 71/0 in pytest-capable envs, metrics hash `e06f9dd0...` unchanged, `axb0306/cme-futures-ohlc` MNQ commit/blobs unchanged, no genuinely free MNQ 1min/15min full-history extension beyond 2026-04-15. No code/strategy/parameter/data/raw/artifact changes across these sessions. Prior session (2026-11-06T02:05Z, HEAD `18b8827`): 6/6 hashes MATCH, 24 artifacts 0 parse errors, pytest **71/0** (0.78s), ledger `research_state/free_data_monitor_2026-11-06T0205Z.json`. Prior session (2026-11-06T02:36Z, HEAD `24691d2`): 6/6 hashes MATCH, 24 artifacts 0 parse errors, pytest **unavailable** (runner drift), axb0306 commit `60abd3fb` (2026-04-15) unchanged. Prior session (2026-11-06T02:46Z, HEAD `918b500`): 6/6 hashes MATCH, 24 artifacts 0 parse errors, pytest **unavailable** (runner drift), metrics hash `e06f9dd0...` unchanged, `scripts/free_data_monitor.py` ran, ledger `free_data_monitor_2026-11-06T0239Z.json` present (17 candidates), direct API re-check confirmed axb0306 commit `60abd3fb` (2026-04-15) unchanged, no free MNQ extension. This session (2026-11-06T02:48Z, HEAD `96bc190`): 6/6 hashes MATCH, 24 artifacts 0 parse errors, pytest **unavailable** (runner drift), metrics hash `e06f9dd0...` unchanged, `scripts/free_data_monitor.py` ran, ledger `free_data_monitor_2026-11-06T0239Z.json` present (17 candidates, checked_at_utc `2026-11-06T02:40:51.240086+00:00`), direct API re-check confirmed axb0306 commit `60abd3fb` (2026-04-15) unchanged, no free MNQ extension.
This session (2026-11-06T03:42Z, HEAD `68c31e0`): 6/6 hashes MATCH, 24 artifacts 0 parse errors, pytest **unavailable** (runner drift), metrics hash `e06f9dd0...` unchanged, `scripts/free_data_monitor.py` ran, ledger `research_state/free_data_monitor_2026-11-06T0342Z.json` present (13 candidates, checked_at_utc `2026-11-06T03:42:27.311015+00:00`), direct API re-check confirmed axb0306 commit `60abd3fb` (2026-04-15) unchanged, no free MNQ extension. New ledger written; no code/strategy/data/raw/artifact changes.

## Blockers / durable constraints

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through 2026-04-15 (re-verified 2026-11-06T02:48Z via GitHub API repo-level commit `60abd3fb` 2026-04-15 unchanged; monitor ledger confirms MNQ files end 2026-04-15).
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- Runner note (2026-11-06T02:48Z): `pytest` **unavailable** in this runner (`/usr/bin/python3: No module named pytest`, exit 1) — recorded as drift. Prior pytest-capable session (2026-11-06T02:05Z) reported **71 passed, 0 failed**. Treat as runner-dependent.
- Carried-forward bounded sweep context (not used/purchased): FinzData ($49+), FirstRate ($99.95/yr), Portara, Kibot ($520–$820), historicalfuturesdata ($59–$129, limited free samples), MarketParquet ($79 full / limited free), Databento API-key/credits (dbn-cache key-gated), Kaggle unverified provenance/license/coverage, `getdata-finance` NQ equity cash/extended sessions (not MNQ futures).

## Next agent (immediate)

Maintenance/re-verification only:
1. Re-verify repo state: `git status --short` (clean), all 6 tracked SHA-256 hashes, `ls artifacts/*.json | wc -l` (24, 0 parse errors), `python3 -m pytest -q` (expected 71 passed, 0 failed in a pytest-capable env). If `pytest` unavailable, record runner constraint as drift and do not claim pass/fail.
2. Bounded free-data monitoring for a genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15. **Record provenance + SHA-256 before use.** Do not purchase data or bypass access controls/terms.
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
