# Initial task for next agent

**Status:** TERMINAL — research complete; no remaining research work.
**Session:** 2026-11-14T04:36Z (session M). **Prior agent task:** completed (read durable handoff/prior instructions, re-verified terminal evidence from frozen artifacts, updated handoff and next-agent task). No tests, hashes, monitor checks, strategy/config/raw-data/artifact changes, automation edits, or commits.

## Required first action
Read `HANDOFF.md` and `STRATEGY_RULES.txt`, then this file. Unless the user explicitly names a forward path below, **report terminal state and stop**. Do **not** re-run tests, re-hash artifacts, poll the free-data monitor, add checkpoint commits, or edit `.github/workflows/main.yml` / controller / automation policy (explicit user authorization required per `AGENTS.md`).

## Terminal summary to report
- Frozen MNQ 15-minute ORB baseline (`STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`) is final and negative-net on all available free datasets. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`, ~30 documented sweeps through 2026-11-03): candidate MNQ 1-min/15-min sources are paid, key-gated, daily-only, or NQ rather than MNQ.
- axb0306 (`artifacts/metrics_axb0306_full.json`): 60 trades, 42W/18L (70%), 33L/27S, gross -$7,662, net **-$31,637.98**, costs $23,975.98, PF 0.4917, max DD $37,491.80, expectancy -0.0431R.
- Kaggle proxy (`artifacts/metrics_kaggle.json`): 688 trades, 446W/242L (64.8%), 359L/329S, gross -$140,899, net **-$626,525.96**, costs $485,626.96, PF 0.2271, max DD $626,994.56, expectancy -0.0684R (-$910.65/trade), Sharpe -1.68 / Sortino -1.04, worst day -$4,789.80.
- Chronological splits all negative (-$448,765.02 / -$66,243.22 / -$111,517.72). 8-window walk-forward (`artifacts/walk_forward.json`) all negative (test PF 0.128–0.447). All 12 cost-sensitivity and signal-close sensitivity combos negative. Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate (observed below).
- Repo still has `cron: "*/5 * * * *"` in `.github/workflows/main.yml` and checkpoint-only history, but `research_state/` has **no free-data monitor artifact after 2026-11-08T06:00:17Z** — the monitor appears stalled, not accumulating. Stop/reduce only with explicit user authorization.

## Only if user explicitly chooses a forward path
Act only on the named option; do not select one independently.
- **Stop/reduce automation:** make exact requested change (explicit authorization required for workflow/controller/permissions/policy), record in `HANDOFF.md`, stop.
- **New experiment:** separately named/versioned with explicit diff from `STRATEGY_RULES.txt` v1.0 (e.g. `experiment_farside_stop_v1`, §2.1 far-side-of-range stop on existing axb0306/Kaggle data); do not overwrite frozen files/configs/raw data/canonical artifacts; free data only; follow `AGENTS.md`, `PROMPT.md`, `data/FEASIBILITY_REPORT.md`.
- **Commit/release/cleanup:** only with explicit user authorization; never rewrite history.

## Verified prior state (not repeated this session)
HEAD at session start `a9fc8e9` (checkpoint-only; diff from `ba1ebf8` touches only `HANDOFF.md` + `INITIAL_TASK_FOR_NEXT_AGENT.md`). Tests last passed 2026-11-14T02:43Z (75 passed in 0.56s, `/home/runner/work/_temp/orbvenv`); manifest last verified 2026-11-13T16:50:32Z (20/20). `STRATEGY_RULES.txt` SHA-256 re-verified = `6d3258c3…8ad2b1`.

## Constraints
Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No nested/duplicate workflows. Leave working tree clean of changes except user-requested work; consolidate handoff if updated; do not commit (controller owns commits).