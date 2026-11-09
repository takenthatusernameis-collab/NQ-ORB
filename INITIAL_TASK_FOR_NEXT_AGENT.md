# Initial Task for Next Agent

## Context
- Repository state: **clean** (git status clean, HEAD at `b0fc86a chore(kilo): checkpoint agent session`)
- All 71 tests pass (`python3 -m pytest tests/ -q` → 71 passed in 0.90s)
- All 7 tracked SHA-256 hashes match; all 4 canonical artifact hashes match
- Monitor ledger: `checked_at_utc` 2026-11-08T06:00:17Z, axb0306/cme-futures-ohlc sha `60abd3fb...`, latest bar 2026-04-15T23:34:55Z (no extension observed)
- 06:00Z maintenance loop **stopped**; no pending work
- Baseline strategy (STRATEGY_RULES.txt) frozen; config `config/orb_mnq_15m_showcase.yaml` reflects current parameters

## Next Concrete Task
**Implement walk-forward evaluation using 1-minute data for exact 15:55 ET forced exit**

### Rationale
- The current baseline uses 15-minute bars only, which are insufficient for an exact 15:55 ET forced exit (per STRATEGY_RULES.txt and AGENTS.md hard boundary #4)
- 1-minute data (`raw/MNQ_1min.csv` and `raw/MNQ_1min_frontmonth.csv`) is available and verified
- This is the next logical step after freezing the baseline: evaluate the strategy with execution-grade resolution

### Required Steps
1. **Audit 1-minute data coverage**: Verify session alignment (09:30 ET range, 15:55 ET forced exit), DST transitions, contract roll dates, gaps, and bar timestamps
2. **Implement 1-minute backtest engine**: Support closed-bar signals, first-breakout handling, both filters, both directions, stop/target calculations, tick rounding, risk sizing, one-trade-per-day, entry cutoff, forced flatten at 15:55 ET
3. **Conservative intrabar event ordering**: When stop and target are both possible within a 1-minute bar, apply conservative ordering (stop first, then target, or vice versa — document assumption explicitly)
4. **Costs**: Include per-contract, per-side commissions, exchange/clearing fees, and slippage; report gross and net performance separately
5. **Walk-forward splits**: Use chronological train/validation/test splits (e.g., 60/20/20 by time). Do not shuffle. Preserve final untouched test interval
6. **Report**: Trade count, win rate, avg win/loss in R, expectancy (R and USD), profit factor, gross/net P&L, CAGR/annualized return (state capital convention), max drawdown, Sharpe/Sortino (state return frequency), worst day, monthly/yearly breakdown, exposure/time-in-market, sensitivity to plausible cost assumptions
7. **Deterministic tests**: Add tests for opening-range construction, first-breakout handling, both filters, both directions, stop/target, tick rounding, risk sizing, one-trade-per-day, entry cutoff, forced flatten, DST transitions, contract rolls, ambiguous intrabar touches

### Constraints
- Historical research only. No broker integration, live trading, or paper-trading execution
- Do not purchase data or use paid/proprietary services
- Do not optimize thresholds, stops, targets, entry rules, or session times before reporting the untouched baseline on 1-minute data
- Any parameter change must be a separately named, versioned experiment with explicit diff from frozen baseline
- Keep raw data separate from processed data and code; avoid committing large datasets
- Run focused tests and full test suite after changes

### Files to Reference
- `STRATEGY_RULES.txt` — authoritative strategy definition
- `PROMPT.md` — research workflow
- `config/orb_mnq_15m_showcase.yaml` — current parameters
- `raw/MNQ_1min.csv`, `raw/MNQ_1min_frontmonth.csv` — 1-minute data
- `tests/` — existing test patterns
- `AGENTS.md` — hard boundaries and standards

### Deliverables
- Updated `HANDOFF.md` with verification snapshot
- New experiment config (e.g., `config/orb_mnq_1m_wf_v1.yaml`)
- Walk-forward results (metrics + trades JSON in `artifacts/`)
- Deterministic test additions in `tests/`
- Updated `INITIAL_TASK_FOR_NEXT_AGENT.md` for the following agent