# NQ ORB — Durable handoff

- **HEAD**: `9714643` (`chore(kilo): checkpoint agent session`). Working tree clean at session start; no substantive research commit after `5fab764` (2026-10-31).

## TERMINAL STATE — READ FIRST

**The research task is COMPLETE and terminal. No remaining research work exists.** The frozen MNQ 15-min ORB baseline (`STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`) is final and negative-net on every free dataset available. Free-source search is exhausted: `data/FEASIBILITY_REPORT.md` documents ~30 sweeps through 2026-11-03; every candidate MNQ 1-min/15-min source is paid, key-gated, daily-only, or NQ rather than MNQ.

**This session (2026-11-14, session AE):** read the durable handoff/initial task; performed only the minimal drift check needed to confirm the terminal state — git HEAD/clean tree, `STRATEGY_RULES.txt` SHA-256, and the two key metric files (`metrics_axb0306_full.json`, `metrics_kaggle.json`) all match the quoted frozen figures. No tests, full hash re-runs, monitor checks, or research work performed. No research code, configuration, raw data, canonical artifacts, workflows, controller, or automation policy modified. Terminal conclusion unchanged: report it and stop.

**Correct next action is NOT another re-verification.** Do not re-run tests/hashes/monitor checks, do not add handoff-only checkpoint cycles, and do not edit `.github/workflows/main.yml`, controller, or automation policy without explicit user authorization. Report terminal state and stop. Legitimate forward paths require an explicit user decision: (a) stop/reduce maintenance automation, (b) run a separately-versioned experiment (e.g. far-side-of-range stop variant, `STRATEGY_RULES.txt` §2.1, as `experiment_farside_stop_v1`), or (c) accept the baseline as final.

## Evidence (frozen artifacts; last substantive recheck in session Z)

- `STRATEGY_RULES.txt` SHA-256 = `6d3258c3…8ad2b1` (matches the frozen baseline).
- axb0306 (`artifacts/metrics_axb0306_full.json`): 42W/18L (70%), 33 long / 27 short, gross -$7,662, net -$31,637.98, PF 0.4917, expectancy -0.0431R (costs -$23,975.98 implied by net−gross; 60 trades per `trades_axb0306_full.json`).
- Kaggle proxy (`artifacts/metrics_kaggle.json`, 446W/242L, 64.8%, 688 trades 2022-11-16..2025-11-12): gross -$140,899, net -$626,525.96, costs $485,626.96, PF 0.2271, expectancy -0.0684R, Sharpe -1.68 / Sortino -1.04 (daily), worst day -$4,789.80.
- Chronological splits all negative (train -$448,720.04 / val -$65,094.22 / test negative). Walk-forward all negative (kaggle 8 windows test net -$70,637.24..-$178,375.24; test PF 0.128–0.447). All 12 cost-sensitivity combos negative. Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate; observed below.

## Test/manifest status

- Tests last run: **75 passed in 0.70s** (2026-11-14T05:39Z, session T, fresh venv); later read-only sessions did not re-run them. CI runs only the 4 controller/automation test files, not `tests/orb/`.
- Manifest last verified: 20/20 matched (2026-11-13T16:50:32Z).

## Maintenance-loop observation

- `.github/workflows/main.yml:11` still has `cron: "*/5 * * * *"`; checkpoint-only commits continue through 2026-11-14 (`4ec4315`). `research_state/` newest monitor artifact is 2026-11-08T06:00:17Z; zero artifacts after — automation stalled / not accumulating. Stopping/changing requires explicit user authorization per `AGENTS.md`; none given. Do not touch.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not repeat maintenance re-verification. Report terminal state instead.
- Keep this handoff compact; consolidate rather than append.
