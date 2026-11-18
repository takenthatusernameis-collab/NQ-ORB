# Initial Task for Next Agent

> **Message from prior agent (2026-11-18, HEAD `ec839648`):**
>
> NQ/MNQ ORB research is complete and terminal. I read the durable handoff, completed the prior
> task (reported the terminal state and the three forward paths to the user), then consolidated
> `HANDOFF.md` and rewrote this file. No research, data, config, artifact, or automation changes.
>
> **Stop the checkpoint cycle.** There are already dozens of consecutive docs-only checkpoint
> commits that each re-verified identical invariants. Another one adds zero evidence.

## Your task

**Report and stop. Do not verify, do not rewrite documentation.**

The terminal state is recorded and verified in `HANDOFF.md`. Re-running `git status`, `sha256sum`,
`pytest`, or artifact counts produces no new evidence and only creates another empty commit. Do not
update `HANDOFF.md` or this file again either — treat the current revision as final.

Unless the user has selected a forward path or supplied new data/scope, your entire turn is:

1. Read `HANDOFF.md` (Status, STOP RULE, Verified state) for context.
2. Report the result to the user in one short message: the frozen MNQ 15-minute ORB baseline is
   implemented, tested, and negative-net on all available free data at full costs.
   - axb0306 (MNQ.M26, 2026-01-20..2026-04-15): 60 trades, gross -$7,662.00, net -$31,637.98,
     PF 0.4917, avg R -0.0431.
   - Kaggle front-month (2022-11-16..2025-11-12): 688 trades, gross -$140,899.00,
     net -$626,525.96, PF 0.2271, avg R -0.0684.
   - Free-data search exhausted per `data/FEASIBILITY_REPORT.md`; 75 tests passing; zero research
     drift since `a797773`.
3. Present the three forward paths and stop.
4. Do **not** modify `.github/workflows/main.yml`, the controller, research code, data, configs, or
   artifacts. Do **not** touch `HANDOFF.md` or this file.

## Forward paths (require explicit user authorization for that exact scope)

- **(a)** Stop or reduce the maintenance automation (`.github/workflows/main.yml` cron) — the only
  action that actually ends the docs-only checkpoint loop.
- **(b)** Run a separately versioned, named experiment with an explicit diff from the frozen baseline
  (cost-model sensitivity, entry-timing variant, or a pre-registered parameter study). Never mutate
  `STRATEGY_RULES.txt` or existing canonical artifacts.
- **(c)** Accept the baseline as final and stop the automation.

If the user supplies new free data or a new scope: audit it first before writing or running any
pipeline (source, license/access, retrieval time, contract months, timezone, timestamps, gaps, roll
rule, hashes).

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no
  paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with an explicit diff from the
  baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without
  explicit authorization for that exact change.
