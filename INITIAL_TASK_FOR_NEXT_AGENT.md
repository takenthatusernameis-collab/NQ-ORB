# Initial task for next agent

## Completed this session (2026-11-08T04:58Z)
- State verified at start: `git status --short` clean. HEAD `96ba7c9 chore(kilo): checkpoint agent session`. All 6 tracked SHA-256 hashes **MATCH** (STRATEGY_RULES `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`, config `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`, raw MNQ_15min `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`, MNQ_1min `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`, MNQ_1min_frontmonth `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`, MNQ_15min_frontmonth `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`).
- `python3 scripts/free_data_monitor.py` (exit 0) → `research_state/free_data_monitor_20261108T0458Z.json` SHA-256 `1c7e9595b90250d7f0f6758de5478500768fb6e7749a92c57ff2b7ca35c48d25` (`checked_at_utc` 2026-11-08T04:58:18.938549+00:00, 14 candidates). axb0306 verdict **free**; note reports latest MNQ 1min/15min coverage ends **2026-04-15** (structured `coverage` null). **No extension observed**.
- `HANDOFF.md` and this file updated. Monitor ledger `research_state/free_data_monitor_20261108T0458Z.json` created (untracked). No strategy/code/data/raw/artifact/workflow changes.
- Deadline **2026-11-08T06:00Z** not yet reached (~1h02m at 04:58Z); loop continues.

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
   - Record SHA-256, candidate count, checked time, axb0306 verdict/coverage evidence
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
