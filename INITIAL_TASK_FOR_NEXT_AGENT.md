# Initial Task for Next Agent

> **Current at HEAD `a0436db4`, 2026-11-19.** `HANDOFF.md` is authoritative; this file is the short
> version.
>
> **Status: TERMINAL. There is no pending code, data, pipeline, or experiment work.** The frozen MNQ
> 15-minute ORB baseline is implemented, tested, and evaluated on every free data source available. It is
> **negative-gross and negative-net on all of them**, and the free-data search is exhausted
> (`data/FEASIBILITY_REPORT.md`). Nothing in this repository can change a number until the user picks a
> forward path or supplies new data.

## Your job, in one line

Drain the user's next instruction. If it is boilerplate ("read the prior task and complete it"), reply with
the status + numbers table + three forward paths below and **stop** — no edits, no verification sweep, no
commit.

## Default turn: send this, then stop

1. **Terminal state.** The strategy loses money gross *and* net on all free data. There is no outstanding work.
2. **Numbers table** (below).
3. **Three forward paths** (below).

No file edits. No `pytest`/`sha256sum`/drift/artifact re-checks. No commit. Re-emitting these documents is
the failure mode this file exists to stop.

## Decision rule

- **Boilerplate turn** → the one message above, then stop.
- **Explicit doc-refresh request** → allowed, **one compact pass only**: re-read the canonical artifacts to
  confirm numbers, bump the HEAD/commit-count references, fold this turn into the existing session line.
  Change nothing else. Never chain a second refresh.
- **Explicit new scope** → act on exactly that scope and nothing wider. New free data must be audited
  (source, license/access, retrieval time, contract months, timezone, timestamps, gaps, roll rule,
  adjustment, hashes) and a fresh untouched baseline frozen before any tuning. A strategy change must be a
  named, versioned experiment with a written diff from the frozen baseline.
- **Nothing else.** Do not invent scope, do not "improve" the baseline, do not search parameters, do not
  re-run the free-data search without a new candidate source.

## Situational facts

- Frozen strategy: `STRATEGY_RULES.txt` v1.0, SHA-256
  `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`.
- Tests: **75 passing** (`python3 -m pytest tests -q`, last executed at `6f73afaf`). Not re-run at
  `a0436db4`: this sandbox has no `pytest`/`numpy`, so status carries forward from a zero-drift source tree.
- Research drift since `a797773`: `git diff --name-only a797773..HEAD -- artifacts config src tests raw data
  scripts` → **0 files**, across **2,057** docs-only commits touching 3 unique paths.
- `artifacts/`: 35 files. Raw data: 4 CSVs, hashes unchanged since first freeze (see `HANDOFF.md`).
- No paid/proprietary data; no credentials requested, used, or stored.

## Numbers to report

| Dataset | Trades | Split | Win % | Gross $ | Net $ | Costs $ | PF | Exp/trade | Gross R | Net R |
|---|---|---|---|---|---|---|---|---|---|---|
| axb0306 (MNQ.M26, 2026-01-20..2026-04-15) | 60 | 33L/27S | 70.00 | -7,662.00 | -31,637.98 | 23,975.98 | 0.4917 | -527.30 | -0.043 | **-0.18** |
| Kaggle front-month (2022-11-16..2025-11-12) | 688 | 359L/329S | 64.83 | -140,899.00 | -626,525.96 | 485,626.96 | 0.2271 | -910.65 | -0.068 | **-0.30** |

Supporting facts, only if the user asks:

- `metrics.avg_r` is **gross and price-based**: `(exit_fill - entry_fill) / risk_points`. Net R is net P&L
  over realized dollar risk (`contracts x risk_points x $2`): portfolio-weighted **-0.1771 / -0.3049**,
  mean per-trade **-0.1773 / -0.3046**. Quote net R, not `avg_r`, for costed performance.
- Chronological splits — axb0306: train (36 trades) **+$1,229.22**, val **-$15,894.08**, test
  **-$16,973.12**. Kaggle: train **-$448,765.02**, val **-$66,243.22**, test **-$111,517.72**. No
  out-of-sample segment is net positive.
- Max DD $37,491.80 / $626,994.56; Sharpe/Sortino (per-trade, daily-equivalent) -1.06/-0.67 and -1.68/-1.04;
  exposure 10.3% / 8.1%; worst day -$3,811.28 / -$4,789.80.
- $3,000 planned risk with a 0.4xATR stop implies 29–278 MNQ contracts, so fees + one tick of adverse
  slippage scale with size: $399.60 / $705.85 fully loaded per trade. No trade exits via the 15:55 ET
  flatten, so reported P&L does not depend on a flatten execution assumption.
- Independent re-aggregation of `artifacts/trades_*.json` reproduces count, long/short split, gross, net,
  costs (`gross - net == costs` to the cent), profit factor, and expectancy exactly.
- Cost sensitivity: all 12 scenarios are net-negative — axb0306 -$24,754.28 to -$40,610.18; kaggle
  -$487,098.57 to -$808,255.35. No cost assumption rescues the baseline.

## The key finding

The 0.4R target requires a **71.43% pre-cost win rate**. Observed win rates are 70.00% and 64.83% **and
gross P&L is negative**, so this is a strategy-edge failure, not a cost-only failure. The only positive
segment anywhere is the in-sample train window on axb0306 — an overfit signature, not a lead.

## Forward paths (each needs explicit user authorization for that exact scope)

- **(a)** Stop or reduce the maintenance automation (`.github/workflows/main.yml`, currently `*/5 * * * *`).
  This agent must not touch it unilaterally.
- **(b)** A separately versioned, named experiment with an explicit diff from the frozen baseline
  (cost-model sensitivity, entry-timing variant, or a pre-registered parameter study). Never mutate
  `STRATEGY_RULES.txt` or canonical artifacts, and never tune to improve reported results.
- **(c)** Accept the baseline as final and stop the automation.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with an explicit diff from the baseline.
- Do not edit `.github/workflows/main.yml`, controller code, or automation policy without explicit authorization.
- Do not delete research evidence or rewrite Git history to conceal a failure.

## Verification commands (only for an explicitly authorized research or refresh session)

```bash
git status --short && git rev-parse --short HEAD
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
sha256sum STRATEGY_RULES.txt raw/MNQ_15min.csv raw/MNQ_1min.csv raw/MNQ_15min_frontmonth.csv raw/MNQ_1min_frontmonth.csv
python3 -m pytest tests -q
python3 src/orb/runner.py --prefix <new> --source axb0306   # compare to artifacts/metrics_axb0306.json
python3 src/orb/runner.py --prefix <new> --source kaggle    # compare to artifacts/metrics_kaggle.json
```

Note: `pytest`, `numpy`, and `pandas` are not installed in the ephemeral CI sandbox; install them before
attempting the last three commands there.

## Session note

- **2026-11-19, HEAD `3b57e481` … `a0436db4`:** the same boilerplate request on every later turn, never a
  forward path. Each was a compact refresh with identical results: clean tree, drift `a797773..HEAD` → **0
  files** over 2,046–2,057 docs-only commits / 3 unique paths, `artifacts/` 35 files, `STRATEGY_RULES.txt`
  and all four raw-data hashes unchanged, both canonical metric files re-read and matching the table above.
  `pytest`/`numpy`/`pandas` unavailable locally (status carried forward from the zero-drift tree). Only
  HEAD/count references changed. Collapsed into one note — these produced no new evidence. **Stop
  refreshing:** see `HANDOFF.md` STOP RULE.
