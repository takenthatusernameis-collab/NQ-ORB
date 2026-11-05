# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification — 2026-11-05T11:30Z, this session)

- Branch: `main`. HEAD at verification: `4ca6568`. `git status --short` clean. **No code/data drift.**
- SHA-256 re-verified from disk (all **MATCH** recorded values):
  - `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` — MATCH (126 lines)
  - `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4` — MATCH (77 lines)
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37` — MATCH (5609 lines)
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99` — MATCH (84078 lines)
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7` — MATCH (1059205 lines)
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4` — MATCH (70615 lines)
- Canonical artifacts: **24** JSON files in `artifacts/` parse cleanly (0 parse errors).
- Baselines/walk-forward unchanged from verified artifacts (`metrics_axb0306_full.json` / `metrics_verify_axb0306.json`: net **-$31637.98**, win rate **70%**, profit factor **0.4917**; `metrics_kaggle.json` / `metrics_verify_kaggle.json`: net **-$626525.96**, win rate **64.8%**, profit factor **0.2271**). Prior verified walk-forward: `axb0306` 3 windows, **all negative net P&L**; Kaggle 8 windows, **all negative net P&L**.
- Committed `artifacts/metrics_axb0306.json` SHA-256 re-verified: `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f` (9055 bytes) — unchanged.
- Tests: `python3 -m pytest -q` → **71 passed, 0 failed** (0.89s, 2026-11-05T11:30Z).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring (2026-11-05T11:30Z bounded check, this session): GitHub API `repos/axb0306/cme-futures-ohlc/commits?path=MNQ&per_page=3` → latest MNQ-path commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z` (`Update 2026-04-15: 368 files updated`); prior `dc0dcf7179dbe40397bb1840f179736276d47dd7` 2026-04-14, `18a6820b` 2026-04-13 — **no extension beyond 2026-04-15**. Web sweep (2026-11-05): PortaraCQG, FirstRate Data, GetData ($49.99), FinzData, MarketParquet paid archive, Databento (credit-gated) are paid/proprietary; TestMax is a replay platform (not downloadable full-history data); Yahoo Finance (MNQ=F) and MarketParquet free are free but intraday-inadequate (30 days 1-min / sample week). **No genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 found.** Highest-value action remains bounded free-data re-sweep, not parameter fitting.

## Prior task (completed 2026-11-05T11:30Z, this session — maintenance re-verification)

- Independently re-verified from `main` at HEAD `4ca6568` (clean working tree; no code/data drift): all 6 tracked SHA-256 hashes **MATCH** (STRATEGY_RULES 126 lines, showcase config 77, raw line counts 5609/84078/1059205/70615). **24** artifact JSON files parse clean (0 errors); `artifacts/metrics_axb0306.json` SHA-256 unchanged (`e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f`, 9055 bytes). `python3 -m pytest -q` → **71 passed, 0 failed** (0.89s).
- Bounded free-data monitoring, this session (2026-11-05T11:30Z): `axb0306` MNQ path latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` — **no extension beyond 2026-04-15**. Web sweep found no free full-history MNQ 1min/15min source beyond 2026-04-15 (paid/proprietary: PortaraCQG, FirstRate, GetData, FinzData, MarketParquet paid, Databento; not downloadable: TestMax replay; free but inadequate: Yahoo 30-day 1-min, MarketParquet sample week). No data purchased; no credentials requested/stored; no code/strategy/parameter changes. Updated `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`.

## Next agent (immediate)

Maintenance/re-verification only:
1. Re-verify repo state: `git status --short` (clean), all 6 tracked SHA-256 hashes, `ls artifacts/*.json | wc -l` (24), `python3 -m pytest -q` (71 passed, 0 failed). Record any drift with concrete evidence.
2. Bounded free-data monitoring for a genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 (current latest free coverage); **record provenance + SHA-256 before use**. Do not purchase data or bypass access controls/terms.
3. No experiments/tuning without explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0. Do not optimize thresholds, stops, targets, entry rules, or session times.
4. Update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence if anything changes (hashes, test counts, artifacts, new data candidates, blockers).

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

(End of file)
