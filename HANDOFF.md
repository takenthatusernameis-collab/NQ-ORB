# NQ ORB — Durable handoff

## Status: terminal research complete

**Last substantive commit:** **`a797773`** (2026-11-09 05:44Z). Baseline frozen at `5fab764` (2026-10-31); only substantive post-baseline work is separately-versioned 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`). `STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`.

**This session (2026-11-15T01:08Z):** prior durable task ("report terminal state and stop") re-verified and completed at HEAD `10d13d5`. Read-only checks only (no test-suite/hashes/monitor re-run per terminal instruction): tracked tree clean, `STRATEGY_RULES.txt` SHA `6d3258c3…8ad2b1` unchanged, `git diff a797773..HEAD --name-only` limited to `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `research_state/workflow_run_diagnostics.jsonl` (doc/diagnostics only; no code/test/baseline/config/artifact changes; `d7f898e`/`10404c5` are checkpoint commits touching only the two handoff docs). Canonical artifacts present (35 files in `artifacts/`, incl. `metrics_axb0306.json`, `metrics_kaggle.json`). No new evidence or code. Handoff and initial task refreshed.

## Terminal state — read first

**Research task is COMPLETE and terminal. No remaining research work exists.** Frozen MNQ 15-min ORB baseline is final and negative-net on every free dataset available. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`, ~30 sweeps through 2026-11-03): every candidate MNQ 1-min/15-min source is paid, key-gated, daily-only, or NQ rather than MNQ.

**Correct next action: report terminal state and stop.** Do not re-run tests/hashes/monitor checks, do not add handoff-only checkpoint cycles, do not edit `.github/workflows/main.yml`, controller, or automation policy without explicit user authorization.

Legitimate forward paths require explicit user decision:
- (a) stop/reduce maintenance automation (edit cron at `.github/workflows/main.yml:11`, explicit auth required),
- (b) run a separately-versioned experiment (e.g. far-side-of-range stop per `STRATEGY_RULES.txt` §2.1, as `experiment_farside_stop_v1`, with explicit diff from baseline),
- (c) accept baseline as final.

## Repository state (accurate)

- **Frozen baseline**: `STRATEGY_RULES.txt` v1.0 + `config/orb_mnq_15m_showcase.yaml`; last baseline commit `5fab764`. Primary artifacts: `artifacts/metrics_axb0306.json`, `artifacts/metrics_kaggle.json`.
- **Separate 1-minute experiment `orb_mnq_1m_wf_v1`** (commits `ae3c49f`, `a797773`): additive `flatten_fill='open'`; byte-identical to 15m baseline (axb0306 net -$31,637.98; kaggle net -$626,525.96). No trade binds on 15:55 ET flatten. Does not modify frozen baseline.
- **No non-doc commits after `a797773`** (2026-11-09). Newest `research_state/` free-data monitor artifact: `free_data_monitor_20261108T060017Z.json` (2026-11-08). Controller diagnostics `research_state/workflow_run_diagnostics.jsonl` is appended by automation and is non-substantive.

## Evidence (frozen artifacts)

- axb0306 (`artifacts/metrics_axb0306.json`): 42W/18L (70%), 33 long / 27 short, gross -$7,662, net -$31,637.98, costs $23,975.98, PF 0.4917, expectancy -0.0431R, maxDD -$37,491.80.
- Kaggle proxy (`artifacts/metrics_kaggle.json`, 446W/242L, 64.8%, 688 trades 2022-11-16..2025-11-12): gross -$140,899, net -$626,525.96, costs $485,626.96, PF 0.2271, expectancy -0.0684R, Sharpe -1.68 / Sortino -1.04 (daily), worst day -$4,789.80.
- All chronological splits, walk-forward, and all 12 cost-sensitivity combos negative. Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate.

## Test/manifest status

- Full suite last verified 2026-11-15T01:04Z: **75 passed in 0.75s**. CI runs only controller/automation tests, not `tests/orb/`.
- Canonical artifacts: 35 files in `artifacts/` (34 JSON + `README.md`). No `*manifest*` file exists; ignore stale "20/20 manifest" references.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Keep this handoff compact; consolidate rather than append.

(End of file - total 43 lines)