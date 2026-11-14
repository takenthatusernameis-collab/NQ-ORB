# NQ ORB — Durable handoff

- **HEAD**: `3b02d80` (`chore(kilo): checkpoint agent session`; session Y's handoff-only edit). Working tree clean. Checkpoint commits (`b49b275`, `4ec4315`, `3b02d80`) touch only `HANDOFF.md` / `INITIAL_TASK_FOR_NEXT_AGENT.md`; no substantive research commit since `5fab764` (2026-10-31).
- **Timestamp (UTC)**: 2026-11-14T06:36Z (session Z).

## TERMINAL STATE — READ FIRST

**The research task is COMPLETE and terminal. No remaining research work exists.** The frozen MNQ 15-min ORB baseline (`STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`) is final and negative-net on every free dataset available. Free-source search is exhausted: `data/FEASIBILITY_REPORT.md` documents ~30 sweeps through 2026-11-03; every candidate MNQ 1-min/15-min source is paid, key-gated, daily-only, or NQ rather than MNQ.

**Session Z (2026-11-14T06:36Z):** third consecutive read-only terminal confirmation (sessions X, Y, Z). Read `HANDOFF.md`, `STRATEGY_RULES.txt`, `INITIAL_TASK_FOR_NEXT_AGENT.md`; working tree clean; HEAD `3b02d80` checkpoint touches handoff files only; SHA-256 matches `6d3258c3…8ad2b1`; canonical metrics unchanged (axb0306 net -$31,637.98 / PF 0.4917; Kaggle net -$626,525.96 / PF 0.2271); newest monitor artifact still `free_data_monitor_20261108T060017Z.json` (2026-11-08), stalled. Did NOT re-run tests/hashes/monitor checks; did NOT edit `.github/workflows/main.yml`, controller, automation policy, research code/config/raw data, or canonical artifacts. Updated `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` only. Terminal conclusion unchanged: stop. Repeating the check adds no evidence.

**Correct next action is NOT another re-verification.** Do not re-run tests/hashes/monitor checks, do not add checkpoint commits, do not edit `.github/workflows/main.yml`, controller, or automation policy (requires explicit user authorization per `AGENTS.md`; none given). Report terminal state and stop. Legitimate forward paths require an explicit user decision: (a) stop/reduce maintenance automation, (b) run a separately-versioned experiment (e.g. far-side-of-range stop variant, `STRATEGY_RULES.txt` §2.1, as `experiment_farside_stop_v1`), or (c) accept baseline as final.

## Evidence (from frozen artifacts; re-confirmed session Y)

- `STRATEGY_RULES.txt` SHA-256 = `6d3258c3…8ad2b1` (matches).
- axb0306 (`artifacts/metrics_axb0306_full.json`): 42W/18L (70%), 33 long / 27 short, gross -$7,662, net -$31,637.98, PF 0.4917, expectancy -0.0431R (costs -$23,975.98 implied by net−gross; 60 trades per `trades_axb0306_full.json`).
- Kaggle proxy (`artifacts/metrics_kaggle.json`, 446W/242L, 64.8%, 688 trades 2022-11-16..2025-11-12): gross -$140,899, net -$626,525.96, costs $485,626.96, PF 0.2271, expectancy -0.0684R, Sharpe -1.68 / Sortino -1.04 (daily), worst day -$4,789.80.
- Chronological splits all negative (train -$448,720.04 / val -$65,094.22 / test negative). Walk-forward all negative (kaggle 8 windows test net -$70,637.24..-$178,375.24; test PF 0.128–0.447). All 12 cost-sensitivity combos negative. Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate; observed below.

## Test/manifest status

- Tests last run: **75 passed in 0.70s** (2026-11-14T05:39Z, session T, fresh venv). CI only runs the 4 controller/automation test files, not `tests/orb/`. Sessions X and Y did not re-run tests (read-only terminal confirmation).
- Manifest last verified: 20/20 matched (2026-11-13T16:50:32Z).

## Maintenance-loop observation

- `.github/workflows/main.yml:11` still has `cron: "*/5 * * * *"`; checkpoint-only commits continue through 2026-11-14 (`4ec4315`). `research_state/` newest monitor artifact is 2026-11-08T06:00:17Z; zero artifacts after — automation stalled / not accumulating. Stopping/changing requires explicit user authorization per `AGENTS.md`; none given. Do not touch.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not repeat maintenance re-verification. Report terminal state instead.
- Keep this handoff compact; consolidate rather than append.

(End of file - total 37 lines)