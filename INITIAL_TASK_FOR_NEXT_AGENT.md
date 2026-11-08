# Initial task for next agent

## Status — prior task complete (verified 2026-11-08T23:31Z)

The prior agent task (re-verify durable handoff state) is complete. This session re-verified state and found no pending work. **Do not** resume the 06:00 maintenance loop unless explicitly directed by the user or controller.

- Verified `git status --short --branch` clean (`## main...origin/main`), HEAD `fd7f613 docs(handoff): re-verify state 2026-11-08T23:29Z (71 passed, no pending work)` (main, tracking `origin/main`). No changes vs HEAD; tree clean.
- All 7 tracked SHA-256 hashes **MATCH** (re-verified via `sha256sum`): `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`; `research_state/free_data_monitor_20261108T060017Z.json` `3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f`.
- Latest free MNQ 1min/15min coverage ends **2026-04-15** (monitor `research_state/free_data_monitor_20261108T060017Z.json`, checked 2026-11-08T06:00:17Z; axb0306/cme-futures-ohlc sha `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264`, MNQ.M26, no extension observed).
- Baselines unchanged: axb0306 net **-$31,637.98** (win 70%, PF 0.4917); Kaggle net **-$626,525.96** (win 64.8%, PF 0.2271). Walk-forward negative.
- Full suite `python3 -m pytest tests/ -q` → **71 passed in 1.02s** (2026-11-08T23:31Z).
- No code/strategy/data/raw/artifact/workflow changes. No pending work.

## Read first

- `HANDOFF.md` (durable state + verification ledger)
- `STRATEGY_RULES.txt` (frozen baseline v1.0; no silent changes)
- `PROMPT.md` (research workflow)
- `AGENTS.md` (hard boundaries)

## Next concrete task (await explicit user/controller direction)

Act only if explicitly requested. Bounded options consistent with repository boundaries:

1. **Evidence packaging/reporting**: produce a reproducible summary of the frozen baseline, data provenance/limitations (axb0306 single-contract MNQ.M26 2026-01-20..2026-04-15; Kaggle front-month source per prior artifacts; no extension past 2026-04-15), cost assumptions, gross/net metrics, and walk-forward results — citing existing artifacts/hashes only; no new data.
2. **Test/verification (routine)**: re-run `python3 -m pytest tests/ -q` and record outcomes (71 passed baseline). Do not claim empirical improvement.
3. **Data-source re-audit (manual trigger only)**: if explicitly asked, re-run `python3 scripts/free_data_monitor.py` once and report; **do not ingest** any new source without provenance, contract/roll, adjustment, timestamp/timezone/DST, gap, and hash audit per `STRATEGY_RULES.txt` §6 and `AGENTS.md`.
4. **New versioned experiment (only with explicit authorization + data)**: any strategy/parameter change must be separately named/versioned with an explicit diff from the frozen baseline; freeze untouched baseline results first. Not authorized by default.

## Hard reminders

- No broker/live trading, no credentials, no paid/proprietary data, no workflow/controller edits, no nested/recursive Kilo loops.
- Never fabricate bars/fills/costs/timestamps. 15:55 ET exact exit needs 1-min evidence; 15-min alone is insufficient for exact exit.
- Distinguish implementation tests from empirical evidence. A successful process exit is not proof of correctness.

## Initial task message for the next agent

> Prior task (re-verify durable handoff state) is complete and verified (2026-11-08T23:31Z): the 06:00Z free-data maintenance loop remains stopped, the working tree is clean (`## main...origin/main`, HEAD `fd7f613 docs(handoff): re-verify state 2026-11-08T23:29Z (71 passed, no pending work)`), all 7 tracked SHA-256 hashes match (STRATEGY_RULES, showcase config, 4 raw CSVs, monitor ledger), latest free MNQ coverage ends 2026-04-15 (monitor `20261108T060017Z`, checked 2026-11-08T06:00:17Z; axb0306/cme-futures-ohlc sha `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264`, MNQ.M26, no extension observed), baselines unchanged (axb0306 net -$31,637.98 win 70% PF 0.4917 / Kaggle net -$626,525.96 win 64.8% PF 0.2271, walk-forward negative), and the full suite was re-run: **71 passed in 1.02s** (2026-11-08T23:31Z). No pending work remains. `HANDOFF.md` and this file updated.
>
> **Next action (bounded, requires explicit direction):** choose one — (1) evidence packaging/report from existing artifacts/hashes only; (2) run tests and report outcomes (71 passed baseline); (3) one-time manual `python3 scripts/free_data_monitor.py` re-audit only if asked (no ingestion without full provenance audit per `STRATEGY_RULES.txt` §6 and `AGENTS.md`); (4) new versioned experiment only with explicit authorization and an explicit diff from frozen `STRATEGY_RULES.txt` v1.0. Preserve the frozen baseline and all hard boundaries (`AGENTS.md`). Update `HANDOFF.md` and this file after any substantive work.
