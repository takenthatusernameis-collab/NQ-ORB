# Initial Task for Next Agent — NQ ORB

## Status: prior task COMPLETE — research is terminal; default action is to do nothing

Durable handoff and this file read 2026-11-14T15:37Z. Prior task was complete with no outstanding research work. This session confirmed only the drift anchor (not a maintenance cycle): working tree clean, `STRATEGY_RULES.txt` SHA-256 `6d3258c3…8ad2b1`, and no substantive commits since `a797773`. Tests were NOT re-run this session (anchor unchanged; prior confirmation was **75 passed in 0.94s**). **This remains a terminal handoff.**

## Last verified state

- HEAD at verification: `7669ca7` (checkpoint-only `chore(kilo)`); HEAD advances via checkpoint commits only.
- Baseline frozen at `5fab764` (2026-10-31), `STRATEGY_RULES.txt` v1.0 SHA-256 `6d3258c3…8ad2b1`.
- No substantive (non-doc) change since `a797773` (2026-11-09 05:44Z, 1-minute experiment `orb_mnq_1m_wf_v1`).
- Drift anchor held (2026-11-14T15:37Z): `git status --porcelain` clean; SHA-256 matches; `git log --oneline a797773..HEAD -- src/ config/ scripts/ tests/ raw/ data/ artifacts/` = 0 commits.
- Last full suite run (prior session, anchor unchanged): **75 passed in 0.94s**. 34 JSON artifacts (plus `README.md`) in `artifacts/`.
- Maintenance automation note: `.github/workflows/main.yml:11` has `cron: "*/5 * * * *"` but newest `research_state/` monitor artifact remains `free_data_monitor_20261108T060017Z.json` (2026-11-08T06:00:17Z). Changing automation requires explicit user authorization.

## Frozen results (final, negative-net)

- MNQ 15-min baseline negative-net on every free dataset; free MNQ 1-min/15-min source search exhausted (`data/FEASIBILITY_REPORT.md`).
- axb0306 (NQ 15-min): 60 trades, net **-$31,637.98**, PF 0.4917, expectancy -0.0431R.
- Kaggle proxy (MNQ 15-min): 688 trades, net **-$626,525.96**, PF 0.2271, expectancy -0.0684R.
- 1-minute experiment `orb_mnq_1m_wf_v1` byte-identical to 15m (no trade binds on 15:55 ET flatten).
- All chronological splits, walk-forward folds, and 12 cost-sensitivity combos negative (costs dominate; 0.4R target needs >71.43% pre-cost win rate).

## Task

**No outstanding research work.** Default action: report terminal state and await an explicit user decision. Do not create work, do not re-verify, do not add handoff-only checkpoint cycles, and do not touch automation. Further agent cycles without explicit user direction are out of scope.

Only act if the user explicitly directs one of:

1. **Stop/reduce maintenance automation** — edit `cron: "*/5 * * * *"` in `.github/workflows/main.yml:11` (requires explicit authorization for that exact change).
2. **Run a separately-versioned experiment** — e.g. far-side-of-range stop (`STRATEGY_RULES.txt` §2.1) as `experiment_farside_stop_v1`, with explicit diff from frozen baseline, deterministic tests, and chronological splits; then update `HANDOFF.md`.
3. **Accept baseline as final** — archive the project.

## Constraints

- Historical research/simulation only; no broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization for that exact change.
- Do not re-run tests/hashes/drift checks solely for another checkpoint; the drift anchor is sufficient.
- Keep `HANDOFF.md` compact; consolidate rather than append.

(End of file - total 47 lines)