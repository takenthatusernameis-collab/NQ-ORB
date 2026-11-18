# Initial Task for Next Agent

> **Message from prior agent (2026-11-18, HEAD `b8bad199`).**

## Situation in one paragraph

NQ/MNQ ORB research is **complete and terminal** under the current scope. The frozen MNQ 15-minute ORB
baseline is implemented, tested, and evaluated on every free data source that was available; it is
negative-net on all of them, and the free-data search is exhausted (`data/FEASIBILITY_REPORT.md`).
`git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` returns **0 files**:
there is no research work left to do. Dozens of prior sessions produced docs-only commits that
re-confirmed identical invariants and added zero evidence. `HANDOFF.md` and this file were just
refreshed at HEAD `b8bad199`, so **do not rewrite them again**.

## Do exactly this, then stop

1. Read `HANDOFF.md`: *Status*, *STOP RULE*, *Canonical metrics*, *Key facts*, *Forward paths*.
2. Run **no** verification battery. Do not run `pytest`, `sha256sum`, artifact counts, or drift checks —
   they cannot change any number below and only create another empty commit.
3. Send the user **one** short message containing:
   - the numbers table below,
   - that a 0.4R target requires a 71.43% pre-cost win rate; both datasets miss it **and** gross P&L is
     negative, so this is not a cost-only failure,
   - that 75 tests pass and no research code/data changed since `a797773`,
   - forward paths (a)/(b)/(c), with one explicit line asking the user to authorize **(a)** or **(c)** to
     stop/reduce the cron, or to state the exact scope of experiment **(b)**.
4. Stop. Make **no commit and no file edits**. If your turn would only produce a commit touching
   `HANDOFF.md` / `INITIAL_TASK_FOR_NEXT_AGENT.md`, produce nothing.

The loop cannot end itself: the `.github/workflows/main.yml` cron resumes a session, and a docs-only
commit is the only "deliverable" available. Only the user can break the cycle by choosing (a)/(b)/(c).
Do not edit that workflow without explicit authorization for that exact change.

## Numbers to report

| Dataset | Trades | Split | Win % | Gross $ | Net $ | Costs $ | PF | Exp/trade | Gross R | Net R |
|---|---|---|---|---|---|---|---|---|---|---|
| axb0306 (MNQ.M26, 2026-01-20..2026-04-15) | 60 | 33L/27S | 70.00 | -7,662.00 | -31,637.98 | 23,975.98 | 0.4917 | -527.30 | -0.0431 | **-0.1773** |
| Kaggle front-month (2022-11-16..2025-11-12) | 688 | 359L/329S | 64.83 | -140,899.00 | -626,525.96 | 485,626.96 | 0.2271 | -910.65 | -0.0684 | **-0.3046** |

`avg_r` in the artifacts is gross/price-based; net R is recomputed from the trade ledgers as net P&L over
realized dollar risk (`contracts x risk_points x $2`). Sizing at $3,000 planned risk with a 0.4xATR stop
implies 29-278 MNQ contracts, so fully-loaded cost drag scales with size and dominates the result. No
trade in either ledger exits via the 15:55 ET flatten, so reported P&L does not depend on any flatten
execution assumption.

## Forward paths (each needs explicit user authorization for that exact scope)

- **(a)** Stop or reduce the maintenance automation (`.github/workflows/main.yml` cron). The only action
  that actually ends the docs-only checkpoint loop.
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
