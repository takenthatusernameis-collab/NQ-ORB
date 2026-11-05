# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification — 2026-11-05 ~09:29 UTC, this session)

- Branch: `main`. HEAD at `950e5dc` (`chore(kilo): checkpoint agent session`) at verification start; working tree clean before handoff edits; only `HANDOFF.md`/`INITIAL_TASK_FOR_NEXT_AGENT.md` modified during this session. Code/data unchanged from prior maintenance checkpoints.
- SHA-256 re-verified from disk (2026-11-05 ~09:29 UTC): all 6 tracked file hashes **MATCH** recorded values:
  - `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` — MATCH
  - `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4` — MATCH
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37` — MATCH (5609 rows)
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99` — MATCH (84078 rows)
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7` — MATCH (1059205 rows)
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4` — MATCH (70615 rows)
- Canonical artifacts: **24** JSON files in `artifacts/` parse cleanly (0 parse errors).
- Baselines/walk-forward unchanged from verified artifacts (`metrics_axb0306_full.json` / `metrics_verify_axb0306.json`: net `-$31637.98`, win rate `70%`, profit factor `0.4917`; `metrics_kaggle.json` / `metrics_verify_kaggle.json`: net `-$626525.96`, win rate `64.8%`, profit factor `0.2271`). Prior verified walk-forward: `axb0306` 3 windows, **all negative net P&L**; Kaggle 8 windows, **all negative net P&L**.
- Raw row counts unchanged (2026-11-05): `MNQ_15min` 5609; `MNQ_1min` 84078; `MNQ_1min_frontmonth` 1059205; `MNQ_15min_frontmonth` 70615 (total 1219507).
- Tests: `python3 -m pytest -q` → **71 passed, 0 failed** (0.88s) at 2026-11-05 ~09:29 UTC.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring (2026-11-05 ~09:29 UTC bounded sweep, this session): GitHub API `repos/axb0306/cme-futures-ohlc/contents/MNQ` lists 1min/15min only through 2026-04-15 (`MNQ_1min_20260120_20260415.csv` 4904282 bytes sha `946c6b76d68548e5b1fe584b6e16de0f19f6d0d4`; `MNQ_15min_20260120_20260415.csv` 333668 bytes sha `7df047964034b648ad7d8639515b6c9a92998af0`) — **no extension beyond 2026-04-15**. Latest commit on MNQ path `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated 2026-04-15T23:34:55Z — unchanged. Kaggle re-scan: `brandenmorris/mnq-1-minute-data-5132025-11122025` still ends 2025-11-12 (already ingested as Kaggle front-month baseline); its byte-identical duplicate `brandenmorris/mnq-1m-q4-2022-q4-2025-ts-ohlcv-sym` yields no new history. All other candidates paid or key-gated: MarketParquet ($79 one-time intraday archive; free tier daily-only + 1-week sample), FirstRate Data ($99.95/yr after 1 free month), Portara (paid), Kibot ($240–820 one-time), Databento (key-gated + credit-based), Yahoo Finance (MNQ=F daily only / 30-day 1-minute), Barchart (intraday needs Premier), FinzData ($49 one-time; free tier last 30 days daily only), CME DataMine (priced), investing.com (daily-only), infoway.io (API key required). **No new genuinely free MNQ 1min/15min full-history source identified.** Highest-value action remains bounded free-data re-sweep, not parameter fitting.

## Prior task (completed 2026-11-05 ~09:29 UTC, this session — maintenance re-verification)

- Re-verified from `main` HEAD `950e5dc` (working tree clean before handoff edits): all 6 tracked SHA-256 hashes **MATCH**; **24** artifact JSON files parse clean (0 errors); raw row counts unchanged (5609/84078/1059205/70615; total 1219507). `python3 -m pytest -q` → **71 passed, 0 failed** (0.88s, 2026-11-05 ~09:29 UTC). Bounded free-data sweep (GitHub API `repos/axb0306/cme-futures-ohlc/contents/MNQ` + commits `?path=MNQ&per_page=1`; Kaggle brandenmorris datasets; live websearch for free MNQ 1min/15min): axb0306 MNQ path latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` 2026-04-15T23:34:55Z — **no extension**; same 8 files with matching sizes/shas. Kaggle brandenmorris still ends 2025-11-12 (already ingested); duplicate yields no new history. No new genuinely free MNQ 1min/15min full-history source located. No data purchased; no credentials requested/stored; no code/strategy/parameter changes. Updated `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence.

## Next agent (immediate)

See `INITIAL_TASK_FOR_NEXT_AGENT.md`. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available; monitor for genuinely free MNQ 1min/15min data (**record provenance + SHA-256 before use**); do not tune/change strategy without separately named versioned experiment with explicit diff from frozen `STRATEGY_RULES.txt` v1.0. Update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
