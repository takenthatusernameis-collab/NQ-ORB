# NQ ORB — Durable handoff

- **HEAD**: `1236eda` (= origin/main, clean `main...origin/main`, 0 ahead / 0 behind). Advanced by controller checkpoint commits since prior handoff (not added by this agent).
- **Timestamp (UTC)**: 2026-11-13T20:57:43Z
- **Last bounded state check (UTC)**: 2026-11-13T20:57:43Z (this session). Verified: clean tree, HEAD == origin/main (0/0), `STRATEGY_RULES.txt` SHA `6d3258c3…` and frozen metric hashes `dddaefa2…` (`metrics_axb0306_full.json`) / `a6ae1006…` (`metrics_kaggle.json`) unchanged (spot-checked via `sha256sum`), net metrics re-read from frozen artifacts. No frozen/research/data/artifact files touched; durable handoff files refreshed only; **no commit added**. No test suite run, no manifest re-hash, no free-data poll (last full suite 75 passed in 0.88s at 2026-11-13T12:48:19Z; last full 20/20 manifest check 2026-11-13T16:50:32Z). Prior agent task completed.

## TERMINAL STATE — READ FIRST

**The research task is COMPLETE. The frozen baseline is final and negative-net.** There is no remaining research work on the current free-data ceiling (`data/FEASIBILITY_REPORT.md`: the free-source search was re-run dozens of times through 2026-11-03 with no new source; every candidate is paid, key-gated, daily-only, or NQ big-contract rather than MNQ).

**This repository is in a degenerate maintenance loop.**
- `.github/workflows/main.yml` runs on `cron: "*/5 * * * *"` and spawns a sequential Kilo session per activation.
- Each session performs an identical "maintenance re-verification" and the workflow commits `chore(kilo): checkpoint agent session`.
- Since 2026-11-01T00:00:00Z: **2,698 commits**, of which **2,397** are exact `chore(kilo): checkpoint agent session` and **2,431** are `chore(kilo)`-prefixed maintenance/bookkeeping; **0** real research commits (last substantive research: `5fab764`, `ce861a2`, 2026-10-31).

**Correct next action is NOT another re-verification.** Do not re-run tests/hashes/monitor checks or add checkpoint commits. Stopping/changing automation (`.github/workflows/main.yml` schedule or controller/policy) requires **explicit user authorization** per `AGENTS.md` ("Do not edit `.github/workflows/main.yml` … unless the user explicitly authorizes that exact change"). No such authorization has been given.

## Research status (frozen)

- **Strategy**: `STRATEGY_RULES.txt` v1.0 (SHA `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`), MNQ 15-min ORB showcase. No parameter changes.
- **Data**: axb0306 MNQ (2026-01-20..2026-04-15, 60 complete days) and Kaggle front-month proxy (2022-11-16..2025-11-12, 688 days). 1-min audits: `research_state/1m_audit_{axb0306,kaggle}.json`. Free-data search exhausted (`data/FEASIBILITY_REPORT.md`).
- **Results (negative net, evidence not edge)**:
  - axb0306 (`artifacts/metrics_axb0306_full.json`): 60 trades, 42W/18L (70%), gross -$7,662, **net -$31,637.98**, costs $23,975.98, PF 0.4917, max DD $37,491.80.
  - Kaggle (`artifacts/metrics_kaggle.json`): 688 trades, 446W/242L (64.8%), gross -$140,899, **net -$626,525.96**, costs $485,626.96, PF 0.2271, max DD $626,994.56.
  - Chronological train/val/test and date-based walk-forward splits are all negative net. Do not present as profitable.
  - Driver: costs (commissions + fees $2.87/side, 1-tick adverse slippage) dominate; 0.4R target needs >71.43% pre-cost win rate and observed rates are below that.

## Test/manifest status

- Last full suite: **75 passed in 0.88s** at 2026-11-13T12:48:19Z. Not re-run this session.
- Last full 20-file manifest check: **20/20 matched** at 2026-11-13T16:50:32Z. Not re-hashed this session.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change must be a separately named, versioned experiment with explicit diff from baseline.
- Do not repeat maintenance re-verification. Report terminal state instead of re-verifying.
- Keep this handoff compact; consolidate repeated confirmations.
