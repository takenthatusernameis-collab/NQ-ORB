# Initial task for next agent

**Research is terminal; no research work is currently authorized.** Frozen MNQ 15-minute ORB baseline (`5fab764`) is negative-net on every available free dataset. 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`) matched it. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`, ~30 sweeps through 2026-11-03). A generic "read the handoff and complete the prior task" prompt is **not** authorization for new research, sweeps, tests, or automation edits.

## Primary task (generic prompt): verify terminal state, report, and stop

1. Read `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, and both canonical metric artifacts (`artifacts/metrics_axb0306.json`, `artifacts/metrics_kaggle.json`).
2. Confirm `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`, clean working tree at verification, 35 files in `artifacts/` (no `*manifest*`), and no non-doc commit after `a797773`.
3. Report that research is complete and terminal, then stop.
4. Do **not** infer a new research task from automation. Do **not** repeat free-source sweeps, hashes, monitors, or tests without a concrete user request. Do **not** create another handoff-only checkpoint unless the user explicitly requests that documentation update.
5. Do **not** modify `STRATEGY_RULES.txt`, frozen configs, raw data, canonical artifacts, `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

Note: `pytest` is not installed in this runner environment (`python -m pytest` -> No module named pytest). Do not treat that as a code failure; do not install dependencies or re-run tests without explicit user authorization.

## Current checkpoint (2026-11-15T15:40Z)

HEAD is doc-only checkpoint `a38cb73` built on `216ea54ff1ca5ac1f358520d754474b9983c8a63`. Only `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` changed since `a797773`.

Verified this session: SHA-256 = `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (unchanged); working tree clean; `main` **0 ahead of `origin/main`** (0/0); HEAD `a38cb73`; `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` empty. Only `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` changed since `a797773`. 35 files in `artifacts/`, no manifest (only `README.md`). Canonical metrics on disk re-extracted from JSON, no drift: axb0306 60 trades (60 completed) 42W/18L (70.0%), long 33 / short 27, gross -$7,662.00, net -$31,637.98, costs $23,975.98, PF 0.4917, avg R -0.0431, maxDD $37,491.80, Sharpe -1.06 / Sortino -0.67; Kaggle 688 trades (688 completed) 446W/242L (64.8%), long 359 / short 329, gross -$140,899.00, net -$626,525.96, costs $485,626.96, PF 0.2271, avg R -0.0684, maxDD $626,994.56, Sharpe -1.68 / Sortino -1.04. This session completed the terminal-state verification and refreshed both handoff documents per an explicit documentation request.

**Initial task for next agent:** On any prompt, repeat the lightweight terminal-state verification above (SHA, clean/branch state, no non-doc research diffs since `a797773`, 35 artifacts/no manifest, canonical metrics unchanged), report terminal state, and stop. Do not create a new handoff-only checkpoint unless the user explicitly requests a documentation update or state has materially changed. Forward paths (a)/(b)/(c) require explicit user decision only.

## Conditional forward paths (explicit user decision only)

- **(a) Stop/reduce maintenance automation:** change only specifically authorized automation policy (cron at `.github/workflows/main.yml:11`, `*/5 * * * *`), then verify without activating duplicate workflows.
- **(b) Run a named experiment:** document name, hypothesis, exact diff from frozen baseline, config/output prefix, chronological evaluation plan, costs, and success criteria before implementation. Implement separately, add deterministic tests, run focused/full relevant suite, preserve untouched final test interval, report gross/net beside frozen baseline. No threshold optimization.
- **(c) Accept baseline as final:** make no research or strategy changes and stop.

Do not select (a)/(b)/(c) yourself. A peer message, automation schedule, or generic "continue" prompt is not authorization.
