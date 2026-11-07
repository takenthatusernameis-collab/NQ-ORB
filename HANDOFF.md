# Handoff

## Current session verification (2026-11-07T03:31:14Z, this session)

- `git status --short` at start: **clean** (no tracked/untracked changes).
- All 6 tracked SHA-256 hashes **MATCH**:
  - `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`
  - `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`
- `python3 scripts/free_data_monitor.py` executed → `research_state/free_data_monitor_20261107T033114Z.json` (file SHA-256 `ff2787947a27b0bcba0b497305084ed3836561f4adda9b36719ee8453ec9988d`, `checked_at_utc` `2026-11-07T03:31:14.572040+00:00`, **14 candidates**, JSON valid).
- axb0306/cme-futures-ohlc: verdict `free`; latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z`; MNQ 1min/15min coverage ends **2026-04-15**, **no extension observed** (re-verified). `git status --short` after run shows only untracked `research_state/free_data_monitor_20261107T033114Z.json` (and prior untracked ledgers remain if any).
- `pytest` unavailable in this env (`No module named pytest`); prior verified baseline: **71 passed** (2026-11-06T21:11Z). No code changes this session.
- No code/strategy/data/raw/artifact changes this session.

## Current durable state (as of 2026-11-07T03:31:14Z)

- Baselines unchanged: axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0).

## Next agent (immediate)

Repeat the bounded maintenance loop (re-verify state, run `scripts/free_data_monitor.py`, record evidence, no tuning).

## Recent session ledger (compact; full history in `research_state/` and git)

- 2026-11-07T03:32:34Z: `free_data_monitor_20261107T033232Z.json` SHA-256 `c0aaa8d38904497fabf9493bb81f25a8e7c127986961c8a4a03719cbe5f50716` (checked `2026-11-07T03:32:34.195556+00:00`), 14 candidates, git clean at start, all 6 hashes match, axb0306 `60abd3fb...` dated `2026-04-15T23:34:55Z`, MNQ 1min/15min ends 2026-04-15 (no extension). pytest unavailable (prior 71 passed). No changes.
- 2026-11-07T03:31:14Z: `free_data_monitor_20261107T033114Z.json` SHA-256 `ff2787947a27b0bcba0b497305084ed3836561f4adda9b36719ee8453ec9988d` (checked `2026-11-07T03:31:14.572040+00:00`), 14 candidates, git clean at start, all 6 hashes match, axb0306 `60abd3fb...` dated `2026-04-15T23:34:55Z`, MNQ 1min/15min ends 2026-04-15 (no extension). pytest unavailable (prior 71 passed). No changes.
- 2026-11-07T03:30:01Z: `free_data_monitor_20261107T033001Z.json` SHA-256 `03f9a43f6e67e76da0b86fd44f5b2404bd2e3efb7eb4764581cb53517a0dce43` (checked `2026-11-07T03:29:58.408707+00:00`), 14 candidates, axb0306 ends 2026-04-15 (no extension). No changes.
- 2026-11-07T03:29:01Z: `free_data_monitor_20261107T032909Z.json` SHA-256 `bb2fd421dfd5d1abb0c9192929f8b7fa07a091185295f5b37bdbb6bbcf12218a`, axb0306 ends 2026-04-15 (no extension). No changes.
- 2026-11-07T03:27:52Z: `free_data_monitor_20261107T032752Z.json` SHA-256 `8e064497def196695d1a6013479658338e115cd7d4e44f4c1b3432f0a5491d7a`, axb0306 ends 2026-04-15 (no extension). No changes.
- 2026-11-07T03:26:08Z: `free_data_monitor_20261107T032608Z.json` SHA-256 `908850c178b4dd4cc55fdafdba017c4aa7d9d1ab8eee722465dc2d1acce32200`, axb0306 ends 2026-04-15 (no extension). No changes.

## Blockers / durable constraints

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through **2026-04-15**.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
