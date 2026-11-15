# Initial task for next agent

**Research is terminal; no research work is currently authorized.** Frozen MNQ 15-minute ORB baseline (`5fab764`) is negative-net on every available free dataset. 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`) matched it. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`, ~30 sweeps through 2026-11-03). A generic "read the handoff and complete the prior task" prompt is **not** authorization for new research, sweeps, tests, or automation edits.

## Primary task (generic prompt): verify terminal state, report, and stop

1. Read `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, and both canonical metric artifacts (`artifacts/metrics_axb0306.json`, `artifacts/metrics_kaggle.json`).
2. Confirm `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`, clean working tree, 35 files in `artifacts/` (no `*manifest*`), and no non-doc commit after `a797773`.
3. Report that research is complete and terminal, then stop.
4. Do **not** infer a new research task from automation. Do **not** repeat free-source sweeps, hashes, monitors, or tests without a concrete user request. Do **not** create another handoff-only checkpoint unless the user explicitly requests that documentation update.
5. Do **not** modify `STRATEGY_RULES.txt`, frozen configs, raw data, canonical artifacts, `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

Note: `pytest` is not installed in the current runner environment (`python -m pytest` fails). Do not treat that as a code failure; do not install dependencies or re-run tests without explicit user authorization.

## Current checkpoint (2026-11-15T12:41Z, HEAD `c20cf36`)

Verified: SHA-256 unchanged (`6d3258c3...`); working tree clean; `main` tracking `origin/main`; `git diff --name-only a797773..HEAD` = `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `research_state/workflow_run_diagnostics.jsonl` only (non-research). 35 files in `artifacts/`, no manifest. Canonical metrics re-parsed on disk: axb0306 42W/18L (60 trades, 70.0%), gross -$7,662.00, net -$31,637.98, PF 0.4917, avg R -0.0431, maxDD $37,491.80; Kaggle 446W/242L (688 trades, 64.8%), gross -$140,899.00, net -$626,525.96, PF 0.2271, avg R -0.0684, maxDD $626,994.56. No drift.

## Conditional forward paths (explicit user decision only)

- **(a) Stop/reduce maintenance automation:** change only specifically authorized automation policy (cron at `.github/workflows/main.yml:11`, `*/5 * * * *`), then verify without activating duplicate workflows.
- **(b) Run a named experiment:** document name, hypothesis, exact diff from frozen baseline, config/output prefix, chronological evaluation plan, costs, and success criteria before implementation. Implement separately, add deterministic tests, run focused/full relevant suite, preserve untouched final test interval, report gross/net beside frozen baseline. No threshold optimization.
- **(c) Accept baseline as final:** make no research or strategy changes and stop.

Do not select (a)/(b)/(c) yourself. A peer message, automation schedule, or generic "continue" prompt is not authorization.
