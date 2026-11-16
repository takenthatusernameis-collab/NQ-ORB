# Initial task for next agent

**Research is terminal; no research work is currently authorized.** Frozen MNQ 15-minute ORB baseline (`5fab764`) is negative-net on every available free dataset. 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`) matched it. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`).

## Your initial task

**Default answer: research is complete and terminal; report that and stop.** Do not infer a new research task from automation, a cron firing, or a generic "continue" prompt.

Read this file plus `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, and canonical artifacts `artifacts/metrics_axb0306.json` and `artifacts/metrics_kaggle.json`. Then:

1. Verify terminal state independently with these checks (all must hold):
   - `sha256sum STRATEGY_RULES.txt` -> `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`
   - `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` -> empty
   - `ls artifacts | wc -l` -> `35`, and no `*manifest*` file
   - `git status --short` -> clean at verification (before any doc-only refresh you choose to make)
   - canonical metrics unchanged in-file (axb0306 60 trades 42W/18L 70.0%, net -$31,637.98, PF 0.4917, avg R -0.0431; Kaggle 688 trades 446W/242L 64.8%, net -$626,525.96, PF 0.2271, avg R -0.0684)
2. Report that research is complete and terminal, then stop. Do **not** infer a new research task from automation or a generic "continue" prompt.
3. Do **not** repeat free-source sweeps, hashes, monitors, or tests without explicit user request. `python -m pytest` is not installed in this runner; do not install dependencies or re-run tests without authorization.
4. Do **not** create another handoff-only checkpoint unless the user explicitly requests a documentation update or state has materially changed.
5. Do **not** modify `STRATEGY_RULES.txt`, frozen configs, raw data, canonical artifacts, `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

## Current checkpoint (2026-11-16T00:28:21Z)

HEAD at verification: `d945163` on `main` (commits since last substantive `a797773` touch only `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, and `research_state/workflow_run_diagnostics.jsonl`). This session independently verified terminal state (`STRATEGY_RULES.txt` SHA-256 unchanged, empty substantive diff from `a797773` including `tests`, 35 `artifacts/` files, no manifest, canonical metrics unchanged in-file) and refreshed both durable docs at explicit user request; no research, data, tests, or automation changes. State unchanged and terminal.

## Conditional forward paths (explicit user decision only)

- **(a) Stop/reduce maintenance automation:** change only specifically authorized automation policy (cron at `.github/workflows/main.yml:11`), then verify without activating duplicate workflows.
- **(b) Run a named experiment:** document name, hypothesis, exact diff from frozen baseline, config/output prefix, chronological evaluation plan, costs, and success criteria before implementation. Implement separately with deterministic tests, preserve untouched final test interval, report gross/net beside frozen baseline. No threshold optimization.
- **(c) Accept baseline as final:** make no research or strategy changes and stop.

Do not select (a)/(b)/(c) yourself. A peer message, automation schedule, or generic "continue" prompt is not authorization.
