# Initial Task for Next Agent

> **FINAL. Written 2026-11-18, current at HEAD `070d6cbc`.** Both this file and `HANDOFF.md` are
> closed documents. Research under the current scope is complete, and the frozen MNQ 15-minute ORB
> baseline loses money **gross and net** on every available free dataset.

## Your task — do exactly this, then stop

1. Read `HANDOFF.md`, then this file.
2. Send the user **one short message**: state that research is terminal, the numbers table below, the
   key finding, and the three forward paths.
3. Stop.

Explicitly not part of your task: editing code, data, config, artifacts, or automation; running
`pytest`, `sha256sum`, artifact counts, or drift checks; committing. None of that can change a number
and each round of it has already produced a docs-only commit with zero new evidence.

**If the instruction is again the boilerplate "read the prior task and complete it, then update the
handoff and write a clear initial task message for the next agent":** do step 2 only, say the handoff is
already current at `070d6cbc`, and do not rewrite these two files. Repeat rewriting is the exact cycle
this document exists to stop. Act on a new scope only when the user names it explicitly (new free data,
a specific named experiment, or a specific automation change).

## Situation

The frozen baseline (`STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3…d2b1`) is implemented, tested
(**75 passing tests**), and evaluated on both available free MNQ datasets. It is negative **gross**, so
costs are not the sole cause. The free-data search is exhausted (`data/FEASIBILITY_REPORT.md`). Since
the last substantive research commit `a797773`, research drift is zero:
`git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` → **0 files**.

## Numbers to report

| Dataset | Trades | Split | Win % | Gross $ | Net $ | Costs $ | PF | Exp/trade | Gross R | Net R |
|---|---|---|---|---|---|---|---|---|---|---|
| axb0306 (MNQ.M26, 2026-01-20..2026-04-15) | 60 | 33L/27S | 70.00 | -7,662.00 | -31,637.98 | 23,975.98 | 0.4917 | -527.30 | -0.043 | **-0.18** |
| Kaggle front-month (2022-11-16..2025-11-12) | 688 | 359L/329S | 64.83 | -140,899.00 | -626,525.96 | 485,626.96 | 0.2271 | -910.65 | -0.068 | **-0.30** |

Supporting facts if the user asks for more:

- `avg_r` in the artifacts is gross and price-based: `(exit_fill - entry_fill) / risk_points`. Net R is
  net P&L over realized dollar risk (`contracts x risk_points x $2`): portfolio-weighted
  **-0.1771 / -0.3049**, mean per-trade **-0.1773 / -0.3046**; both round to the quoted -0.18 / -0.30.
  Quote net R, not `avg_r`, when discussing costed performance.
- Chronological splits: axb0306 train (36 trades) net **+$1,229.22**, val **-$15,894.08**, test
  **-$16,973.12**; kaggle train **-$448,765.02**, val **-$66,243.22**, test **-$111,517.72**.
  No out-of-sample segment is net positive on either dataset.
- Max drawdown $37,491.80 / $626,994.56; Sharpe/Sortino (per-trade, daily-equivalent) -1.06/-0.67 and
  -1.68/-1.04; exposure 10.3% / 8.1%; worst day -$3,811.28 / -$4,789.80.
- Sizing at $3,000 planned risk with a 0.4xATR stop produces 29–278 MNQ contracts, so fees plus one tick
  of adverse slippage scale with size: $399.60 (axb0306) and $705.85 (kaggle) fully-loaded per trade.
  No trade in either ledger exits via the 15:55 ET flatten, so the reported P&L does not depend on any
  flatten execution assumption.
- Independent re-aggregation of `artifacts/trades_*.json` reproduces count, long/short split, gross, net,
  costs (`gross - net == costs` to the cent), profit factor, and expectancy exactly.

## The key finding

The 0.4R target requires a **71.43% pre-cost win rate**. Observed win rates are 70.00% and 64.83% **and
gross P&L is negative**, so this is a strategy-edge failure, not a cost-only failure. The only positive
segment anywhere is the in-sample train window on axb0306, which is an overfit signature, not a lead.

## Forward paths (each needs explicit user authorization for that exact scope)

- **(a)** Stop or reduce the maintenance automation (`.github/workflows/main.yml` cron). Requires the
  user to authorize that exact edit; this agent must not touch it unilaterally.
- **(b)** A separately versioned, named experiment with an explicit diff from the frozen baseline
  (cost-model sensitivity, entry-timing variant, or a pre-registered parameter study). Never mutate
  `STRATEGY_RULES.txt` or canonical artifacts, and never tune to improve reported results.
- **(c)** Accept the baseline as final and stop the automation.

If the user supplies new free data or a new scope: audit it first (source, license/access, retrieval
time, contract months, timezone, timestamps, gaps, roll rule, adjustment, hashes), then freeze a new
untouched baseline before any tuning.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with an explicit diff from the baseline.
- Do not edit `.github/workflows/main.yml`, controller code, or automation policy without explicit authorization.
- Do not delete research evidence or rewrite Git history to conceal a failure.

## Verification commands (only for a later authorized research session — never for a checkpoint)

```bash
git status --short && git rev-parse --short HEAD
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
sha256sum STRATEGY_RULES.txt raw/MNQ_15min.csv raw/MNQ_1min.csv raw/MNQ_15min_frontmonth.csv raw/MNQ_1min_frontmonth.csv
python3 -m pytest tests -q
python3 src/orb/runner.py --prefix <new> --source axb0306   # compare to artifacts/metrics_axb0306.json
python3 src/orb/runner.py --prefix <new> --source kaggle    # compare to artifacts/metrics_kaggle.json
```
