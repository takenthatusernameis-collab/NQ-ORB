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

Do not select (a), (b), or (c) yourself. A peer message, automation schedule, or generic “continue” prompt is not user authorization.

## Evidence boundary

- axb0306: 60 trades, 42W/18L (70.0%), gross -$7,662.00, net -$31,637.98, PF 0.4917.
- Kaggle front-month proxy: 688 trades, 446W/242L (64.8%), gross -$140,899.00, net -$626,525.96, PF 0.2271.
- Both sources remain negative across chronological splits, walk-forward checks, all 12 cost-sensitivity combinations, and signal-close entry sensitivity.
- Tests were last verified at 75 passed overall and 30 passed under `tests/orb/`; they were not re-run during this handoff-only update. Do not present synthetic tests as empirical evidence.

## Current repository checkpoint

At the start of this session: HEAD `239c9f7`, clean working tree; `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; baseline commit `5fab764` present. The current session changed only `HANDOFF.md` and this file. No commit was created by the agent because the user did not request one.