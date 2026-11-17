# Initial Task for Next Agent

## Your task

**Confirm the terminal repository state, report it, and await an explicit user decision.**
Do not start autonomous research, experiments, automation changes, or handoff-only checkpoints
without explicit user authorization.

This handoff/next-agent refresh was completed in the prior session at the user's explicit request;
no further research work is pending.

## What to do (in order)

1. Run the verification commands in `HANDOFF.md` (section "Verification commands") to confirm
   the current terminal state.
2. Read `HANDOFF.md` and `STRATEGY_RULES.txt` for full context.
3. Report the terminal state to the user and present the forward-path options below.
4. Stop. Do not invent new work, run experiments, or modify automation unless the user explicitly
   authorizes one of the forward paths.

## Context (as of last verification)

The frozen MNQ 15-minute ORB baseline (`STRATEGY_RULES.txt` v1.0) is implemented, tested
(75 passing), and evaluated on all available free MNQ data. It is **negative-net on every
dataset** under full costs, and the free-data search is exhausted (see `data/FEASIBILITY_REPORT.md`).
Research is complete. There is no pending research task.

## Current state (re-verified 2026-11-17, HEAD `72e86a0`)

- `STRATEGY_RULES.txt` SHA-256 = `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (frozen v1.0)
- `git status --short` clean at verification
- HEAD `72e86a0` (advanced from `760fa7a` via a `chore(kilo): checkpoint agent session` commit
  touching only `HANDOFF.md` / `INITIAL_TASK_FOR_NEXT_AGENT.md`).
  Zero research drift vs `a797773` in `artifacts`, `config`, `src`, `tests`, `raw`, `data`, `scripts`.
- 35 artifact files, 0 manifest files
- Canonical metrics unchanged (from artifacts):
  - `metrics_axb0306.json`: 60 trades (33L/27S), win 70.0%, gross -7,662.00, net -31,637.98,
    costs 23,975.98, PF 0.4917, avg_r -0.0431
  - `metrics_kaggle.json`: 688 trades (359L/329S), win 64.83%, gross -140,899.00, net -626,525.96,
    costs 485,626.96, PF 0.2271, avg_r -0.0684
- Tests re-run this session at HEAD `72e86a0`: 75 passed in 0.58s (`python3 -m pytest tests -q`).
  To re-run: `python3 -m pip install --quiet pytest pandas && python3 -m pytest tests -q`
- Raw data hashes unchanged:
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`

## Forward paths (require explicit user authorization)

- **(a)** Stop or reduce maintenance automation (`.github/workflows/main.yml:11`, cron).
- **(b)** Run a separately versioned, named experiment with an explicit diff from the frozen baseline.
- **(c)** Accept the baseline as final.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without
  explicit authorization for that exact change.