## Status (maintenance re-verification — 2026-11-06T19:07Z, this session)

- `git status --short` **clean** before work (exit 0).
- Verification: all 6 tracked SHA-256 hashes **MATCH** (`STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`). 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed / 0 failed** (exit 0, 0.94s). No strategy/code/data/raw/artifact drift.
- Free-data monitoring (`scripts/free_data_monitor.py`): ledger `research_state/free_data_monitor_20261106T190748Z.json` (checked_at_utc `2026-11-06T19:07:48.818291+00:00`, file SHA-256 `7b34f33c05ef915f958e1ef3d79af9bbbeb92ae736092aee53b33526270094fe`, 14 candidates, JSON valid). `axb0306/cme-futures-ohlc` verdict **free** (commit `60abd3fb`, dated `2026-04-15T23:34:55Z`); note "Latest MNQ 1min/15min coverage ends 2026-04-15. Re-verified each session; no extension observed." **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

## Status (maintenance re-verification — 2026-11-06T19:05Z, this session)

- `git status --short` **clean** before work (exit 0).
- Verification: all 6 tracked SHA-256 hashes **MATCH** (`STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`). 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed / 0 failed** (exit 0, 0.89s). No strategy/code/data/raw/artifact drift.
- Free-data monitoring (`scripts/free_data_monitor.py`): ledger `research_state/free_data_monitor_20261106T190512Z.json` (checked_at_utc `2026-11-06T19:05:12.434292+00:00`, file SHA-256 `4328817a40e09496fcaa8394f1445713eaa6da75202d07c88140885358f3c55a`, 14 candidates, JSON valid). `axb0306/cme-futures-ohlc` verdict **free**; note "Latest MNQ 1min/15min coverage ends 2026-04-15. Re-verified each session; no extension observed." **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

## Status (maintenance re-verification — 2026-11-06T17:57Z, this session)

- `git status --short` **clean** before work (exit 0).
- Verification: all 6 tracked SHA-256 hashes **MATCH**. 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed / 0 failed** (exit 0, 0.93s). No strategy/code/data/raw/artifact drift.
- Free-data monitoring (`scripts/free_data_monitor.py`): ledger `research_state/free_data_monitor_2026-11-06T1757Z.json` (checked_at_utc `2026-11-06T17:57:35.820031+00:00`, file SHA-256 `ce3080567e9a7c329156a543a1bad9237e7482f5366cf1ab3bb5426baa21f6d0`, 14 candidates, JSON valid). `axb0306/cme-futures-ohlc` verdict **free**; note "Latest MNQ 1min/15min coverage ends 2026-04-15. Re-verified each session; no extension observed." **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

# Initial Task for Next Agent

## Status (maintenance re-verification — 2026-11-06T17:57Z, this session)

- `git status --short` **clean** before work (exit 0).
- Verification: all 6 tracked SHA-256 hashes **MATCH**. 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed / 0 failed** (exit 0, 0.98s). No strategy/code/data/raw/artifact drift.
- Free-data monitoring (`scripts/free_data_monitor.py`): ledger `research_state/free_data_monitor_2026-11-06T1756Z.json` (checked_at_utc `2026-11-06T17:56:59.390492+00:00`, file SHA-256 `fca2cb6e2283994f0fa297dfb598bdb2d722f6ba39e1dc2ded40810c10b37505`, 14 candidates, JSON valid). `axb0306/cme-futures-ohlc` verdict **free**; note "Latest MNQ 1min/15min coverage ends 2026-04-15. Re-verified each session; no extension observed." **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found.

## Status (maintenance re-verification — 2026-11-06T17:56Z, this session)

