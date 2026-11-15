# Initial task for next agent

**Research is terminal; no research work is currently authorized.** Frozen MNQ 15-minute ORB baseline (`5fab764`) is negative-net on every available free dataset. 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`) matched it. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`).

## Your initial task

**Default answer: research is complete and terminal; report that and stop.** Do not infer a new research task from automation, a cron firing, or a generic "continue" prompt.

Read this file plus `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, and canonical artifacts `artifacts/metrics_axb0306.json` and `artifacts/metrics_kaggle.json`. Then:

1. Verify terminal state independently with these checks (all must hold):
   - `sha256sum STRATEGY_RULES.txt` -> `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`
   - `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` -> empty
   - `ls artifacts | wc -l` -> `35`, and no `*manifest*` file
   - `git status --short` -> clean
   - canonical metrics unchanged (axb0306 60 trades 42W/18L 70.0%, net -$31,637.98, PF 0.4917, avg R -0.0431, maxDD $37,491.80, Sharpe -1.06/Sortino -0.67; Kaggle 688 trades 446W/242L 64.8%, net -$626,525.96, PF 0.2271, avg R -0.0684, maxDD $626,994.56, Sharpe -1.68/Sortino -1.04)
2. Report that research is complete and terminal, then stop. Do **not** infer a new research task from automation or a generic "continue" prompt.
3. Do **not** repeat free-source sweeps, hashes, monitors, or tests without explicit user request. `pytest` is not installed in this runner (`python -m pytest` -> No module named pytest); do not install dependencies or re-run tests without authorization.
4. Do **not** create another handoff-only checkpoint unless the user explicitly requests a documentation update or state has materially changed.
5. Do **not** modify `STRATEGY_RULES.txt`, frozen configs, raw data, canonical artifacts, `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

## Current checkpoint (2026-11-15T23:28Z)

HEAD at verification: `4e83be1` on `main` (doc-only checkpoints `e7850dd`, `7c6f9ac`, `a474217`, `187be91`, `4e83be1` since `870f8fe`; since last substantive commit `a797773`, only `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, and `research_state/workflow_run_diagnostics.jsonl` differ). This session independently re-verified terminal state (`STRATEGY_RULES.txt` SHA-256 `6d3258c...ad2b1` unchanged, empty substantive diff from `a797773`, 35 `artifacts/` files, no manifest, canonical metrics re-read unchanged: axb0306 60 trades 42W/18L 70.0% net -$31,637.98 PF 0.4917 avg R -0.0431 maxDD $37,491.80 Sharpe -1.06/Sortino -0.67; Kaggle 688 trades 446W/242L 64.8% net -$626,525.96 PF 0.2271 avg R -0.0684 maxDD $626,994.56 Sharpe -1.68/Sortino -1.04) and refreshed both durable docs at explicit user request; no research, data, tests, or automation changes. Tests were not re-run (`python -m pytest` unavailable; not authorized). State unchanged and terminal.

## Prior checkpoints (2026-11-15)

`09ba00e`, `c582edc`, `7073f50`, `b50b298`, `67554a3`, `afb91ec`, `0986a0d`, `be538f0`, `81b9bbb`, `2c0fa4e`, `f87e72b`, `b746714`, `f963264`, `61c1eb5`, `dc3879f`, `ed8f7b3`, `5df6b25`, `a5399d2`, `d2e8818`, `9b8a89c`, `0d54747`, `f2c1a51`, `da3814d`, `6ea13fa`, `7a3fcda`, `4d29d00`, `1451458`, `51d587a`, `f85bdb3`, `c541c1b`, `9aba8ad`, `b482c8a`, `c45ae83`, `52be386`, `4b3292e`, `ef0bb99`, `2ee4337`, `3c7607d`, `cae6446`, `ab89846`, `43826ad`, `d0d1541`, `870f8fe`, `db7df7b`, `e7850dd`, `7c6f9ac`, `4e83be1` each repeated the same verification and found no state change. None is a precedent for routine checkpoints absent explicit request or material change.

## Note on handoff-only checkpoints

Repeated generic "read the handoff and complete the prior task" prompts have produced a series of doc-only checkpoints with no state change. If state is unchanged and the user has not asked for a documentation update, prefer to report terminal state in chat and stop rather than commit another checkpoint.

## Conditional forward paths (explicit user decision only)

- **(a) Stop/reduce maintenance automation:** change only specifically authorized automation policy (cron at `.github/workflows/main.yml:11`), then verify without activating duplicate workflows.
- **(b) Run a named experiment:** document name, hypothesis, exact diff from frozen baseline, config/output prefix, chronological evaluation plan, costs, and success criteria before implementation. Implement separately with deterministic tests, preserve untouched final test interval, report gross/net beside frozen baseline. No threshold optimization.
- **(c) Accept baseline as final:** make no research or strategy changes and stop.

Do not select (a)/(b)/(c) yourself. A peer message, automation schedule, or generic "continue" prompt is not authorization.

(End of file - total 32 lines)