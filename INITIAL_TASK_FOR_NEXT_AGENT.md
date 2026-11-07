# Initial task for next agent

## Completed this session (2026-11-07T07:42:42Z)
- State re-verified: all 6 tracked SHA-256 hashes match; `git log --oneline -1` at start = `b59e0f8 chore(kilo): checkpoint agent session`; `git status --short` clean at start.
- `python3 scripts/free_data_monitor.py` ran → `research_state/free_data_monitor_20261107T074242Z.json` (SHA-256 `b961964727c051ea4e2ec97a81d2a73a76e58eec27c7371e19443c6e9a107918`, checked `2026-11-07T07:42:42Z`, 14 candidates, JSON valid). Recorded in `HANDOFF.md`.
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
   - `git log --oneline -1`
2. **Run monitor**
   - `python3 scripts/free_data_monitor.py` (redirect to `research_state/free_data_monitor_<timestamp>Z.json`)
   - Record SHA-256, checked_at, candidate count, axb0306 commit/date, MNQ coverage end, verdict
3. **Update durable state**
   - Prepend a `## Current session verification (...)` block to `HANDOFF.md`
   - Append a ledger line under `## Recent session ledger`
   - Refresh `INITIAL_TASK_FOR_NEXT_AGENT.md` with this session's evidence
4. **Stop conditions**
   - If axb0306 (or any free candidate) shows new MNQ 1min/15min coverage beyond 2026-04-15 → stop loop and report extension; do not ingest without provenance audit.
   - If deadline 2026-11-08T06:00Z reached → stop and report final status.
   - Otherwise continue. No parameter tuning, no strategy changes, no data ingestion.
