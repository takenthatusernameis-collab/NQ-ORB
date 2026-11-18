# Initial Task for Next Agent

> **Message from prior agent (2026-11-18, HEAD `4682067`):**
>
> The NQ/MNQ opening-range-breakout research is complete and terminal. The frozen baseline is
> implemented, tested (75 passing), and evaluated on every available free MNQ data source. It is
> negative-net on all datasets under full costs, and the free-data search is exhausted. I have
> re-verified the terminal state at HEAD `4682067` (docs-only checkpoint since `e49de68` /
> `b31f7d8`): clean tree, zero research drift vs `a797773`, unchanged `STRATEGY_RULES.txt` hash and
> raw data hashes, 35 artifacts / 0 manifests, canonical metrics unchanged. No research, experiments,
> or automation changes were made.

## Your task

**Confirm the terminal repository state, report it to the user, and await an explicit user
decision.**

Do not start autonomous research, experiments, automation changes, or handoff-only checkpoints
without explicit user authorization. A handoff/doc update is authorized only when the user
explicitly requests it.

## Steps

1. Run the verification commands in `HANDOFF.md` ("Verification commands") to confirm terminal state.
2. Read `HANDOFF.md` and `STRATEGY_RULES.txt` for full context.
3. Report the terminal state and the forward-path options below to the user.
4. Stop. Do not invent work or modify automation unless the user explicitly authorizes a forward path.

## Current state (re-verified 2026-11-18, HEAD `4682067`)

- Status: **TERMINAL** — baseline implemented/tested/evaluated on all available free MNQ data;
  negative-net everywhere; free-data search exhausted (`data/FEASIBILITY_REPORT.md`).
- `git rev-parse --short HEAD`: `4682067`
- `git status --short`: clean
- `git diff --name-only b31f7d8..HEAD`: `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md` only (docs-only checkpoint)
- `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts`: empty (zero research drift)
- `git diff --name-only a797773..HEAD`: `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`,
  `research_state/workflow_run_diagnostics.jsonl` only
- `STRATEGY_RULES.txt` SHA-256: `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (frozen v1.0)
- Artifacts: 35 files, 0 manifests
- Tests: `python3 -m pytest tests -q` → **75 passed in 0.58s**
- Canonical metrics (unchanged):
  - axb0306 (`artifacts/metrics_axb0306.json`): 60 trades (33L/27S), win 70.0%, gross -$7,662.00,
    net -$31,637.98, costs $23,975.98, PF 0.4917, avg R -0.0431, expectancy -$527.30/trade
  - Kaggle front-month (`artifacts/metrics_kaggle.json`): 688 trades (359L/329S), win 64.83%,
    gross -$140,899.00, net -$626,525.96, costs $485,626.96, PF 0.2271, avg R -0.0684,
    expectancy -$910.65/trade
- Raw data hashes unchanged:
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`

## Forward paths (require explicit user authorization)

- **(a)** Stop or reduce maintenance automation (`.github/workflows/main.yml` cron) — requires explicit authorization for that exact change.
- **(b)** Run a separately versioned, named experiment with an explicit diff from the frozen baseline.
- **(c)** Accept the baseline as final.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.
