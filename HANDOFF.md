# NQ ORB — Durable handoff

- **HEAD**: `88d8f92` at this session start (transient — the controller's `chore(kilo): checkpoint agent session` commits advance it every ~5 min).
- **Timestamp (UTC)**: 2026-11-14T00:53:52Z
- **This session**: read `HANDOFF.md` + `INITIAL_TASK_FOR_NEXT_AGENT.md`; verified repo state via read-only `git`/`ls`/`sha256sum` and direct reads of the frozen metrics JSONs + `walk_forward.json` (no test run, no manifest re-hash, no monitor poll, no commit); confirmed every handoff claim (`STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged; working tree clean); consolidated durable docs. Research is terminal; no further work. Prior agent task completed — report terminal state and stop.

## TERMINAL STATE — READ FIRST

**The research task is COMPLETE. The frozen baseline is final and negative-net.** No remaining research work is available on the current free-data ceiling (`data/FEASIBILITY_REPORT.md`: free-source search exhausted through 2026-11-03; every candidate is paid, key-gated, daily-only, or NQ big-contract rather than MNQ).

**This repository is in a degenerate maintenance loop.** `.github/workflows/main.yml` runs on `cron: "*/5 * * * *"`, and each activation commits `chore(kilo): checkpoint agent session`. Since 2026-11-01: **2,741 commits**, of which **2,442** are checkpoint-only; the remainder are `chore: capture completed workflow run diagnostics` and `handoff: maintenance re-verification` commits — **0 research**. Last substantive research commit: `5fab764` (2026-10-31, `feat: complete required performance reporting...`). `research_state/` contains many `free_data_monitor_*` files from the same loop.

**Correct next action is NOT another re-verification.** Do not re-run tests/hashes/monitor checks, do not add checkpoint commits. Stopping/changing automation (`.github/workflows/main.yml` schedule or controller/policy) requires **explicit user authorization** per `AGENTS.md`. None has been given.

## Research status (frozen — verified this session by direct JSON read)

- **Strategy**: `STRATEGY_RULES.txt` v1.0 (SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`), MNQ 15-min ORB showcase. No parameter changes.
- **Data**: axb0306 MNQ (2026-01-20..2026-04-15, 60 complete days) and Kaggle front-month proxy (2022-11-16..2025-11-12, 688 days). 1-min audits: `research_state/1m_audit_{axb0306,kaggle}.json`.
- **Results (negative net, evidence not edge)** — re-read directly from the frozen JSON this session:
  - axb0306 (`artifacts/metrics_axb0306_full.json`): 60 trades, 42W/18L (70%), 33 long / 27 short, gross -$7,662, **net -$31,637.98**, costs $23,975.98, PF 0.4917, max DD $37,491.80, expectancy -0.0431R, avg win +0.3775R / avg loss -1.0245R.
  - Kaggle (`artifacts/metrics_kaggle.json`): 688 trades, 446W/242L (64.8%), 359 long / 329 short, gross -$140,899, **net -$626,525.96**, costs $485,626.96, PF 0.2271, max DD $626,994.56, expectancy -0.0684R, Sharpe -1.68 / Sortino -1.04 (daily), worst day -$4,789.80, exposure 8.07%, 2.99 years covered.
  - Kaggle chronological train/val/test: train -$448,765.02 (246W, 59.7%), val -$66,243.22 (105W, 76.6%), test -$111,517.72 (95W, 68.3%) — all negative net. Long/short splits also all negative net.
  - Walk-forward (`artifacts/walk_forward.json`, 8 windows, train 150 / test 150, step 50, source kaggle) is negative net in every window (test PF 0.128–0.447). Cost sensitivity: net stays negative across all 12 slip_mult × cost_mult combos (range -$487,099 to -$808,255); signal-close sensitivity also all negative.
  - Driver: costs (commissions + fees $2.87/side, 1-tick adverse slippage) dominate; the 0.4R target needs a >71.43% pre-cost win rate, observed rates are below that.
- **Note for future readers**: the axb0306 60-day sample's *gross* P&L is -$7,662 and its chronological train split is +$1,229.22 net (36 trades, 30W/6L); this is small-sample noise, not an edge, and is not used as a claim.

## Test/manifest status (not re-run this session)

- Last full suite: **75 passed in 0.88s** at 2026-11-13T12:48:19Z.
- Last full 20-file manifest check: **20/20 matched** at 2026-11-13T16:50:32Z.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change must be a separately named, versioned experiment with an explicit diff from baseline.
- Do not repeat maintenance re-verification. Report terminal state instead.
- Keep this handoff compact; consolidate rather than append.

(End of file)
