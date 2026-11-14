# NQ ORB — Durable handoff

- **HEAD**: `688135c` (`chore(kilo): checkpoint agent session`, local; checkpoint-only since substantive research commit `5fab764`, 2026-10-31). Working tree clean except documentation updates to `HANDOFF.md` / `INITIAL_TASK_FOR_NEXT_AGENT.md` this session (controller owns commits).
- **Timestamp (UTC)**: 2026-11-14T03:50Z (session I).

## TERMINAL STATE — READ FIRST

**The research task is COMPLETE and terminal. No remaining research work exists.** The frozen MNQ 15-min ORB baseline (`STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`) is final and negative-net on every free dataset available. The free-source search is exhausted: `data/FEASIBILITY_REPORT.md` documents ~30 documented sweeps through 2026-11-03; every candidate MNQ 1-min/15-min source is paid, key-gated, daily-only, or NQ (big contract) rather than MNQ.

**This session (2026-11-14T03:50Z):** completed the prior agent task from the durable handoff (read `HANDOFF.md`/`INITIAL_TASK_FOR_NEXT_AGENT.md`/`PROMPT.md`, confirmed terminal state and evidence, updated handoff and next-agent task). No strategy/config/raw-data/artifact changes, no tests, hashes, monitor checks, automation edits, or commits (controller owns commits). Terminal conclusion unchanged.

**Correct next action is NOT another re-verification.** Do not re-run tests/hashes/monitor checks, do not add checkpoint commits, do not edit `.github/workflows/main.yml`, controller, or automation policy (requires explicit user authorization per `AGENTS.md`; none given). Report terminal state and stop. Legitimate forward paths require an explicit user decision: (a) stop/reduce maintenance automation, (b) run a separately-versioned experiment (e.g. far-side-of-range stop variant, `STRATEGY_RULES.txt` §2.1, as `experiment_farside_stop_v1`), or (c) accept baseline as final.

## Research status (frozen)

- **Strategy**: `STRATEGY_RULES.txt` v1.0, MNQ 15-min ORB. No parameter changes.
- **Data**: axb0306 MNQ.M26 (2026-01-20..2026-04-15, 60 days, single contract, no roll) and Kaggle front-month proxy (`raw/MNQ_15min_frontmonth.csv`, 2022-11-16..2025-11-12, 688 days, unadjusted). 1-min audits: `research_state/1m_audit_{axb0306,kaggle}.json`.
- **Results (negative net, evidence not edge)** — frozen JSONs:
  - axb0306 (`artifacts/metrics_axb0306_full.json`): 60 trades, 42W/18L (70%), 33 long / 27 short, gross -$7,662, **net -$31,637.98**, costs $23,975.98, PF 0.4917, max DD $37,491.80, expectancy -0.0431R, avg win +0.3775R / avg loss -1.0245R.
  - Kaggle (`artifacts/metrics_kaggle.json`): 688 trades, 446W/242L (64.8%), 359 long / 329 short, gross -$140,899, **net -$626,525.96**, costs $485,626.96, PF 0.2271, max DD $626,994.56, expectancy -0.0684R (USD -$910.65/trade), Sharpe -1.68 / Sortino -1.04 (daily), worst day -$4,789.80 (2023-05-12), exposure 8.07%, 2.99 years. Yearly net: 2022 -$26,742.04, 2023 -$266,936.14, 2024 -$197,366.90, 2025 -$135,480.88.
  - Chronological train/val/test (688-trade Kaggle): -$448,765.02 / -$66,243.22 / -$111,517.72 — all negative net.
  - Walk-forward (`artifacts/walk_forward.json`, 8 windows, 150-trade test, step 50): test PF 0.128–0.447, net -$70,637.24..-$178,375.24 — negative in every window.
  - Cost sensitivity: all 12 combos negative (-$487,098.57..-$808,255.35); signal-close sensitivity all negative (-$607,226.96..-$734,132.96).
  - Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; the 0.4R target needs >71.43% pre-cost win rate; observed rates are below that.
- **Note**: axb0306 train split small-sample positive net (+$1,229.22, 36 trades) is noise, not an edge.

## Test/manifest status

- Tests last run: **75 passed in 0.56s** (2026-11-14T02:43Z, venv `/home/runner/work/_temp/orbvenv`). Not re-run this session. CI (`.github/workflows/main.yml:61-62`) only runs the 4 controller/automation test files in a `pytest numpy requests` venv, not the ORB logic tests (`tests/orb/`).
- Manifest last verified: 20/20 matched (2026-11-13T16:50:32Z). Not re-hashed this session.

## Maintenance-loop diagnosis

- Repo is in a degenerate maintenance loop: `.github/workflows/main.yml` runs `cron: "*/5 * * * *"`; recent history is only `chore(kilo): checkpoint agent session` commits (last substantive research commit `5fab764`, 2026-10-31); `research_state/free_data_monitor_*.json` accumulates at sub-hourly cadence (471 files) with no new findings.
- Stopping or changing that automation requires **explicit user authorization** per `AGENTS.md`. None has been given. Do not touch it unilaterally.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with an explicit diff from baseline.
- Do not repeat maintenance re-verification. Report terminal state instead.
- Keep this handoff compact; consolidate rather than append.

(End of file)