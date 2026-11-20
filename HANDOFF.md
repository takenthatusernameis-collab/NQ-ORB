# NQ ORB — Durable handoff

## Status: TERMINAL — research complete; blocked on an explicit user decision

The frozen MNQ 15-minute ORB baseline is implemented, tested, and evaluated on every available free MNQ
data source. It is **negative-gross and negative-net on all of them** under full costs, and the free-data
search is exhausted (`data/FEASIBILITY_REPORT.md`). No autonomous research, experiment, or automation
change may begin without an explicit user decision on a forward path.

Last refreshed: 2026-11-20 at HEAD `f1a9e1ae`.

## STOP RULE (read first)

This repository has produced **2,069 consecutive docs-only commits** that re-confirm identical invariants
and add nothing. That cycle is the failure mode, not the job.

- A boilerplate turn ("read the prior agent task and complete it") is: read
  `INITIAL_TASK_FOR_NEXT_AGENT.md`, send the user the terminal status + numbers table + forward paths,
  and stop. **No edits, no verification pass, no commit.**
- Do not re-run `pytest`/`sha256sum`/drift/artifact checks to manufacture another checkpoint commit.
  Everything such a pass could find is already recorded below.
- Only act on: an explicitly selected forward path, a *specific* requested doc change, or new supplied
  data/scope. Then act on exactly that scope.

## Verified state (HEAD `f1a9e1ae`, 2026-11-20)

This session re-verified the two items previous sessions could only carry forward, so nothing below is
"carried forward" any more:

- `python3 -m pytest tests -q` → **75 passed** at `f1a9e1ae`. Run after installing `pytest`/`numpy`/`pandas`
  into the session sandbox (`pip install pytest numpy pandas`, pytest 9.2.0). This is the first actual
  execution since `6f73afaf`; the earlier "not re-runnable in CI" caveat is resolved.
- **Deterministic reproduction confirmed.** `python3 src/orb/runner.py --prefix <tmp> --source axb0306` and
  `--source kaggle` were re-run at `f1a9e1ae`; the resulting `metrics_*.json` are **byte-identical** (full
  dict equality) to `artifacts/metrics_axb0306.json` and `artifacts/metrics_kaggle.json`. Scratch outputs
  were deleted afterwards; `artifacts/` remains at its canonical 35 files.
- Research drift: `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts`
  → **0 files**. All 2,069 commits after `a797773` touch only 3 unique paths: `HANDOFF.md`,
  `INITIAL_TASK_FOR_NEXT_AGENT.md`, `research_state/workflow_run_diagnostics.jsonl`.
