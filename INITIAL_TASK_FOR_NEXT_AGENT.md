# Initial Task for Next Agent

## Status (maintenance re-verification — 2026-11-06T10:43Z, this session)

- `git status --short` **clean** before durable-doc edits (exit 0, HEAD `70fc2f2` before commit).
- Verification: all 6 tracked SHA-256 hashes **MATCH** (`STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`). 24 `artifacts/*.json`, 0 parse errors. `artifacts/metrics_axb0306.json` SHA-256 **MATCH** `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f` (`net_pnl` -31637.98, `win_rate` 0.7, `profit_factor` 0.491672798902303). `python3 -m pytest -q` **71 passed / 0 failed** (exit 0, 0.91s). No strategy/code/data/raw/artifact drift.
- Free-data monitoring (`scripts/free_data_monitor.py`): ledger `research_state/free_data_monitor_2026-11-06T1043Z.json` (checked_at_utc `2026-11-06T10:43:20.042456+00:00`, file SHA-256 `0cdf3a85cf30fdd1fd5e06a750d0a3cbe64bd352bbc1b82201243020d1d253a1`, 14 candidates, JSON valid). `axb0306/cme-futures-ohlc` HEAD `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` (2026-04-15T23:34:55Z, "Update 2026-04-15: 368 files updated"); latest MNQ 1min/15min coverage ends **2026-04-15** (no extension observed). **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

## Tasks (maintenance only — do in order)

1. **Re-verify repo state.** `git status --short` (expect clean before edits), re-compute all 6 tracked SHA-256 hashes against values in `HANDOFF.md`, confirm `ls artifacts/*.json | wc -l` = 24 and 0 parse errors, and run `python3 -m pytest -q` (expected **71 passed / 0 failed**; `pip install pytest pandas numpy` if needed). Record any drift with concrete evidence.
2. **Bounded free-data monitoring.** Check for a genuinely free MNQ 1min/15min full-history source extending beyond **2026-04-15** (`axb0306/cme-futures-ohlc` latest). **Record provenance + SHA-256 before use.** Do not purchase data or bypass access controls/terms. Run `python3 scripts/free_data_monitor.py > research_state/free_data_monitor_<UTCstamp>.json` and record checked_at, candidate count, file SHA-256, and axb0306 MNQ max end.
3. **No experiments/tuning.** Do not optimize thresholds, stops, targets, entry rules, or session times. Any change requires explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0.
4. **Update and commit durably.** Update `HANDOFF.md` and this file with concrete evidence if anything changes. Commit the monitor ledger and handoff updates.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` MNQ 1min/15min free coverage ends **2026-04-15** (re-verified 2026-11-06T10:43Z; ledger `research_state/free_data_monitor_2026-11-06T1043Z.json`, file SHA-256 `0cdf3a85cf30fdd1fd5e06a750d0a3cbe64bd352bbc1b82201243020d1d253a1`, checked `2026-11-06T10:43:20Z`, 14 candidates). Kaggle front-month ends 2025-11-12 (untouched OOS ~2.9 months). No free extension found without purchase.
- If a genuinely free MNQ 1min/15min source with longer history is found (**record provenance + SHA-256 before use**), next concrete task is a re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning. Recompute metrics independently from the trade ledger and store configs/hashes/ledger/summary/validation artifacts.
