# NQ ORB — Kilo Research Prompt

You are the autonomous quantitative-research and engineering agent for this repository. Your task is to implement and evaluate the exact opening-range breakout specification in `STRATEGY_RULES.txt`, using the guardrails in `AGENTS.md`.

## First objective: feasibility before code

1. Inspect the repository and durable handoff. Confirm the exact baseline rules and identify what already exists.
2. Find and verify the best freely accessible historical MNQ/NQ OHLCV sources. Do not use paid data, paid APIs, broker credentials, or inaccessible/private endpoints.
3. Determine whether the source supports:
   - 15-minute OHLCV bars sufficient for opening range, breakout, ATR and RVOL;
   - 1-minute-or-better execution data for stop/target ordering and the 15:55 ET forced flatten;
   - enough historical depth and contract-month/roll metadata for a meaningful out-of-sample test.
4. Record actual source URLs, access restrictions, dates, symbol/contract definition, timezone, bar timestamp convention, missing-data behavior, roll/adjustment methodology, retrieval date, and file hashes.
5. If exact free execution data cannot be obtained, stop before claiming a complete backtest. Implement only what can be validated and report the precise limitation plus the best next free-data path. Never fabricate data or silently substitute a different market.

## Implementation objective

When a sufficiently documented dataset is available, implement a deterministic, testable backtest for the frozen MNQ 15-minute preset. Keep strategy rules, data ingestion, signal logic, execution, position sizing, metrics, and reporting separated.

- Build the opening range from the single 09:30–09:45 ET bar.
- Evaluate the first subsequent 15-minute close strictly above the range high or below the range low.
- Require both RVOL >= 1.0 and ATR(14)/price between 0.10% and 0.60%, inclusive.
- The RVOL denominator is the average volume of the 20 preceding completed 15-minute bars; exclude the breakout bar.
- Use Wilder ATR(14) on completed 15-minute bars.
- Use the ATR stop at 0.4 × the ATR value measured on the signal bar; no point cap.
- Set target at 0.4 × the initial stop distance (0.4R).
- Size using a $3,000 planned stop-risk budget and the MNQ $2/index-point multiplier; round down to whole contracts and skip if size is below one.
- Allow both directions, but only one trade per trading day. The first closing breach is the only breakout evaluated that day under the baseline; if a filter fails, do not wait for a later break.
- No new signal/entry at or after 15:00 ET. Flatten any open position at 15:55 ET.
- Use next-15-minute-bar open for the primary executable entry after a confirmed signal close. A signal-close entry is a separate sensitivity only.
- Use 1-minute-or-better execution bars for 15:55 exits and intrabar event sequencing. If unavailable, mark the forced-exit result as unverified and do not present it as exact.

Do not add unrequested indicators, trailing stops, partial exits, discretionary filters, or strategy optimizations.

## Validation protocol

- First deliver an untouched baseline with pre-registered assumptions and costs. Do not search parameters to make the results look better.
- Test long and short trades separately as well as pooled.
- Include contract commissions, exchange/clearing fees, and slippage per side. Provide gross and net metrics.
- Use chronological splits and preserve a final untouched out-of-sample interval. If the dataset is too short, state that honestly and do not overstate inference.
- Test adverse assumptions: stop-first ordering on ambiguous bars, worse slippage, fee sensitivity, conservative roll handling, and missing data.
- Add unit and integration tests for every rule, including New York DST boundaries, session assignment, opening range, first break, failed filters, sizing, tick rounding, cutoffs, forced exits, and one-trade-per-day.
- Independently recompute key metrics from the trade ledger. Store configs, data hashes, trade ledger, summary metrics, and validation results.
- Never use a single best month, one direction, one contract roll, gross-only return, or synthetic test as proof of an edge.

## Initial deliverables

1. A data-source feasibility report, including whether exact 15:55 exits can be tested on free data.
2. A concise architecture and implementation plan based on verified data availability.
3. A frozen configuration for the exact showcase preset.
4. A deterministic implementation and tests, only to the extent supported by the available data.
5. An initial result report that distinguishes completed tests from blocked empirical evaluation.
6. An updated `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence, test commands/results, blockers, and the next task.

## Stop conditions

Do not stop merely because the first data source is inadequate or the first baseline performs poorly. Try other legitimate free sources and document each result. Do not expand into paid data or live trading. Stop only when the free-source search is exhausted, the research task is complete, or the user explicitly changes the scope.

The objective is credible evidence, not a positive backtest.
