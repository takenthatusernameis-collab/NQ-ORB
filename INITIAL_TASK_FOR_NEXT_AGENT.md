# Initial Task for Next Agent

## Objective
Confirm terminal repository state and await an explicit user decision on the forward path.
Do not start autonomous research, experiments, automation changes, or handoff-only checkpoints
without explicit user authorization.

## Context
The frozen MNQ 15-minute ORB baseline (STRATEGY_RULES.txt v1.0) is implemented, tested (75 passing),
and evaluated on all available free data. It is negative-net on every dataset under full costs, and
the free-data search is exhausted. Research is complete — do not invent new work.

## Current state (re-verified 2026-11-16, HEAD `e743e1a`)

- `STRATEGY_RULES.txt` SHA-256 = `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (frozen v1.0)
- `git status --short` clean
- HEAD `e743e1a` is a `chore(kilo): checkpoint agent session` commit touching only HANDOFF.md and
  INITIAL_TASK_FOR_NEXT_AGENT.md; zero research drift vs `a797773` in `artifacts`, `config`, `src`, `tests`, `raw`, `data`, `scripts`
- 35 artifact files, 0 manifest files
- Canonical metrics unchanged (from artifacts):
  - `metrics_axb0306.json`: 60 trades (33L/27S), win 70.0%, gross -7,662.00, net -31,637.98, costs 23,975.98, PF 0.4917, avg_r -0.0431
  - `metrics_kaggle.json`: 688 trades (359L/329S), win 64.83%, gross -140,899.00, net -626,525.96, costs 485,626.96, PF 0.2271, avg_r -0.0684
- Tests: `python3 -m pytest tests -q` -> 75 passed
- Raw data hashes unchanged:
  - raw/MNQ_15min.csv `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`
  - raw/MNQ_1min.csv `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`
  - raw/MNQ_15min_frontmonth.csv `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`
  - raw/MNQ_1min_frontmonth.csv `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`

## Required Actions

1. Run the verification commands in `HANDOFF.md` (Verification commands) to confirm terminal state.
2. Report the terminal state and await an explicit user decision on the forward path (a), (b), or (c).
3. Do NOT initiate research, experiments, automation changes, or handoff-only checkpoints on generic
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