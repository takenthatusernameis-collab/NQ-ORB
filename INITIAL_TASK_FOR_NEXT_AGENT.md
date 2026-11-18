# Initial Task for Next Agent

> **Final message from prior agent (2026-11-18, HEAD `838f8c03`).** Research is complete under the
> current scope. Do not create another docs-only checkpoint commit.

## One-line task

**Send the user one short decision request (state, numbers table, forward paths) and stop. Make no file
edits and no commit.**

## Situation

The frozen MNQ 15-minute ORB baseline is implemented, tested (**75 passing tests**), and evaluated on
both available free MNQ datasets. It loses money **gross and net** on both, and the free-source search
is exhausted (`data/FEASIBILITY_REPORT.md`). Since the last substantive research commit `a797773`,
every change has been documentation-only:
`git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` → **0 files**.
There is nothing left to implement, verify, or search.

## Do exactly this

1. Read `HANDOFF.md` — *Status*, *STOP RULE*, *Canonical metrics*, *Key facts*, *Forward paths*. Both
   handoff files are **final**; treat them as read-only.
2. Run **no** verification battery (no `pytest`, `sha256sum`, artifact counts, drift checks). They cannot
   change any number and only produce another empty commit.
3. Send the user **one** message containing the table below and this decision request:
   - The 0.4R target needs a 71.43% pre-cost win rate. Observed win rates are 70.00% and 64.83% **and
     gross P&L is negative**, so this is not a cost-only failure.
   - "Please authorize one of: **(a)** stop/reduce the `.github/workflows/main.yml` cron (the only action
     that ends this loop), **(b)** a named, versioned experiment with an explicit diff from the frozen
     baseline — say which one — or **(c)** accept the baseline as final and stop the automation."
4. Stop. Do **not** edit `HANDOFF.md` or this file, and do **not** commit. If no new authorization or
   data arrives, the correct output is one message and nothing else.

The loop cannot end itself: the workflow cron resumes a session, and a docs-only commit is the only
"deliverable" available. Only the user can break the cycle. Never edit `.github/workflows/main.yml` or
the controller without explicit authorization for that exact change.

## Numbers to report

| Dataset | Trades | Split | Win % | Gross $ | Net $ | Costs $ | PF | Exp/trade | Gross R | Net R |
|---|---|---|---|---|---|---|---|---|---|---|
| axb0306 (MNQ.M26, 2026-01-20..2026-04-15) | 60 | 33L/27S | 70.00 | -7,662.00 | -31,637.98 | 23,975.98 | 0.4917 | -527.30 | -0.043 | **-0.18** |
| Kaggle front-month (2022-11-16..2025-11-12) | 688 | 359L/329S | 64.83 | -140,899.00 | -626,525.96 | 485,626.96 | 0.2271 | -910.65 | -0.068 | **-0.30** |

`avg_r` in the artifacts is gross and price-based. Net R is net P&L over realized dollar risk
(`contracts x risk_points x $2`), recomputed from the trade ledgers: portfolio-weighted
-0.1771 / -0.3049, mean per-trade -0.1773 / -0.3046 — both round to the quoted -0.18 / -0.30. Sizing at
$3,000 planned risk with a 0.4xATR stop produces 29-278 MNQ contracts, so commission/fee/slippage drag
scales with size and dominates. No trade exits via the 15:55 ET flatten, so reported P&L does not depend
on any flatten execution assumption. Max drawdown is $37,491.80 (axb0306) and $626,994.56 (kaggle).

## Forward paths (each needs explicit user authorization for that exact scope)

- **(a)** Stop or reduce the maintenance automation (`.github/workflows/main.yml` cron).
- **(b)** A separately versioned, named experiment with an explicit diff from the frozen baseline
  (cost-model sensitivity, entry-timing variant, or a pre-registered parameter study). Never mutate
  `STRATEGY_RULES.txt` or canonical artifacts, and never tune to improve reported results.
- **(c)** Accept the baseline as final and stop the automation.

If the user supplies new free data or a new scope: audit first (source, license/access, retrieval time,
contract months, timezone, timestamps, gaps, roll rule, adjustment, hashes) before writing any pipeline.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with an explicit diff from the baseline.
- Do not delete research evidence or rewrite Git history to conceal a failure.

## Verification commands (only for a later authorized research session — not for another checkpoint)

```bash
git status --short && git rev-parse --short HEAD
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
sha256sum STRATEGY_RULES.txt raw/MNQ_15min.csv raw/MNQ_1min.csv raw/MNQ_15min_frontmonth.csv raw/MNQ_1min_frontmonth.csv
python3 -m pytest tests -q
python3 src/orb/runner.py --prefix <new> --source axb0306   # compare to artifacts/metrics_axb0306.json
python3 src/orb/runner.py --prefix <new> --source kaggle    # compare to artifacts/metrics_kaggle.json
```
