# Initial Task for Next Agent

## Status (maintenance re-verification — 2026-11-06T01:59Z, this session)

- `git status --short` **clean** (exit 0) before durable-doc edits. Repo HEAD at verification `31d9c4a`.
- This-session verification (2026-11-06T01:59Z): all 6 tracked SHA-256 hashes **MATCH** (full): `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`. 24 `artifacts/*.json`, 0 parse errors; `artifacts/metrics_axb0306.json` SHA-256 unchanged `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f` (net -$31637.98, win 0.7, PF 0.491672798902303). `python3 -m pytest -q` **71 passed, 0 failed** (0.67s). No strategy/code/data/raw/artifact drift. Evidence: `research_state/free_data_monitor_2026-11-06T01Z.json`.
- Free-data monitoring (2026-11-06T01:58Z, GitHub API + independent sweep): `axb0306/cme-futures-ohlc` latest commit unchanged `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` (2026-04-15T23:34:55Z); MNQ 1min/15min files end `20260120_20260415`. **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified artifacts): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L.
- Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

## Tasks (maintenance only — do in order)

1. **Re-verify repo state.** Run `git status --short` (expect clean before edits), re-compute all 6 tracked SHA-256 hashes against values above, confirm `ls artifacts/*.json | wc -l` = 24 and 0 parse errors, and run `python3 -m pytest -q` (expected **71 passed / 0 failed** in a pytest-capable environment). If `pytest` is unavailable, record the runner constraint with concrete evidence and do not claim pass/fail. Record any drift with concrete evidence.
2. **Bounded free-data monitoring.** Check for a genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 (current latest free coverage in `axb0306/cme-futures-ohlc`). **Record provenance + SHA-256 before use.** Do not purchase data or bypass access controls/terms. Append a new `research_state/free_data_monitor_<timestamp>.json` ledger entry each session.
3. **No experiments/tuning.** Do not optimize thresholds, stops, targets, entry rules, or session times. Any change requires explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0.
4. **Update handoff files.** Update `HANDOFF.md` and this file with concrete evidence if anything changes (hashes, test counts, artifacts, new data candidates, blockers, runner/test constraints). Commit durably.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through 2026-04-15 (re-verified 2026-11-06T01:58Z; repo commit `60abd3fb` unchanged; MNQ files end `20260120_20260415`).
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- Runner note (2026-11-06T01:59Z): `pytest` available — **71 passed, 0 failed** (0.67s). Prior sessions observed runner drift (pytest unavailable); treat as runner-dependent.
- If a genuinely free MNQ 1min/15min source with longer history is found (**record provenance + SHA-256 before use**), the next concrete task is a re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning. Recompute metrics independently from the trade ledger and store configs/hashes/ledger/summary/validation artifacts.
