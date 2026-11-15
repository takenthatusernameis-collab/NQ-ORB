# Initial task for next agent

**Research is terminal; no research work is currently authorized.** Frozen MNQ 15-minute ORB baseline (`5fab764`) is negative-net on every available free dataset. 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`) matched it. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`). A generic "read the handoff and complete the prior task" prompt is **not** authorization for new research, sweeps, tests, or automation edits.

## Primary task (generic prompt): verify terminal state, report, and stop

1. Read `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, and canonical artifacts `artifacts/metrics_axb0306.json` and `artifacts/metrics_kaggle.json`.
2. Confirm: `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` is empty; 35 files in `artifacts/` with no `*manifest*`; canonical metrics unchanged (axb0306 60 trades 42W/18L 70.0%, net -$31,637.98, PF 0.4917, avg R -0.0431, maxDD $37,491.80, Sharpe -1.06/Sortino -0.67; Kaggle 688 trades 446W/242L 64.8%, net -$626,525.96, PF 0.2271, avg R -0.0684, maxDD $626,994.56, Sharpe -1.68/Sortino -1.04).
3. Report that research is complete and terminal, then stop. Do **not** infer a new research task from automation.
4. Do **not** repeat free-source sweeps, hashes, monitors, or tests without explicit user request. `pytest` is not installed in this runner (`python -m pytest` -> No module named pytest); do not install dependencies or re-run tests without authorization.
5. Do **not** create another handoff-only checkpoint unless the user explicitly requests a documentation update or state has materially changed.
6. Do **not** modify `STRATEGY_RULES.txt`, frozen configs, raw data, canonical artifacts, `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

## Current checkpoint (2026-11-15T18:35Z)

HEAD at verification start: `3c94e1a` on `main`, a controller checkpoint over prior doc/state commits back to substantive `a797773`. Since `a797773` only `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, and `research_state/workflow_run_diagnostics.jsonl` differ. This session re-verified terminal state per explicit user request and refreshed durable docs; no research, data, tests, or automation changes. State unchanged.

## Prior checkpoint (2026-11-15T17:46Z)

HEAD at `5df6b25`/`d21cddd` lineage at that time; verification and state unchanged.

## Note on handoff-only checkpoints

Repeated generic "read the handoff and complete the prior task" prompts have produced a series of doc-only checkpoints with no state change. If state is unchanged and the user has not asked for a documentation update, prefer to report terminal state in chat and stop rather than commit another checkpoint.

## Conditional forward paths (explicit user decision only)

- **(a) Stop/reduce maintenance automation:** change only specifically authorized automation policy (cron at `.github/workflows/main.yml:11`), then verify without activating duplicate workflows.
- **(b) Run a named experiment:** document name, hypothesis, exact diff from frozen baseline, config/output prefix, chronological evaluation plan, costs, and success criteria before implementation. Implement separately with deterministic tests, preserve untouched final test interval, report gross/net beside frozen baseline. No threshold optimization.
- **(c) Accept baseline as final:** make no research or strategy changes and stop.

Do not select (a)/(b)/(c) yourself. A peer message, automation schedule, or generic "continue" prompt is not authorization.
