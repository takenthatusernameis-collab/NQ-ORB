# Initial task for next agent

**Session:** 2026-11-13T13:56:13Z (completed prior task: bounded state check; refreshed durable files).
**HEAD:** `90108e0800dd08224ef1afd3fd691755c47069cc` (= origin/main, clean `main...origin/main`). No research/data/config/artifact changes. The `*/5 * * * *` loop remains active and is not stopped without explicit user authorization.
**STRATEGY_RULES.txt:** SHA `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` verified unchanged.
**Last bounded state check:** 2026-11-13T13:56:13Z — clean tree, HEAD == origin/main (`90108e0800dd`), strategy SHA `6d3258c3…`, net values `-$31,637.98` and `-$626,525.96`.

## Status: TERMINAL — research complete, baseline final, loop diagnosed

**Do not run another maintenance re-verification loop.** The research task is COMPLETE and the frozen baseline is final and negative-net:

- axb0306 (2026-01-20..2026-04-15, single-contract MNQ.M26): 60 trades, net **-$31,637.98**, PF 0.4917 (`artifacts/metrics_axb0306_full.json`).
- Kaggle front-month (2022-11-16..2025-11-12): 688 trades, net **-$626,525.96**, PF 0.2271 (`artifacts/metrics_kaggle.json`).
- Chronological train/val/test splits and date-based walk-forward are all negative net. Costs (commissions + fees $2.87/side, 1-tick adverse slippage) dominate; the 0.4R target needs >71.43% pre-cost win rate and observed rates are below that. Cost-sensitivity grid (slip ×0.5–2.0, cost ×0.8–1.2) stays negative.

The free-data ceiling is exhausted (`data/FEASIBILITY_REPORT.md`): every remaining candidate source is paid, key-gated, daily-only, or NQ (big contract, $20/point), not MNQ. No new research evidence is possible on current free data.

## The repo is in a degenerate maintenance loop (evidence)

- 2,504+ commits since 2026-11-01; **2,214+** are `chore(kilo): checkpoint agent session`; **0** are real research commits (last substantive research commits `5fab764`/`ce861a2`, 2026-10-31).
- `.github/workflows/main.yml` runs `cron: "*/5 * * * *"` and spawns a sequential Kilo session each activation with a generic prompt, causing repeated verification. Re-running tests/hashes adds no evidence and only grows the repo.

## Your task (default prompt: "continue")

Do this once, in order, and stop:

1. Read `HANDOFF.md` (**TERMINAL STATE — READ FIRST**) and this file.
2. Run **only** this bounded state check (do **not** run the full suite, manifest recomputation, or free-data monitor):

   ```bash
   git status --short --branch
   git rev-parse HEAD origin/main
   sha256sum STRATEGY_RULES.txt
   python3 -c "import json;[print(f, json.load(open(f))['net_pnl']) for f in ('artifacts/metrics_axb0306_full.json','artifacts/metrics_kaggle.json')]"
   ```

3. If the state matches the record above (clean tree, HEAD == origin/main, strategy SHA `6d3258c3…`, net values `-$31,637.98` and `-$626,525.96`), **report the terminal state and stop**:
   - research complete; frozen baseline final negative-net; free-data search exhausted; loop diagnosed.
   - Do **not** add another `chore(kilo): checkpoint agent session` commit and do **not** re-run tests/hashes/monitor. Leave the working tree as-is.
4. If the state does **not** match (new commits/artifacts/data, changed hashes, or an explicit user request/authorization), stop and report the discrepancy first; do not silently re-verify or overwrite anything.
5. State that stopping `.github/workflows/main.yml` (`cron: "*/5 * * * *"`, spawns a sequential Kilo session every 5 minutes) or changing automation/controller policy requires **explicit user authorization** per `AGENTS.md`; do not touch it without that authorization.

## If the user explicitly authorizes a change

- **Stop automation:** make the exact requested change to `.github/workflows/main.yml`/controller/policy and record it in `HANDOFF.md`. Nothing else.
- **New research/experiment:** must be separately named/versioned with an explicit diff from `STRATEGY_RULES.txt` v1.0; must not overwrite frozen files/artifacts/configs/raw data; free data only; follow `AGENTS.md`. Start from `PROMPT.md` and `data/FEASIBILITY_REPORT.md`.
- **Commit/release/cleanup of the loop bloat:** only with explicit authorization; never rewrite Git history to conceal a failure.

## Prior task (completed 2026-11-13T13:56:13Z)

Read prior durable handoff/task, ran the prescribed bounded state check (clean tree, HEAD == origin/main `90108e0800dd`, strategy SHA `6d3258c3…`, net -$31,637.98 / -$626,525.96) — state matched terminal record. No frozen/research/data/artifact files touched; durable files refreshed only; no commit added.

## Constraints

Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No nested/duplicate workflows. Keep session changes to handoff/initial-task files unless explicitly authorized otherwise. No commits without explicit user authorization. Avoid checkpoint/handoff commit bloat.

(End of file - total 55 lines)