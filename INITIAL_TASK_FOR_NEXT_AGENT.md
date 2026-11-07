# Initial task for next agent

## Completed this session (2026-11-07T06:29:54Z)
- State re-verified: all 6 tracked SHA-256 hashes match; `git log --oneline -1` at start = `84d3cd3 chore(kilo): checkpoint agent session`.
- `python3 scripts/free_data_monitor.py` ran → `research_state/free_data_monitor_20261107T062954Z.json` (SHA-256 `ff9e6d5686ada43bdeeea15768e7addf09d6e0e7d9dc4611ab2b68d016573ef0`, checked `2026-11-07T06:29:54.199270+00:00`, 14 candidates, JSON valid). Recorded in `HANDOFF.md` Current session verification + Recent session ledger.
- axb0306/cme-futures-ohlc: verdict `free`; latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z`; MNQ 1min/15min coverage ends **2026-04-15**, no extension observed. No free-data extension appeared.
- No code/strategy/data/raw/artifact changes. `pytest` unavailable in this env (prior verified baseline: 71 passed, 2026-11-06T21:11Z).

## Completed prior session (2026-11-07T05:40:25Z)
- State re-verified: all 6 tracked SHA-256 hashes match (STRATEGY_RULES.txt `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`, config/orb_mnq_15m_showcase.yaml `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`, raw/MNQ_15min.csv `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`, raw/MNQ_1min.csv `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`, raw/MNQ_1min_frontmonth.csv `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`, raw/MNQ_15min_frontmonth.csv `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`); `git log --oneline -1` at start = `4347fdc chore(kilo): checkpoint agent session`.
- `python3 scripts/free_data_monitor.py` ran → `research_state/free_data_monitor_20261107T054025Z.json` (SHA-256 `c71282e184cb68c197fe0a8d008c91bd2e072908ecfbc861b37d714a13d95bb6`, checked `2026-11-07T05:40:40.847493+00:00`, 14 candidates, JSON valid). Recorded in `HANDOFF.md` Current session verification + Recent session ledger.
- axb0306/cme-futures-ohlc: verdict `free`; latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z`; MNQ 1min/15min coverage ends **2026-04-15**, no extension observed. No free-data extension appeared.
- No code/strategy/data/raw/artifact changes. `pytest` unavailable in this env (prior verified baseline: 71 passed, 2026-11-06T21:11Z).

## Read first (do not skip)
- `HANDOFF.md` (current state, recent ledger, deadline 2026-11-08T06:00Z)
- `STRATEGY_RULES.txt` (frozen baseline v1.0; no silent changes)
- `PROMPT.md` (research workflow)
- `AGENTS.md` (hard boundaries)

## Immediate task (bounded maintenance loop)
Repeat until controller deadline **2026-11-08T06:00Z** or a verified free-data extension appears:

1. **Verify state** (start of session)
   - `git status --short` (expect clean except expected untracked `research_state/free_data_monitor_*.json` ledgers)
   - Verify tracked SHA-256 hashes for: `STRATEGY_RULES.txt`, `config/orb_mnq_15m_showcase.yaml`, `raw/MNQ_15min.csv`, `raw/MNQ_1min.csv`, `raw/MNQ_1min_frontmonth.csv`, `raw/MNQ_15min_frontmonth.csv`
   - Confirm `git log --oneline -1`

2. **Run free-data monitor and record evidence**
   - `python3 scripts/free_data_monitor.py` (no downloads/purchases)
   - Save output as `research_state/free_data_monitor_YYYYMMDDTHHMMSSZ.json` (UTC)
   - Compute SHA-256 of that JSON and record it in `HANDOFF.md` recent ledger
   - Re-verify axb0306/cme-futures-ohlc latest commit/date and MNQ 1min/15min coverage end (must be **2026-04-15** if unchanged)

3. **Report only; do not tune**
   - Baselines remain frozen (axb0306 net -$31637.98, win 70%, PF 0.4917; Kaggle net -$626525.96, win 64.8%, PF 0.2271). All verified walk-forward windows negative.
   - If axb0306 coverage extends past 2026-04-15 with verifiable provenance/license, **STOP tuning** and record full provenance (repo, commit, paths, tz/roll/adjustment, contract months, gaps, hashes) before ingesting. If no extension, append to ledger and continue loop.

4. **Update handoff and exit cleanly**
   - Update `HANDOFF.md` Current session verification + Recent session ledger (append entry), keep prior entries intact
   - No code/strategy/data/raw/artifact changes unless a verified free-data extension appears (and even then only per rules)
   - Do **not** delete evidence. Do not reset/rewrite git history.

## Constraints (hard)
- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- No credentials, no purchases, no bypassing access controls/terms.
- No nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller code/permissions/automation policy without explicit authorization.
- Frozen baseline; no parameter fitting/optimization until/unless new free verifiable data appears.

## Goal
Maintain continuous, auditable re-verification of free MNQ/MNQ-related intraday sources every ~1-2 min until deadline or extension. Preserve all evidence, report accurately.