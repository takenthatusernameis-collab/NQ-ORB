# Initial Task for Next Agent — NQ ORB

## Status: prior task COMPLETE — research is terminal; default action is to do nothing

Session 2026-11-14 (latest pass) read the durable handoff and re-confirmed the drift anchor:
`git status --porcelain` empty; `sha256sum STRATEGY_RULES.txt` == `6d3258c3…8ad2b1`; `git log
a797773..HEAD -- src/ config/ scripts/ tests/ raw/ data/ artifacts/` empty. No code, no
experiment, no tests, no workflow edits. Working tree clean.

## Verified state

- HEAD `44d4289` (doc-only controller checkpoint; prior in-session doc refresh `4b060bb`).
- Baseline frozen at `5fab764` (2026-10-31), `STRATEGY_RULES.txt` v1.0 SHA-256 `6d3258c3…8ad2b1`.
- No substantive (non-doc) change since `a797773` (2026-11-09 05:44Z), the 1-minute experiment.
- ~3,030 commits since baseline; all are `chore(kilo)` checkpoint/diagnostics/maintenance or doc-only handoff refreshes.
- Maintenance automation (`cron: */5 * * * *`, `.github/workflows/main.yml:11`) stalled: newest `research_state/` free-data monitor artifact is `free_data_monitor_20261108T060017Z.json` (2026-11-08T06:00:17Z), zero since.

## Frozen results (final, negative-net)

- MNQ 15-min baseline is negative-net on every free dataset available; the free MNQ 1-min/15-min source search is exhausted (`data/FEASIBILITY_REPORT.md`, ~30 sweeps through 2026-11-03).
- axb0306 (NQ 15-min): 60 trades, 42W/18L (70%), net **-$31,637.98**, costs $23,975.98, PF 0.4917, expectancy -0.0431R, maxDD -$37,491.80.
- Kaggle proxy (MNQ 15-min): 688 trades, 446W/242L (64.8%), net **-$626,525.96**, costs $485,626.96, PF 0.2271, expectancy -0.0684R, Sharpe -1.68 / Sortino -1.04 (daily), worst day -$4,789.80.
- 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`): byte-identical to the 15m baseline — no trade binds on the 15:55 ET flatten, so resolution changes nothing.
- All chronological splits, walk-forward folds, and 12 cost-sensitivity combos negative. Driver: $2.87/side + 1-tick adverse slippage; the 0.4R target needs >71.43% pre-cost win rate (not observed).
- Tests: last full suite on record **75 passed in 0.63s** (2026-11-14T07:41Z); not re-run this session. CI runs only the 4 controller/automation test files, not `tests/orb/`.
- No `*manifest*` file exists in the tree; ignore the stale "20/20 manifest" reference.

## Task

**No outstanding research work.** Default action: report the terminal state and await an explicit
user decision. Do not create work, do not re-verify, do not add handoff-only checkpoint cycles,
do not touch automation.

Only act if the user explicitly directs one of:

1. **Stop/reduce maintenance automation** — edit `cron: "*/5 * * * *"` in `.github/workflows/main.yml:11` (requires explicit authorization for that exact change; workflow stalled since 2026-11-08T06:00:17Z).
2. **Run a separately-versioned experiment** — e.g. far-side-of-range stop (`STRATEGY_RULES.txt` §2.1) as `experiment_farside_stop_v1`, with an explicit diff from the frozen baseline, deterministic tests, and chronological splits; then update `HANDOFF.md`.
3. **Accept baseline as final** — archive the project.

## Constraints

- Historical research/simulation only; no broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without the user's explicit authorization for that exact change.
- Do not re-run tests/hashes/drift checks for the sole purpose of another checkpoint; the drift anchor above is sufficient.
- Keep `HANDOFF.md` compact; consolidate rather than append.

(End of file - total 42 lines)