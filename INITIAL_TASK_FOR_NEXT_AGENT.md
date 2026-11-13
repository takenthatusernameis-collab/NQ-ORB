# Initial task for next agent

**Session:** 2026-11-13T11:46:54Z (this session — read prior durable handoff/task, completed as terminal-state confirmation, refreshed durable files)
**HEAD:** `2789f5c` (= origin/main, clean `main...origin/main` at start; working tree has only `HANDOFF.md`/`INITIAL_TASK_FOR_NEXT_AGENT.md` refreshed at end). No research/data/config/artifact changes. **No commit added.**
**STRATEGY_RULES.txt:** SHA `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` verified unchanged.
**Last full sanity check:** 2026-11-13T11:01:40Z — **75 passed in 1.02s** (`/tmp/kilo-verify-venv/bin/python -m pytest tests/ -q`), 20/20 manifest hashes matched. This session did not repeat the full suite/manifest (nothing research-related changed).

## Status: TERMINAL — research complete, baseline final, loop diagnosed

**Do not run another maintenance re-verification loop.** The research task is COMPLETE and the frozen baseline is final and negative-net:

- axb0306 (2026-01-20..2026-04-15, single-contract MNQ.M26): 60 trades, net **-$31,637.98**, PF 0.4917 (`artifacts/metrics_axb0306_full.json`).
- Kaggle front-month (2022-11-16..2025-11-12): 688 trades, net **-$626,525.96**, PF 0.2271 (`artifacts/metrics_kaggle.json`).
- Chronological train/val/test splits and date-based walk-forward are all negative net. Costs (commissions + fees $2.87/side, 1-tick adverse slippage) dominate; the 0.4R target needs >71.43% pre-cost win rate and observed rates are below that. Cost-sensitivity grid (slip ×0.5–2.0, cost ×0.8–1.2) stays negative.

The free-data ceiling is exhausted (`data/FEASIBILITY_REPORT.md`): every remaining candidate source is paid, key-gated, daily-only, or NQ (big contract, $20/point), not MNQ. No new research evidence is possible on current free data.

## The repo is in a degenerate maintenance loop (evidence, 2026-11-13T11:45:14Z)

- 2,501 commits since 2026-11-01; **2,210** are `chore(kilo): checkpoint agent session`; **0** are real research commits (last substantive research commits `5fab764`/`ce861a2`, 2026-10-31). No commit since 2026-11-01 touches `.github/`.
- The workflow `.github/workflows/main.yml` runs `cron: "*/5 * * * *"` and spawns a sequential Kilo session each activation with the generic prompt "Read the prior agent task from the durable handoff and complete it." That prompt is what causes every session to repeat the same verification.
- Re-running tests/hashes every few minutes adds no evidence and only grows the repo.

## Next task (default prompt: "continue")

1. Read `HANDOFF.md` (**TERMINAL STATE — READ FIRST**) and this file.
2. Confirm state is clean/expected (`git status --short --branch`) and `STRATEGY_RULES.txt` SHA `6d3258c3…` unchanged.
3. Report the terminal state and stop: research complete, baseline final negative-net, free-data search exhausted, loop diagnosed.
4. State that stopping `.github/workflows/main.yml` (`cron: "*/5 * * * *"`, spawns a sequential Kilo session every 5 minutes) or changing automation/controller policy requires **explicit user authorization** per `AGENTS.md`; do not touch it without that authorization.
5. **Do not add another `chore(kilo): checkpoint agent session` commit** and do not re-run the full suite/manifest unless something changed. History is already bloated. Leave the working tree as-is unless the user explicitly authorizes a commit or an automation change.

## If explicitly authorized by the user

- **Stop automation:** only with explicit authorization, make the exact requested change to `.github/workflows/main.yml`/controller/policy and record it.
- **New research/experiment:** must be separately named/versioned with an explicit diff from `STRATEGY_RULES.txt` v1.0; must not overwrite frozen files/artifacts/configs/raw data; free data only; follow `AGENTS.md`. Start from `PROMPT.md` and `data/FEASIBILITY_REPORT.md`.

## Prior task (completed 2026-11-13T11:46:54Z)

Terminal-state confirmation at HEAD `2789f5c` (= origin/main, clean `main...origin/main`, working tree clean at start): read the prior durable handoff/task and completed it. Per "do not repeat maintenance re-verification" directive, full suite/manifest not re-run; verified clean branch/tree, `STRATEGY_RULES.txt` SHA unchanged, and canonical metrics (axb0306 net -$31,637.98 PF 0.4917; Kaggle net -$626,525.96 PF 0.2271). No frozen/research/data/artifact files touched; **no commit added**. Durable files refreshed in working tree only.

## Constraints

Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No nested/duplicate workflows. Keep session changes to handoff/initial-task files unless explicitly authorized otherwise. No commits without explicit user authorization. Avoid checkpoint/handoff commit bloat.