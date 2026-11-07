# Initial task for next agent

## Completed this session (2026-11-07T09:29:58Z)
- State re-verified: `git status --short` clean at start; `git log --oneline -1` at start = `64adce2 chore(kilo): checkpoint agent session`; all 6 tracked SHA-256 hashes match (`STRATEGY_RULES.txt`, `config/orb_mnq_15m_showcase.yaml`, `raw/MNQ_15min.csv`, `raw/MNQ_1min.csv`, `raw/MNQ_1min_frontmonth.csv`, `raw/MNQ_15min_frontmonth.csv`).
- `python3 scripts/free_data_monitor.py` ran → `research_state/free_data_monitor_20261107T092958Z.json` SHA-256 `56d957100065f3c1406cdb9f4d38c1e4c51af85a38684fc992f02e109e14189d` (14 candidates, JSON valid; checked_at `2026-11-07T09:29:58.034580+00:00`). axb0306/cme-futures-ohlc: verdict `free`; latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z`; MNQ 1min/15min coverage ends **2026-04-15** (no extension observed).
- No code/strategy/data/raw/artifact changes. `pytest` unavailable in this env (prior verified baseline: 71 passed, 2026-11-06T21:11Z).
- `HANDOFF.md` updated: prepended `## Current session verification (2026-11-07T09:29:58Z, this session)` block.

## Read first (do not skip)
- `HANDOFF.md` (current state, recent ledger, deadline 2026-11-08T06:00Z)
- `STRATEGY_RULES.txt` (frozen baseline v1.0; no silent changes)
- `PROMPT.md` (research workflow)
- `AGENTS.md` (hard boundaries)

## Immediate task (bounded maintenance loop)
Repeat until controller deadline **2026-11-08T06:00Z** or a verified free-data extension appears:

1. **Verify state** (start of session)
   - `git status --short` (expect clean or only expected untracked `research_state/free_data_monitor_*.json` ledgers)
   - Verify tracked SHA-256 hashes for: `STRATEGY_RULES.txt`, `config/orb_mnq_15m_showcase.yaml`, `raw/MNQ_15min.csv`, `raw/MNQ_1min.csv`, `raw/MNQ_1min_frontmonth.csv`, `raw/MNQ_15min_frontmonth.csv`
   - `git log --oneline -1`
2. **Run monitor**
   - `python3 scripts/free_data_monitor.py` → `research_state/free_data_monitor_<UTC>Z.json`
   - Record SHA-256, candidate count, axb0306 verdict/coverage evidence as present in JSON
3. **Update durable state**
   - Prepend a `## Current session verification (...)` block to `HANDOFF.md`
   - Refresh `INITIAL_TASK_FOR_NEXT_AGENT.md` with this session's evidence
4. **Stop conditions**
   - If axb0306 (or any free candidate) shows new MNQ 1min/15min coverage beyond 2026-04-15 → stop loop and report extension; **do not ingest without provenance audit**.
   - If deadline 2026-11-08T06:00Z reached → stop and report final status.
   - Otherwise continue. No parameter tuning, no strategy changes, no data/raw ingestion.

## Durable state (unchanged)
- Baselines unchanged: axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Walk-forward negative (axb0306 3 windows, Kaggle 8 windows). Frozen baseline `STRATEGY_RULES.txt` v1.0 preserved.
