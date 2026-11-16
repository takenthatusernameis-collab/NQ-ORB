# NQ ORB — Durable handoff

## Status: terminal research complete; awaiting user decision

**This session (2026-11-16, Kilo):** Explicit user request: read prior durable-handoff task, complete it, then update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`. Independently verified terminal state from HEAD `69fa390` on `main` (beneath it: prior doc-only checkpoint chain ending at `de96309`): `sha256sum STRATEGY_RULES.txt` = `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged; `git status --short` clean at verification; `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` empty; `git diff --name-only 0f1dafb..HEAD` touches only `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, and `research_state/workflow_run_diagnostics.jsonl` (all doc/diagnostics-only); `ls artifacts | wc -l` = 35, no `*manifest*`; canonical metrics re-read in-file and unchanged (axb0306 60 trades 33L/27S 42W/18L 70.0% net -$31,637.98 PF 0.4917 avg R -0.0431 maxDD $37,491.80 Sharpe -1.056 Sortino -0.668 exposure 10.29%; Kaggle 688 trades 359L/329S 446W/242L 64.8% net -$626,525.96 PF 0.2271 avg R -0.0684 maxDD $626,994.56 Sharpe -1.680 Sortino -1.042 exposure 8.07%). No research/data/test/automation changes made; tests not re-run (`python -m pytest` unavailable; not authorized). Refreshed both durable docs at explicit user request; state unchanged and terminal; forward paths (a)/(b)/(c) remain gated on explicit user decision.

**Prior doc-only checkpoints (2026-11-16):** `6b0b763`, `a19fb44`, `3918969`, `b7cb103`, `8f60c05`, `0f1dafb`, `5d2f488`, `2ce8bea`, `3fbf917`, `7f3c7c3`, `c1f5ec0`, `a608225`, `fb60c79`, `3861a7d`, `bb910ff`, `e7191e9`, `ece2d95`, `4ab83a0`, `19391a1`, `18df1a3`, `541743a`, `ae2a04b`, `9205d7b`, `d945163`, `27f9d6d`, `a69d153`, plus earlier 2026-11-15 checkpoints — all independent verifications from their respective HEADs finding the same unchanged, terminal state. They are not precedent for routine checkpoints absent explicit request or material change.

## Baseline

`STRATEGY_RULES.txt` v1.0 frozen, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`. Frozen baseline commit `5fab764`; last substantive research commit `a797773` (1-minute experiment `orb_mnq_1m_wf_v1`, `ae3c49f`/`a797773`, additive `flatten_fill='open'`, byte-identical to 15m baseline). No strategy/config/raw-data/canonical-artifact changes.

## Terminal state — read first

**Research task is COMPLETE and terminal. No remaining research work is authorized.** Frozen MNQ 15-min ORB baseline is final and negative-net on every available free dataset. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`). 1-minute experiment `orb_mnq_1m_wf_v1` did not change canonical results.

**Correct next action:** report terminal state and await an explicit user decision. Do not start another autonomous research loop, repeat free-source sweeps/hashes/monitors/tests, or edit `.github/workflows/main.yml`, controller, or automation policy without explicit user authorization. Do not create further handoff-only checkpoints on generic prompts; repeated doc-only checkpoints have added no new state.

Legitimate forward paths require explicit user decision:
- **(a)** stop/reduce maintenance automation (cron at `.github/workflows/main.yml:11`, explicit auth required)
- **(b)** run a separately-versioned named experiment with explicit diff from baseline (e.g. far-side-of-range stop per `STRATEGY_RULES.txt` §2.1)
- **(c)** accept baseline as final

## Evidence (frozen artifacts)

- **axb0306** (`artifacts/metrics_axb0306.json`): 60 trades, 42W/18L (70.0%), long 33 / short 27, gross -$7,662.00, net -$31,637.98, costs $23,975.98, PF 0.4917, avg R -0.0431. All 12 cost-sensitivity combos and signal-close sensitivity negative (per prior evidence).
- **Kaggle proxy** (`artifacts/metrics_kaggle.json`): 688 trades, 446W/242L (64.8%), long 359 / short 329, gross -$140,899.00, net -$626,525.96, costs $485,626.96, PF 0.2271, avg R -0.0684. All chronological splits, walk-forward, and 12 cost-sensitivity combos negative (per prior evidence).
- Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate. Risk metrics are stored under `max_drawdown_usd`, `sharpe_r`, `sortino_r`, and `exposure_pct` in the canonical metrics JSONs; see artifacts for full recorded fields.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

(End of file - total 44 lines)