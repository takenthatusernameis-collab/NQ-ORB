# Initial Task for Next Agent

> **Message from prior agent (2026-11-18, HEAD `555bd7ee`):**
>
> NQ/MNQ ORB research is **complete and terminal**. The frozen MNQ 15-minute ORB baseline is
> implemented, tested, and evaluated on every free data source available; it is negative-net on all of
> them. The free-data search is exhausted, and the required performance-reporting surface is already
> produced (`monthly_net_pnl`, `yearly_net_pnl`, `sharpe_r`, `sortino_r`, `exposure_pct`,
> `cost_sensitivity`, `chronological_splits`, `signal_close_entry_sensitivity`, `walk_forward_*.json`).
>
> State was re-verified at `1ba05c42`: empty research-drift check, 75 tests passing, `STRATEGY_RULES.txt`
> and all four raw-data hashes unchanged, `artifacts/` 35 files. If you are reading this and nothing in
> `artifacts config src tests raw data scripts` has changed since `a797773`, there is **no** work here.

## Do exactly this — and nothing else

1. Read `HANDOFF.md`: *Status*, *STOP RULE*, *Key facts*, *Forward paths*.
2. Send the user **one** short message: the table below, the statement that a 0.4R target needs a
   71.43% pre-cost win rate (both datasets miss it and gross P&L is negative too), that 75 tests pass,
   and forward paths (a)/(b)/(c).
3. Then **stop**. Do not re-run verification, do not rewrite `HANDOFF.md` or this file, do not recount
   artifacts, and do not make a commit. If your turn would produce only a commit touching these two
   files, you have added nothing — make no commit at all.

This is the loop-terminating instruction. There is no remaining research work under the current scope,
and no verification you can run produces new evidence: the last five sessions re-derived the identical
hashes, test count, drift check, and metrics.

The loop cannot terminate itself: each session is resumed by the `.github/workflows/main.yml` cron and
each session's only ostensible deliverable is a docs-only commit. Therefore, when your turn ends, end it
by asking the user, in one line, to authorize **either (a)/(c) to stop or reduce the cron** or the
specific scope of a new experiment (b). Do not ask for a re-verification and do not schedule any
follow-up.

## Numbers to report

| Dataset | Trades | Split | Win % | Gross $ | Net $ | Costs $ | PF | Exp/trade | Gross R | Net R |
|---|---|---|---|---|---|---|---|---|---|---|
| axb0306 (MNQ.M26, 2026-01-20..2026-04-15) | 60 | 33L/27S | 70.00 | -7,662.00 | -31,637.98 | 23,975.98 | 0.4917 | -527.30 | -0.0431 | **-0.1773** |
| Kaggle front-month (2022-11-16..2025-11-12) | 688 | 359L/329S | 64.83 | -140,899.00 | -626,525.96 | 485,626.96 | 0.2271 | -910.65 | -0.0684 | **-0.3046** |

`avg_r` in the artifacts is gross/price-based; net R above is recomputed from the ledgers. Position
sizing at $3,000 risk with a 0.4xATR stop implies 29-278 MNQ contracts, so cost drag scales with size
and dominates the result. No trade in either ledger exits via the 15:55 ET flatten.

## Forward paths (each requires explicit user authorization for that exact scope)

- **(a)** Stop or reduce the maintenance automation (`.github/workflows/main.yml` cron). This is the only
  action that actually ends the docs-only checkpoint loop. Not permitted without explicit approval for
  that exact edit.
- **(b)** Run a separately versioned, named experiment with an explicit diff from the frozen baseline
  (cost-model sensitivity, entry-timing variant, or a pre-registered parameter study). Never mutate
  `STRATEGY_RULES.txt` or existing canonical artifacts, and never tune to improve reported results.
- **(c)** Accept the baseline as final and stop the automation.

If the user supplies new free data or a new scope: audit first (source, license/access, retrieval time,
contract months, timezone, timestamps, gaps, roll rule, adjustment, hashes) before writing or running
any pipeline.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with an explicit diff from the frozen baseline.
- Do not edit `.github/workflows/main.yml`, the controller, permissions, or automation policy without
  explicit authorization for that exact change.
