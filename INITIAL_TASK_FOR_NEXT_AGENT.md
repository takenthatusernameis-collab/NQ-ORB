# Initial Task for Next Agent

> **Message from prior agent (2026-11-18, HEAD `7b49a455`):**
>
> NQ/MNQ ORB research is **complete and terminal**. The prior-agent task was carried out: state
> re-verified at `7b49a455` (75 tests pass, no research drift since `a797773`, working tree clean).
> No code, data, config, artifact, or automation changes were made.

## Do exactly this — and nothing else

1. Read `HANDOFF.md`: *Status*, *STOP RULE*, *Key facts*, *Forward paths*.
2. Send the user **one** short message with the numbers below, list forward paths (a)/(b)/(c), and stop.
3. Do **not** re-run verification, rewrite `HANDOFF.md`, rewrite this file, recount artifacts, or make a
   new commit. If your turn produces only a commit touching these two files, you have added nothing.

## Numbers to report

| Dataset | Trades | Split | Win % | Gross $ | Net $ | Costs $ | PF | Exp/trade | Gross R | Net R |
|---|---|---|---|---|---|---|---|---|---|---|
| axb0306 (MNQ.M26, 2026-01-20..2026-04-15) | 60 | 33L/27S | 70.00 | -7,662.00 | -31,637.98 | 23,975.98 | 0.4917 | -527.30 | -0.0431 | **-0.1773** |
| Kaggle front-month (2022-11-16..2025-11-12) | 688 | 359L/329S | 64.83 | -140,899.00 | -626,525.96 | 485,626.96 | 0.2271 | -910.65 | -0.0684 | **-0.3046** |

Also state: a 0.4R target needs a 71.43% pre-cost win rate; both datasets miss it and gross P&L is
negative too, so costs are not the only cause. Free-data search is exhausted (`data/FEASIBILITY_REPORT.md`).
75 tests pass.

## Forward paths (each requires explicit user authorization for that exact scope)

- **(a)** Stop or reduce the maintenance automation (`.github/workflows/main.yml` cron). This is the only
  action that actually ends the docs-only checkpoint loop. Not permitted without explicit approval for
  that exact edit.
- **(b)** Run a separately versioned, named experiment with an explicit diff from the frozen baseline
  (cost-model sensitivity, entry-timing variant, or a pre-registered parameter study). Never mutate
  `STRATEGY_RULES.txt` or existing canonical artifacts, and never tune to improve reported results.
- **(c)** Accept the baseline as final and stop the automation.

If the user supplies new free data or a new scope: audit first (source, license/access, retrieval time,
contract months, timezone, timestamps, gaps, roll rule, adjustment, hashes) before writing or running
any pipeline.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with an explicit diff from the frozen baseline.
- Do not edit `.github/workflows/main.yml`, the controller, permissions, or automation policy without
  explicit authorization for that exact change.
