# NQ ORB — Durable handoff

## Status: terminal research complete; awaiting user decision

**This session (2026-11-15T18:33Z):** Completed prior task per explicit user request: verified terminal state and refreshed durable handoff + next-agent task. Verified: `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` empty; `artifacts/` has 35 files and no `*manifest*`; canonical metrics unchanged (axb0306 60 trades 33L/27S, 42W/18L 70.0%, gross -$7,662.00, net -$31,637.98, costs $23,975.98, PF 0.4917, avg R -0.0431, maxDD $37,491.80, Sharpe -1.06 / Sortino -0.67; Kaggle 688 trades 359L/329S, 446W/242L 64.8%, gross -$140,899.00, net -$626,525.96, costs $485,626.96, PF 0.2271, avg R -0.0684, maxDD $626,994.56, Sharpe -1.68 / Sortino -1.04). HEAD at verification start was `ab1a47a` (checkpoint on `main`, 0/0 vs `origin/main`); since `a797773` only `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, and `research_state/workflow_run_diagnostics.jsonl` differ. No research/data/test/automation changes. State unchanged and terminal; forward paths (a)/(b)/(c) gated on explicit user decision.

**Prior session (2026-11-15T17:46Z):** Read prior durable handoff/task (`HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, canonical artifacts `artifacts/metrics_axb0306.json` and `artifacts/metrics_kaggle.json`). Explicit user request was to refresh the handoff and write the next-agent task; no research authorized or performed. Independently re-verified terminal state. HEAD was `5df6b25` (doc-only "refresh terminal-state handoff", child of checkpoint `4218cc1`); `main` 0/0 vs `origin/main` (same hash), clean tree. `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (unchanged); `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` empty; `a797773` confirmed ancestor of HEAD; 35 files in `artifacts/`, no `*manifest*`; canonical metrics unchanged (same values as above). Since `a797773` only `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, and `research_state/workflow_run_diagnostics.jsonl` changed. No research/data/test/automation change. Research remains terminal; forward paths (a)/(b)/(c) gated on explicit user decision.

**Prior session (2026-11-15T17:35Z):** same terminal-state verification and doc refresh (HEAD then `ed8f7b3`).

## Baseline

`STRATEGY_RULES.txt` v1.0 frozen, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`. Frozen baseline commit `5fab764`; last substantive research commit `a797773` (1-minute experiment `orb_mnq_1m_wf_v1`, `ae3c49f`/`a797773`, additive `flatten_fill='open'`, byte-identical to 15m baseline). No strategy/config/raw-data/canonical-artifact changes.

## Terminal state — read first

**Research task is COMPLETE and terminal. No remaining research work is authorized.** Frozen MNQ 15-min ORB baseline is final and negative-net on every available free dataset. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`, ~30 sweeps through 2026-11-03). 1-minute experiment `orb_mnq_1m_wf_v1` did not change canonical results.

**Correct next action:** report terminal state and await an explicit user decision. Do not start another autonomous research loop, repeat free-source sweeps/hashes/monitors/tests, or edit `.github/workflows/main.yml`, controller, or automation policy without explicit user authorization. Do not create further handoff-only checkpoints on generic prompts; repeated doc-only checkpoints have added no new state.

Legitimate forward paths require explicit user decision:
- **(a)** stop/reduce maintenance automation (cron at `.github/workflows/main.yml:11`, explicit auth required)
- **(b)** run a separately-versioned named experiment with explicit diff from baseline (e.g. far-side-of-range stop per `STRATEGY_RULES.txt` §2.1)
- **(c)** accept baseline as final

## Evidence (frozen artifacts)

- **axb0306** (`artifacts/metrics_axb0306.json`): 60 trades, 42W/18L (70.0%), long 33 / short 27, gross -$7,662.00, net -$31,637.98, costs $23,975.98, PF 0.4917, avg R -0.0431, maxDD $37,491.80, Sharpe -1.06 / Sortino -0.67. All 12 cost-sensitivity combos and signal-close sensitivity negative.
- **Kaggle proxy** (`artifacts/metrics_kaggle.json`): 688 trades, 446W/242L (64.8%), long 359 / short 329 (2022-11-16..2025-11-12), gross -$140,899.00, net -$626,525.96, costs $485,626.96, PF 0.2271, avg R -0.0684, maxDD $626,994.56, Sharpe -1.68 / Sortino -1.04. All chronological splits, walk-forward, and 12 cost-sensitivity combos negative.
- Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

(End of file - total 42 lines)
