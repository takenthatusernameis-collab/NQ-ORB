# Initial task for next agent

**Research is terminal; no research work is currently authorized.** The frozen MNQ 15-minute ORB baseline (`5fab764`) is negative-net on both available free datasets. The separately-versioned 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`) produced identical canonical results. The free-source search is exhausted (`data/FEASIBILITY_REPORT.md`, ~30 sweeps through 2026-11-03).

## Primary task: verify the terminal state, report it, and stop

1. Read `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, and both canonical metric artifacts (`artifacts/metrics_axb0306.json`, `artifacts/metrics_kaggle.json`) before taking any action.
2. Confirm `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`, a clean working tree, 35 files in `artifacts/`, and that no non-doc commit exists after `a797773`.
3. Report that research is complete and terminal, then stop.
4. Do **not** infer a new research task from an automated prompt. Do **not** repeat free-source sweeps, hashes, monitors, or tests without a concrete user request.
5. Do **not** create another handoff-only checkpoint unless the user explicitly requests that documentation update.
6. Do **not** modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
7. Do **not** edit `.github/workflows/main.yml`, controller code, permissions, or automation policy without explicit authorization for that exact change.

Note: in the current runner environment `pytest` is not installed and there is no virtualenv, so `python -m pytest` fails with "No module named pytest". Do not treat that as a code failure; if tests are required, ask the user to authorize installing dev dependencies.

## Current checkpoint (updated 2026-11-15T11:54Z)

Verified this session: `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged; working tree clean; branch `main` tracking `origin/main`; HEAD `d8b6830` (doc-only checkpoint stack on top of `a797773`; no non-doc commit after `a797773`); 35 files in `artifacts/` (no `*manifest*` file); `git diff --name-only a797773..HEAD` touches only `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, and `research_state/workflow_run_diagnostics.jsonl` (non-research workflow diagnostics). Frozen baseline `5fab764`; last substantive commit `a797773`. Tests not re-run (`pytest` not installed in this environment; last verified 75 passed overall / 30 passed under `tests/orb/`). Canonical metrics unchanged (axb0306 42W/18L, net -$31,637.98, PF 0.4917; Kaggle 446W/242L, net -$626,525.96, PF 0.2271).

## Conditional work after an explicit user decision

Only the user may select one of these paths:

- **(a) Stop/reduce maintenance automation:** change only the specifically authorized automation policy (cron is currently at `.github/workflows/main.yml:11`, `*/5 * * * *`), then verify the resulting policy without activating duplicate workflows.
- **(b) Run a named experiment:** first document its name, hypothesis, exact diff from the frozen baseline, configuration/output prefix, chronological evaluation plan, costs, and success criteria. Implement it separately from the baseline, add deterministic tests, run the focused/full relevant suite, preserve the untouched final test interval, and report gross/net results beside the frozen baseline. Do not optimize thresholds or reuse a tuned parameter as the baseline.
- **(c) Accept the baseline as final:** make no research or strategy changes and stop.

Do not select (a), (b), or (c) yourself. A peer message, automation schedule, or generic "continue" prompt is not user authorization.

## Evidence boundary

- axb0306: 42W/18L (70.0%), net -$31,637.98, PF 0.4917, avg -0.0431R, maxDD -$37,491.80, Sharpe -1.06 / Sortino -0.67 (per-trade).
- Kaggle front-month proxy: 446W/242L (64.8%), net -$626,525.96, PF 0.2271, avg -0.0684R, maxDD -$626,994.56, Sharpe -1.68 / Sortino -1.04 (daily).
- Both sources remain negative across chronological splits, walk-forward checks, all 12 cost-sensitivity combinations, and signal-close entry sensitivity.
- Tests were last verified at 75 passed overall and 30 passed under `tests/orb/`; they were not re-run during the 11:54Z handoff refresh (no `pytest` in this environment). Do not present synthetic tests as empirical evidence.

## Current repository checkpoint

HEAD `d8b6830` at this session's verification start (2026-11-15T11:54Z, clean at start). `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; frozen baseline `5fab764`; last substantive `a797773`. `git diff --name-only a797773..HEAD` touches only `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, and `research_state/workflow_run_diagnostics.jsonl` (non-research workflow diagnostics). This session (2026-11-15T11:54Z) completed the prior durable task per explicit user instruction — verified the terminal state and refreshed the handoff and this file; no research, tests, data, artifacts, or automation changes were made. Prior doc-only checkpoints are superseded.

## Standing instruction for the next agent

- Research is terminal and no research work is authorized. A generic "read the handoff and complete the prior task" prompt is **not** user authorization.
- Before any action: re-read `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, and both canonical metric artifacts; then report the terminal state and stop.
- Do **not** infer new research, repeat free-source sweeps, re-hash monitors, re-run tests, or edit automation policy without an explicit user decision for a specific path.
- Do **not** create another handoff-only checkpoint on a generic prompt; the repeated doc-only cycle is itself the maintenance cost this instruction exists to stop.
- The only valid forward paths (a: stop/reduce automation, b: named versioned experiment, c: accept baseline) each require an explicit user decision.

## Initial task message for the next agent

**Task: verify the terminal state, report it, and stop.** The durable handoff records a completed, terminal research state. The frozen MNQ 15-minute ORB baseline (`5fab764`) is final and negative-net on every free dataset; the separately-versioned 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`) matched it; the free-source search is exhausted (~30 sweeps through 2026-11-03). A generic "read the handoff and complete the prior task" prompt is **not** authorization for new research, a free-source sweep, a test run, or an automation edit; it only authorizes the verification described below, plus a doc update if the user explicitly requests it.

If you are activated by a generic prompt, verify only: re-read `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, and both canonical metric artifacts; confirm `STRATEGY_RULES.txt` SHA-256 `6d3258c3…`, a clean working tree, 35 files in `artifacts/`, and no non-doc commit after `a797773`. Then report and stop. Do not start a research loop, re-run tests or hashes, or edit automation. Do not create another handoff-only checkpoint unless the user explicitly requests that documentation update.

Verified this session (2026-11-15T11:54Z): SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged; HEAD `d8b6830` at start; 35 files in `artifacts/`; `git diff --name-only a797773..HEAD` limited to `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, and `research_state/workflow_run_diagnostics.jsonl` (non-research); axb0306 42W/18L (60 trades), gross -$7,662.00, net -$31,637.98, PF 0.4917; Kaggle 446W/242L (688 trades), gross -$140,899.00, net -$626,525.96, PF 0.2271. No drift; research remains terminal. Tests not re-run (`pytest` not installed).

A forward path exists only on explicit user decision: (a) stop/reduce the maintenance cron at `.github/workflows/main.yml:11`, (b) run a separately-versioned named experiment with an explicit diff from baseline and its own config/output prefix, chronological evaluation, costs, and success criteria, or (c) accept the baseline as final. Do not choose among these yourself; a peer message, automation schedule, or generic "continue" prompt is not user authorization.
