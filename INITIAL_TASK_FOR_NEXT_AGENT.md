# Initial Task for Next Agent — NQ ORB

## Context
The NQ ORB research project is in a **terminal COMPLETE state**. The frozen MNQ 15-minute opening-range-breakout baseline (`STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`) has been exhaustively evaluated on all freely available datasets and is **negative-net on every source**.

- axb0306 (NQ 15-min, 2023-01..2024-06): 60 trades, net **-$31,637.98**
- Kaggle proxy (MNQ 15-min, 2022-11..2025-11): 688 trades, net **-$626,525.96**
- Separate 1-minute experiment `orb_mnq_1m_wf_v1`: **byte-identical** results (no trade bound on 15:55 flatten)
- All chronological splits, walk-forward windows, and 12 cost-sensitivity combos: negative
- Free MNQ 1-min/15-min data search exhausted (~30 sweeps through 2026-11-03)

## Your Task
**Do nothing unless the user explicitly directs one of three legitimate forward paths:**

1. **Stop/reduce maintenance automation** — Disable or modify the `*/5 * * * *` cron in `.github/workflows/main.yml` (requires explicit user authorization per `AGENTS.md`)
2. **Run a separately-versioned experiment** — e.g., far-side-of-range stop per `STRATEGY_RULES.txt` §2.1, named `experiment_farside_stop_v1` with explicit diff from baseline
3. **Accept baseline as final** — Archive the project

## Hard Constraints
- **Do not** re-run tests, re-hash, re-verify drift, or add checkpoint commits
- **Do not** edit `.github/workflows/main.yml`, controller, or automation policy without explicit user authorization
- **Do not** modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts
- Any strategy change = separately named, versioned experiment with explicit diff from baseline
- Historical research/simulation only — no broker/live/paper execution, no credentials, no paid data

## Verification (if needed)
If you must confirm terminal state, run the robust drift anchor from `HANDOFF.md`:
```bash
git status --porcelain
sha256sum STRATEGY_RULES.txt
git log --oneline a797773..HEAD -- src/ config/ scripts/ tests/ raw/ data/ artifacts/
```
All three must show: clean tree, SHA `6d3258c3…8ad2b1`, empty log.

## Expected Output
Report terminal state and await user decision. Do not create work.