# NQ ORB — Durable handoff

## Status: terminal research complete; awaiting user decision

**This session (2026-11-16T01:26:11Z):** Explicit user request: read prior durable-handoff task, complete it, then update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`. Completed the prior task: independent verification from HEAD `e7191e9` on `main` confirms terminal state — `git status --short` clean at verification; `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged; `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` empty; `artifacts/` has 35 files and no `*manifest*`. Canonical artifact metrics unchanged in-file: `artifacts/metrics_axb0306.json` — 60 trades (33L/27S), win_rate 0.700, gross -$7,662.00, net -$31,637.98, costs $23,975.98, PF 0.4917, avg R -0.0431, maxDD $37,491.80, Sharpe -1.056, Sortino -0.668, exposure 10.29%; `artifacts/metrics_kaggle.json` — 688 trades (359L/329S), win_rate 0.648, gross -$140,899.00, net -$626,525.96, costs $485,626.96, PF 0.2271, avg R -0.0684, maxDD $626,994.56, Sharpe -1.680, Sortino -1.042, exposure 8.07%. No research/data/test/automation changes made; tests not re-run (`python -m pytest` unavailable; not authorized). Refreshed both durable docs at explicit user request; state unchanged and terminal; forward paths (a)/(b)/(c) remain gated on explicit user decision.

**This session (2026-11-16T01:28:41Z):** independent verification from HEAD `bb910ff` on `main` confirms terminal state unchanged — `git status --short` clean; `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged; `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` empty; `ls artifacts | wc -l` = 35, no `*manifest*`; canonical metrics unchanged in-file (axb0306 60 trades 33L/27S 70.0% net -$31,637.98 PF 0.4917 avg R -0.0431; Kaggle 688 trades 359L/329S 64.8% net -$626,525.96 PF 0.2271 avg R -0.0684). State unchanged and terminal; no research, data, tests, or automation changes.

**Prior session checkpoint (2026-11-16T01:24:52Z):** doc-only refresh of both durable docs at explicit user request, verification from HEAD `e7191e9` confirmed same terminal state.

**Prior session checkpoint (2026-11-16T00:34:13Z):** doc-only refresh of both durable docs at explicit user request, verification from HEAD `ece2d95` confirmed same terminal state.

**Prior session checkpoint (2026-11-16T00:31:59Z):** doc-only refresh of both durable docs at explicit user request, verification from HEAD `4ab83a0` confirmed same terminal state.

**Prior session checkpoint (2026-11-16T00:31:30Z):** doc-only refresh of both durable docs at explicit user request, verification from HEAD `19391a1` confirmed same terminal state.

**Prior session checkpoints (2026-11-16):** `a69d153`, `d945163`, `27f9d6d` were doc-only verifications with same terminal finding. `ae2a04b` and `9205d7b` were prior doc-only checkpoint commits before this refresh. `541743a`, `19391a1`, `4ab83a0`, and `18df1a3` are the doc-only checkpoint commits since `a69d153`.

**Prior doc-only checkpoints (2026-11-15):** repeated independent verifications from earlier HEADs found no state change. They are not precedent for routine checkpoints absent explicit request or material change.

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
- Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate. MaxDD/Sharpe/Sortino values cited in earlier checkpoints are not present as top-level fields in the current canonical metrics JSONs; see artifacts for full recorded fields.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

(End of file - total 44 lines)