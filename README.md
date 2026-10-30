# NQ ORB — Opening Range Breakout Research

This repository contains a frozen, user-specified Nasdaq futures opening-range breakout (ORB) research specification and its autonomous Kilo research workflow.

## Strategy baseline

The strategy builds the opening range from the first 15-minute bar after the 09:30 ET New York cash open, then evaluates the first post-range 15-minute close outside that range. A trade is allowed only when **both** the relative-volume and ATR-percent filters pass.

The showcase preset is **MNQ 15-minute**:

- Opening range: 09:30–09:45 ET, one 15-minute bar.
- Stop: 0.4 × Wilder ATR(14), no point cap.
- Target: 0.4 × initial stop distance (0.4R).
- Sizing: $3,000 fixed stop-risk budget per trade.
- RVOL: at least 1.0 × the preceding 20 completed 15-minute bars' average volume.
- ATR regime: 0.10%–0.60% of price, inclusive.
- Both long and short; one trade per trading day.
- No new entries at or after 15:00 ET; flatten any open position at 15:55 ET.

The authoritative, plain-text rule file is [STRATEGY_RULES.txt](STRATEGY_RULES.txt). Do not silently change it.

## Important execution details

CME specifies MNQ at $2 × the Nasdaq-100 Index, with a 0.25-index-point minimum tick ($0.50 per contract). NQ is a different contract at $20 × the index. The $3,000 showcase risk calculation must therefore use the MNQ $2/point multiplier, not NQ's $20/point multiplier. See the official [CME MNQ product page](https://www.cmegroup.com/markets/equities/nasdaq/micro-e-mini-nasdaq-100.html) and [CME NQ contract specifications](https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html).

A 15-minute signal chart alone cannot establish an exact 15:55 exit or the order in which a stop and target were touched inside a bar. Use 1-minute-or-better execution data where available. If an adequate free source is unavailable, report the limitation; do not fabricate fills or claim exact 15:55 execution.

The 0.4R target implies a pre-cost break-even win rate of approximately 71.43% (before slippage, commissions, and other fees). Treat that as a mathematical implication, not a performance claim.

## Repository status

This is a new research bootstrap. No backtest, profitability, CAGR, Sharpe ratio, drawdown, or live-trading claim has been established yet. The first Kilo task is to audit free-data feasibility and then implement a reproducible, cost-aware, out-of-sample research path.

## Kilo automation

The repository's `.github/workflows/main.yml` is based on the latest established Kilo general-agent workflow found in the account's EMA hourly continuation research repository on 2026-10-30. The workflow is paired here with its controller progress helper and targeted regression tests, so its declared test and runtime dependencies exist in this repository.

The workflow is scheduled every five minutes and has a bounded 355-minute controller cutoff per activation. A workflow-file push runs controller diagnostics/tests only; scheduled or manually dispatched activations run the Kilo worker loop. Kilo must continue the durable task in [HANDOFF.md](HANDOFF.md), not launch nested workflows or independent Kilo activations.

## Research-only boundary

This repository is for historical research and simulation. Do not connect a broker, submit orders, enable live trading, or store broker credentials. No live deployment is authorized.
