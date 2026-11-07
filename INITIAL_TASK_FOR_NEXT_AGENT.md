# Initial task for next agent

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
   - Commit with a clear message if you create new evidence files? Follow repo norms; `research_state/` files are evidence (check .gitignore) — do **not** delete evidence. Do not reset/rewrite git history.

## Constraints (hard)
- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- No credentials, no purchases, no bypassing access controls/terms.
- No nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller code/permissions/automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, reset/rewrite git history.
- Frozen baseline; no parameter fitting/optimization until/unless new free verifiable data appears.

## Goal
Maintain continuous, auditable re-verification of free MNQ/MNQ-related intraday sources every ~1-2 min until deadline or extension. Preserve all evidence, report accurately.
