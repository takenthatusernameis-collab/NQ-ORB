# Initial Task for Next Agent

> **Current at HEAD `797d5035`, 2026-11-18.** `HANDOFF.md` is authoritative; this file is the short
> version. Research under the current scope is **complete and terminal**: the frozen MNQ 15-minute ORB
> baseline loses money **gross and net** on every free dataset available, and the free-data search is
> exhausted (`data/FEASIBILITY_REPORT.md`).

## The one thing to do

Send the user one short message: research is terminal, the numbers table below, the key finding, and
the three forward paths. Then stop.

There is no code work pending. Nothing in this repository can change a number until the user picks a
forward path or supplies new data.

## Decision rule — read before doing anything else

- **Boilerplate turn** ("read the prior task and complete it, then update the handoff and write an
  initial task for the next agent" with no new scope): do the message above only. Do **not** rewrite
  `HANDOFF.md` or this file, do **not** re-run `pytest`/`sha256sum`/drift checks/artifact counts, and
  do **not** commit. Both documents are already current at `797d5035`; repeating verification only
  produces docs-only commits with zero new evidence.
- **Explicit refresh request** ("update the handoff and write a new initial task"): a one-line
  verification pass (`git rev-parse --short HEAD`, `git status`, `pytest tests -q`, drift check) plus
  the two-file refresh is acceptable. Update the "Last refreshed" line, add one session-history
  bullet, do not change any number.
- **New scope named by the user** (new free data, a named experiment, or a specific automation
  change): act on exactly that scope and nothing wider.

Any controllable scope expansion beyond the above is a violation of the frozen-baseline discipline in
`AGENTS.md`, not initiative.

## Situational facts

- Frozen strategy: `STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`.
- Tests: **75 passing** (`python3 -m pytest tests -q`).
- Research drift since the last substantive commit `a797773`:
  `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` → **0 files**.
  Everything after `a797773` is docs-only plus the controller log
  `research_state/workflow_run_diagnostics.jsonl`.
- `artifacts/`: 35 files. Raw data hashes are in `HANDOFF.md` and unchanged.

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
  No trade in either ledger exits via the 15:55 ET flatten, so reported P&L does not depend on any
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

## Verification commands (only for an explicitly authorized research or refresh session)

```bash
git status --short && git rev-parse --short HEAD
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
sha256sum STRATEGY_RULES.txt raw/MNQ_15min.csv raw/MNQ_1min.csv raw/MNQ_15min_frontmonth.csv raw/MNQ_1min_frontmonth.csv
python3 -m pytest tests -q
python3 src/orb/runner.py --prefix <new> --source axb0306   # compare to artifacts/metrics_axb0306.json
python3 src/orb/runner.py --prefix <new> --source kaggle    # compare to artifacts/metrics_kaggle.json
```
