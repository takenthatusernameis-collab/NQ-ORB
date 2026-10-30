# Initial task for the next Kilo worker — NQ ORB

Read `AGENTS.md`, `STRATEGY_RULES.txt`, `PROMPT.md`, and `HANDOFF.md` before making changes.

## Current state
- Free-data feasibility done (axb0306/cme-futures-ohlc MNQ 1min/15min, 2026-01-20 to 2026-04-15). 15:55 flatten testable with 1min. Infrastructure scaffolded in `src/orb/`, baseline signal generation ran (60 trades on sample). See `data/FEASIBILITY_REPORT.md`, `artifacts/trades_baseline.json`.

## Priority tasks
1. **Data coverage**: Find longer free MNQ history. Try other public repos, Kaggle (check MNQ specifically), or other legitimate free sources. Record provenance/hashes for any new data. Do not purchase data.
2. **Full execution engine**: Extend `src/orb/backtest.py` to simulate exits using 1min bars: check stop/target intrabar, apply stop-first on ambiguous bars, enforce 15:55 flatten, track PnL with commissions/exchange fees/slippage per side, output gross and net.
3. **Metrics & reporting**: Compute trade count, win rate, avg win/loss R, expectancy R/USD, profit factor, gross/net, max DD, exposure, long/short splits. Save trade ledger + summary.
4. **Tests**: Add tests for OR construction, first-break logic, filters, sizing/tick rounding, cutoffs, flatten, one-trade-per-day.
5. **Validation rigor**: Chronological splits, sensitivity to costs, report uncertainty. Do not optimize parameters.

## Constraints
No parameter optimization, no strategy-rule changes, no broker integration, no live/paper orders. Update `HANDOFF.md` with evidence, commands, results, blockers, next task.
