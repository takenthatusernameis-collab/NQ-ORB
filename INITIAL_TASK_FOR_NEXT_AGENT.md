# Initial task for next agent

**Session:** 2026-11-13T23:36:27Z. **Prior agent task:** completed (read durable handoff, verified frozen numbers against on-disk JSON read-only, confirmed clean tree + checkpoint loop, refreshed `HANDOFF.md` + this file). **HEAD at start:** `004224d` (transient due to checkpoint loop). **Research status: TERMINAL — complete, frozen baseline final, negative net.**

## Default prompt: "continue" — do this

1. Read `HANDOFF.md` (**TERMINAL STATE — READ FIRST**) and this file.
2. Do **not** run another maintenance re-verification: no test suite, no manifest re-hash, no free-data monitor poll, no checkpoint commit, no workflow/controller edits.
3. Report the terminal state and stop:
   - Research complete; frozen baseline final and negative-net; free-data search exhausted (`data/FEASIBILITY_REPORT.md`); maintenance loop diagnosed (`.github/workflows/main.yml` cron `*/5 * * * *` → 2,510 commits since 2026-11-01, 2,220 checkpoints, 0 research; last research commit `5fab764`, 2026-10-31).
   - axb0306 (`artifacts/metrics_axb0306_full.json`): 60 trades, 42W/18L (70%), gross -$7,662, net **-$31,637.98**, costs $23,975.98, PF 0.4917, max DD $37,491.80.
   - Kaggle proxy (`artifacts/metrics_kaggle.json`): 688 trades, 446W/242L (64.8%), gross -$140,899, net **-$626,525.96**, costs $485,626.96, PF 0.2271, max DD $626,994.56.
   - Chronological train/val/test: -$448,765.02 / -$66,243.22 / -$111,517.72; 8-window walk-forward (`artifacts/walk_forward.json`) also all negative. Costs (commissions + fees $2.87/side, 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate, observed below that.
4. State that stopping `.github/workflows/main.yml` (`cron: "*/5 * * * *"`) or changing controller/automation policy requires **explicit user authorization** per `AGENTS.md`. Do not touch it without that authorization.
5. Stop. Leave the working tree as-is. If you must touch durable handoff files, consolidate rather than append, and do not commit (the controller owns commits).

## If the user explicitly authorizes a change

- **Stop automation:** make the exact requested change, record it in `HANDOFF.md`, do nothing else.
- **New research/experiment:** separately named/versioned with an explicit diff from `STRATEGY_RULES.txt` v1.0; do not overwrite frozen files/configs/raw data/canonical artifacts; free data only; follow `AGENTS.md`, `PROMPT.md`, `data/FEASIBILITY_REPORT.md`.
- **Commit/release/cleanup:** only with explicit authorization; never rewrite Git history to conceal a failure.

## Verified state (this session)

- Frozen figures re-checked against JSON: `artifacts/metrics_axb0306_full.json`, `artifacts/metrics_kaggle.json` (incl. `chronological_splits`), `artifacts/walk_forward.json` — all match the handoff (axb0306 net -$31,637.98, PF 0.4917; Kaggle net -$626,525.96, PF 0.2271; chronological train/val/test -$448,765.02 / -$66,243.22 / -$111,517.72; 8/8 walk-forward windows negative).
- HEAD at start `b245cf5`; working tree clean and in sync with `origin/main` (0 ahead / 0 behind). Checkpoint loop active (`*/5` cron).
- Last full suite: **75 passed in 0.88s** (2026-11-13T12:48:19Z). Last full 20-file manifest: **20/20 matched** (2026-11-13T16:50:32Z). Not re-run this session. No commit made.

## Constraints

Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No nested/duplicate workflows. Do not add commits without explicit user authorization.