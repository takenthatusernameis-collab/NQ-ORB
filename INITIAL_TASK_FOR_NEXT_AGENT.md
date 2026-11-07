# Initial task for next agent

## Completed this session (2026-11-07T21:01Z)
- State verified at start: `git status --short` **clean**. HEAD `a8df5b1 chore(kilo): checkpoint agent session`. All 6 tracked SHA-256 hashes match expected values.
- `python3 scripts/free_data_monitor.py` ran (exit 0) → `research_state/free_data_monitor_20261107T210131Z.json` SHA-256 `90291f0310d6a0d4c52e8ca21954268d1856849f36b763275508475e8f4c3f65` (checked_at_utc `2026-11-07T21:01:35.329775+00:00`; 14 candidates, JSON valid). axb0306 (`axb0306/cme-futures-ohlc`) verdict `free`; latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z`. **No coverage extension observed.**
- `HANDOFF.md` updated to current-session verification. This file refreshed. No strategy/code/data/raw/artifact changes.
- Deadline **2026-11-08T06:00Z** not yet reached; loop continues.

## Read first (do not skip)
- `HANDOFF.md` (current state, durable facts, ledger note; deadline 2026-11-08T06:00Z)
- `STRATEGY_RULES.txt` (frozen baseline v1.0; no silent changes)
- `PROMPT.md` (research workflow)
- `AGENTS.md` (hard boundaries)

## Immediate task (bounded maintenance loop)
Repeat until controller deadline **2026-11-08T06:00Z** or a verified free-data extension appears:

1. **Verify state** (start of session)
   - `git status --short` (expect clean or only expected untracked `research_state/free_data_monitor_*.json` ledgers)
   - Verify tracked SHA-256 hashes for: `STRATEGY_RULES.txt`, `config/orb_mnq_15m_showcase.yaml`, `raw/MNQ_15min.csv`, `raw/MNQ_1min.csv`, `raw/MNQ_1min_frontmonth.csv`, `raw/MNQ_15min_frontmonth.csv`
   - `git --no-pager log --oneline -1`
2. **Run monitor**
   - `python3 scripts/free_data_monitor.py` → save stdout to `research_state/free_data_monitor_<UTC>Z.json`
   - Record SHA-256, candidate count, checked time, axb0306 verdict/coverage evidence/fallback SHA
   - If the script errors, re-run once; report any persistent failure.
3. **Update durable state**
   - Update/replace `## Current session verification (...)` in `HANDOFF.md` with this session's evidence (keep durable state + ledger note; full history remains in git)
   - Refresh `INITIAL_TASK_FOR_NEXT_AGENT.md` with this session's evidence
4. **Stop conditions**
   - If axb0306 (or any free candidate) shows new MNQ 1min/15min coverage beyond **2026-04-15** → stop loop and report extension; **do not ingest without provenance/contract/roll/timestamp audit**.
   - If deadline **2026-11-08T06:00Z** reached → stop and report final status.
   - Otherwise continue. No parameter tuning, no strategy changes, no data/raw ingestion, no workflow/controller edits.

## Durable state (unchanged)
- Frozen baseline: `STRATEGY_RULES.txt` v1.0 preserved (hash `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`).
- Baselines unchanged: axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Walk-forward negative (axb0306 3 windows, Kaggle 8 windows).
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest observed free 1min/15min coverage through **2026-04-15**.
- `pytest` unavailable in this env (prior verified baseline: 71 passed, 2026-11-06T21:11Z).