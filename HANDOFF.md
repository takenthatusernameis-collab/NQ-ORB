# NQ ORB — Durable handoff

## Status: terminal research complete; awaiting user decision

**This session (2026-11-15T21:25Z):** Explicit user request: read prior durable-handoff task, complete it (verify terminal state and report), then update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`. Independent verification from HEAD `c582edc` on `main`: working tree clean before these doc edits; `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged; `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` empty; `artifacts/` has 35 files and no `*manifest*`; canonical metrics re-read unchanged — axb0306: 60 trades (33L/27S), 42W/18L 70.0%, gross -$7,662.00, net -$31,637.98, costs $23,975.98, PF 0.4917, avg R -0.0431, maxDD $37,491.80, Sharpe -1.06 / Sortino -0.67; Kaggle: 688 trades (359L/329S), 446W/242L 64.8%, gross -$140,899.00, net -$626,525.96, costs $485,626.96, PF 0.2271, avg R -0.0684, maxDD $626,994.56, Sharpe -1.68 / Sortino -1.04. No research/data/test/automation changes made; tests were not re-run (recovered task prohibits them without authorization; `python -m pytest` unavailable). State unchanged and terminal; forward paths (a)/(b)/(c) remain gated on explicit user decision.

**Prior session (2026-11-15T21:23Z):** Verified terminal state from HEAD `4c54d0a`; no state change.

**Prior session (2026-11-15T21:21Z):** Verified terminal state from HEAD `5be0510`; no state change.

**This session (2026-11-15T21:21Z):** Explicit user request: read prior durable-handoff task, complete it (verify terminal state and report), then update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`. Independent verification from HEAD `5be0510` on `main`: working tree clean; `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged; `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` empty; `artifacts/` has 35 data files and no `*manifest*`; canonical metrics re-read unchanged (axb0306: 60 trades, 42W/18L 70.0%, net -$31,637.98, PF 0.4917, avg R -0.0431, maxDD $37,491.80, Sharpe -1.06/Sortino -0.67; Kaggle: 688 trades, 446W/242L 64.8%, net -$626,525.96, PF 0.2271, avg R -0.0684, maxDD $626,994.56, Sharpe -1.68/Sortino -1.04). No research/data/test/automation changes made. State unchanged and terminal.

**Earlier terminal-state doc checkpoints (2026-11-15):** `b50b298`, `67554a3`, `afb91ec`, `0986a0d`, `be538f0`, `81b9bbb`, `f87e72b`, `b746714`, `f963264`, `61c1eb5`, `dc3879f`, `ed8f7b3`, `5df6b25`, `a5399d2`, `d2e8818`, `9b8a89c`, `0d54747`, `f2c1a51`, `da3814d`, `6ea13fa`, `7a3fcda`, `4d29d00`, `1451458`, `51d587a`, `f85bdb3`, `c541c1b`, `9aba8ad`, `b482c8a` each repeated the same verification and found no state change. None is precedent for routine checkpoints absent explicit request or material change.

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
