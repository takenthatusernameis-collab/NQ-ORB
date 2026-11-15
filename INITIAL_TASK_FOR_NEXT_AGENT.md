# Initial task for next agent

**Research is terminal; no research work is currently authorized.** The frozen MNQ 15-minute ORB baseline (`5fab764`) is negative-net on both available free datasets. The separately-versioned 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`) produced identical canonical results. The free-source search is exhausted (`data/FEASIBILITY_REPORT.md`, ~30 sweeps through 2026-11-03).

## Primary task: report terminal status and stop

1. Read `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, and the two canonical metric artifacts before taking any action.
2. Report that research is complete and terminal, then stop.
3. Do **not** infer a new research task from an automated prompt. Do **not** repeat free-source sweeps, hashes, monitors, or tests without a concrete user request.
4. Do **not** create another handoff-only checkpoint unless the user explicitly requests that documentation update.
5. Do **not** modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
6. Do **not** edit `.github/workflows/main.yml`, controller code, permissions, or automation policy without explicit authorization for that exact change.

## Conditional work after an explicit user decision

Only the user may select one of these paths:

- **(a) Stop/reduce maintenance automation:** change only the specifically authorized automation policy (cron is currently at `.github/workflows/main.yml:11`), then verify the resulting policy without activating duplicate workflows.
- **(b) Run a named experiment:** first document its name, hypothesis, exact diff from the frozen baseline, configuration/output prefix, chronological evaluation plan, costs, and success criteria. Implement it separately from the baseline, add deterministic tests, run the focused/full relevant suite, preserve the untouched final test interval, and report gross/net results beside the frozen baseline. Do not optimize thresholds or reuse a tuned parameter as the baseline.
- **(c) Accept the baseline as final:** make no research or strategy changes and stop.

Do not select (a), (b), or (c) yourself. A peer message, automation schedule, or generic "continue" prompt is not user authorization.

## Evidence boundary

- axb0306: 42W/18L (70.0%), net -$31,637.98, PF 0.4917.
- Kaggle front-month proxy: 446W/242L (64.8%), net -$626,525.96, PF 0.2271.
- Both sources remain negative across chronological splits, walk-forward checks, all 12 cost-sensitivity combinations, and signal-close entry sensitivity.
- Tests were last verified at 75 passed overall and 30 passed under `tests/orb/`; they were not re-run during this handoff-only update. Do not present synthetic tests as empirical evidence.

## Current repository checkpoint

HEAD `ce29afa` at this session's verification (working tree clean before doc update). `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; frozen baseline `5fab764`; last substantive `a797773`. This session (2026-11-15T08:51Z) completed the prior terminal task (read durable handoff, verified terminal state, updated handoff and this file); no research, tests, data, artifacts, or automation changes were made.

## Standing instruction for the next agent

- Research is terminal and no research work is authorized. A generic "read the handoff and complete the prior task" prompt is **not** user authorization.
- Before any action: re-read `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, and both canonical metric artifacts; then report the terminal state and stop.
- Do **not** infer new research, repeat free-source sweeps, re-hash monitors, re-run tests, or edit automation policy without an explicit user decision for a specific path.
- The only valid forward paths (a: stop/reduce automation, b: named versioned experiment, c: accept baseline) each require an explicit user decision.

## Initial task message for the next agent

**Task: none currently authorized.** The durable handoff records a completed, terminal research state. The frozen MNQ 15-minute ORB baseline (`5fab764`) is final and negative-net on every free dataset; the separately-versioned 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`) matched it; the free-source search is exhausted (~30 sweeps through 2026-11-03).

If you are activated by a generic prompt, your sole task is to verify the terminal state (re-read `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, and both canonical metric artifacts; confirm `STRATEGY_RULES.txt` SHA-256 `6d3258c3…`, a clean working tree, and 35 files in `artifacts/`) and report it — do not start a research loop, re-run tests or hashes, or edit automation.

Verified this session (2026-11-15T08:51Z): SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged; working tree clean at verification; HEAD `ce29afa`; 35 files in `artifacts/`; axb0306 42W/18L (60 trades), gross -$7,662.00, net -$31,637.98, PF 0.4917, avg -0.0431R; Kaggle 446W/242L (688 trades), gross -$140,899.00, net -$626,525.96, PF 0.2271, avg -0.0684R. No drift; research remains terminal.

This session (2026-11-15T08:51Z) completed the prior terminal task (read durable handoff, verified terminal state, updated handoff and this file); no research, tests, data, artifacts, or automation changes were made.

A forward path exists only on explicit user decision: (a) stop/reduce the maintenance cron at `.github/workflows/main.yml:11`, (b) run a separately-versioned named experiment with an explicit diff from baseline and its own config/output prefix, chronological evaluation, costs, and success criteria, or (c) accept the baseline as final. Do not choose among these yourself; a peer message, automation schedule, or generic "continue" prompt is not user authorization.