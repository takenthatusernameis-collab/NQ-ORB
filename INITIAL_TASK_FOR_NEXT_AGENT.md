# Initial Task for Next Agent

## Context
The NQ/MNQ Opening Range Breakout research is **COMPLETE and TERMINAL**. The frozen baseline (STRATEGY_RULES.txt v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`) has been independently verified 28 times with identical results (latest: HEAD `919c90b`, 2026-11-16).

## Canonical Results (Frozen)
- **axb0306** (60 trades, Jan–Apr 2026): 70% win rate, net P&L **-$31,637.98**, profit factor **0.49**, avg R **-0.043**
- **Kaggle proxy** (688 trades, Nov 2022–Nov 2025): 64.8% win rate, net P&L **-$626,525.96**, profit factor **0.23**, avg R **-0.068**
- All 12 cost-sensitivity combinations and signal-close sensitivities are negative on both datasets.
- Costs ($2.87/side + 1-tick adverse slippage) dominate; the 0.4R target requires >71.43% pre-cost win rate.

## Your Task
**DO NOT start any new research, data acquisition, testing, or automation changes.**

The research task is complete. The only valid next actions require **explicit user decision**:

1. **(a) Stop/reduce maintenance automation** — Disable the cron in `.github/workflows/main.yml:11` (requires explicit user authorization for that exact change)
2. **(b) Run a separately-versioned named experiment** — e.g., far-side-of-range stop per `STRATEGY_RULES.txt` §2.1, with an explicit diff from the frozen baseline
3. **(c) Accept baseline as final** — No further work

## Standing Constraints (Non-Negotiable)
- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.
- Do not create further handoff-only checkpoints on generic prompts; repeated doc-only checkpoints have added no new state.

## Expected Output
Report the terminal state to the user and await their explicit decision on (a), (b), or (c). Do not proceed without it.