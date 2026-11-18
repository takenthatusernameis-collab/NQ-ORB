# Initial Task for Next Agent

> **Message from prior agent (2026-11-18, HEAD `7f82e992`).**

## Read this first

NQ/MNQ ORB research is **complete and terminal** under the current scope. The frozen MNQ 15-minute ORB
baseline is implemented, tested, and evaluated on every free data source that was available; it is
negative-net on all of them, and the free-data search is exhausted (`data/FEASIBILITY_REPORT.md`).

Nothing in `artifacts config src tests raw data scripts` has changed since `a797773`. That means **there
is no research work for you to do.** Do not re-run the verification battery, do not recount artifacts,
do not re-derive metrics, and do not rewrite these two files. Every such session produces a docs-only
commit and zero new evidence.

## Do exactly this, then stop

1. Read `HANDOFF.md`: *Status*, *STOP RULE*, *Key facts*, *Forward paths*.
2. Send the user **one** short message containing:
   - the numbers table below,
   - that a 0.4R target requires a 71.43% pre-cost win rate (both datasets miss it, and gross P&L is
     negative as well, so this is not a cost-only failure),
   - that 75 tests pass,
   - forward paths (a)/(b)/(c), and one line asking the user to authorize either **(a)** or **(c)** to
     stop/reduce the cron, or the exact scope of a new experiment **(b)**.
3. Stop. Make **no commit**. If the only thing your turn would produce is a commit touching
   `HANDOFF.md` / `INITIAL_TASK_FOR_NEXT_AGENT.md`, make no commit at all.

The loop cannot end itself: `.github/workflows/main.yml` cron resumes a session, and a docs-only commit
is the only "deliverable" available. Only the user can break the cycle by picking (a)/(b)/(c).

## Numbers to report

| Dataset | Trades | Split | Win % | Gross $ | Net $ | Costs $ | PF | Exp/trade | Gross R | Net R |
|---|---|---|---|---|---|---|---|---|---|---|
| axb0306 (MNQ.M26, 2026-01-20..2026-04-15) | 60 | 33L/27S | 70.00 | -7,662.00 | -31,637.98 | 23,975.98 | 0.4917 | -527.30 | -0.0431 | **-0.1773** |
| Kaggle front-month (2022-11-16..2025-11-12) | 688 | 359L/329S | 64.83 | -140,899.00 | -626,525.96 | 485,626.96 | 0.2271 | -910.65 | -0.0684 | **-0.3046** |

`avg_r` in the artifacts is gross/price-based; the net R above is recomputed from the trade ledgers as
net P&L over realized dollar risk (`contracts x risk_points x $2`). Position sizing at $3,000 planned
risk with a 0.4xATR stop implies 29-278 MNQ contracts, so fully-loaded cost drag scales with size and
dominates the result. No trade in either ledger exits via the 15:55 ET flatten, so reported P&L does not
depend on any flatten execution assumption.

## Forward paths (each needs explicit user authorization for that exact scope)

- **(a)** Stop or reduce the maintenance automation (`.github/workflows/main.yml` cron). The only action
  that actually ends the docs-only checkpoint loop. Not permitted without explicit approval for that
  exact edit.
- **(b)** Run a separately versioned, named experiment with an explicit diff from the frozen baseline
  (cost-model sensitivity, entry-timing variant, or a pre-registered parameter study). Never mutate
  `STRATEGY_RULES.txt` or existing canonical artifacts, and never tune to improve reported results.
- **(c)** Accept the baseline as final and stop the automation.

If the user supplies new free data or a new scope: audit first (source, license/access, retrieval time,
contract months, timezone, timestamps, gaps, roll rule, adjustment, hashes) before writing or running any
pipeline.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with an explicit diff from the frozen baseline.
- Do not edit `.github/workflows/main.yml`, the controller, permissions, or automation policy without
  explicit authorization for that exact change.
