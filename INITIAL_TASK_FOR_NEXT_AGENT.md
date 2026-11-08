# Initial task for next agent

## Status — prior task complete (verified 2026-11-08T10:49Z)

The prior agent task is complete: the free-data maintenance monitoring loop stopped at the 2026-11-08T06:00Z deadline. This session confirmed no pending work. **Do not** resume the 06:00Z maintenance loop unless explicitly directed by the user or controller.

- Verified `git status --short` clean at HEAD `727e16bcb9c38449074b4e78488888628bada32e` (`chore(kilo): checkpoint agent session`, 2026-11-08T10:48:54Z). This session updates only `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`.
- All 7 tracked SHA-256 hashes **MATCH** (re-verified via `sha256sum`): STRATEGY_RULES `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`; monitor ledger `research_state/free_data_monitor_20261108T060017Z.json` `3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f`.
- Latest free MNQ 1min/15min coverage ends **2026-04-15** (axb0306/cme-futures-ohlc). No extension observed.
- Baselines unchanged: axb0306 net **-$31637.98** (win 70%, PF 0.4917); Kaggle net **-$626525.96** (win 64.8%, PF 0.2271). Walk-forward negative.
- `pytest` unavailable in this env (prior verified: 71 passed, 2026-11-06T21:11Z). Frozen baseline `STRATEGY_RULES.txt` v1.0 preserved.

## Read first

- `HANDOFF.md` (durable state + verification ledger)
- `STRATEGY_RULES.txt` (frozen baseline v1.0; no silent changes)
- `PROMPT.md` (research workflow)
- `AGENTS.md` (hard boundaries)

## Next concrete task (await explicit user/controller direction)

Act only if explicitly requested. Bounded options consistent with repository boundaries:

1. **Evidence packaging/reporting**: produce a reproducible summary of the frozen baseline, data provenance/limitations (axb0306 single-contract MNQ.M26 2026-01-20..2026-04-15; no extension past 2026-04-15), cost assumptions, gross/net metrics, and walk-forward results — citing existing artifacts/hashes only; no new data.
2. **Test/verification hardening (env permitting)**: if `pytest` becomes available, run focused/full suite and record outcomes; otherwise document the limitation. Do not claim empirical improvement.
3. **Data-source re-audit (manual trigger only)**: if explicitly asked, re-run `python3 scripts/free_data_monitor.py` once and report; **do not ingest** any new source without provenance, contract/roll, adjustment, timestamp/timezone/DST, gap, and hash audit per `STRATEGY_RULES.txt` §6 and `AGENTS.md`.
4. **New versioned experiment (only with explicit authorization + data)**: any strategy/parameter change must be separately named/versioned with an explicit diff from the frozen baseline; freeze untouched baseline results first. Not authorized by default.

## Hard reminders

- No broker/live trading, no credentials, no paid/proprietary data, no workflow/controller edits, no nested/recursive Kilo loops.
- Never fabricate bars/fills/costs/timestamps. 15:55 ET exact exit needs 1-min evidence; 15-min alone is insufficient for exact exit.
- Distinguish implementation tests from empirical evidence. A successful process exit is not proof of correctness.

## Initial task message for the next agent

Prior task (free-data maintenance monitoring loop; 2026-11-08T06:00Z deadline) is complete and verified (session 2026-11-08T10:49Z): the loop stopped at its deadline, the working tree was clean at `727e16b`, and all 7 tracked SHA-256 hashes match (STRATEGY_RULES, showcase config, 4 raw CSVs, monitor ledger). No further polling of the maintenance loop is authorized unless the user/controller explicitly directs it.

If you act, stay within the bounded options above and require explicit direction. Do not resume the stopped maintenance loop, do not modify the frozen baseline or strategy rules, and do not ingest new data without a full provenance audit.
