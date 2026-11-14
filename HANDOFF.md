# NQ ORB — Durable handoff

- **HEAD**: `4d2d14c` (transient controller checkpoint loop); prior checkpoint `2644093`. Working tree clean at session start.
- **Timestamp (UTC)**: 2026-11-14T01:47:20Z

## TERMINAL STATE — READ FIRST

**The research task is COMPLETE and terminal. No remaining research work.** The frozen MNQ 15-min ORB baseline (`STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`) is final and negative-net on every free dataset available; free-source search is exhausted (`data/FEASIBILITY_REPORT.md`, through 2026-11-03).

**This session (2026-11-14T01:47:20Z):** read `HANDOFF.md`, `PROMPT.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`; confirmed working tree clean and HEAD (`4d2d14c`, advanced from `2644093` via controller checkpoint) via `git status`/`git log`; verified `STRATEGY_RULES.txt` SHA-256 matches the frozen hash and canonical artifacts present (`artifacts/metrics_axb0306_full.json`, `artifacts/metrics_kaggle.json`, `artifacts/walk_forward.json`, `data/FEASIBILITY_REPORT.md`). No test run, no manifest re-hash, no monitor poll, no commit. Handoff/next-task files consolidated.

**Correct next action is NOT another re-verification.** Do not re-run tests/hashes/monitor checks, do not add checkpoint commits, do not edit `.github/workflows/main.yml`, controller, or automation policy (requires explicit user authorization per `AGENTS.md`; none given). Report terminal state and stop.

## Research status (frozen)

- **Strategy**: `STRATEGY_RULES.txt` v1.0, MNQ 15-min ORB. No parameter changes.
- **Data**: axb0306 MNQ (2026-01-20..2026-04-15, 60 days) and Kaggle front-month proxy (2022-11-16..2025-11-12, 688 days). 1-min audits: `research_state/1m_audit_{axb0306,kaggle}.json`.
- **Results (negative net, evidence not edge)** — frozen JSONs:
  - axb0306 (`artifacts/metrics_axb0306_full.json`): 60 trades, 42W/18L (70%), 33 long / 27 short, gross -$7,662, **net -$31,637.98**, costs $23,975.98, PF 0.4917, max DD $37,491.80, expectancy -0.0431R, avg win +0.3775R / avg loss -1.0245R.
  - Kaggle (`artifacts/metrics_kaggle.json`): 688 trades, 446W/242L (64.8%), 359 long / 329 short, gross -$140,899, **net -$626,525.96**, costs $485,626.96, PF 0.2271, max DD $626,994.56, expectancy -0.0684R, Sharpe -1.68 / Sortino -1.04 (daily), worst day -$4,789.80, exposure 8.07%, 2.99 years.
  - Chronological train/val/test: -$448,765.02 / -$66,243.22 / -$111,517.72 — all negative net.
  - Walk-forward (`artifacts/walk_forward.json`, 8 windows): negative net in every window (test PF 0.128–0.447). Cost sensitivity: all 12 combos negative (-$487,099..-$808,255); signal-close sensitivity all negative.
  - Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate; observed rates below that.
- **Note**: axb0306 gross is -$7,662; its chronological train split is +$1,229.22 net (36 trades) — small-sample noise, not an edge, not used as a claim.

## Test/manifest status (not re-run this session)

- Last full suite: **75 passed in 0.88s** (2026-11-13T12:48:19Z).
- Last full 20-file manifest: **20/20 matched** (2026-11-13T16:50:32Z).
- This session: no test run, no manifest re-hash, no commit.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not repeat maintenance re-verification. Report terminal state instead.
- Keep this handoff compact; consolidate rather than append.

(End of file)