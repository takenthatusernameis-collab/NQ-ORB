# Initial task for next agent

## Completed this session (2026-11-08T05:58Z)
- State verified at start: `git status --short` clean. HEAD `bedcb97 chore(kilo): checkpoint agent session`. All 6 tracked SHA-256 hashes **MATCH** (STRATEGY_RULES `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`, config `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`, raw MNQ_15min `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`, raw MNQ_1min `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`, raw MNQ_1min_frontmonth `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`, raw MNQ_15min_frontmonth `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`).
- `python3 scripts/free_data_monitor.py` (exit 0) → `research_state/free_data_monitor_20261108T055819Z.json` SHA-256 `b63558fa2b0ad4e410d9ffb9543cb0c1a0f918112be91a7fc07ef8a44b4d99bf` (`checked_at_utc` 2026-11-08T05:58:26.276439+00:00, 14 candidates). axb0306/cme-futures-ohlc verdict **free**; note: "Latest MNQ 1min/15min coverage ends 2026-04-15. Re-verified each session; no extension observed." No coverage extension.
- `HANDOFF.md` and this file updated. Monitor ledger created (uncommitted). No strategy/code/data/raw/artifact/workflow changes.
- Deadline **2026-11-08T06:00Z** is imminent/reached at next cycle. If >= 2026-11-08T06:00Z, report final status and stop maintenance loop.

## Read first (do not skip)
- `HANDOFF.md` (current state, durable facts, ledger note; deadline 2026-11-08T06:00Z)
- `STRATEGY_RULES.txt` (frozen baseline v1.0; no silent changes)
- `PROMPT.md` (research workflow)
- `AGENTS.md` (hard boundaries)

## Immediate task (bounded maintenance loop)
If current UTC < **2026-11-08T06:00Z**, repeat until deadline or verified free-data extension:
1. **Verify state**: `git status --short`; verify 6 tracked SHA-256 hashes (`STRATEGY_RULES.txt`, `config/orb_mnq_15m_showcase.yaml`, `raw/MNQ_15min.csv`, `raw/MNQ_1min.csv`, `raw/MNQ_1min_frontmonth.csv`, `raw/MNQ_15min_frontmonth.csv`); `git --no-pager log --oneline -1`.
2. **Run monitor**: `python3 scripts/free_data_monitor.py` → `research_state/free_data_monitor_<UTC>Z.json`; record SHA-256, checked time, candidate count, axb0306 verdict/coverage. Re-run once on error.
3. **Update durable state**: update `## Current session verification (...)` in `HANDOFF.md`; refresh this file.
4. **Stop conditions**: if any free candidate shows MNQ 1min/15min coverage beyond **2026-04-15** → stop and report; **do not ingest without provenance/contract/roll/timestamp audit**. If >= **2026-11-08T06:00Z** → stop and report final status. Otherwise continue. No parameter tuning, no strategy changes, no data/raw ingestion, no workflow/controller edits.

If current UTC >= **2026-11-08T06:00Z**: do not continue the maintenance loop; report final status (no extension observed through last verified monitor; hashes stable; baselines unchanged) and await explicit user/controller direction.

## Durable state (unchanged)
- Frozen baseline: `STRATEGY_RULES.txt` v1.0 preserved (hash `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`).
- Baselines unchanged: axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Walk-forward negative (axb0306 3 windows, Kaggle 8 windows).
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest observed free 1min/15min coverage through **2026-04-15**.
- `pytest` unavailable in this env (prior verified baseline: 71 passed, 2026-11-06T21:11Z).