- `git status --short` clean. Frozen showcase preset `5fab764`. Last substantive research commit `a797773`.
- `STRATEGY_RULES.txt` SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`
  (frozen v1.0).
- Raw data hashes (unchanged):

| file | SHA-256 |
|---|---|
| `raw/MNQ_15min.csv` | `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37` |
| `raw/MNQ_1min.csv` | `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99` |
| `raw/MNQ_15min_frontmonth.csv` | `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4` |
| `raw/MNQ_1min_frontmonth.csv` | `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7` |

## Canonical metrics

| Dataset | Trades | Split | Win % | Gross $ | Net $ | Costs $ | PF | Exp/trade | Gross R | Net R |
|---|---|---|---|---|---|---|---|---|---|---|
| axb0306 (MNQ.M26, 2026-01-20..2026-04-15, single contract, no roll) | 60 | 33L/27S | 70.00 | -7,662.00 | -31,637.98 | 23,975.98 | 0.4917 | -527.30 | -0.043 | **-0.18** |
| Kaggle front-month (unadjusted by max volume, 2022-11-16..2025-11-12) | 688 | 359L/329S | 64.83 | -140,899.00 | -626,525.96 | 485,626.96 | 0.2271 | -910.65 | -0.068 | **-0.30** |

Sources: `artifacts/metrics_axb0306.json`, `artifacts/metrics_kaggle.json` +
matching `trades_*.json`. Max DD $37,491.80 / $626,994.56.

## Key facts

- `metrics.avg_r` is a **gross, price-based R multiple**: `(exit_fill - entry_fill) / risk_points`
  (sign-adjusted) — before commissions and slippage. It is **not** net R. Net R = net P&L over realized
  dollar risk (`contracts × risk_points × $2`): portfolio-weighted **-0.1771 / -0.3049**, mean per-trade
  **-0.1773 / -0.3046**. Quote net R, not `avg_r`.
- `gross − net == costs` holds to the cent on both datasets. 60/688 trades on 60/688 unique dates
  (one-trade-per-day intact). Independent re-aggregation of the ledgers reproduces count, L/S split, gross,
  net, costs, PF, and expectancy exactly; an independent signal-funnel cross-check reproduces trade counts.
- Sizing at $3,000 planned risk with a 0.4×ATR stop implies very large MNQ size: 29–122 contracts (median
  63.5) on axb0306, 34–278 (median 122) on kaggle. Fully-loaded cost (1 tick adverse slippage + $2.87/side
  fees) is $399.60 and $705.85 per trade — cost drag scales with size, not with the raw edge.
- No trade in either ledger exits via the 15:55 ET flatten (exit reasons: `target`, `stop`,
  `stop_first_ambiguous`; latest exit 12:00 ET / 14:15 ET). The flatten/DST/intrabar-ordering paths are
  test-covered, but reported P&L does not depend on a flatten execution assumption.
- The 0.4R target implies a **71.43% pre-cost break-even win rate**. Observed win rates are 70.00% and
  64.83% **and gross P&L is negative** → a strategy-edge failure, not a cost-only failure.
- Chronological splits kill the "good regime" hypothesis. axb0306: train (36 trades) **+$1,229.22**, val
  **-$15,894.08**, test **-$16,973.12**. Kaggle: train **-$448,765.02**, val **-$66,243.22**, test
  **-$111,517.72**. No out-of-sample segment is net positive; the single positive segment is in-sample.
- Sharpe/Sortino (per-trade, daily-equivalent) **-1.06/-0.67** and **-1.68/-1.04**; exposure 10.3% / 8.1%;
  worst day -$3,811.28 / -$4,789.80.
- `cost_sensitivity` (12 scenarios) is net-negative in **every** scenario: axb0306 -$24,754.28 to
  -$40,610.18; kaggle -$487,098.57 to -$808,255.35. No plausible cost assumption rescues the baseline.
- Reporting surface already complete: `monthly_net_pnl`, `yearly_net_pnl`, `sharpe_r`, `sortino_r`,
  `exposure_pct`, `cost_sensitivity`, `chronological_splits`, `signal_close_entry_sensitivity` in
  `metrics_*.json`; `walk_forward_*.json` present.
- No paid/proprietary data used; no credentials requested, used, or stored; free-source search exhausted.

## Forward paths (each requires explicit user authorization for that exact scope)

- **(a)** Stop or reduce the maintenance automation (`.github/workflows/main.yml`, cron `*/5 * * * *`).
  Requires explicit approval for that exact edit. This is the only path that ends the docs-only loop.
- **(b)** A separately versioned, named experiment with a written diff from the frozen baseline
  (cost-model sensitivity, entry-timing variant, or a pre-registered parameter study). Must not touch
  `STRATEGY_RULES.txt` or canonical artifacts, and must not tune to improve reported results.
- **(c)** Accept the baseline as final and stop the automation.
- **(d)** Supply new free data or a new scope — audited first (source, license/access, retrieval time,
  contract months, timezone, timestamps, gaps, roll rule, adjustment, hashes), then frozen as a fresh
  untouched baseline before any tuning.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with an explicit diff from the baseline.
- Do not edit `.github/workflows/main.yml`, controller code, permissions, or automation policy without
  explicit authorization for that exact change.
- Do not delete research evidence or rewrite Git history to conceal a failure.

## Verification (only for an authorized research or refresh session — never for another checkpoint)

```bash
git status --short && git rev-parse --short HEAD
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
sha256sum STRATEGY_RULES.txt raw/MNQ_15min.csv raw/MNQ_1min.csv raw/MNQ_15min_frontmonth.csv raw/MNQ_1min_frontmonth.csv
pip install pytest numpy pandas && python3 -m pytest tests -q
python3 src/orb/runner.py --prefix <tmp> --source axb0306   # diff vs artifacts/metrics_axb0306.json
python3 src/orb/runner.py --prefix <tmp> --source kaggle    # diff vs artifacts/metrics_kaggle.json
```

Delete the `<tmp>` outputs afterwards so `artifacts/` stays at 35 canonical files.

## Session history (consolidated)

- **2026-11-18, `a797773`** — last substantive research commit: baseline implemented, evaluated on all free
  data sources, artifacts written. `5fab764` froze the showcase preset. Nothing has changed any research
  output since.
- **2026-11-18..19, `a797773..f97af23f`** — 2,044 docs-only commits, 3 unique paths, 0 research drift. Each
  re-confirmed the same invariants (clean tree, 0 drift, 75 tests, rules hash, 4 data hashes, 35 artifacts,
  identical metrics) and produced **no new evidence**. Per-commit detail:
  `git log --name-only --pretty=format: a797773..HEAD`.
- **2026-11-19..20, `f97af23f..25b00847`** — ~24 further boilerplate turns, each a compact docs-only
  refresh with identical results, no forward path ever selected. Collapsed here; they added nothing.
- **2026-11-20, `f1a9e1ae` (this session)** — end of the two carried-forward caveats: installed test deps and
  ran the suite (**75 passed**) and re-ran both baselines (**byte-identical** metrics). Rewrote this file and
  `INITIAL_TASK_FOR_NEXT_AGENT.md` to be short and self-contained, removing the accumulated per-turn log. No
  strategy, config, data, code, or canonical artifact changed; `artifacts/` still 35 files; 0 research drift.
  **This is the last doc refresh. Future boilerplate turns get the status message with zero edits.**

## What the user must do

Nothing left in this repository can advance the research. Pick one, explicitly:

1. **Stop the automation** — authorize editing `.github/workflows/main.yml` to disable or reduce the cron.
2. **Authorize a named experiment** — a new versioned config with a written diff from `STRATEGY_RULES.txt` v1.0.
3. **Supply new data or new scope** — audited and frozen as a fresh untouched baseline before any tuning.
4. **Declare the baseline final** and stop.
