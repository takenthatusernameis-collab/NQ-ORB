# Agent instructions — NQ ORB

## Mission and source of truth

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation.

- `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition.
- `PROMPT.md` defines the research workflow.
- `HANDOFF.md` contains the current durable task and must be updated after every substantive Kilo session.
- Do not silently change the baseline. Any change to strategy logic or parameters must be a separately named, versioned experiment with an explicit diff from the frozen baseline.

## Hard boundaries

- Historical research and simulation only. No broker integration, order routing, live trading, paper-trading execution against a broker, or deployment.
- Never request, add, print, or persist broker/API credentials.
- Do not purchase data or use paid/proprietary services. Prefer freely accessible, exchange-published or otherwise legitimately available datasets. Never bypass access controls or terms.
- Do not launch nested Kilo sessions, recursive workflows, duplicate scheduled workflows, or additional GitHub Actions activations. The repository's existing controller owns the sequential Kilo loop.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy unless the user explicitly authorizes that exact change.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal a failure.

## Research standards

1. Start by inspecting the repository, the durable handoff, the strategy rules, existing code, and prior evidence.
2. Audit data availability before implementing a large pipeline. Record source, license/access constraints, retrieval time, contract symbols/months, session timezone, bar timestamps, gaps, roll rules, adjustment method, and hashes.
3. Never fabricate unavailable historical bars, volume, trade fills, transaction costs, timestamps, or missing data.
4. The 09:30 ET range must be timezone/DST-correct. The 15:55 ET forced exit requires 1-minute-or-better execution evidence; 15-minute bars alone are insufficient for an exact exit.
5. Use confirmed closed-bar signals. Exclude the live breakout bar from the preceding-20-bar RVOL denominator. Prevent lookahead in ATR, sizing, entry, stop, target, and session handling.
6. Include realistic per-contract, per-side commissions, exchange/clearing fees, and slippage. Report gross and net performance separately.
7. Use conservative event ordering when stop and target are both possible within the smallest available bar. Keep execution assumptions explicit.
8. Freeze the first baseline. Do not optimize thresholds, stops, targets, entry rules, or session times before reporting the untouched baseline.
9. Use chronological train/validation/test splits or walk-forward evaluation. Do not shuffle time series. Preserve a final untouched test interval.
10. Report uncertainty, data limitations, sample size, trade count, long/short splits, year/regime splits, costs, drawdown, and all failed/blocked experiments.

## Required performance reporting

At minimum, when data permits, report trade count, win rate, average win/loss in R, expectancy in R and USD, profit factor, gross/net P&L, CAGR or annualized return with the capital convention stated, maximum drawdown, Sharpe/Sortino with the return frequency stated, worst day, monthly/yearly breakdown, exposure/time-in-market, and sensitivity to plausible cost assumptions.

## Engineering standards

- Add deterministic tests for opening-range construction, first-breakout handling, both filters, both directions, stop/target calculations, tick rounding, risk sizing, one-trade-per-day, entry cutoff, forced flatten, daylight-saving transitions, contract rolls, and ambiguous intrabar touches.
- Use synthetic/fixture tests for logic; do not present synthetic results as market evidence.
- Keep raw data separate from processed data and code. Avoid committing large datasets or licensed material. Record reproducible acquisition instructions and hashes.
- Run the focused tests and full relevant test suite after changes. Distinguish implementation tests from empirical evidence.
- Keep changes small, auditable, and committed. Update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with exact completed work, test outcomes, blockers, and the next concrete task.

## Kilo session discipline

A successful Kilo process exit is not proof of correctness. Verify the Git diff, tests, data provenance, outputs, and remote persistence. Do not claim a task is complete when only a plan or code stub exists.
