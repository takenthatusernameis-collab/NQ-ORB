# Initial Task for Next Agent

> **Message from prior agent (2026-11-18, HEAD `b809e0e6`):**
>
> NQ/MNQ ORB research remains complete and terminal. I read the durable handoff and completed the
> prior task: reported the terminal state and the three forward paths to the user at HEAD
> `b809e0e6` (tree clean, zero research drift vs `a797773`, `STRATEGY_RULES.txt` SHA-256
> `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` and raw-data hashes
> unchanged, 35 artifacts / 0 manifests, last test run **75 passed in 0.68s**). No new
> verification checks were run per the loop warning; no research, experiments, or automation
> changes were made. `HANDOFF.md` and this file updated as explicitly requested by the user.
>
> **This is one of many consecutive verification-only checkpoints** (see the preserved HEAD list in
> `HANDOFF.md`). Do not repeat it.

## Your task

**Do not verify or re-check anything. Report and stop.**

The terminal state is already verified and recorded below. Running `git status`, `sha256sum`, and
`pytest` again produces no new evidence and only creates another docs-only commit. Unless the user
has selected a forward path or supplied new data/scope, your entire turn is:

1. Read `HANDOFF.md` (Status + Required action sections) and `STRATEGY_RULES.txt` for context.
2. Summarize the result to the user in one short message: frozen MNQ 15-minute ORB baseline is
   implemented, tested, and negative-net on all available free data at full costs (axb0306 60
   trades, net -$31,637.98, PF 0.4917, avg R -0.0431; Kaggle 688 trades, net -$626,525.96,
   PF 0.2271, avg R -0.0684); free-data search exhausted per `data/FEASIBILITY_REPORT.md`.
3. Present the three forward paths (a/b/c below) and stop.
4. Do **not** modify `.github/workflows/main.yml`, the controller, research code, data, configs, or
   artifacts. Do **not** update `HANDOFF.md` or this file unless the user explicitly asks.

## Forward paths (require explicit user authorization)

- **(a)** Stop or reduce maintenance automation (`.github/workflows/main.yml` cron). This is the
  highest-value action available: the loop currently exits the research phase and spends each run
  re-confirming an unchanged terminal state. Requires explicit authorization for that exact edit.
- **(b)** Run a separately versioned, named experiment with an explicit diff from the frozen
  baseline. Candidate pre-registered experiments, in order of informational value:
  1. Cost-model sensitivity at 0 / 1 / 2 / 3 ticks adverse slippage plus fee tiers, reported gross
     and net, to quantify how much of the negative result is cost-driven versus signal-driven.
  2. Entry-timing variant: signal-close entry as primary (currently a sensitivity only), to test
     whether one-bar entry delay explains the result.
  3. Pre-registered parameter study (0.4R target vs alternatives, ATR multiples) on train/validation
     only, with the untouched test interval withheld until a single configuration is frozen.
  Each must be a new named config + artifact set; never mutate `STRATEGY_RULES.txt` or existing
  canonical artifacts.
- **(c)** Accept the baseline as final and stop the automation.

If the user supplies new free data or a new scope: audit it first (source URL, license/access
constraints, retrieval time, contract months, timezone, timestamp convention, gaps, roll rule,
adjustment method, SHA-256) before writing or running any pipeline.

## Current state (re-verified 2026-11-18, HEAD `b809e0e6`)

- Status: **TERMINAL** — baseline implemented/tested/evaluated on all available free MNQ data; negative-net everywhere; free-data search exhausted (`data/FEASIBILITY_REPORT.md`).
- `git rev-parse --short HEAD`: `b809e0e6` (at verification)
- `git status --short`: clean at verification
- `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts`: empty (zero research drift)
- `git diff --name-only a797773..HEAD`: `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `research_state/workflow_run_diagnostics.jsonl` only (docs + excluded controller log)
- `STRATEGY_RULES.txt` SHA-256: `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (frozen v1.0)
- Artifacts: 35 files, 0 manifests
- Tests: `python3 -m pytest tests -q` → **75 passed in 0.68s**
- Canonical metrics (unchanged):
  - axb0306 (`artifacts/metrics_axb0306.json`): 60 trades (33L/27S), win 0.7000, gross -$7,662.00, net -$31,637.98, costs $23,975.98, PF 0.491673, avg R -0.043097, expectancy -$527.30/trade, max DD $37,491.80
  - Kaggle front-month (`artifacts/metrics_kaggle.json`): 688 trades (359L/329S), win 0.648256, gross -$140,899.00, net -$626,525.96, costs $485,626.96, PF 0.227090, avg R -0.068417, expectancy -$910.65/trade, max DD $626,994.56
- Raw data hashes unchanged (`raw/MNQ_15min.csv` f417f22d..., `raw/MNQ_1min.csv` 129623f4..., `raw/MNQ_15min_frontmonth.csv` 7e129ae3..., `raw/MNQ_1min_frontmonth.csv` edbadc73...)

Only run the verification block below if the user explicitly asks for a re-audit, or if you are
about to rely on a claim that a file is unchanged.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

## Verification commands (only on explicit request)

```bash
git status --short
git rev-parse --short HEAD
sha256sum STRATEGY_RULES.txt
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
ls artifacts | wc -l && ls artifacts | grep -c manifest || true
sha256sum raw/MNQ_15min.csv raw/MNQ_1min.csv raw/MNQ_15min_frontmonth.csv raw/MNQ_1min_frontmonth.csv
python3 -m pytest tests -q   # if pytest installed
```
