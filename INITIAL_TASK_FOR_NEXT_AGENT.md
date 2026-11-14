# Initial task for next agent

**Status:** TERMINAL — research complete; no remaining research work. No action required unless the user explicitly names a forward path (see "Only if user explicitly chooses a forward path" below).

## Required first action

1. Read `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, `PROMPT.md`, and this file.
2. Confirm terminal state using the **robust drift check** in `HANDOFF.md` ("Robust drift anchor"):
   - `git status --porcelain` is empty (clean);
   - `sha256sum STRATEGY_RULES.txt` == `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`;
   - `git log --oneline a797773..HEAD -- src/ config/ scripts/ tests/ raw/ data/ artifacts/` is empty (no new substantive commits since 2026-11-09).
   - Do **not** compare exact HEAD: the controller commits this file after the agent writes it, so the HEAD recorded in `HANDOFF.md` is always one checkpoint behind the real HEAD. A one-commit-ahead HEAD is expected, not drift.
3. Report the terminal state below and stop. Do not re-run tests, re-hash artifacts beyond the drift check, poll the free-data monitor, add another handoff-only checkpoint, or edit `.github/workflows/main.yml` / controller / automation policy without explicit user authorization.

## Terminal summary to report

- Frozen MNQ 15-minute ORB baseline (`STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3…8ad2b1`) is final and negative-net on all available free datasets.
- axb0306 (`artifacts/metrics_axb0306_full.json`): 60 trades, 42W/18L, gross -$7,662, net **-$31,637.98**, costs -$23,975.98, PF 0.4917, expectancy -0.0431R.
- Kaggle proxy (`artifacts/metrics_kaggle.json`): 688 trades, 446W/242L, gross -$140,899, net **-$626,525.96**, costs $485,626.96, PF 0.2271, expectancy -0.0684R.
- Separate 1-minute experiment `orb_mnq_1m_wf_v1` (added 2026-11-09, commits `ae3c49f`/`a797773`) is **byte-identical** to the 15m baseline (no trade binds on the 15:55 flatten) — it corroborates the negative result and does not change the frozen baseline.
- Chronological splits and walk-forward all negative; all 12 cost-sensitivity combos negative. Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate (observed below).
- Free-source search exhausted (`data/FEASIBILITY_REPORT.md`, ~30 sweeps through 2026-11-03): every candidate MNQ 1-min/15-min source is paid, key-gated, daily-only, or NQ rather than MNQ.
- `cron: "*/5 * * * *"` still present at `.github/workflows/main.yml:11`; no free-data monitor artifact after 2026-11-08T06:00:17Z — automation stalled. Stop/reduce only with explicit user authorization.
- Full test suite (last recorded run): **75 passed in 0.63s** (2026-11-14T07:41Z). CI runs only the 4 controller/automation test files, not `tests/orb/`. This session did not re-run tests per "do not repeat maintenance re-verification".
- Last substantive commit `a797773` (2026-11-09); 2,982 checkpoint/diagnostic commits since baseline `5fab764` (2026-10-31). Real HEAD is one checkpoint ahead of the last recorded handoff HEAD (expected). Drift check re-confirmed clean this session (2026-11-14T08:41Z): clean tree, SHA `6d3258c3…8ad2b1`, no non-doc commits since `a797773`; real HEAD `b107004`.

## Only if user explicitly chooses a forward path

Act only on the named option; do not select one independently.

- **Stop/reduce automation:** make the exact requested change (explicit authorization required for workflow/controller/permissions/policy), record it in `HANDOFF.md`, stop.
- **New experiment:** separately named/versioned with explicit diff from `STRATEGY_RULES.txt` v1.0 (e.g. `experiment_farside_stop_v1`, §2.1); do not overwrite frozen files/configs/raw data/canonical artifacts; free data only; report gross vs net, costs, and out-of-sample results.
- **Commit/release/cleanup:** only with explicit user authorization; never rewrite history.

## Constraints

Historical research/simulation only. No broker/live/paper execution, credentials, or paid/proprietary data. Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. No nested/duplicate workflows. Leave the working tree clean of changes except user-requested work; consolidate the handoff if updated; do not commit (the controller owns commits).