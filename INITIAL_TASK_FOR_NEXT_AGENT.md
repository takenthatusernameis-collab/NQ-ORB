# Initial task for next agent

**Session:** 2026-11-13T21:00:11Z. **Prior agent task:** completed (terminal-state report + durable-file refresh). **HEAD:** `1236eda` (= origin/main, clean). **Research status: TERMINAL — complete, frozen baseline final.**

## Do this (default prompt: "continue")

1. Read `HANDOFF.md` (**TERMINAL STATE — READ FIRST**) and this file.
2. Do **not** run another maintenance re-verification. Do not run the test suite, re-hash the manifest, poll the free-data monitor, or add a checkpoint commit.
3. Report the terminal state and stop:
   - Research complete; frozen baseline final and negative-net; free-data search exhausted; maintenance loop diagnosed.
   - axb0306: 60 trades, 42W/18L, gross -$7,662, net **-$31,637.98**, PF 0.4917.
   - Kaggle front-month proxy: 688 trades, 446W/242L, gross -$140,899, net **-$626,525.96**, PF 0.2271.
   - Chronological train/val/test and date-based walk-forward splits all negative net. Costs (commissions + fees $2.87/side, 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate, observed below that.
4. State that stopping `.github/workflows/main.yml` (`cron: "*/5 * * * *"`) or changing controller/automation policy requires **explicit user authorization** per `AGENTS.md`. Do not touch it without that authorization.
5. Stop. Leave the working tree as-is. If you must touch durable handoff files, consolidate rather than append, and do not commit.

## If the user explicitly authorizes a change

- **Stop automation:** make the exact requested change, record it in `HANDOFF.md`, and do nothing else.
- **New research/experiment:** separately named/versioned with explicit diff from `STRATEGY_RULES.txt` v1.0; do not overwrite frozen files/configs/raw data/canonical artifacts; free data only; follow `AGENTS.md`, `PROMPT.md`, `data/FEASIBILITY_REPORT.md`.
- **Commit/release/cleanup:** only with explicit authorization; never rewrite Git history to conceal a failure.

## Verified state (this session)

- Strategy SHA-256: `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (unchanged).
- Frozen metric hashes: `dddaefa2…` (`metrics_axb0306_full.json`), `a6ae1006…` (`metrics_kaggle.json`).
- Since 2026-11-01T00:00:00Z: **2,698 commits**, **2,397** exact `chore(kilo): checkpoint agent session`, **2,431** `chore(kilo)`-prefixed; **0** real research commits.
- Last full suite: **75 passed in 0.88s** (2026-11-13T12:48:19Z). Last full 20-file manifest: **20/20 matched** (2026-11-13T16:50:32Z). Not re-run this session.

## Constraints

Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No nested/duplicate workflows. Do not add commits without explicit user authorization.