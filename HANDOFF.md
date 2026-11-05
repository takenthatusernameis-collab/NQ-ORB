# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification — 2026-11-05T14:26Z, this session)

- Session-start verification (2026-11-05T14:25Z): `git status --short` clean before edits; HEAD `a7aae67` (checkpoint drift only; no strategy/code/data changes). All 6 tracked SHA-256 hashes **MATCH** recorded values; `ls artifacts/*.json | wc -l` = **24** (0 parse errors, all JSON parsed clean); `python3 -m pytest -q` → **71 passed, 0 failed** (0.65s).
- SHA-256 re-verified from disk (all **MATCH**): STRATEGY_RULES `6d3258c3...`, showcase config `2a6c5ff8...`, raw line counts 5609/84078/1059205/70615 (unchanged).
- Bounded free-data monitoring (2026-11-05T14:26Z): GitHub API `axb0306` MNQ path latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` — **no extension beyond 2026-04-15**. No genuinely free MNQ 1min/15min full-history source found. No data purchased; no credentials requested/stored; no code/strategy/parameter changes.
- Frozen baseline preserved; no code/strategy/parameter changes.

## Current durable state (maintenance re-verification — 2026-11-05T13:45Z, this session)

- Session-start verification (2026-11-05T13:44Z): `git status --short` clean before edits; HEAD `b2e3868` (checkpoint/history drift only from prior `3f63cdd`; no strategy/code/data changes). All 6 tracked SHA-256 hashes **MATCH** recorded values; `ls artifacts/*.json | wc -l` = **24** (0 parse errors, all JSON parsed clean); `python3 -m pytest -q` → **71 passed, 0 failed** (0.64s).
- SHA-256 re-verified from disk (all **MATCH**): STRATEGY_RULES `6d3258c3...`, showcase config `2a6c5ff8...`, raw line counts 5609/84078/1059205/70615 (unchanged).
- Bounded free-data monitoring (2026-11-05T13:45Z): GitHub API `axb0306` MNQ path latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` — **no extension beyond 2026-04-15**. No genuinely free MNQ 1min/15min full-history source found. No data purchased; no credentials requested/stored; no code/strategy/parameter changes.

## Current durable state (maintenance re-verification — 2026-11-05T13:43Z, this session)

- Session-start verification (2026-11-05T13:42Z): `git status --short` clean before edits; HEAD `3f63cdd` (recent `chore(kilo): checkpoint agent session` commits; prior handoff referenced `219f300` — checkpoint/history drift only, no strategy/code/data changes indicated). All 6 tracked SHA-256 hashes **MATCH** recorded values; `ls artifacts/*.json | wc -l` = **24** (0 parse errors, all JSON parsed clean); `python3 -m pytest -q` → **71 passed, 0 failed** (0.66s).
- SHA-256 re-verified from disk (all **MATCH**):
  - `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (126 lines)
  - `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4` (77 lines)
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37` (5609 lines)
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99` (84078 lines)
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7` (1059205 lines)
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4` (70615 lines)
- `artifacts/metrics_axb0306.json` SHA-256 unchanged: `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f` (9055 bytes).
- Baselines/walk-forward unchanged from verified artifacts (`metrics_axb0306_full.json` / `metrics_verify_axb0306.json`: net **-$31637.98**, win rate **70%**, profit factor **0.4917**; `metrics_kaggle.json` / `metrics_verify_kaggle.json`: net **-$626525.96**, win rate **64.8%**, profit factor **0.2271**). Prior verified walk-forward: `axb0306` 3 windows, **all negative net P&L**; Kaggle 8 windows, **all negative net P&L**.
- Bounded free-data monitoring (2026-11-05T13:43Z, this session):
  - GitHub API `repos/axb0306/cme-futures-ohlc/commits?path=MNQ&per_page=3` → latest MNQ-path commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` (priors `dc0dcf7179db` 2026-04-14, `18a6820b4c05` 2026-04-13) — **no extension beyond 2026-04-15**.
  - Bounded web sweep (2026-11-05): paid/proprietary — MarketParquet MNQ full 1-min archive 2019-05-06..2026-10-23 ($79 one-time; free = ~365d daily + Apr 6–10 2026 intraday sample pack), FirstRate Data MNQ intraday 2019-05-05..2026-11-02 (purchase + $99.95/yr updates), Portara MNQ 1-min full ~199.6 MB (paid), Kibot All Futures Continuous + individual 1-min (from 2009; MNQ from 2019-05-05, $820 bundle / paid tiers), FinzData/Barchart Premier/CME DataMine/Databento GLBX.MDP3 (credits/usage, not unrestricted free full history) — **not used/purchased**. Free but intraday-inadequate: Yahoo `MNQ=F`/`NQ=F` (1-min last ~30 days, 5-min 60d, 1h 730d), MarketParquet free (~365d daily + sample week), Barchart free (2y daily only). Kaggle `tgtanalytics/nq-futures-1min-bar-2022-2025` ends 2025-11-12 (no newer upload observed); `brandenmorris/mnq-1-minute-data-5132025-11122025` is a narrow 2025 slice only. **No genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 found.** No data purchased; no credentials requested/stored; no code/strategy/parameter changes.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.

## Prior task (completed 2026-11-05T13:38Z, this session — maintenance re-verification)

- Independently re-verified from `main` at session start (clean working tree before edits): all 6 tracked SHA-256 hashes **MATCH** (STRATEGY_RULES 126 lines, showcase config 77, raw line counts 5609/84078/1059205/70615). **24** artifact JSON files parse clean (0 errors); `artifacts/metrics_axb0306.json` SHA-256 unchanged (`e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f`, 9055 bytes). `python3 -m pytest -q` → **71 passed, 0 failed** (0.62s).
- HEAD advanced `b364ce6` → `219f300` via two intermediate checkpoint commits (`c20a2ae`, `219f300`); `git diff --stat b364ce6..HEAD` = only `HANDOFF.md` (16+/15-) and `INITIAL_TASK_FOR_NEXT_AGENT.md` (16+/15-) — **no code/data drift**.
- Bounded free-data monitoring (2026-11-05T13:38Z):
  - GitHub API `axb0306` MNQ path latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` (priors 2026-04-14/13) — **no extension beyond 2026-04-15**.
  - Kaggle `tgtanalytics/nq-futures-1min-bar-2022-2025` repo no longer resolves via GitHub API (`Not Found`) — consistent with prior observation that it ends 2025-11-12; **no newer upload, no extension**.
  - Bounded web sweep (2026-11-05, checked 2026-10-29..11-05): paid/proprietary — MarketParquet full 1-min archive 2007-12-31..2026-11-04 ($79 one-time), FirstRate Data (MNQ intraday 2019-05-05..2026-11-03, purchase + $99.95/yr updates), HistoricalFuturesData (MNQ 2019-05-05..2026-10-29, annual bars $59/yr; free tier = latest 3 months 10-sec/1m/2m/5m/30m/1h/4h + full daily only), Portara (MNQ 1-min full, paid), Kibot All Futures Continuous 1-min ($520 one-time, MNQ from 2019-05-05), FinzData/Barchart Premier/CME DataMine/Databento GLBX.MDP3 (credits/usage, not unrestricted free full history) — **not used/purchased**. Free but intraday-inadequate: Yahoo `MNQ=F`/`NQ=F` (1-min last ~30 days, 5-min 60d, 1h 730d), MarketParquet free (~365d daily + Apr 6–10 2026 intraday sample pack), Barchart free (2y daily only). **No genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 found.** No data purchased; no credentials requested/stored; no code/strategy/parameter changes.
- Updated `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`.

## Prior task (completed 2026-11-05T13:40Z, this session — maintenance re-verification)

- Independently re-verified from `main` at session start (clean working tree before edits): `git status --short` clean; all 6 tracked SHA-256 hashes **MATCH** recorded values (STRATEGY_RULES 126 lines, showcase config 77, raw line counts 5609/84078/1059205/70615). **24** artifact JSON files parse clean (0 errors); `artifacts/metrics_axb0306.json` SHA-256 unchanged (`e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f`, 9055 bytes). `python3 -m pytest -q` → **71 passed, 0 failed** (0.70s, 2026-11-05T13:40Z).
- HEAD unchanged at `219f300`; **no code/data drift** (no edits made beyond these handoff files).
- Bounded free-data monitoring (2026-11-05T13:40Z, this session):
  - GitHub API `axb0306` MNQ path latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` (priors 2026-04-14/13) — **no extension beyond 2026-04-15**.
  - Bounded web sweep (2026-11-05): paid/proprietary — MarketParquet full 1-min archive 2007-12-31..2026-11-04 ($79 one-time), FirstRate Data (MNQ intraday 2019-05-05..2026-11-03, purchase + $99.95/yr updates), HistoricalFuturesData (MNQ 2019-05-05..2026-10-29, annual bars $59/yr; free tier = latest 3 months only), Portara (MNQ 1-min full, paid), Kibot All Futures Continuous 1-min ($520 one-time), FinzData/Barchart Premier/CME DataMine/Databento GLBX.MDP3 (credits/usage, not unrestricted free full history) — **not used/purchased**. Free but intraday-inadequate: Yahoo `MNQ=F`/`NQ=F` (1-min last ~30 days, 5-min 60d, 1h 730d), MarketParquet free (~365d daily + Apr 6–10 2026 intraday sample pack), Barchart free (2y daily only). Kaggle `tgtanalytics/nq-futures-1min-bar-2022-2025` repo no longer resolves via GitHub API (`Not Found`); ends 2025-11-12; **no newer upload**. **No genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 found.** No data purchased; no credentials requested/stored; no code/strategy/parameter changes.
- Updated `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`.

## Next agent (immediate)

Maintenance/re-verification only:
1. Re-verify repo state: `git status --short` (clean), all 6 tracked SHA-256 hashes, `ls artifacts/*.json | wc -l` (24, 0 parse errors), `python3 -m pytest -q` (71 passed, 0 failed). Record any drift with concrete evidence.
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
