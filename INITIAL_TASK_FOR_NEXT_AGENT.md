# Initial task for next agent

**Session:** 2026-11-13T01:04:05Z (maintenance re-verification + loop diagnosis)
**HEAD at verification start:** `6c08091` (clean `main...origin/main` before edits; `git fetch --dry-run` no remote changes, `git diff origin/main --stat` empty). `6c08091` is the workflow's own `chore(kilo): checkpoint agent session` commit (2026-11-13T01:02:57Z) on top of `b93a133`; only `HANDOFF.md` changed, no research/data/config/artifact drift.
**Tests:** 75 passed in 0.88s. Command: `/tmp/kilo-verify-venv/bin/python -m pytest tests/ -q` (venv with `pytest` 9.2.0 + `pandas` 3.1.1).
**SHA-256:** 20/20 manifest hashes matched (recomputed 2026-11-13T01:04:05Z). `STRATEGY_RULES.txt` SHA `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (v1.0, 126 lines — unchanged). `artifacts/metrics_axb0306_full.json` authoritative on-disk hash `dddaefa2aaa23df2f34b10d5dee0220a08d6cfe6e86f9e39a19e6f912ee22f8f` (known historical manifest transcription typo `ddddaefa…` only; unchanged). Monitor file SHA `3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f` unchanged.
**Automation/monitor:** `research_state/free_data_monitor_20261108T060017Z.json` unchanged (`checked_at_utc` 2026-11-08T06:00:17.980919+00:00). `crontab -l` → `no crontab for runner`; `/etc/cron.d/` OS defaults only (e2scrub_all, php, sphinxsearch, sysstat); only `.github/workflows/main.yml`; `ps aux | grep -Ei "orb|free_data_monitor|research"` empty (no duplicate processes).

## Prior task (completed)
Maintenance re-verification completed at 2026-11-13T01:04:05Z: inspected `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `STRATEGY_RULES.txt` (v1.0, 126 lines — unchanged), `PROMPT.md`, `AGENTS.md`, `data/FEASIBILITY_REPORT.md`; confirmed clean `main...origin/main` with no remote diff; ran full tests (**75 passed in 0.88s**); recomputed 20/20 manifest SHA-256 hashes — **20/20 matched** (known `metrics_axb0306_full.json` historical typo only, on-disk authoritative hash unchanged); confirmed monitor state/SHA/`checked_at_utc` unchanged and no duplicate processes. No frozen files modified. **Diagnosed the degenerate maintenance loop** (see below). Handoff-only checkpoint committed on top of HEAD `6c08091`.

## Research status (COMPLETE — frozen, no further work)
- **Strategy**: `STRATEGY_RULES.txt` v1.0 (MNQ 15-min ORB showcase). Baseline results are negative net and must not be presented as profitable: axb0306 net -$31,637.98 (60 trades, PF 0.492); kaggle net -$626,525.96 (688 trades, PF 0.227). Date-based WF OOS tests negative net.
- **Data**: axb0306 MNQ (2026-01-20..2026-04-15, 60 complete days) and kaggle front-month proxy (2022-11-16..2025-11-12, 688 days). 1-min audits in `research_state/1m_audit_{axb0306,kaggle}.json`. Free-data search exhausted (`data/FEASIBILITY_REPORT.md`); 06:00Z monitor stopped.

## Degenerate maintenance loop (READ THIS FIRST)
The repository is stuck in a no-value loop and the next agent must NOT repeat it:
- `.github/workflows/main.yml` runs `cron: "*/5 * * * *"` and spawns a sequential Kilo session each activation.
- Each session performs an identical "maintenance re-verification" (tests + hash manifest + monitor check) and the workflow commits a `chore(kilo): checkpoint agent session` checkpoint.
- Since 2026-11-01 there have been **0 real research commits**. All 1033 commits since 2026-11-08 are checkpoints / re-verifications / diagnostics (924 are `chore(kilo): checkpoint agent session`).
- This consumes the workflow budget, bloats `HANDOFF.md`/git history, and produces no new evidence.

## Next task
**Do NOT run another maintenance re-verification loop.** The research is complete, the baseline is final and negative-net, and the free-data ceiling is documented. The correct behaviour on "continue" is to report the terminal state, not to re-run the same checks.

If you are invoked again with a generic "continue" instruction, do the following and then stop:
1. Read `HANDOFF.md` (especially the **TERMINAL STATE** section) and this file.
2. Confirm the tree is clean (`git status --short --branch`) and, if you wish, do ONE quick sanity check that tests pass (`/tmp/kilo-verify-venv/bin/python -m pytest tests/ -q`) and that `STRATEGY_RULES.txt` is unchanged (SHA `6d3258c3…`). Do not loop on it.
3. Report that the task is complete and the repository is in a terminal state; note the maintenance loop and that stopping the automation requires explicit user authorization.

**If the user explicitly authorizes stopping the automation** (editing `.github/workflows/main.yml`, changing the `*/5` schedule, or adding a terminal no-op), do exactly that and nothing more, then record it. Without that explicit authorization, do not touch `main.yml`, controller code, permissions, or automation policy.

**If the user explicitly asks for NEW research** (a new experiment, new data source, or a strategy variant): it must be a separately named, versioned experiment with an explicit diff from `STRATEGY_RULES.txt` v1.0, must not overwrite frozen files, and must follow `AGENTS.md` guardrails (free data only, no optimization before the untouched baseline is reported, chronological splits, gross+net reporting). Start by re-reading `PROMPT.md` and `data/FEASIBILITY_REPORT.md`.

**Constraints:** Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Do not restart the 06:00Z loop or launch nested/duplicate workflows. Keep session changes to handoff/initial-task files unless explicitly authorized for a separately versioned experiment.

(End of file - total 44 lines)