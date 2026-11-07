# Initial task for next agent

## Completed this session (2026-11-07T14:34:28Z)
- State re-verified at start: `git status --short` **clean**; `git log --oneline -1` = `d6553ab chore(kilo): checkpoint agent session`; all 6 tracked SHA-256 hashes match (`STRATEGY_RULES.txt`, `config/orb_mnq_15m_showcase.yaml`, `raw/MNQ_15min.csv`, `raw/MNQ_1min.csv`, `raw/MNQ_1min_frontmonth.csv`, `raw/MNQ_15min_frontmonth.csv`).
- `python3 scripts/free_data_monitor.py` ran (exit 0, no stderr) → `research_state/free_data_monitor_20261107T143428Z.json` SHA-256 `e56b6ea333f27655a52df2a99a6b21b8cff9e2482fd0581a833399d7a74d566a` (checked `2026-11-07T14:34:50.560719+00:00`, 14 candidates, JSON valid). Monitor JSON has `checked_at_utc`; axb0306 verdict `free`/`ok: true`, SHA `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z` ("Update 2026-04-15: 368 files updated"); `axb0306_head_sha_fallback` `ok: true` via `git_ls_remote`, same SHA. **No coverage extension observed.**
- `HANDOFF.md` updated (prepended `## Current session verification (2026-11-07T14:34:28Z, this session)`). No strategy/code/data/raw/artifact changes.

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
   - Record SHA-256, candidate count, axb0306 verdict/coverage evidence as present in JSON (include `checked_at_utc` if present)
   - If the script errors, re-run once; `git ls-remote` fallback should succeed under API rate limiting. Report any persistent failure.
3. **Update durable state**
   - Prepend a `## Current session verification (...)` block to `HANDOFF.md`
   - Refresh `INITIAL_TASK_FOR_NEXT_AGENT.md` with this session's evidence
4. **Stop conditions**
   - If axb0306 (or any free candidate) shows new MNQ 1min/15min coverage beyond 2026-04-15 → stop loop and report extension; **do not ingest without provenance audit**.
   - If deadline 2026-11-08T06:00Z reached → stop and report final status.
   - Otherwise continue. No parameter tuning, no strategy changes, no data/raw ingestion.

## Durable state (unchanged)
- Baselines unchanged: axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Walk-forward negative (axb0306 3 windows, Kaggle 8 windows). Frozen baseline `STRATEGY_RULES.txt` v1.0 preserved.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest observed free 1min/15min coverage through **2026-04-15**.