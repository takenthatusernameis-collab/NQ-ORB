# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification pass — 2026-11-05 07:34–07:36 UTC)

- Branch: `main`. HEAD at verification: `dc23a6a` (2026-11-05, `chore(kilo): checkpoint agent session`). Working tree clean at verification start (`git status --short` empty). Recent commits: 3022343, 0d9618d, 650ae0a, 514b8b3, 4f6a37b.
- SHA-256 re-verified from disk (2026-11-05): all 6 tracked file hashes match recorded values:
  - `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` — MATCH
  - `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4` — MATCH
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37` — MATCH (5609 rows)
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99` — MATCH (84078 rows)
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7` — MATCH (1059205 rows)
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4` — MATCH (70615 rows)
- Canonical artifacts: 25 JSON files in `artifacts/` parse cleanly (0 parse errors; 25 files).
- Baselines/walk-forward unchanged from verified artifacts (`metrics_axb0306_full.json` / `metrics_verify_axb0306.json`: 60 trades, net `-$31637.98`, win rate `70%`, profit factor `0.4917`; `metrics_kaggle.json` / `metrics_verify_kaggle.json`: 688 trades, net `-$626525.96`, win rate `64.8%`, profit factor `0.2271`). Prior verified walk-forward: `axb0306` 3 windows, **all negative net P&L**; Kaggle 8 windows, **all negative net P&L**.
- Raw row counts unchanged (wc -l): `MNQ_15min` 5609; `MNQ_1min` 84078; `MNQ_1min_frontmonth` 1059205; `MNQ_15min_frontmonth` 70615 (total 1219507).
- Tests: `python3 -m pytest -q` → **71 passed, 0 failed** (0.94s) at 2026-11-05 07:36 UTC.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring (2026-11-05 bounded sweep, this session): axb0306/cme-futures-ohlc MNQ path still shows the same 8 files (1min/5min/15min/30min/1h/4h/daily/tick) with 1min covering `20260120_20260415` — no extension beyond the already-ingested short series. No new GitHub-hosted MNQ 1min/15min full-history source found in search. MarketParquet free tier remains daily-only (last ~365 days) + 1-week intraday sample (Apr 6–10, 2026); full MNQ 1-min archive $79 one-time (paid). FirstRate Data $99.95/yr after 1 month updates (paid). Kibot $520 all-futures continuous 1-min (paid). Yahoo Finance daily-only for MNQ=F history; intraday limited windows (not a free full-history archive). NQ sources (e.g. getdata-finance/nq-1m, FirstRate NQ, Yahoo NQ) are NQ ($20/point), not MNQ — excluded per STRATEGY_RULES.txt. **No new genuinely free MNQ 1min/15min full-history source identified.** Highest-value action remains bounded free-data re-sweep, not parameter fitting.

## Prior task (completed 2026-11-05, this session — maintenance re-verification)

- Re-verified from `main` HEAD `30223432adb34ab1fb3bdd0b88498bef9df9e9e3`: working tree clean at start; all 6 tracked SHA-256 hashes match (`STRATEGY_RULES.txt`, `config/orb_mnq_15m_showcase.yaml`, `raw/MNQ_{15min,1min,1min_frontmonth,15min_frontmonth}.csv`); 24 artifact JSON files parse clean; raw row counts unchanged (5609/84078/1059205/70615). `python3 -m pytest -q` → **71 passed, 0 failed** (0.89s). Bounded free-data sweep found no new genuinely free MNQ 1min/15min source extending verified history (axb0306 MNQ intraday still 2026-01-20..2026-04-15; Kaggle-brand sources still end 2025-11-12 / no extension; MarketParquet/FirstRate/Kibot/Databento/Yahoo/investor portals paid/key-gated/daily-only/insufficient; NQ sources excluded). No data purchased; no credentials requested/stored; no code/strategy/parameter changes. Updated `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence.

## Next agent (immediate)

See `INITIAL_TASK_FOR_NEXT_AGENT.md`. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available; monitor for genuinely free MNQ 1min/15min data (**record provenance + SHA-256 before use**); do not tune/change strategy without separately named versioned experiment with explicit diff from frozen `STRATEGY_RULES.txt` v1.0. Update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
