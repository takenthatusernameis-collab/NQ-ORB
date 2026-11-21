# Initial Task for Next Agent

Read `HANDOFF.md` first — it is authoritative and complete. This page is the short version.

## State at HEAD `55280466` (2026-11-21): TERMINAL
There is **no pending code, data, pipeline, or experiment work**. The frozen MNQ 15-minute ORB baseline
(`STRATEGY_RULES.txt` v1.0) is implemented, tested (75 passing), and evaluated on every free MNQ dataset
available. It is **negative-gross and negative-net on all of them**, and the free-data search is exhausted
(`data/FEASIBILITY_REPORT.md`). Nothing here can change a number until the user picks a forward path or
supplies new data.

## Your job

1. Read `HANDOFF.md`.
2. If the instruction is generic — "read the prior task and complete it", "continue", "update the handoff",
   "write the initial task for the next agent" — reply with the terminal status, the numbers table below, and
   the four forward paths, then **stop. No file edits, no test/drift/artifact re-checks, no commit.** Writing
   this page again is a no-op that only adds a docs-only commit.
3. If the user names a specific change or a forward path (a)–(d), do exactly that scope and nothing wider.
   Only refresh this file when a verified fact, the HEAD reference, or the available data genuinely changed.

## Numbers to report

| Dataset | Trades | L/S | Win % (net) | Gross $ | Net $ | Costs $ | PF | Exp/trade | Gross R | Net R |
|---|---|---|---|---|---|---|---|---|---|---|
| axb0306 (MNQ.M26, 2026-01-20..2026-04-15) | 60 | 33/27 | 70.00 | -7,662.00 | -31,637.98 | 23,975.98 | 0.4917 | -527.30 | -0.043 | **-0.18** |
| Kaggle front-month (2022-11-16..2025-11-12) | 688 | 359/329 | 64.83 | -140,899.00 | -626,525.96 | 485,626.96 | 0.2271 | -910.65 | -0.068 | **-0.30** |

Max drawdown $37,491.80 / $626,994.56. Source: `artifacts/metrics_axb0306.json`, `artifacts/metrics_kaggle.json`
(re-verified 2026-11-21 at HEAD `55280466`; `gross − net == costs` to the cent on both).

## The key finding

The 0.4R target requires a **71.43% pre-cost win rate**. Observed gross win rates are 70.00% / 69.48% and
gross P&L is already negative, so this is a **strategy-edge failure, not a cost-only failure**. All 12 cost
scenarios are net-negative, and no out-of-sample chronological segment is net positive (the only positive
segment is the in-sample axb0306 train window — an overfit signature).

## Forward paths (each needs explicit user authorization for that exact scope)

- **(a)** Stop or reduce the maintenance automation (`.github/workflows/main.yml`, cron `*/5 * * * *`).
  This agent must not touch it unilaterally. **The only path that ends the docs-only loop.**
- **(b)** One named, versioned experiment with a written diff from the frozen baseline (cost model,
  entry timing, or a pre-registered parameter study). Never mutate `STRATEGY_RULES.txt` or `artifacts/`,
  never tune to improve reported results.
- **(c)** Accept the baseline as final and stop the automation.
- **(d)** Supply new free data or a new scope — audited (source, license/access, retrieval time, contract
  months, timezone, timestamps, gaps, roll rule, adjustment, hashes), then frozen as a fresh untouched
  baseline before any tuning.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical `artifacts/`.
- Any strategy/rule change = separately named, versioned experiment with an explicit diff from the baseline.
- Do not edit `.github/workflows/main.yml`, controller code, permissions, or automation policy without
  explicit authorization.
- Do not delete research evidence or rewrite Git history to conceal a failure.

## Verification (only inside an authorized research or refresh session)

```bash
git status --short && git rev-parse --short HEAD
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts   # expect 0 files
sha256sum STRATEGY_RULES.txt raw/*.csv                                            # compare with HANDOFF.md
pip install pytest numpy pandas && python3 -m pytest tests -q                       # last run: 75 passed
python3 src/orb/runner.py --prefix <tmp> --source axb0306   # diff vs artifacts/metrics_axb0306.json
python3 src/orb/runner.py --prefix <tmp> --source kaggle    # diff vs artifacts/metrics_kaggle.json
```

Delete the `<tmp>` outputs afterwards so `artifacts/` stays at 35 canonical files.
