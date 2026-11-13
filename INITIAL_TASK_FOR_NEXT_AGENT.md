# Initial task for next agent

**Session:** 2026-11-13T03:48:10Z (terminal-state sanity check complete)
**HEAD at check start:** `0604410` (clean `main...origin/main`; `0604410` = origin/main, a `chore(kilo): checkpoint agent session` commit on top of `a348c91`). **No commit made this session** — durable handoff files updated in the working tree only, uncommitted, to avoid extending the degenerate maintenance loop.
**Tests:** 2026-11-13T03:48:10Z → **75 passed in 0.58s** (`/tmp/kilo-verify-venv/bin/python -m pytest tests/ -q`). Manifest previously 20/20 matched; frozen files unchanged. Do not re-run these as a loop.
**Frozen baseline:** `STRATEGY_RULES.txt` SHA `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged (v1.0). Research complete/frozen, negative-net (axb0306 -$31,637.98 / 60 trades / PF 0.492; kaggle -$626,525.96 / 688 trades / PF 0.227). Free-data ceiling exhausted (`data/FEASIBILITY_REPORT.md`).

## Status: TERMINAL

**Do not run another maintenance re-verification loop.** No new research evidence is possible on the current free-data ceiling. Every candidate free source has been re-checked exhaustively; all remaining sources are paid, key-gated, daily-only, or NQ (big contract), not MNQ.

## Environment note

The runner has no system `pytest`/`pandas`. If a test run is genuinely needed, use/create venv `/tmp/kilo-verify-venv` (`pip install pytest pandas`); it may need rebuilding on a fresh runner. Tests currently: **75 passed**.

## Next task (default prompt is the generic "continue")

1. Read `HANDOFF.md` (**TERMINAL STATE — READ FIRST**) and this file.
2. Confirm the tree is clean (`git status --short --branch`). Optionally do **one** quick sanity check (tests and/or `STRATEGY_RULES.txt` SHA) — do not repeat/loop.
3. Report the terminal state and stop: research complete, baseline final negative-net, free-data search exhausted.
4. State that stopping `.github/workflows/main.yml` (`cron: "*/5 * * * *"`, spawns a sequential Kilo session every 5 minutes) or changing automation/controller policy requires **explicit user authorization** per `AGENTS.md`; do not touch it without that authorization.
5. **Do not add another `chore(kilo): checkpoint agent session` commit.** History is already bloated with ~1,000+ checkpoint/handoff commits since 2026-11-08. Leave the working tree as-is unless the user explicitly authorizes a commit or an automation change.

## If explicitly authorized by the user

- **Stop automation:** only with explicit authorization, make the exact requested change to `.github/workflows/main.yml`/controller/policy and record it.
- **New research/experiment:** must be separately named/versioned with an explicit diff from `STRATEGY_RULES.txt` v1.0; must not overwrite frozen files/artifacts/configs/raw data; free data only; follow `AGENTS.md`. Start from `PROMPT.md` and `data/FEASIBILITY_REPORT.md`.

## Prior task (completed 2026-11-13T03:48:10Z)

Terminal-state sanity check at HEAD `0604410`: inspected `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `STRATEGY_RULES.txt` (v1.0); confirmed clean `main...origin/main`; verified `STRATEGY_RULES.txt` SHA `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged; ran tests → **75 passed in 0.58s**. No frozen files modified. No new commit added. Handoff and initial-task refreshed.

**Constraints:** Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No nested/duplicate workflows. Keep session changes to handoff/initial-task files unless explicitly authorized otherwise.