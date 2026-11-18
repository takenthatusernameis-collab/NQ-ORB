# Initial Task for Next Agent

> **Message from prior agent (2026-11-18, HEAD `b89aae14`):**
>
> NQ/MNQ ORB research is **complete and terminal**. I read `HANDOFF.md`, completed the prior task by
> independently recomputing both trade ledgers (all monetary metrics reconcile to the cent), and
> recorded the resulting facts. No code, data, config, artifact, or automation changes.

## Do exactly this (nothing else)

The research question is answered: the frozen MNQ 15-minute ORB baseline is implemented, tested, and
**negative-net on every available free dataset** at full costs. The free-data search is exhausted
(`data/FEASIBILITY_REPORT.md`).

1. Read `HANDOFF.md` -> *Status*, *STOP RULE*, *Key facts*.
2. Report to the user, in one short message and then stop:
   - axb0306 (MNQ.M26, 2026-01-20..2026-04-15): 60 trades (33L/27S), 70.0% win, gross -$7,662.00,
     net -$31,637.98, costs $23,975.98, PF 0.4917, expectancy -$527.30/trade, gross R -0.0431,
     **net R -0.1773**.
   - Kaggle front-month (2022-11-16..2025-11-12): 688 trades (359L/329S), 64.83% win,
     gross -$140,899.00, net -$626,525.96, costs $485,626.96, PF 0.2271, expectancy -$910.65/trade,
     gross R -0.0684, **net R -0.3046**.
   - Pre-cost break-even win rate for a 0.4R target is 71.43%; both datasets miss it, and gross P&L
     is negative as well. 75 tests pass; zero research drift since `a797773`.
3. Present the three forward paths and stop. Do not start any of them without the user explicitly
   selecting one and stating the exact scope.

## Why not "keep working"

Dozens of consecutive commits after `a797773` are docs-only checkpoints that re-verified identical
invariants and produced no new evidence. Another verification pass, another `HANDOFF.md` rewrite, or
another artifact recount adds nothing and only creates an empty commit. `avg_r` and every other
monetary figure have already been independently recomputed from the ledgers this session.

## Forward paths (each requires explicit user authorization for that exact scope)

- **(a)** Stop or reduce the maintenance automation (`.github/workflows/main.yml` cron) - the only
  action that actually ends the docs-only checkpoint loop. Not permitted without explicit approval
  for that exact edit.
- **(b)** Run a separately versioned, named experiment with an explicit diff from the frozen baseline
  (cost-model sensitivity, entry-timing variant, or a pre-registered parameter study). Never mutate
  `STRATEGY_RULES.txt` or existing canonical artifacts, and never tune to improve reported results.
- **(c)** Accept the baseline as final and stop the automation.

If the user supplies new free data or a new scope: audit first (source, license/access, retrieval
time, contract months, timezone, timestamps, gaps, roll rule, adjustment, hashes) before writing or
running any pipeline.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no
  paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with an explicit diff from the
  frozen baseline.
- Do not edit `.github/workflows/main.yml`, the controller, permissions, or automation policy without
  explicit authorization for that exact change.
