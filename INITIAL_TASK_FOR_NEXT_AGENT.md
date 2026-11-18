# Initial Task for Next Agent

> **Message from prior agent (2026-11-18, HEAD `b809e0e6`):**
>
> NQ/MNQ ORB research remains complete and terminal. I read the durable handoff and completed the
> prior task: reported the terminal state and the three forward paths to the user at HEAD
> `b809e0e6` (no new verification run per loop warning). No research, experiments, or automation
> changes were made. `HANDOFF.md` and this file updated as explicitly requested by the user.
>
> **This is one of many consecutive verification-only checkpoints** (see the preserved HEAD list in
> `HANDOFF.md`). Do not repeat it.

## Your task

**Do not verify or re-check anything. Report and stop.**

The terminal state is already verified and recorded. Running `git status`, `sha256sum`, and
`pytest` again produces no new evidence and only creates another docs-only commit. Unless the user
has selected a forward path or supplied new data/scope, your entire turn is:

1. Read `HANDOFF.md` (Status + Required action sections) and `STRATEGY_RULES.txt` for context.
2. Summarize the result to the user in one short message: frozen MNQ 15-minute ORB baseline is
   implemented, tested, and negative-net on all available free data at full costs (axb0306 60
   trades, net -$31,637.98, PF 0.4917, avg R -0.0431; Kaggle 688 trades, net -$626,525.96,
   PF 0.2271, avg R -0.0684); free-data search exhausted per `data/FEASIBILITY_REPORT.md`.
3. Present the three forward paths (a/b/c below) and stop.
4. Do **not** modify `.github/workflows/main.yml`, the controller, research code, data, configs, or
   artifacts. Do **not** update `HANDOFF.md` or this file unless the user explicitly asks.

## Forward paths (require explicit user authorization)

- **(a)** Stop or reduce maintenance automation (`.github/workflows/main.yml` cron). Requires explicit authorization for that exact edit.
- **(b)** Run a separately versioned, named experiment with an explicit diff from the frozen baseline (cost-model sensitivity, entry-timing variant, or pre-registered parameter study). Never mutate `STRATEGY_RULES.txt` or existing canonical artifacts.
- **(c)** Accept the baseline as final and stop the automation.

If the user supplies new free data or a new scope: audit it first before writing or running any pipeline.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.
