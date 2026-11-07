# Initial task for next agent

## Completed this session (2026-11-07T10:20:12Z)
- State re-verified: `git status --short` clean at start; `git log --oneline -1` at start = `fc1f84a fix(free_data_monitor): guard GitHub API dict-error + git ls-remote fallback; record 2026-11-07T10:18Z monitor evidence`; all 6 tracked SHA-256 hashes match (`STRATEGY_RULES.txt`, `config/orb_mnq_15m_showcase.yaml`, `raw/MNQ_15min.csv`, `raw/MNQ_1min.csv`, `raw/MNQ_1min_frontmonth.csv`, `raw/MNQ_15min_frontmonth.csv`).
- `python3 scripts/free_data_monitor.py` ran → `research_state/free_data_monitor_20261107T102012Z.json` SHA-256 `cb95afec99bf250ee74c002584f7266c55606efd5f5167129ed5d350b6224772` (checked `2026-11-07T10:20:12.949424+00:00`, 14 candidates, JSON valid). GitHub API again rate-limited (`ok: false`, `API rate limit exceeded for 20.120.220.144`); `git ls-remote` fallback returned `ok: true`, SHA `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` — **identical to prior sessions**, so no new commits since `2026-04-15T23:34:55Z`. Independent raw-file tail check confirms MNQ 1min coverage ends `2026-04-15T23:29:00` and MNQ 15min ends `2026-04-15T23:15:00`; front-month files end `2025-11-12`. **No coverage extension observed.**
- No strategy/data/raw/artifact changes. `pytest` unavailable in this env (prior verified baseline: 71 passed, 2026-11-06T21:11Z).
- `HANDOFF.md` updated: prepended `## Current session verification (2026-11-07T10:20:12Z, this session)` block including the rate-limited-API + ls-remote-fallback evidence and the independent raw-tail confirmation.

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