# Initial task for next agent

## Completed this session (2026-11-07T10:22:15Z)
- State re-verified: `git status --short` clean at start; `git log --oneline -1` at start = `8fbfeea chore(kilo): checkpoint agent session`; all 6 tracked SHA-256 hashes match (`STRATEGY_RULES.txt`, `config/orb_mnq_15m_showcase.yaml`, `raw/MNQ_15min.csv`, `raw/MNQ_1min.csv`, `raw/MNQ_1min_frontmonth.csv`, `raw/MNQ_15min_frontmonth.csv`).
- `python3 scripts/free_data_monitor.py` ran → `research_state/free_data_monitor_20261107T102153Z.json` SHA-256 `e5ffe5a2ead484d2d8203dc7ef2cf20b3730c15809f202fbc3a8b51e1b8b78c5` (checked `2026-11-07T10:22:15.316283+00:00`, 14 candidates, JSON valid). GitHub API returned `ok: true` this run (no rate-limit error), latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z`, message `Update 2026-04-15: 368 files updated`; `git ls-remote` fallback independently returned the same SHA. Independent raw-file tail check confirms MNQ 1min coverage ends `2026-04-15T23:29:00` and MNQ 15min ends `2026-04-15T23:15:00`; front-month files end `2025-11-12`. **No coverage extension observed.**
- `HANDOFF.md` updated: prepended `## Current session verification (2026-11-07T10:22:15Z, this session)` block including the API-OK + ls-remote-corroborated evidence and the independent raw-tail confirmation.

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
   - If the script errors, re-run `python3 scripts/free_data_monitor.py` once; the `git ls-remote` fallback should now succeed even under API rate limiting. Report any persistent failure.
3. **Update durable state**
   - Prepend a `## Current session verification (...)` block to `HANDOFF.md`
   - Refresh `INITIAL_TASK_FOR_NEXT_AGENT.md` with this session's evidence
4. **Stop conditions**
   - If axb0306 (or any free candidate) shows new MNQ 1min/15min coverage beyond 2026-04-15 → stop loop and report extension; **do not ingest without provenance audit**.
   - If deadline 2026-11-08T06:00Z reached → stop and report final status.
   - Otherwise continue. No parameter tuning, no strategy changes, no data/raw ingestion.

## Durable state (unchanged)
- Baselines unchanged: axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Walk-forward negative (axb0306 3 windows, Kaggle 8 windows). Frozen baseline `STRATEGY_RULES.txt` v1.0 preserved.