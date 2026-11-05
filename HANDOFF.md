# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification pass — 2026-11-05 08:25 UTC, this session)

- Branch: `main`. HEAD at verification: `2f5b27b` (2026-11-05, `chore(kilo): checkpoint agent session`). Working tree clean at verification (`git status --short` empty). Recent commits: 2f5b27b, 1f365bc, 7e57736.
- SHA-256 re-verified from disk (2026-11-05): all 6 tracked file hashes match recorded values:
  - `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` — MATCH
  - `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4` — MATCH
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37` — MATCH (5609 rows)
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99` — MATCH (84078 rows)
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7` — MATCH (1059205 rows)
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4` — MATCH (70615 rows)
- Canonical artifacts: **24** JSON files in `artifacts/` parse cleanly (0 parse errors).
- Baselines/walk-forward unchanged from verified artifacts (`metrics_axb0306_full.json` / `metrics_verify_axb0306.json`: net `-$31637.98`, win rate `70%`, profit factor `0.4917`; `metrics_kaggle.json` / `metrics_verify_kaggle.json`: net `-$626525.96`, win rate `64.8%`, profit factor `0.2271`). Prior verified walk-forward: `axb0306` 3 windows, **all negative net P&L**; Kaggle 8 windows, **all negative net P&L**.
- Raw row counts unchanged (wc -l): `MNQ_15min` 5609; `MNQ_1min` 84078; `MNQ_1min_frontmonth` 1059205; `MNQ_15min_frontmonth` 70615 (total 1219507).
- Tests: `python3 -m pytest -q` → **71 passed, 0 failed** (0.92s) at 2026-11-05 08:25 UTC.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring (2026-11-05 bounded sweep, this session): `axb0306/cme-futures-ohlc` MNQ `contents/MNQ` listing shows `MNQ_1min_20260120_20260415.csv` / `MNQ_15min_20260120_20260415.csv` (no newer MNQ 1min/15min filenames; latest intraday coverage remains through 2026-04-15). MarketParquet/FirstRate/Kibot/Databento/Yahoo remain paid, key-gated, daily/limited intraday, or insufficient for free full-history MNQ 1min/15min. **No new genuinely free MNQ 1min/15min full-history source identified.** Highest-value action remains bounded free-data re-sweep, not parameter fitting.

## Prior task (completed 2026-11-05 08:25 UTC, this session — maintenance re-verification)

- Re-verified from `main` HEAD `2f5b27b` (clean at verification): all 6 tracked SHA-256 hashes MATCH (`STRATEGY_RULES.txt`, `config/orb_mnq_15m_showcase.yaml`, `raw/MNQ_{15min,1min,1min_frontmonth,15min_frontmonth}.csv`); **24** artifact JSON files parse clean (0 errors); raw row counts unchanged (5609/84078/1059205/70615; total 1219507). `python3 -m pytest -q` → **71 passed, 0 failed** (0.92s, 2026-11-05 08:25 UTC). Bounded free-data sweep: `axb0306/cme-futures-ohlc` MNQ `contents/MNQ` still lists `MNQ_1min_20260120_20260415.csv` / `MNQ_15min_20260120_20260415.csv` — no extension beyond 2026-04-15. No new genuinely free MNQ 1min/15min full-history source identified. No data purchased; no credentials requested/stored; no code/strategy/parameter changes. Updated `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence.

## Next agent (immediate)

See `INITIAL_TASK_FOR_NEXT_AGENT.md`. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available; monitor for genuinely free MNQ 1min/15min data (**record provenance + SHA-256 before use**); do not tune/change strategy without separately named versioned experiment with explicit diff from frozen `STRATEGY_RULES.txt` v1.0. Update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
