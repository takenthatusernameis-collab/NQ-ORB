# Initial task for next agent

**Session:** 2026-11-13T02:02:17Z (terminal-state sanity check complete)
**HEAD at check start:** `76c681b` (clean `main...origin/main`, workflow checkpoint touching only handoff files). This session updates durable handoff files only.
**Tests:** 2026-11-13T02:02:17Z → **75 passed in 0.89s** (`/tmp/kilo-verify-venv/bin/python -m pytest tests/ -q`). Do not re-run as a loop.
**Frozen baseline:** `STRATEGY_RULES.txt` SHA `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged (v1.0). Research complete/frozen, negative-net (axb0306 -$31,637.98/60/PF 0.492; kaggle -$626,525.96/688/PF 0.227). Free-data ceiling exhausted (`data/FEASIBILITY_REPORT.md`).

## Status
Terminal. **Do not run another maintenance re-verification loop.** No new research evidence possible on current free-data ceiling.

## Next task (default: generic "continue")
1. Read `HANDOFF.md` (**TERMINAL STATE — READ FIRST**) and this file.
2. Confirm tree clean (`git status --short --branch`). Optionally do **one** quick sanity check (tests and/or `STRATEGY_RULES.txt` SHA) — do not repeat/loop.
3. Report terminal state and stop: research complete, baseline final negative-net, free-data search exhausted. State that stopping `.github/workflows/main.yml` (`cron: "*/5 * * * *"`) or changing automation/controller policy requires explicit user authorization; do not touch it without that authorization.

## If explicitly authorized by user
- **Stop automation:** only with explicit authorization, make the exact requested change to `.github/workflows/main.yml`/controller/policy and record it.
- **New research/experiment:** must be separately named/versioned with explicit diff from `STRATEGY_RULES.txt` v1.0, must not overwrite frozen files/artifacts/configs/raw data, free data only, follow `AGENTS.md`. Start from `PROMPT.md` and `data/FEASIBILITY_REPORT.md`.

## Prior task (completed)
Terminal-state sanity check at 2026-11-13T02:02:17Z: inspected handoff/initial-task/strategy/prompt/AGENTS/feasibility; confirmed clean `main...origin/main` (HEAD `76c681b`); verified `STRATEGY_RULES.txt` and key hashes unchanged; ran full tests (**75 passed in 0.89s**). No frozen files modified. Handoff and initial-task refreshed.

**Constraints:** Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No nested/duplicate workflows. Keep session changes to handoff/initial-task files unless explicitly authorized otherwise.