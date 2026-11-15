# NQ ORB — Durable handoff

## Status: terminal research complete

**Last substantive commit:** `a797773` (2026-11-09 05:44Z). Baseline frozen at `5fab764`; only substantive post-baseline work is separately-versioned 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`). `STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`.

**This session (2026-11-15T04:39Z):** completed prior durable task ("acknowledge terminal state and stop") as requested. Minimal drift verification only (no tests/diagnostics re-run, per terminal-state instruction): `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; HEAD `acf66f2`, working tree clean and in sync with `origin/main`; `artifacts/` 35 entries; diagnostics 63 entries. Evidence unchanged (axb0306 60 trades, net -$31,637.98; Kaggle 688 trades, net -$626,525.96). No research, code, tests, data, artifacts, or automation-policy edits. Terminal state reconfirmed.

**Churn warning:** `0d9a01a` and `acf66f2` are handoff-only checkpoint commits that only bump the timestamp/HEAD — no research value. The recurring automated cycle is itself the problem. Highest-value user action remains (a) below (edit cron at `.github/workflows/main.yml:11`, explicit auth required). No further handoff-only turns should be generated without that decision.

## Terminal state — read first

**Research task is COMPLETE and terminal. No remaining research work exists.** Frozen MNQ 15-min ORB baseline is final and negative-net on every free dataset available. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`, ~30 sweeps through 2026-11-03): every candidate MNQ 1-min/15-min source is paid, key-gated, daily-only, or NQ rather than MNQ.

**Correct next action: report terminal state and stop.** Do not re-run tests/hashes/monitor checks, do not add handoff-only checkpoint cycles, do not edit `.github/workflows/main.yml`, controller, or automation policy without explicit user authorization.

Recurring handoff-only checkpoint cycles are themselves maintenance churn: repeated "verify terminal state, refresh handoff" turns add no research value. The most useful user decision is (a) below.

Legitimate forward paths require explicit user decision:
- (a) stop/reduce maintenance automation (edit cron at `.github/workflows/main.yml:11`, explicit auth required),
- (b) run a separately-versioned experiment (e.g. far-side-of-range stop per `STRATEGY_RULES.txt` §2.1, as `experiment_farside_stop_v1`, with explicit diff from baseline),
- (c) accept baseline as final.

## Repository state

- **Frozen baseline**: `STRATEGY_RULES.txt` v1.0 + `config/orb_mnq_15m_showcase.yaml`; last baseline commit `5fab764`. Primary artifacts: `artifacts/metrics_axb0306.json`, `artifacts/metrics_kaggle.json`.
- **Separate 1-minute experiment `orb_mnq_1m_wf_v1`** (`ae3c49f`, `a797773`): additive `flatten_fill='open'`; byte-identical to 15m baseline (axb0306 net -$31,637.98; kaggle net -$626,525.96). No trade binds on 15:55 ET flatten. Does not modify frozen baseline.
- **No non-doc commits after `a797773`**. `research_state/workflow_run_diagnostics.jsonl` appended by automation (non-substantive); 63 entries. Commits since `daca6a7` touch only `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`.

## Evidence (frozen artifacts)

- axb0306 (`artifacts/metrics_axb0306.json`): 60 trades, 42W/18L (70%), 33 long / 27 short, gross -$7,662.00, net -$31,637.98, costs $23,975.98, PF 0.4917, expectancy -0.0431R, maxDD -$37,491.80, Sharpe -1.06 / Sortino -0.67 (per-trade), worst day -$3,811.28 (2026-01-27). All 12 cost-sensitivity combos and signal-close sensitivity negative.
- Kaggle proxy (`artifacts/metrics_kaggle.json`, 446W/242L, 64.8%, 688 trades 2022-11-16..2025-11-12): gross -$140,899, net -$626,525.96, costs $485,626.96, PF 0.2271, expectancy -0.0684R, Sharpe -1.68 / Sortino -1.04 (daily), worst day -$4,789.80.
- All chronological splits, walk-forward, and all 12 cost-sensitivity combos negative. Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate.

## Test/manifest status

- Full suite last verified 2026-11-15T01:04Z: **75 passed in 0.75s**. `tests/orb/` last verified 2026-11-15T02:03Z: **30 passed in 0.26s**. CI runs only controller/automation tests, not `tests/orb/`. Not re-run this session (terminal state; no code changed).
- Canonical artifacts: 35 files in `artifacts/` (34 JSON + `README.md`). No `*manifest*` file exists.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Keep this handoff compact.

(End of file - total 43 lines)
