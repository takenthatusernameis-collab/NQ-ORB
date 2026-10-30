# Initial task for the next Kilo worker — NQ ORB

Read `AGENTS.md`, `STRATEGY_RULES.txt`, `PROMPT.md`, and `HANDOFF.md` before making changes.

Your first priority is a source-backed, free-data feasibility audit for MNQ/NQ futures. Establish whether freely accessible historical data can support both 15-minute ORB signals and 1-minute-or-better execution through the 15:55 ET forced flatten. Verify the data source, contract months, timestamps/timezone, volume, coverage, missing bars, and roll/adjustment method. Do not assume that a chart screenshot, synthetic data, back-adjusted series, or 15-minute bars can prove exact 15:55 execution.

If a sufficient dataset exists, implement the exact frozen MNQ showcase in `STRATEGY_RULES.txt`, add deterministic tests, realistic costs, chronological out-of-sample validation, and a reproducible trade ledger. If no adequate free source exists, do not fabricate or purchase data; report the verified blocker and the next legitimate source to test.

No parameter optimization, no strategy-rule changes, no broker integration, and no live/paper orders. Update `HANDOFF.md` and this file with evidence, results, blockers, and the next task.
