# NQ ORB — Durable handoff

## Status: TERMINAL — research complete; awaiting explicit user decision

The frozen MNQ 15-minute ORB baseline is implemented, tested, and evaluated on every available
free MNQ data source. It is **negative-net on all datasets** under full costs, and the free-data
search is exhausted (see `data/FEASIBILITY_REPORT.md`). Do not start further autonomous research,
experiments, automation changes, or handoff-only checkpoints without an explicit user decision.

## Verified state (re-verified this session, 2026-11-16, HEAD `57cba7a`)

- `git rev-parse --short HEAD`: `57cba7a`; working tree clean (`git status --short` empty).
  `57cba7a` ("chore(kilo): checkpoint agent session") touches only `HANDOFF.md` and
  `INITIAL_TASK_FOR_NEXT_AGENT.md` (doc-only checkpoint; no research drift). Prior handoff HEAD
  `3b800a5`; diff `3b800a5..57cba7a` touches only `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`.
- `git diff --name-only a797773..57cba7a`: only `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`,
  and `research_state/workflow_run_diagnostics.jsonl` (the diagnostics file is runtime/controller log
  capture, not research code, data, or a strategy artifact; excluded from the research-drift check).
- `sha256sum STRATEGY_RULES.txt`: `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (frozen v1.0).
- `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts`: empty (zero research drift vs last substantive research commit `a797773`).
- Baseline context: frozen showcase preset at `5fab764`; last substantive research commit `a797773`.
- `artifacts/`: 35 files, 0 `*manifest*` files.
- Test suite: `python3 -m pytest tests -q` -> **75 passed** (re-run this session).
- Raw data SHA-256 (all unchanged):
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`

## Canonical metrics (unchanged; re-read from artifacts this session)

### axb0306 — single-contract MNQ.M26, 2026-01-20..2026-04-15, no roll / no adjustment
- 60 trades (33 long / 27 short); win rate 70.0%
- gross -7,662.00; net -31,637.98; costs 23,975.98; avg R -0.0431; expectancy -527.30/trade
- profit factor 0.4917; max DD 37,491.80; Sharpe -1.06; Sortino -0.67
- worst day 2026-01-27 (-3,811.28); longs -17,601.84; shorts -14,036.14
- 1-minute data supports exact 15:55 ET flatten / intrabar ordering on all 60 trade days.
- Source: `artifacts/metrics_axb0306.json`, `artifacts/trades_axb0306.json`

### Kaggle front-month — unadjusted front-month by max volume, 2022-11-16..2025-11-12
- 688 trades (359 long / 329 short); win rate 64.83%
- gross -140,899.00; net -626,525.96; costs 485,626.96; avg R -0.0684; expectancy -910.65/trade
- profit factor 0.2271; max DD 626,994.56; Sharpe -1.68; Sortino -1.04
- worst day 2023-05-12 (-4,789.80); longs -287,054.04; shorts -339,471.92
- Source: `artifacts/metrics_kaggle.json`, `artifacts/trades_kaggle.json`

## Key facts

- The 0.4R target implies a pre-cost break-even win rate of 71.43%; both datasets fall short after
  costs, and losses are ~2.7x wins in R. Gross P&L is also negative, so costs are not the only issue.
- Costs (commission + exchange/clearing $2.87/side, 1 tick adverse slippage) dominate net results.
- Independent signal-funnel cross-check reproduces engine trade counts exactly (axb0306 60, kaggle 688).
- No paid/proprietary data used; no credentials requested or stored; free-source search exhausted.
- `research_state/workflow_run_diagnostics.jsonl` is controller/runtime log capture (GitHub Actions run diagnostics), not research code, data, or a strategy artifact; it is excluded from the research-drift check.

## Prior session trail

Repeated independent Kilo verifications (2026-10-31 through 2026-11-16) all confirmed the same
terminal state: frozen rules hash, zero drift vs `a797773`, 35 artifacts / no manifests, unchanged
canonical metrics, and 75 passing tests. HEAD advanced only via `chore(kilo): checkpoint agent
session` and `chore(kilo): consolidate terminal-state handoff...` commits touching handoff /
  next-agent docs; no research drift. Latest: `57cba7a` re-verified 2026-11-16 (rules hash
`6d3258c3...`, zero research drift vs `a797773`, 35 artifacts / 0 manifests, 75 tests passed, metrics unchanged).
Granular per-session entries are preserved in git history.

## Required action for next agent

**Do not start autonomous research and do not create handoff-only checkpoints on generic prompts.**
Report the terminal state and await an explicit user decision.

Legitimate forward paths (only with explicit user authorization):
- **(a)** Stop/reduce maintenance automation (`.github/workflows/main.yml:11`, cron) — requires explicit authorization for that exact change.
- **(b)** Run a separately versioned, named experiment with an explicit diff from the frozen baseline (e.g. far-side-of-range stop per `STRATEGY_RULES.txt` §2.1) — requires explicit authorization and a named experiment design.
- **(c)** Accept the baseline as final — requires explicit user confirmation.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

## Verification commands

```bash
git status --short
git rev-parse --short HEAD
sha256sum STRATEGY_RULES.txt
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
ls artifacts | wc -l && ls artifacts | grep -c manifest || true
sha256sum raw/MNQ_15min.csv raw/MNQ_1min.csv
python3 -m pytest tests -q   # if pytest + pandas installed
```