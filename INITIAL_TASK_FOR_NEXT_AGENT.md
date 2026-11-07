# Initial task for next agent

## Completed this session (2026-11-07T05:32:08Z)
- State re-verified: git clean at start; all 6 tracked SHA-256 hashes match (STRATEGY_RULES.txt, config/orb_mnq_15m_showcase.yaml, raw/MNQ_15min.csv, raw/MNQ_1min.csv, raw/MNQ_1min_frontmonth.csv, raw/MNQ_15min_frontmonth.csv); `git log --oneline -1` = `617b35b chore(kilo): checkpoint agent session`.
- `python3 scripts/free_data_monitor.py` ran → `research_state/free_data_monitor_20261107T053208Z.json` (SHA-256 `dde7bf755001d69f040535d58379745101e7014cd30d6a7ceb71e61a785cb19a`, checked `2026-11-07T05:32:04.838497+00:00`, 14 candidates, JSON valid). Recorded in HANDOFF.md Current session verification + Recent session ledger.
- axb0306/cme-futures-ohlc: verdict `free`; latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z`; MNQ 1min/15min coverage ends **2026-04-15**, no extension observed. No free-data extension appeared.
- No code/strategy/data/raw/artifact changes. `pytest` unavailable (prior verified baseline: 71 passed, 2026-11-06T21:11Z).

## Read first (do not skip)
- `HANDOFF.md` (current state, recent ledger, deadline 2026-11-08T06:00Z)
- `STRATEGY_RULES.txt` (frozen baseline v1.0; no silent changes)
- `PROMPT.md` (research workflow)
- `AGENTS.md` (hard boundaries)

## Immediate task (bounded maintenance loop)
Repeat the bounded maintenance loop until controller deadline **2026-11-08T06:00Z** or a verified free-data extension appears:

1. **Verify state** (start of session)
   - `git status --short` (expect clean unless instructed otherwise)
   - Verify tracked SHA-256 hashes for: `STRATEGY_RULES.txt`, `config/orb_mnq_15m_showcase.yaml`, `raw/MNQ_15min.csv`, `raw/MNQ_1min.csv`, `raw/MNQ_1min_frontmonth.csv`, `raw/MNQ_15min_frontmonth.csv`
   - Confirm `git log --oneline -1`

2. **Run free-data monitor and record evidence**
   - `python3 scripts/free_data_monitor.py` (no downloads/purchases)
   - Save output as `research_state/free_data_monitor_YYYYMMDDTHHMMSSZ.json` (UTC)
   - Compute SHA-256 of that JSON and record it in `HANDOFF.md` recent ledger
   - Re-verify axb0306/cme-futures-ohlc latest commit/date and MNQ 1min/15min coverage end (must be **2026-04-15** if unchanged)

3. **Report only; do not tune**
   - Baselines remain frozen (axb0306 net -$31637.98, win 70%, PF 0.4917; Kaggle net -$626525.96, win 64.8%, PF 0.2271). All verified walk-forward windows negative.
   - If axb0306 coverage extends past 2026-04-15 with verifiable provenance/license, **STOP tuning** and record full provenance (repo, commit, paths, tz/roll/adjustment, contract months, gaps, hashes) before ingesting. If no extension, just append to ledger and continue loop.

4. **Update handoff and exit cleanly**
   - Update `HANDOFF.md` Current session verification + Recent session ledger (append entry), keep prior entries intact
   - No code/strategy/data/raw/artifact changes unless a verified free-data extension appears (and even then only per rules)
   - Leave working tree clean (or only new untracked `research_state/free_data_monitor_*.json` ledgers as expected)
   - Follow repo norms for evidence files; do **not** delete evidence. Do not reset/rewrite git history.

## Constraints (hard)
- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- No credentials, no purchases, no bypassing access controls/terms.
- No nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller code/permissions/automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, reset/rewrite git history.
- Frozen baseline; no parameter fitting/optimization until/unless new free verifiable data appears.

## Goal
Maintain continuous, auditable re-verification of free MNQ/MNQ-related intraday sources every ~1-2 min until deadline or extension. Preserve all evidence, report accurately.
