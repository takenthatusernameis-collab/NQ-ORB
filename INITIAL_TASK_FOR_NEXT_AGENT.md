# Initial task for next agent

**Session:** 2026-11-14T03:47Z (session G). **Prior agent task:** completed. This session read the durable handoff and terminal-state instructions; no research work remained. No tests, hashes, monitor checks, strategy/config/raw-data/artifact changes, automation edits, or commits were made.

## Read first

Read `HANDOFF.md` and `STRATEGY_RULES.txt`, then this file. **Research status: TERMINAL — complete, frozen baseline final, negative net.**

## Do not repeat verification

Do **not** re-run the test suite, re-hash artifacts, poll the free-data monitor, add checkpoint commits, or edit `.github/workflows/main.yml` / controller / automation policy. The repo is in a degenerate maintenance loop (`cron: "*/5 * * * *"`, checkpoint-only recent history, 471 `free_data_monitor_*.json` files). Automation changes require explicit user authorization per `AGENTS.md`.

## Report and stop

Unless the user explicitly selects a forward path, report this terminal state and stop:

- The frozen MNQ 15-minute ORB baseline (`STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`) is final and negative-net on all available free datasets. The free-source search is exhausted (`data/FEASIBILITY_REPORT.md`, ~30 sweeps through 2026-11-03): candidate MNQ 1-minute/15-minute sources are paid, key-gated, daily-only, or NQ rather than MNQ.
- axb0306 (`artifacts/metrics_axb0306_full.json`): 60 trades, 42W/18L (70%), 33 long / 27 short, gross -$7,662, net **-$31,637.98**, costs $23,975.98, PF 0.4917, max DD $37,491.80, expectancy -0.0431R, average win +0.3775R / average loss -1.0245R.
- Kaggle proxy (`artifacts/metrics_kaggle.json`): 688 trades, 446W/242L (64.8%), 359 long / 329 short, gross -$140,899, net **-$626,525.96**, costs $485,626.96, PF 0.2271, max DD $626,994.56, expectancy -0.0684R (-$910.65/trade), Sharpe -1.68 / Sortino -1.04 (daily), worst day -$4,789.80 (2023-05-12), exposure 8.07%, 2.99 years.
- Chronological train/validation/test: -$448,765.02 / -$66,243.22 / -$111,517.72. Eight-window walk-forward (`artifacts/walk_forward.json`): all negative, test PF 0.128-0.447. All 12 cost-sensitivity combinations and signal-close sensitivity are negative. Costs ($2.87/side plus one-tick adverse slippage) dominate; the 0.4R target requires a >71.43% pre-cost win rate, above the observed rates.
- Maintenance-loop diagnosis is recorded in `HANDOFF.md`; stop/reduce automation requires explicit user authorization.

Leave the working tree as-is unless the user explicitly selects a forward path. If durable handoff files are updated, consolidate rather than append; do not commit (controller owns commits).

## Only if the user explicitly chooses a forward path

Act only on the named option; do not select one independently.

- **Stop/reduce automation:** make the exact requested change and record it in `HANDOFF.md`; do nothing else. Explicit authorization is required for `.github/workflows/main.yml`, controller, permissions, or automation-policy changes.
- **New experiment:** separately named/versioned with an explicit diff from `STRATEGY_RULES.txt` v1.0; do not overwrite frozen files/configs/raw data/canonical artifacts; use free data only and follow `AGENTS.md`, `PROMPT.md`, and `data/FEASIBILITY_REPORT.md`. The strongest candidate is the far-side-of-range stop explicitly permitted by `STRATEGY_RULES.txt` §2.1, runnable on the existing axb0306/Kaggle data as `experiment_farside_stop_v1`.
- **Commit/release/cleanup:** only with explicit user authorization; never rewrite Git history to conceal a failure.

## Verified prior state

Prior verification recorded HEAD `35abe2c` with a clean working tree and all canonical artifacts present. Tests last passed 2026-11-14T02:43Z (75 passed in 0.56s, `/home/runner/work/_temp/orbvenv`); manifest last verified 2026-11-13T16:50:32Z (20/20). These were not repeated this session.

## Constraints

Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No nested or duplicate workflows. No commits without explicit user authorization.