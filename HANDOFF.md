# NQ ORB — Durable handoff

## Status: TERMINAL — research complete; awaiting explicit user decision

The frozen MNQ 15-minute ORB baseline is implemented, tested, and evaluated on every available
free MNQ data source. It is **negative-net on all datasets** under full costs, and the free-data
search is exhausted (see `data/FEASIBILITY_REPORT.md`). Do not start autonomous research,
experiments, automation changes, or handoff-only checkpoints without an explicit user decision.

## Verified state (re-verified 2026-11-18, HEAD `9167cd0`)

- `git rev-parse --short HEAD`: `9167cd0`
- `git status --short`: clean
- `git diff --name-only b31f7d8..HEAD`: `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md` only (docs-only checkpoints since prior verification)
- `git diff --name-only bb05347..HEAD`: `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md` only (latest checkpoint is docs-only)
- `git diff --name-only 463fa35..HEAD`: `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md` only (prior docs-only checkpoint)
- `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts`: empty (zero research drift vs last substantive research commit `a797773`)
- `git diff --name-only a797773..HEAD`: `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `research_state/workflow_run_diagnostics.jsonl` only (docs + excluded controller log)
- `STRATEGY_RULES.txt` SHA-256: `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (frozen v1.0)
- Baseline context: frozen showcase preset at `5fab764`; last substantive research commit `a797773`
- `artifacts/`: 35 files, 0 `*manifest*` files
- `python3 -m pytest tests -q`: **75 passed in 0.61s** (2026-11-18, HEAD `9167cd0`)

Raw data hashes (unchanged):
- `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`
- `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`
- `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`
- `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`

## Canonical metrics (unchanged; re-read from artifacts)

### axb0306 — single-contract MNQ.M26, 2026-01-20..2026-04-15, no roll / no adjustment
- 60 trades (33L/27S); win rate 70.0%
- gross -7,662.00; net -31,637.98; costs 23,975.98; avg R -0.0431; expectancy -527.30/trade
- profit factor 0.4917; max DD 37,491.80
- 1-minute data supports exact 15:55 ET flatten / intrabar ordering on all 60 trade days
- Source: `artifacts/metrics_axb0306.json`, `artifacts/trades_axb0306.json`

### Kaggle front-month — unadjusted front-month by max volume, 2022-11-16..2025-11-12
- 688 trades (359L/329S); win rate 64.83%
- gross -140,899.00; net -626,525.96; costs 485,626.96; avg R -0.0684; expectancy -910.65/trade
- profit factor 0.2271; max DD 626,994.56
- Source: `artifacts/metrics_kaggle.json`, `artifacts/trades_kaggle.json`

## Key facts

- 0.4R target implies a pre-cost break-even win rate of 71.43%; both datasets fall short after costs. Gross P&L is also negative.
- Costs (commission + exchange/clearing $2.87/side, 1 tick adverse slippage) dominate net results.
- Independent signal-funnel cross-check reproduces engine trade counts exactly (axb0306 60, kaggle 688).
- No paid/proprietary data used; no credentials requested or stored; free-source search exhausted.
- `research_state/workflow_run_diagnostics.jsonl` is controller/runtime log capture (excluded from research-drift checks).

## Session note (2026-11-18, HEAD `9167cd0`)

Prior agent task completed: confirmed terminal state at HEAD `9167cd0` (docs-only checkpoint on top
of `463fa35`; `git diff 463fa35..9167cd0` touches only `HANDOFF.md` and
`INITIAL_TASK_FOR_NEXT_AGENT.md`). Re-verified all guardrails: clean tree; zero research drift vs
`a797773` (empty diff on `artifacts config src tests raw data scripts`); `STRATEGY_RULES.txt` hash
`6d3258c3...` and all four raw-data hashes unchanged; 75 tests passed in 0.61s; 35 artifacts / 0
manifests; canonical metrics unchanged — axb0306 60/70.0%/gross -7,662.00/net -31,637.98/costs
23,975.98/PF 0.4917/avgR -0.0431/expectancy -527.30/maxDD 37,491.80; kaggle 688/64.83%/gross
-140,899.00/net -626,525.96/costs 485,626.96/PF 0.2271/avgR -0.0684/expectancy -910.65/maxDD
626,994.56. The prior agent task (confirm terminal state, report, await explicit user decision) is
complete. Per explicit user request, the handoff and next-agent task were refreshed. No research,
experiments, or automation changes were made.

## Required action for next agent

**Confirm the terminal state, report it, and await an explicit user decision.** Do not start
autonomous research, experiments, automation changes, or handoff-only checkpoints without explicit
user authorization. A handoff update is authorized only when the user explicitly requests it.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

## Verification commands

```bash
git status --short
git rev-parse --short HEAD
sha256sum STRATEGY_RULES.txt
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
ls artifacts | wc -l && ls artifacts | grep -c manifest || true
sha256sum raw/MNQ_15min.csv raw/MNQ_1min.csv raw/MNQ_15min_frontmonth.csv raw/MNQ_1min_frontmonth.csv
python3 -m pytest tests -q   # if pytest + pandas installed
```