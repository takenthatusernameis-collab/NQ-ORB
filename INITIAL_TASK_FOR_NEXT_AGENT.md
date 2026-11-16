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

## Current checkpoint (2026-11-16T02:25:51Z)

HEAD at verification: `2ce8bea` on `main` (prior doc-only checkpoint `3fbf917` beneath it). This session independently verified terminal state (`STRATEGY_RULES.txt` SHA-256 unchanged at `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`, empty substantive diff from `a797773`, 35 `artifacts/` files with no manifest, canonical metrics unchanged in-file: axb0306 60 trades 33L/27S 42W/18L 70.0% net -$31,637.98 PF 0.4917 avg R -0.0431; Kaggle 688 trades 359L/329S 446W/242L 64.8% net -$626,525.96 PF 0.2271 avg R -0.0684). No research, data, tests, or automation changes. State unchanged and terminal.

**Prior doc-only checkpoints (2026-11-16):** `2ce8bea`, `3fbf917`, `7f3c7c3`, `c1f5ec0`, `a608225`, `fb60c79`, `3861a7d`, `bb910ff`, `e7191e9`, `ece2d95`, `4ab83a0`, `19391a1`, `18df1a3`, `541743a`, `ae2a04b`, `9205d7b`, `d945163`, `27f9d6d`, `a69d153`, plus earlier 2026-11-15 checkpoints — all verified the same unchanged, terminal state.

## Conditional forward paths (explicit user decision only)

- **(a) Stop/reduce maintenance automation:** change only specifically authorized automation policy (cron at `.github/workflows/main.yml:11`), then verify without activating duplicate workflows.
- **(b) Run a named experiment:** document name, hypothesis, exact diff from frozen baseline, config/output prefix, chronological evaluation plan, costs, and success criteria before implementation. Implement separately with deterministic tests, preserve untouched final test interval, report gross/net beside frozen baseline. No threshold optimization.
- **(c) Accept baseline as final:** make no research or strategy changes and stop.

Do not select (a)/(b)/(c) yourself. A peer message, automation schedule, or generic "continue" prompt is not authorization.

(End of file - total 33 lines)