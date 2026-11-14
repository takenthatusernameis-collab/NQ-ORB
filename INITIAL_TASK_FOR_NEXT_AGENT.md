# Initial task for next agent

**Session:** 2026-11-14T02:46Z. **Prior agent task:** completed — read durable handoff, confirmed terminal state, updated handoff and this task message. Per the no-repeat rule, did not re-run tests/hashes/monitor checks, did not commit, did not touch automation. **Research status: TERMINAL — complete, frozen baseline final, negative net.**

## Default prompt: "continue" — do this

You are the next Kilo agent for the NQ-ORB repository. Read this file and `HANDOFF.md` first.

**Current state: the research task is COMPLETE and terminal.** The frozen MNQ 15-min ORB baseline (`STRATEGY_RULES.txt` v1.0) is final and negative-net on every free dataset available. The free-source search is exhausted (`data/FEASIBILITY_REPORT.md`, ~30 documented sweeps through 2026-11-03): every candidate MNQ 1-min/15-min source is paid, key-gated, daily-only, or NQ big-contract rather than MNQ. Usable free sources: axb0306 (~3 months, single-contract MNQ.M26, no roll, ends 2026-04-15) and Kaggle front-month (~3 years, unadjusted).

**Do NOT start another maintenance re-verification loop.** Do not re-run the test suite, re-hash the manifest, poll the free-data monitor, add checkpoint commits, or edit `.github/workflows/main.yml` / controller / automation policy. The repo is in a degenerate maintenance loop (`cron: "*/5 * * * *"`; recent history is only `chore(kilo): checkpoint agent session`; last substantive research commit `5fab764`, 2026-10-31).

**Your job is to report the terminal state and stop — unless the user explicitly chooses a forward path.** Concretely:

1. Read `HANDOFF.md` (**TERMINAL STATE — READ FIRST**) and this file.
2. Do not run tests/hashes/monitor checks, do not commit, do not touch automation.
3. Report, concisely:
   - Research complete; frozen baseline final and negative-net; free-data search exhausted.
   - axb0306 (`artifacts/metrics_axb0306_full.json`, identical in `metrics_axb0306.json`): 60 trades, 42W/18L (70%), 33 long / 27 short, gross -$7,662, net **-$31,637.98**, costs $23,975.98, PF 0.4917, max DD $37,491.80, expectancy -0.0431R, avg win +0.3775R / avg loss -1.0245R.
   - Kaggle proxy (`artifacts/metrics_kaggle.json`): 688 trades, 446W/242L (64.8%), 359 long / 329 short, gross -$140,899, net **-$626,525.96**, costs $485,626.96, PF 0.2271, max DD $626,994.56, expectancy -0.0684R / -$910.65 USD, Sharpe -1.68 / Sortino -1.04 (daily), worst day -$4,789.80 (2023-05-12), exposure 8.07%, 2.99 years.
   - Chronological train/val/test: -$448,765.02 / -$66,243.22 / -$111,517.72; 8-window walk-forward (`artifacts/walk_forward.json`) all negative (test PF 0.128–0.447); 12-way cost-sensitivity grid all negative (-$487,098.57..-$808,255.35); signal-close sensitivity all negative. Costs ($2.87/side, 1-tick adverse slippage) dominate; the 0.4R target needs >71.43% pre-cost win rate; observed rates are below that.
   - Maintenance-loop diagnosis; stopping/changing `.github/workflows/main.yml` requires explicit user authorization.
4. Stop. Leave the working tree as-is. If you must touch durable handoff files, consolidate rather than append, and do not commit (the controller owns commits).

## If the user explicitly chooses a forward path

Only act on the option the user names; do not pick one yourself.

- **Stop/reduce automation:** make the exact requested change, record it in `HANDOFF.md`, do nothing else. Editing `.github/workflows/main.yml`, the controller, permissions, or automation policy requires this explicit authorization.
- **New research/experiment:** separately named/versioned with an explicit diff from `STRATEGY_RULES.txt` v1.0; do not overwrite frozen files/configs/raw data/canonical artifacts; free data only; follow `AGENTS.md`, `PROMPT.md`, `data/FEASIBILITY_REPORT.md`. The strongest candidate is the far-side-of-range stop variant explicitly permitted by `STRATEGY_RULES.txt` §2.1 (baseline uses the ATR-multiple stop), runnable on the existing axb0306/Kaggle data as `experiment_farside_stop_v1`.
- **Commit/release/cleanup:** only with explicit authorization; never rewrite Git history to conceal a failure.

## Verified state (as of 2026-11-14T02:46Z)

- `STRATEGY_RULES.txt` v1.0 SHA-256 `6d3258c3...ad2b1` unchanged.
- Canonical artifacts: `artifacts/metrics_axb0306.json`, `artifacts/metrics_axb0306_full.json`, `artifacts/metrics_kaggle.json`, `artifacts/walk_forward.json`, `data/FEASIBILITY_REPORT.md`.
- HEAD at session start: `1e70bbe`. Tests/manifest last independently re-run 2026-11-14T02:43Z (75 passed); not repeated this session per no-repeat rule.

## Constraints

Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No nested/duplicate workflows. Do not add commits without explicit user authorization.

## If the user explicitly chooses a forward path

Only act on the option the user names; do not pick one yourself.

- **Stop/reduce automation:** make the exact requested change, record it in `HANDOFF.md`, do nothing else. Editing `.github/workflows/main.yml`, the controller, permissions, or automation policy requires this explicit authorization.
- **New research/experiment:** separately named/versioned with an explicit diff from `STRATEGY_RULES.txt` v1.0; do not overwrite frozen files/configs/raw data/canonical artifacts; free data only; follow `AGENTS.md`, `PROMPT.md`, `data/FEASIBILITY_REPORT.md`. The strongest candidate is the far-side-of-range stop variant explicitly permitted by `STRATEGY_RULES.txt` §2.1 (baseline uses the ATR-multiple stop), runnable on the existing axb0306/Kaggle data as `experiment_farside_stop_v1`.
- **Commit/release/cleanup:** only with explicit authorization; never rewrite Git history to conceal a failure.

## Verified state (2026-11-14T02:46Z)

- `STRATEGY_RULES.txt` v1.0 SHA-256 `6d3258c3...ad2b1` unchanged.
- Canonical artifacts confirmed: `artifacts/metrics_axb0306.json`, `artifacts/metrics_axb0306_full.json`, `artifacts/metrics_kaggle.json`, `artifacts/walk_forward.json`, `data/FEASIBILITY_REPORT.md`.
- Working tree clean at start; HEAD `1e70bbe`.
- Test suite last run **75 passed in 0.56s** (venv `/home/runner/work/_temp/orbvenv`). CI (`.github/workflows/main.yml:61-62`) only gates the 4 controller/automation test files.
- Manifest last verified 20/20 (2026-11-13T16:50:32Z); not re-hashed this session.

## Constraints

Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No nested/duplicate workflows. Do not add commits without explicit user authorization.

(End of file)
