# NQ ORB — Durable handoff

## Status: terminal research complete; awaiting user decision

**Last substantive commit:** `a797773` (2026-11-09 05:44Z). Baseline frozen at `5fab764`; only substantive post-baseline work is separately-versioned 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`). `STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`.

**This session (2026-11-15T07:37Z):** executed the prior agent task, which is terminal (report and stop). Verified: `STRATEGY_RULES.txt` SHA-256 unchanged (`6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`), working tree clean, HEAD `8751652` (only automation checkpoint commits on top of `31b837d`), 35 files in `artifacts/`, canonical metrics unchanged (axb0306 60 trades, 42W/18L, net -$31,637.98, PF 0.4917; Kaggle 688 trades, 446W/242L, net -$626,525.96, PF 0.2271). No research, tests, hashes/monitor checks, free-source sweep, data/artifact change, or automation edit performed. Only `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` updated (doc-only, per explicit user request).

**Prior sessions (2026-11-15T06:46Z, 06:47Z):** re-read handoff, `PROMPT.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `data/FEASIBILITY_REPORT.md`, and both canonical metric artifacts. Re-verified terminal state. No code/data/artifact change.

**Decision required before any further research work:** the user must choose (a) stop/reduce maintenance automation (edit cron at `.github/workflows/main.yml:11`, explicit auth required), (b) authorize a separately-versioned experiment, or (c) accept the baseline as final. Do not add further handoff-only research cycles; avoid repeating free-source sweeps, hashes, monitors, or tests absent a concrete new task.

## Terminal state — read first

**Research task is COMPLETE and terminal. No remaining research work exists.** Frozen MNQ 15-min ORB baseline is final and negative-net on every free dataset available. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`, ~30 sweeps through 2026-11-03): every candidate MNQ 1-min/15-min source is paid, key-gated, daily-only, or NQ rather than MNQ.

**Correct next action: report the terminal state and await an explicit user decision.** Do not start another autonomous research loop, re-run tests/hashes/monitor checks, or edit `.github/workflows/main.yml`, controller, or automation policy without explicit user authorization.

Legitimate forward paths require explicit user decision:
- (a) stop/reduce maintenance automation (edit cron at `.github/workflows/main.yml:11`, explicit auth required),
- (b) run a separately-versioned experiment (e.g. far-side-of-range stop per `STRATEGY_RULES.txt` §2.1, as `experiment_farside_stop_v1`, with explicit diff from baseline),
- (c) accept baseline as final.

## Repository state

- **Frozen baseline**: `STRATEGY_RULES.txt` v1.0 + `config/orb_mnq_15m_showcase.yaml`; last baseline commit `5fab764`. Primary artifacts: `artifacts/metrics_axb0306.json`, `artifacts/metrics_kaggle.json`. `STRATEGY_RULES.txt` SHA-256 re-verified this session: `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`.
- **Separate 1-minute experiment `orb_mnq_1m_wf_v1`** (`ae3c49f`, `a797773`): additive `flatten_fill='open'`; byte-identical to 15m baseline (axb0306 net -$31,637.98; kaggle net -$626,525.96). No trade binds on 15:55 ET flatten. Does not modify frozen baseline.
- **No non-doc commits after `a797773`**. Diagnostics log appended by automation (non-substantive). Recent commits include automation checkpoints and doc-only handoff updates. Current HEAD `8751652` at this session's verification (checkpoint commits only on top of `31b837d`); working tree clean.

## Evidence (frozen artifacts)

- axb0306 (`artifacts/metrics_axb0306.json`): 60 trades, 42W/18L (70%), gross -$7,662.00, net -$31,637.98, costs $23,975.98, PF 0.4917, expectancy -0.0431R, maxDD -$37,491.80, Sharpe -1.06 / Sortino -0.67 (per-trade). All 12 cost-sensitivity combos and signal-close sensitivity negative.
- Kaggle proxy (`artifacts/metrics_kaggle.json`): 688 trades (446W/242L, 64.8%, 2022-11-16..2025-11-12), gross -$140,899.00, net -$626,525.96, costs $485,626.96, PF 0.2271, expectancy -0.0684R, Sharpe -1.68 / Sortino -1.04 (daily).
- All chronological splits, walk-forward, and all 12 cost-sensitivity combos negative. Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate.

## Test/manifest status

- Full suite last verified 2026-11-15T01:04Z: **75 passed in 0.75s**. `tests/orb/` last verified 2026-11-15T02:03Z: **30 passed in 0.26s**. CI runs only controller/automation tests, not `tests/orb/`. Not re-run this session (terminal-state verification only; no code/data/artifact change since `a797773`).
- Canonical artifacts: 35 files in `artifacts/` (34 JSON + `README.md`). No `*manifest*` file exists.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Keep this handoff compact.
