# Initial task for next agent

## Completed this session (2026-11-07T18:14Z)
- State verified at start: `git status --short` **clean**; HEAD `f2e3621 chore(kilo): checkpoint agent session` (`git log --oneline -1`); all 6 tracked SHA-256 hashes match expected values (STRATEGY_RULES, config/orb_mnq_15m_showcase.yaml, raw/MNQ_15min.csv, raw/MNQ_1min.csv, raw/MNQ_1min_frontmonth.csv, raw/MNQ_15min_frontmonth.csv).
- `python3 scripts/free_data_monitor.py` ran (exit 0) → `research_state/free_data_monitor_20261107T1814Z.json` SHA-256 `f1fdddfb875fbd471ed3d7d76a2acd92537e45edfed801050f2479f10aaa0600` (checked `2026-11-07T18:14:06.028137+00:00`, 14 candidates, JSON valid). axb0306 verdict `free`, note: "Latest MNQ 1min/15min coverage ends 2026-04-15. Re-verified each session; no extension observed." **No coverage extension observed.**
- `HANDOFF.md` updated (prepended `## Current session verification (2026-11-07T18:14Z, this session)`); this file refreshed. No strategy/code/data/raw/artifact changes.

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
   - `python3 scripts/free_data_monitor.py` → save stdout to `research_state/free_data_monitor_<UTC>Z.json`
   - Record SHA-256, candidate count, checked time, axb0306 verdict/coverage evidence
   - If the script errors, re-run once; report any persistent failure.
3. **Update durable state**
   - Prepend a `## Current session verification (...)` block to `HANDOFF.md`
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
