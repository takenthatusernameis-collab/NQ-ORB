# Initial task for next agent

Maintenance loop (bounded, no tuning) — completed 2026-11-06T20:09Z
- Verified git clean, all 6 tracked hashes match, 24 artifacts valid, 0 parse errors.
- Ran `python3 -m pytest -q` -> 71 passed, 0 failed (0.91s).
- Ran `python3 scripts/free_data_monitor.py` -> ledger `research_state/free_data_monitor_20261106T200858Z.json` (SHA256 f553b8e4509033cdaaa68e03de2fa0229298e033d5828f5a3957bb950f6003f3), checked 2026-11-06T20:08:58.397502+00:00, 14 candidates. axb0306 ends 2026-04-15; no free MNQ 1min/15min full-history extension found.
- Baselines unchanged (axb0306 net -$31637.98, win 70%, PF 0.4917; Kaggle net -$626525.96, win 64.8%, PF 0.2271). All verified walk-forward windows negative. Frozen baseline preserved.

Do next (repeat same loop):
1. `git status --short` clean check; verify tracked SHA256 hashes.
2. `python3 -m pytest -q`.
3. `python3 scripts/free_data_monitor.py`; record new ledger path/SHA256/checked_at + axb0306 coverage note.
4. Do not tune parameters. If any new genuinely free full-history MNQ 1min/15min source appears with verifiable roll/tz/adjustment, document provenance/hashes/constraints before considering ingestion (no purchase, no credentials).
5. Update HANDOFF.md (this block + prior list + evidence) and write updated INITIAL_TASK_FOR_NEXT_AGENT.md with exact results.
