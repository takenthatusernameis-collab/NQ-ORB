# Initial task for next agent

**Session:** 2026-11-13T09:57:35Z (this session — read prior agent task from durable handoff, confirmed terminal state, refreshed durable files)
**HEAD:** `631cc6a6` (= origin/main, clean `main...origin/main` at session start). Working tree: only `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` modified (uncommitted) by this session. No research/data/config/artifact changes. **No commit added.**
**STRATEGY_RULES.txt:** SHA `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` verified unchanged.
**Last full sanity check:** 2026-11-13T09:44:56Z — 75 passed (0.91s), 20/20 manifest matched. This session: branch/hash/tree confirmed only (no re-run, to avoid maintenance loop).

## Status: TERMINAL

**Do not run another maintenance re-verification loop.** The research task is COMPLETE and the frozen baseline is final and negative-net:

- axb0306 (2026-01-20..2026-04-15, single-contract MNQ.M26): 60 trades, net **-$31,637.98**, PF 0.492 (`artifacts/metrics_axb0306_full.json`).
- Kaggle front-month (2022-11-16..2025-11-12): 688 trades, net **-$626,525.96**, PF 0.227 (`artifacts/metrics_kaggle.json`).
- Chronological train/val/test splits and date-based walk-forward are all negative net. Costs (commissions + fees $2.87/side, 1-tick adverse slippage) dominate; the 0.4R target needs >71.43% pre-cost win rate and observed rates are below that. Cost-sensitivity grid (slip ×0.5–2.0, cost ×0.8–1.2) stays negative.

The free-data ceiling is exhausted (`data/FEASIBILITY_REPORT.md`): every remaining candidate source is paid, key-gated, daily-only, or NQ (big contract, $20/point), not MNQ. No new research evidence is possible on current free data.

## Next task (default prompt is the generic "continue")

1. Read `HANDOFF.md` (**TERMINAL STATE — READ FIRST**) and this file.
2. Confirm the tree is clean or only contains expected handoff-only working-tree edits (`git status --short --branch`). Optionally do **one** quick sanity check (`STRATEGY_RULES.txt` SHA `6d3258c3…`) — do not repeat/loop.
3. Report the terminal state and stop: research complete, baseline final negative-net, free-data search exhausted.
4. State that stopping `.github/workflows/main.yml` (`cron: "*/5 * * * *"`, spawns a sequential Kilo session every 5 minutes) or changing automation/controller policy requires **explicit user authorization** per `AGENTS.md`; do not touch it without that authorization.
5. **Do not add another `chore(kilo): checkpoint agent session` commit.** History is already bloated with checkpoint/handoff commits. Leave the working tree as-is unless the user explicitly authorizes a commit or an automation change.

## If explicitly authorized by the user

- **Stop automation:** only with explicit authorization, make the exact requested change to `.github/workflows/main.yml`/controller/policy and record it.
- **New research/experiment:** must be separately named/versioned with an explicit diff from `STRATEGY_RULES.txt` v1.0; must not overwrite frozen files/artifacts/configs/raw data; free data only; follow `AGENTS.md`. Start from `PROMPT.md` and `data/FEASIBILITY_REPORT.md`.

## Prior task (completed 2026-11-13T09:56:07Z)

Terminal-state confirmation at HEAD `f90972d` (= origin/main, clean `main...origin/main`, clean working tree at start): read prior agent task from durable handoff; confirmed prior task COMPLETE. Verified `STRATEGY_RULES.txt` SHA `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged. Baseline metrics spot-checked from artifacts (axb0306 net -$31,637.98 PF 0.4917; Kaggle net -$626,525.96 PF 0.2271). No frozen/research files touched, no tests/manifest rerun (avoids maintenance loop; last full 75 passed, 20/20 on 2026-11-13T09:44:56Z), **no commit added**. `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` refreshed in the working tree only, uncommitted.

## Constraints

Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No nested/duplicate workflows. Keep session changes to handoff/initial-task files unless explicitly authorized otherwise. No commits without explicit user authorization. Avoid checkpoint/handoff commit bloat.