# NQ ORB — Durable handoff

## Status: TERMINAL — research complete; awaiting explicit user decision

The frozen MNQ 15-minute ORB baseline is implemented, tested, and evaluated on every available
free MNQ data source. It is **negative-net on all datasets** under full costs, and the free-data
search is exhausted (see `data/FEASIBILITY_REPORT.md`). Do not start autonomous research,
experiments, automation changes, or handoff-only checkpoints without an explicit user decision.

## Verified state (re-verified 2026-11-18, HEAD `f01b206`)

- `git rev-parse --short HEAD`: `f01b206` (docs-only checkpoints on top of substantive research; clean tree)
- `git status --short`: clean (before this session's doc update)
- `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts`: empty (zero research drift vs last substantive research commit `a797773`)
- `git diff --name-only a797773..HEAD` (excluding this session's doc edits): `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `research_state/workflow_run_diagnostics.jsonl` only (docs + excluded controller log)
- `STRATEGY_RULES.txt` SHA-256: `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (frozen v1.0)
- Baseline context: frozen showcase preset at `5fab764`; last substantive research commit `a797773`
- `artifacts/`: 35 files, 0 `*manifest*` files
- `python3 -m pytest tests -q`: **75 passed in 0.58s** (2026-11-18, HEAD `eecdab0`)

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

## Session note (2026-11-18, HEAD `c13d045`)

Prior agent task completed: confirmed terminal state at HEAD `ade54f5` and reported it. This session
re-verified all guardrails at HEAD `c13d045` (a docs-only checkpoint on top of `c7f407d`): clean tree;
zero research drift vs `a797773` (empty diff on `artifacts config src tests raw data scripts`);
`STRATEGY_RULES.txt` hash `6d3258c3...` and all four raw-data hashes unchanged; 35 artifacts / 0
manifests; 75 tests passed in 0.56s; canonical metrics unchanged (axb0306: 60 trades, 70.0% win, net
-31,637.98; kaggle: 688 trades, 64.83% win, net -626,525.96). No research, experiments, or automation
changes were made in this session. Repository remains terminal awaiting explicit user decision.

## Session note (2026-11-18, HEAD `8216fb1`)

Prior agent task completed: confirmed terminal state at HEAD `c13d045` and reported it. This session
re-verified all guardrails at HEAD `8216fb1` (a docs-only checkpoint on top of `c13d045`): clean tree;
zero research drift vs `a797773` (empty diff on `artifacts config src tests raw data scripts`);
`STRATEGY_RULES.txt` hash `6d3258c3...` and all four raw-data hashes unchanged; 35 artifacts / 0
manifests; 75 tests passed in 0.58s; canonical metrics unchanged (axb0306: 60 trades, 70.0% win, net
-31,637.98; kaggle: 688 trades, 64.83% win, net -626,525.96). No research, experiments, or automation
changes were made in this session. Repository remains terminal awaiting explicit user decision.

## Session note (2026-11-18, HEAD `9f23617`)

Prior agent task completed: confirmed terminal state at HEAD `8216fb1` and reported it. This session
re-verified all guardrails at HEAD `9f23617` (a docs-only checkpoint on top of `8216fb1`): clean tree;
zero research drift vs `a797773` (empty diff on `artifacts config src tests raw data scripts`);
`STRATEGY_RULES.txt` hash `6d3258c3...` and all four raw-data hashes unchanged; 35 artifacts / 0
manifests; 75 tests passed in 0.58s; canonical metrics unchanged (axb0306: 60 trades, 70.0% win, net
-31,637.98; kaggle: 688 trades, 64.83% win, net -626,525.96). No research, experiments, or automation
changes were made in this session. Repository remains terminal awaiting explicit user decision.

## Session note (2026-11-18, HEAD `784b8c2`)

Prior agent task completed: confirmed terminal state at HEAD `3908356` and reported it. This session
re-verified all guardrails at HEAD `784b8c2` (a docs-only checkpoint on top of `3908356`): clean tree;
zero research drift vs `a797773` (empty diff on `artifacts config src tests raw data scripts`);
`STRATEGY_RULES.txt` hash `6d3258c3...` and all four raw-data hashes unchanged; 35 artifacts / 0
manifests; 75 tests passed in 0.71s; canonical metrics unchanged (axb0306: 60 trades, 70.0% win, net
-31,637.98; kaggle: 688 trades, 64.83% win, net -626,525.96). No research, experiments, or automation
changes were made. Repository remains terminal awaiting explicit user decision.

## Session note (2026-11-18, HEAD `3908356`)

Prior agent task completed: confirmed terminal state at HEAD `9f23617` and reported it. This session
re-verified all guardrails at HEAD `3908356` (a docs-only checkpoint on top of `9f23617`): clean tree;
zero research drift vs `a797773` (empty diff on `artifacts config src tests raw data scripts`);
`STRATEGY_RULES.txt` hash `6d3258c3...` and all four raw-data hashes unchanged; 35 artifacts / 0
manifests; 75 tests passed in 0.59s; canonical metrics unchanged (axb0306: 60 trades, 70.0% win, net
-31,637.98; kaggle: 688 trades, 64.83% win, net -626,525.96). No research, experiments, or automation
changes were made. Repository remains terminal awaiting explicit user decision.

## Session note (2026-11-18, HEAD `eecdab0`)

Prior agent task completed: confirmed terminal state and reported it as requested. This session
re-verified all guardrails at HEAD `eecdab0`: clean tree; zero research drift vs `a797773` (empty diff
on `artifacts config src tests raw data scripts`); `STRATEGY_RULES.txt` hash `6d3258c3...` and all four
raw-data hashes unchanged; 35 artifacts / 0 manifests; 75 tests passed in 0.58s; canonical metrics
unchanged (axb0306: 60 trades, 70.0% win, net -31,637.98; kaggle: 688 trades, 64.83% win, net
-626,525.96). No research, experiments, or automation changes were made. Repository remains terminal
awaiting explicit user decision. This session updated `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`
as explicitly requested.

## Session note (2026-11-18, HEAD `08f141b`)

Prior agent task completed: confirmed terminal state at HEAD `8453eac` and reported it. This session
re-verified all guardrails at HEAD `08f141b` (a docs-only checkpoint on top of `8453eac`): clean tree;
zero research drift vs `a797773` (empty diff on `artifacts config src tests raw data scripts`);
`STRATEGY_RULES.txt` hash `6d3258c3...` and all four raw-data hashes unchanged; 35 artifacts / 0
manifests; 75 tests passed in 0.58s; canonical metrics unchanged (axb0306: 60 trades, 70.0% win, net
-31,637.98; kaggle: 688 trades, 64.83% win, net -626,525.96). No research, experiments, or automation
changes were made. Repository remains terminal awaiting explicit user decision. This session updated
`HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` as explicitly requested.

## Session note (2026-11-18, HEAD `f36ada9`)

Prior agent task completed: confirmed terminal state at HEAD `eecdab0` and reported it. This session
re-verified all guardrails at HEAD `f36ada9` (a docs-only checkpoint on top of `eecdab0`): clean tree;
zero research drift vs `a797773` (empty diff on `artifacts config src tests raw data scripts`);
`STRATEGY_RULES.txt` hash `6d3258c3...` and all four raw-data hashes unchanged; 35 artifacts / 0
manifests; 75 tests passed in 0.64s; canonical metrics unchanged (axb0306: 60 trades, 70.0% win, net
-31,637.98; kaggle: 688 trades, 64.83% win, net -626,525.96). No research, experiments, or automation
changes were made. Repository remains terminal awaiting explicit user decision. This session updated
`HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` as explicitly requested.

## Session note (2026-11-18, HEAD `3a3324f`)

Prior agent task completed: confirmed terminal state at HEAD `f36ada9` and reported it. This session
re-verified all guardrails at HEAD `3a3324f` (a docs-only checkpoint on top of `f36ada9`): clean tree;
zero research drift vs `a797773` (empty diff on `artifacts config src tests raw data scripts`);
`STRATEGY_RULES.txt` hash `6d3258c3...` and all four raw-data hashes unchanged; 35 artifacts / 0
manifests; 75 tests passed in 0.71s; canonical metrics unchanged (axb0306: 60 trades, 70.0% win, net
-31,637.98; kaggle: 688 trades, 64.83% win, net -626,525.96). No research, experiments, or automation
changes were made. Repository remains terminal awaiting explicit user decision. This session updated
`HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` as explicitly requested.

## Session note (2026-11-18, HEAD `8453eac`)

Prior agent task completed: confirmed terminal state at HEAD `3a3324f` and reported it. This session
re-verified all guardrails at HEAD `8453eac` (a docs-only checkpoint on top of `3a3324f`): clean tree;
zero research drift vs `a797773` (empty diff on `artifacts config src tests raw data scripts`);
`STRATEGY_RULES.txt` hash `6d3258c3...` and all four raw-data hashes unchanged; 35 artifacts / 0
manifests; 75 tests passed in 0.61s; canonical metrics unchanged (axb0306: 60 trades, 70.0% win, net
-31,637.98; kaggle: 688 trades, 64.83% win, net -626,525.96). No research, experiments, or automation
changes were made. Repository remains terminal awaiting explicit user decision. This session updated
`HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` as explicitly requested.

## Session note (2026-11-18, HEAD `f01b206`)

Prior agent task completed: confirm the terminal state and report it. This session re-verified all
guardrails at HEAD `f01b206` (a docs-only checkpoint on top of `08f141b`): clean tree (before this
doc update); zero research drift vs `a797773` (empty diff on `artifacts config src tests raw data
scripts`); `STRATEGY_RULES.txt` hash `6d3258c3...` and all four raw-data hashes unchanged; 35
artifacts / 0 manifests; 75 tests passed in 0.58s; canonical metrics unchanged (axb0306: 60 trades,
70.0% win, net -31,637.98; kaggle: 688 trades, 64.83% win, net -626,525.96). No research,
experiments, or automation changes were made. Repository remains terminal awaiting explicit user
decision. This session updated `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` as explicitly
requested by the user.

## Session note (2026-11-18, HEAD `c5246ea`)

Prior agent task completed: confirmed terminal state at HEAD `f01b206` and reported it. This session
re-verified all guardrails at HEAD `c5246ea` (a docs-only checkpoint on top of `f01b206`): clean tree;
zero research drift vs `a797773` (empty diff on `artifacts config src tests raw data scripts`);
`STRATEGY_RULES.txt` hash `6d3258c3...` and all four raw-data hashes unchanged; 35 artifacts / 0
manifests; 75 tests passed in 0.66s; canonical metrics unchanged (axb0306: 60 trades, 70.0% win, net
-31,637.98; kaggle: 688 trades, 64.83% win, net -626,525.96). No research, experiments, or automation
changes were made. Repository remains terminal awaiting explicit user decision. This session updated
`HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` as explicitly requested.

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
