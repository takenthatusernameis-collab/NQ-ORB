# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification pass — 514b8b3, 2026-11-05 07:28 UTC)

- Branch: `main`. HEAD `514b8b37c527dd6ba6b359b78852591da75116e1` (514b8b3). Working tree clean at verification start (`git status --short` empty). Recent commits: 514b8b3, 4f6a37b, 5335b33, e05c643, 35cb08b.
- SHA-256 re-verified from disk (2026-11-05 07:28 UTC): all 6 tracked file hashes match recorded values:
  - `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` — MATCH
  - `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4` — MATCH
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37` — MATCH (5609 rows)
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99` — MATCH (84078 rows)
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7` — MATCH (1059205 rows)
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4` — MATCH (70615 rows)
- Canonical artifacts: 25 entries in `artifacts/` (24 JSON files parse cleanly, 0 parse errors).
- Baselines/walk-forward unchanged from prior verified artifacts:
  - `axb0306`: 60 trades, net `-$31637.98`, win rate `70%`, profit factor `0.4917`, max DD `$37491.80`; walk-forward 3 windows, **all negative net P&L**.
  - `Kaggle front-month`: 688 trades, net `-$626525.96`, win rate `64.8%`, profit factor `0.2271`; walk-forward 8 windows, **all negative net P&L**.
  - Raw ranges (recorded): `MNQ_15min.csv` 5609 rows `2026-01-20T13:15 → 2026-04-15T23:15`; `MNQ_1min.csv` 84078 rows `2026-01-20T13:27 → 2026-04-15T23:29`; `MNQ_1min_frontmonth.csv` 1059205 rows `→ 2025-11-12T23:59`; `MNQ_15min_frontmonth.csv` 70615 rows `→ 2025-11-12T23:45`.
- Tests: `python3 -m pytest -q` → **71 passed, 0 failed** (0.89s) at 2026-11-05 07:28 UTC.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring (2026-11-05 bounded sweep): re-checked MarketParquet/historicalfuturesdata (MNQ 1min/15min annual bars paid $59/year; free limited to recent monthly samples / daily/account scope, intraday history beyond sample paid), FirstRate Data (intraday MNQ paid, $99.95/yr updates), Portara (paid), FinzData (paid $49+), Databento (paid credits/key-gated), Barchart (intraday paid), Yahoo Finance (daily only / limited recent intraday), Kibot (paid), GetData/TestMax (paid/restricted). Kaggle scan found MNQ 1-min dataset `brandenmorris/mnq-1-minute-data-5132025-11122025` (CC BY 4.0, 2025-05-13–2025-11-12, 200.6 MB OHLCV 1m) — **overlaps existing front-month coverage window ending 2025-11-12 and does not extend history**; NQ datasets are different instrument/contract scaling (not MNQ). **No new genuinely free MNQ 1min/15min full-history source identified.** Highest-value action remains bounded free-data re-sweep, not parameter fitting.

## Prior task (completed 2026-11-05, this session — maintenance re-verification)

- Re-verified git state (clean at start, HEAD 514b8b3), SHA-256 hashes (all 6 match), artifacts (24 JSON parse OK), raw row counts, tests (71 passed, 0 failed), baseline metrics (axb0306 net -$31637.98 / Kaggle net -$626525.96; all walk-forward windows negative). Ran bounded free-data monitoring sweep; no new free MNQ 1min/15min source that extends verified history. No data purchased; no credentials requested/stored. Updated `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`.

## Next agent (immediate)

See `INITIAL_TASK_FOR_NEXT_AGENT.md`. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available; monitor for genuinely free MNQ 1min/15min data (**record provenance + SHA-256 before use**); do not tune/change strategy without separately named versioned experiment with explicit diff from frozen `STRATEGY_RULES.txt` v1.0. Update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
