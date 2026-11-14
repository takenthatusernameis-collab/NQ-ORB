# Initial Task for Next Agent — NQ ORB

## Status: prior task COMPLETE — drift check completed; research terminal; default action is to do nothing

Durable handoff and this file refreshed 2026-11-14T20:16Z. Prior task complete — completed prescribed read-only drift check on arrival: `git status --porcelain` clean; `STRATEGY_RULES.txt` SHA-256 `6d3258c3…8ad2b1`; no non-doc commits since `a797773`; 35 entries (34 JSON + `README.md`) in `artifacts/`; automation still stalled (newest `research_state/` monitor `free_data_monitor_20261108T060017Z.json`). All anchors held → state unchanged. Only docs refreshed this session (HEAD at check `0cdfb78`, chore checkpoint only).

## Last recorded state (verified this session)

- Last substantive (non-doc) commit: `a797773` (2026-11-09 05:44Z).
- Baseline frozen at `5fab764` (2026-10-31).
- 35 entries (34 JSON + `README.md`) in `artifacts/`. Automation stalled / not accumulating (newest `research_state/` monitor `free_data_monitor_20261108T060017Z.json`, 2026-11-08).
- Last recorded test run: **75 passed in 0.94s** (`python -m pytest -q`, 2026-11-14T14:27Z); not re-run. CI runs only 4 controller/automation tests, not `tests/orb/`.

## Frozen results (final, negative-net)

- axb0306 (NQ 15-min): 60 trades, net **-$31,637.98**, PF 0.4917, expectancy -0.0431R.
- Kaggle proxy (MNQ 15-min): 688 trades, net **-$626,525.96**, PF 0.2271, expectancy -0.0684R.
- 1-minute experiment `orb_mnq_1m_wf_v1` byte-identical to 15m. All splits/walk-forward folds and 12 cost combos negative (costs dominate; 0.4R target needs >71.43% pre-cost win rate). Free-source search exhausted (`data/FEASIBILITY_REPORT.md`).

## Task

**No outstanding research work.** Report terminal state and await explicit user direction. Do not re-verify tests/hashes, do not add handoff-only checkpoint cycles, and do not touch automation.

Only act if the user explicitly directs one of:

1. **Stop/reduce maintenance automation** — edit `cron` in `.github/workflows/main.yml:11` (requires explicit authorization).
2. **Run a separately-versioned experiment** — e.g. far-side-of-range stop as `experiment_farside_stop_v1` with explicit diff from baseline, deterministic tests, chronological splits; update `HANDOFF.md`.
3. **Accept baseline as final** — archive the project.

## Constraints

- Historical research/simulation only; no broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization.
- Keep `HANDOFF.md` compact.

(End of file - total 37 lines)