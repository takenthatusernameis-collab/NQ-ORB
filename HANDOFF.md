# NQ ORB — Durable handoff

- **HEAD:** `20425c6` (2026-11-14; `chore(kilo)` checkpoint). Baseline frozen at `5fab764` (2026-10-31); only substantive post-baseline work is separately-versioned 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`). Use the robust drift anchor below, not exact HEAD.

## TERMINAL STATE — READ FIRST

**Research task is COMPLETE and terminal. No remaining research work exists.** Frozen MNQ 15-min ORB baseline (`STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`) is final and negative-net on every free dataset available. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`, ~30 sweeps through 2026-11-03): every candidate MNQ 1-min/15-min source is paid, key-gated, daily-only, or NQ rather than MNQ.

**This session (2026-11-14T13:31Z):** read prior durable handoff and confirmed terminal state — `git status --porcelain` clean (no tracked/untracked changes), `sha256sum STRATEGY_RULES.txt` == `6d3258c3…8ad2b1`, `git log --oneline a797773..HEAD -- src/ config/ scripts/ tests/ raw/ data/ artifacts/` = 0 commits. No new code/experiment, no tests re-run, no workflow edits. HEAD advanced only via `chore(kilo)` checkpoint commits; state unchanged.

**Correct next action is NOT re-verification.** Do not re-run tests/hashes/monitor checks, do not add handoff-only checkpoint cycles, and do not edit `.github/workflows/main.yml`, controller, or automation policy without explicit user authorization. Report terminal state and stop. Legitimate forward paths require explicit user decision: (a) stop/reduce maintenance automation, (b) run a separately-versioned experiment (e.g. far-side-of-range stop, `STRATEGY_RULES.txt` §2.1, as `experiment_farside_stop_v1`), or (c) accept baseline as final.

## Repository state (accurate)

- **Frozen baseline**: `STRATEGY_RULES.txt` v1.0 + `config/orb_mnq_15m_showcase.yaml`; last baseline commit `5fab764` (2026-10-31). Primary artifacts: `metrics_axb0306_full.json`, `metrics_kaggle.json`.
- **Separate 1-minute experiment `orb_mnq_1m_wf_v1`** (added 2026-11-09, commits `ae3c49f` and `a797773`): new `config/orb_mnq_1m_wf_v1.yaml`, YAML loader `src/orb/config.py`, additive `flatten_fill='open'` (default preserves baseline), plus 1m artifacts `metrics_audit1m.json` / `metrics_kaggle1m.json`. It does **not** modify the frozen baseline. Result: **byte-identical** to the 15m baseline (axb0306 60 trades net -$31,637.98; kaggle 688 trades net -$626,525.96). No trade binds on 15:55 ET flatten, so 1-minute resolution changes nothing.
- **No non-doc commits after `a797773`** (2026-11-09 05:44Z). Subsequent commits are all `chore(kilo)` checkpoint/maintenance and doc-only.

## Evidence (frozen artifacts)

- axb0306 (`artifacts/metrics_axb0306_full.json`): 42W/18L (70%), 33 long / 27 short, gross -$7,662, net -$31,637.98, costs $23,975.98, PF 0.4917, expectancy -0.0431R, maxDD -$37,491.80.
- Kaggle proxy (`artifacts/metrics_kaggle.json`, 446W/242L, 64.8%, 688 trades 2022-11-16..2025-11-12): gross -$140,899, net -$626,525.96, costs $485,626.96, PF 0.2271, expectancy -0.0684R, Sharpe -1.68 / Sortino -1.04 (daily), worst day -$4,789.80.
- Chronological splits all negative; walk-forward all negative; all 12 cost-sensitivity combos negative. Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate (observed below).

## Test/manifest status

- Last full suite result on record: **75 passed in 0.63s** (2026-11-14T07:41Z). CI runs only the 4 controller/automation test files, not `tests/orb/`. Not re-run this session.
- No `*manifest*` file exists in the tree; ignore stale "20/20 manifest" references.

## Maintenance-loop observation

- `.github/workflows/main.yml:11` still has `cron: "*/5 * * * *"`; ~3,041 checkpoint/diagnostic/doc commits since baseline. Newest `research_state/` free-data monitor artifact is still `free_data_monitor_20261108T060017Z.json` (2026-11-08T06:00:17Z); none after — automation stalled / not accumulating. Stopping/changing requires explicit user authorization per `AGENTS.md`; none given. Do not touch.

## Robust drift anchor (use this, not exact HEAD)

- Last substantive (non-doc) commit: **`a797773`** (2026-11-09 05:44Z).
- Verify: `git status --porcelain` (clean, aside from intentional doc edits in-session); `sha256sum STRATEGY_RULES.txt` == `6d3258c3…8ad2b1`; `git log --oneline a797773..HEAD -- src/ config/ scripts/ tests/ raw/ data/ artifacts/` (empty). If all hold, state is unchanged — report terminal and stop.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not repeat maintenance re-verification. Report terminal state instead.
- Keep this handoff compact; consolidate rather than append.

(End of file)
