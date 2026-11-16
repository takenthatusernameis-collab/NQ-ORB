# Initial Task for Next Agent

## Objective
Confirm terminal repository state and await explicit user decision on forward path.

## Required Actions
1. Run all verification commands listed in `HANDOFF.md` (Verification commands section).
2. Report the following confirmed facts:
   - Frozen `STRATEGY_RULES.txt` SHA-256: `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`
   - Zero drift vs commit `a797773` across `artifacts`, `config`, `src`, `tests`, `raw`, `data`, `scripts`
   - 35 artifact files, 0 manifest files
   - Canonical metrics unchanged:
     - `metrics_axb0306.json`: 60 trades, net P&L -$31,638, profit factor 0.49
     - `metrics_kaggle.json`: 688 trades, net P&L -$626,526, profit factor 0.23
   - Test suite status: `python3 -m pytest -q` (pytest may be absent; last recorded pass in pytest-available envs: 75 passed)
3. State clearly: **"Terminal — awaiting explicit user decision on forward path (a), (b), or (c)."**
4. Do NOT initiate any research, experiments, or automation changes without explicit user authorization.

## Forward Paths (require explicit user authorization)
- **(a)** Stop/reduce maintenance automation (`.github/workflows/main.yml:11`, cron)
- **(b)** Run a separately versioned, named experiment with explicit diff from frozen baseline
- **(c)** Accept baseline as final

## Hard Constraints
- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.