- `git status --short` **clean** before work (exit 0).
- Verification: all 6 tracked SHA-256 hashes **MATCH** (`STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`). 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed / 0 failed** (exit 0, 1.00s). No strategy/code/data/raw/artifact drift.
- Free-data monitoring (`scripts/free_data_monitor.py`): ledger `research_state/free_data_monitor_2026-11-06T1756Z.json` (checked_at_utc `2026-11-06T17:56:06.138468+00:00`, file SHA-256 `f375269280be1299da85516f99c222b6f8739c8e66e41b1267eda36570459366`, 14 candidates, JSON valid). `axb0306/cme-futures-ohlc` verdict **free**; note "Latest MNQ 1min/15min coverage ends 2026-04-15. Re-verified each session; no extension observed." **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

- `git status --short` **clean** before work (exit 0).
- Verification: all 6 tracked SHA-256 hashes **MATCH** (`STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`). 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed / 0 failed** (exit 0, 0.98s). No strategy/code/data/raw/artifact drift.
- Free-data monitoring (`scripts/free_data_monitor.py`): ledger `research_state/free_data_monitor_2026-11-06T1752Z.json` (checked_at_utc `2026-11-06T17:51:57.422724+00:00`, file SHA-256 `948e34d199a5d0ff00d3977123312dbe71b7ce9ddcc90a81255299157620b334`, 14 candidates, JSON valid). `axb0306/cme-futures-ohlc` verdict **free**; note "Latest MNQ 1min/15min coverage ends 2026-04-15. Re-verified each session; no extension observed." **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
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

## Status (maintenance re-verification — 2026-11-06T17:58Z, this session)

- `git status --short` **clean** before work (exit 0).
- Verification: all 6 tracked SHA-256 hashes **MATCH**. 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed / 0 failed** (exit 0, 0.89s). No strategy/code/data/raw/artifact drift.
- Free-data monitoring (`scripts/free_data_monitor.py`): ledger `research_state/free_data_monitor_2026-11-06T1758Z.json` (checked_at_utc `2026-11-06T17:58:11.571519+00:00`, file SHA-256 `f1421ca053cfe80e34870d0dee04bf74476c2226e717d423e978546bdb3cfa06`, 14 candidates, JSON valid). `axb0306/cme-futures-ohlc` verdict **free**; note "Latest MNQ 1min/15min coverage ends 2026-04-15. Re-verified each session; no extension observed." **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

### Next agent task (2026-11-06T19:07Z)

Repeat bounded maintenance loop: re-verify repo state (`git status --short` clean before edits; re-compute all 6 tracked SHA-256 hashes against values in `HANDOFF.md`; confirm `ls artifacts/*.json | wc -l` = 24 and 0 parse errors; run `python3 -m pytest -q`, expected **71 passed / 0 failed**), run `python3 scripts/free_data_monitor.py > research_state/free_data_monitor_<UTCstamp>.json`, and record ledger SHA-256 / checked_at / candidate count / axb0306 MNQ max end. No tuning — do not optimize thresholds, stops, targets, entry rules, or session times; any change requires explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0. Update `HANDOFF.md` and this file with concrete evidence if anything changes, then commit durably.

Latest completed: **2026-11-06T19:07Z** (ledger `research_state/free_data_monitor_20261106T190748Z.json`, SHA-256 `7b34f33c05ef915f958e1ef3d79af9bbbeb92ae736092aee53b33526270094fe`, checked `2026-11-06T19:07:48.818291+00:00`, 14 candidates; axb0306 MNQ 1min/15min ends 2026-04-15, no extension observed).

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` MNQ 1min/15min free coverage ends **2026-04-15** (re-verified 2026-11-06T19:05Z; ledger `research_state/free_data_monitor_20261106T190512Z.json`, file SHA-256 `4328817a40e09496fcaa8394f1445713eaa6da75202d07c88140885358f3c55a`, checked `2026-11-06T19:05:12.434292+00:00`, 14 candidates). Kaggle front-month ends 2025-11-12 (untouched OOS ~2.9 months). No free extension found without purchase.
- If a genuinely free MNQ 1min/15min source with longer history is found (**record provenance + SHA-256 before use**), next concrete task is a re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning. Recompute metrics independently from the trade ledger and store configs/hashes/ledger/summary/validation artifacts.