# Initial Task for Next Agent

## Objective
Confirm terminal repository state and await an explicit user decision on the forward path.
Do not start autonomous research, experiments, automation changes, or handoff-only checkpoints
without explicit user authorization.

## Context
The frozen MNQ 15-minute ORB baseline (STRATEGY_RULES.txt v1.0) is implemented, tested (75 passing),
and evaluated on all available free data. It is negative-net on every dataset under full costs, and
the free-data search is exhausted. Research is complete — do not invent new work.

## Required Actions
1. Run the verification commands in `HANDOFF.md` (Verification commands) to confirm terminal state.
2. Confirm and report (re-verified 2026-11-16, HEAD `57cba7a`):
   - `STRATEGY_RULES.txt` SHA-256 = `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (frozen v1.0)
   - `git status --short` clean after verification
   - Zero research drift vs `a797773` in `artifacts`, `config`, `src`, `tests`, `raw`, `data`, `scripts`
   - `3b800a5..57cba7a` touches only `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` (doc-only checkpoint; no research drift)
   - 35 artifact files, 0 manifest files
   - Canonical metrics unchanged:
     - `metrics_axb0306.json`: 60 trades (33L/27S), net -31,637.98, PF 0.4917, avg_r -0.0431
     - `metrics_kaggle.json`: 688 trades (359L/329S), net -626,525.96, PF 0.2271, avg_r -0.0684
   - Tests: `python3 -m pytest tests -q` -> 75 passed
3. State: **"Terminal — awaiting explicit user decision on forward path (a), (b), or (c)."**
4. Do NOT initiate research, experiments, automation changes, or handoff-only checkpoints on generic
   prompts without explicit user authorization.

## Forward Paths (require explicit user authorization)
- **(a)** Stop/reduce maintenance automation (`.github/workflows/main.yml:11`, cron)
- **(b)** Run a separately versioned, named experiment with explicit diff from frozen baseline
- **(c)** Accept baseline as final

## Hard Constraints
- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.