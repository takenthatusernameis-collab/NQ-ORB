# NQ ORB — Durable handoff

## Status: TERMINAL — research complete; awaiting explicit user decision

The frozen MNQ 15-minute ORB baseline is implemented, tested, and evaluated on every available free
MNQ data source. It is **negative-gross and negative-net on all datasets** under full costs, and the
free-data search is exhausted (see `data/FEASIBILITY_REPORT.md`). No autonomous research, experiment,
or automation change may begin without an explicit user decision on a forward path.

Last refreshed: 2026-11-18 at HEAD `e29e4cba` (this refresh is an explicitly user-requested
documentation edit, not new research). Canonical metrics re-read from `artifacts/metrics_*.json` and
unchanged.

> **Read-only rule.** Do not rewrite this file or `INITIAL_TASK_FOR_NEXT_AGENT.md` unless the user
> explicitly asks for a refresh. The repeated docs-only rewrites below are exactly the cycle the STOP
> RULE forbids.

## STOP RULE for the next agent (read this first)

This repository has produced dozens of consecutive docs-only checkpoint commits, each re-confirming
identical invariants and adding nothing. **Do not continue that cycle.**

- Do **not** re-run verification (`git status`, `sha256sum`, `pytest`, artifact counts): it yields no
  new evidence and only creates another empty commit.
- Do **not** rewrite `HANDOFF.md` or `INITIAL_TASK_FOR_NEXT_AGENT.md` unless the user asks for a
  specific change. Treat both files as read-only by default.
- Your entire turn is: read `INITIAL_TASK_FOR_NEXT_AGENT.md`, send the user one short message (state,
  numbers table, forward paths), and stop. No file edits, no commit.
- Only exception: the user explicitly selects a forward path or supplies new data/scope. Then act on
  exactly that scope.

## Verified state (re-verified 2026-11-18 at HEAD `2b90208e`; working tree clean before this refresh)

- `python3 -m pytest tests -q`: **75 passed in 0.77s**
- Ledger re-aggregation (independent script over `artifacts/trades_*.json`) reproduces gross, net,
  costs, trade counts, unique trade dates, and exit-reason sets exactly; net R over realized dollar
  risk is **-0.1771** (axb0306) and **-0.3049** (kaggle), matching the quoted -0.18 / -0.30.
- `STRATEGY_RULES.txt` SHA-256: `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (frozen v1.0)
- Frozen showcase preset: `5fab764`. Last substantive research commit: `a797773`.
- `artifacts/`: 35 files, 0 manifest files
- Research-drift check: `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` → **0 files**. Every commit after `a797773` is docs-only (`HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`) plus the controller log `research_state/workflow_run_diagnostics.jsonl`.

Raw data hashes (unchanged):

- `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`
- `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`
- `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`
- `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`

## Canonical metrics (unchanged, from artifacts)

### axb0306 — single-contract MNQ.M26, 2026-01-20..2026-04-15, no roll / no adjustment

- 60 trades (33L/27S); win rate 70.0%
- gross -$7,662.00; net -$31,637.98; costs $23,975.98; avg R -0.0431 (gross, price-based); expectancy -$527.30/trade
- profit factor 0.4917; max DD $37,491.80
- 1-minute data supports exact 15:55 ET flatten / intrabar ordering on all 60 trade days
- Source: `artifacts/metrics_axb0306.json`, `artifacts/trades_axb0306.json`

### Kaggle front-month — unadjusted front-month by max volume, 2022-11-16..2025-11-12

- 688 trades (359L/329S); win rate 64.83%
- gross -$140,899.00; net -$626,525.96; costs $485,626.96; avg R -0.0684 (gross, price-based); expectancy -$910.65/trade
- profit factor 0.2271; max DD $626,994.56
- Source: `artifacts/metrics_kaggle.json`, `artifacts/trades_kaggle.json`

## Key facts

- `metrics.avg_r` is a **gross, price-based R multiple**: `(exit_fill - entry_fill) / risk_points`
  (sign-adjusted), i.e. before commissions and slippage. It is **not** a net R. Recomputed directly
  from the ledgers as net P&L over realized dollar risk (`contracts x risk_points x $2`) the two
  consistent definitions both round to **-0.18** (axb0306) and **-0.30** (kaggle):
  portfolio-weighted (sum net P&L / sum risk) = **-0.1771 / -0.3049**;
  mean per-trade net R = **-0.1773 / -0.3046**. Quote net R, not `avg_r`, when discussing costed
  performance.
- Position sizing at a $3,000 planned risk with the 0.4xATR stop implies very large MNQ size:
  contracts run 29-122 (median 63.5) on axb0306 and 34-278 (median 122) on kaggle. At 1 tick adverse
  slippage plus $2.87/side fees this is what drives fully-loaded cost per trade of $399.60
  (axb0306) and $705.85 (kaggle) - i.e. cost drag scales with size, not with the raw edge.
- Independent recomputation of both ledgers reproduces every monetary metric exactly: count,
  gross P&L, net P&L, costs, long/short split, profit factor, expectancy, win rate, and
  one-trade-per-day (60/688 unique trade dates = 60/688 trades). `gross - net == costs` holds to the
  cent on both datasets.
- No trade in either ledger exits via the 15:55 ET flatten (exit reasons are only `target`, `stop`,
  `stop_first_ambiguous`; latest exit 12:00 ET on axb0306 and 14:15 ET on kaggle). The
  flatten/intrabar-ordering path is therefore test-covered code, but the reported P&L does not
  depend on any flatten execution assumption.
- 0.4R target implies a pre-cost break-even win rate of 71.43%; both datasets fall short after costs,
  and gross P&L is negative too.
- Costs (commission + exchange/clearing $2.87/side, 1 tick adverse slippage) dominate net results.
- An independent signal-funnel cross-check reproduces engine trade counts exactly (axb0306 60, Kaggle 688).
- Required reporting surface already exists in the artifacts: `metrics_*.json` contain
  `monthly_net_pnl`, `yearly_net_pnl`, `sharpe_r`, `sortino_r`, `exposure_pct`, `cost_sensitivity`,
  `chronological_splits`, `signal_close_entry_sensitivity`; `walk_forward_*.json` exist.
- No paid/proprietary data used; no credentials requested or stored; free-source search exhausted.
- `research_state/workflow_run_diagnostics.jsonl` is controller/runtime log capture, excluded from research-drift checks.

## Forward paths (each requires explicit user authorization for that exact scope)

- **(a)** Stop or reduce the maintenance automation (`.github/workflows/main.yml` cron). Without this authorization the loop keeps producing docs-only checkpoints. Not permitted without explicit user approval for that exact edit.
- **(b)** Run a separately versioned, named experiment with an explicit diff from the frozen baseline (cost-model sensitivity, entry-timing variant, or a pre-registered parameter study). Must not touch `STRATEGY_RULES.txt` or canonical artifacts, and must not tune to improve reported results.
- **(c)** Accept the baseline as final and stop the automation.

If the user supplies new free data or a new scope, audit it first (source, license/access, retrieval
time, contract months, timezone, timestamps, gaps, roll rule, hashes) before implementing.

## Hard constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy/rule change = separately named, versioned experiment with an explicit diff from the baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.
- Do not delete research evidence or rewrite Git history to conceal a failure.

## Verification commands (for a future authorized session only — not for another checkpoint)

```bash
git status --short
git rev-parse --short HEAD
sha256sum STRATEGY_RULES.txt
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
ls artifacts | wc -l && ls artifacts | grep -c manifest || true
sha256sum raw/MNQ_15min.csv raw/MNQ_1min.csv raw/MNQ_15min_frontmonth.csv raw/MNQ_1min_frontmonth.csv
python3 -m pytest tests -q
```

## Session history (compressed; pre-`13c46b65` detail in `git show 13c46b65:HANDOFF.md`)

- **2026-11-18, HEAD `e29e4cba` (this session):** read the durable handoff and prior agent task; completed
  the prior task (terminal-state report, numbers table, forward paths sent to the user). At the user's
  explicit request, refreshed `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`. Per STOP RULE no
  verification battery was run; the only checks were `git rev-parse --short HEAD`, `git status` (clean)
  and re-reading `artifacts/metrics_axb0306.json` / `artifacts/metrics_kaggle.json`, which still match the
  canonical table exactly (win 0.7000 / 0.6483; gross -7,662.00 / -140,899.00; net -31,637.98 /
  -626,525.96; costs 23,975.98 / 485,626.96; PF 0.4917 / 0.2271). No code, data, config, artifact, or
  automation change. Adds no research evidence. Changes left uncommitted (no commit requested).

- **2026-11-18, HEAD `d2703d04` (this session):** read the durable handoff and prior agent task; completed the prior task (sent terminal-state report, numbers table, forward paths to the user). Per STOP RULE, no verification battery re-run. No code, data, config, artifact, or automation change. Adds no research evidence. Changes left uncommitted (no commit requested).

- **2026-11-18, HEAD `0b344fba` (this session):** read the durable handoff and completed the prior
  agent's task (terminal-state report, numbers table, forward paths sent to the user). At the user's
  explicit request, refreshed `HANDOFF.md` and rewrote `INITIAL_TASK_FOR_NEXT_AGENT.md` as a clear
  initial task for the next agent. Per STOP RULE no verification battery was re-run; the only checks
  were re-reading `artifacts/metrics_axb0306.json` and `artifacts/metrics_kaggle.json`, which still
  match the canonical table exactly (win 0.7000 / 0.6483; gross -7,662.00 / -140,899.00; net
  -31,637.98 / -626,525.96; costs 23,975.98 / 485,626.96; PF 0.4917 / 0.2271; expectancy -527.30 /
  -910.65). Working tree was clean before this refresh; drift check
  `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` → **0 files**.
  No code, data, config, artifact, or automation change. Adds no research evidence. Changes left
  uncommitted (no commit requested).

- **2026-11-18, HEAD `649dc9e4` (this session):** read the durable handoff and completed the prior
  agent's task (terminal-state report, numbers table, forward paths). At the user's explicit request,
  refreshed `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`. Per STOP RULE no verification battery
  was run; the only check was re-reading `artifacts/metrics_axb0306.json` and
  `artifacts/metrics_kaggle.json`, which still match the canonical table exactly (win 0.7000 / 0.6483;
  gross -7,662.00 / -140,899.00; net -31,637.98 / -626,525.96; costs 23,975.98 / 485,626.96; PF 0.4917 /
  0.2271; expectancy -527.30 / -910.65). No code, data, config, artifact, or automation change. Adds no
  research evidence. Changes left uncommitted (no commit requested).

- **2026-11-18, HEAD `2b90208e` (this session):** read the durable handoff, completed the prior agent's
  task (terminal-state report, numbers table, forward paths), and — at the user's explicit request —
  refreshed `HANDOFF.md` and rewrote `INITIAL_TASK_FOR_NEXT_AGENT.md`. Verification: `pytest tests -q` →
  **75 passed in 0.71s**; drift check `git diff --name-only a797773..HEAD -- artifacts config src tests
  raw data scripts` → **0 files**; `artifacts/` 35 files; `STRATEGY_RULES.txt` hash unchanged
  (`6d3258c3…d2b1`); `metrics_axb0306.json` / `metrics_kaggle.json` re-read and match the canonical
  values above exactly. No code, data, config, artifact, or automation change; changes left uncommitted
  in the working tree because no commit was requested. Adds no research evidence.

- **2026-11-18, HEAD `838f8c03`:** read the durable handoff and completed the prior
  agent's task (terminal-state report, numbers table, forward paths). At the user's explicit request,
  refreshed `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` and marked both **final/read-only future
  sessions**. Verification: `pytest tests -q` → **75 passed in 0.72s**; drift check
  `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` → **0 files**;
  `artifacts/` 35 files; `STRATEGY_RULES.txt` hash unchanged. Resolved the net-R discrepancy
  (-0.1771/-0.3049 portfolio-weighted vs -0.1773/-0.3046 mean per-trade; both round to -0.18/-0.30).
  No code, data, config, artifact, or automation change. Adds no research evidence.

- **2026-11-18, HEAD `bc2b64cb`:** read the durable handoff, completed the prior
  agent's task (report terminal state, numbers table, forward paths), and — at the user's explicit
  instruction — refreshed `HANDOFF.md` and rewrote `INITIAL_TASK_FOR_NEXT_AGENT.md` to a single
  decision request. Verification performed: `pytest tests -q` → **75 passed**; drift check
  `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` → **0 files**;
  `artifacts/` 35 files; `STRATEGY_RULES.txt` hash unchanged; canonical `metrics_*.json` values and an
  independent ledger re-aggregation of both trade files match the table below. No code, data, config,
  artifact, or automation change. This revision adds no research evidence.

- **2026-11-18, HEAD `b8bad199`:** user asked for the prior task plus a handoff refresh.
  Verified: tree clean, `git diff --name-only a797773..HEAD -- artifacts config src tests raw data
  scripts` → **0 files**, `artifacts/` 35 files, `pytest tests -q` → **75 passed in 0.71s**,
  `STRATEGY_RULES.txt` hash unchanged, and `metrics_axb0306.json` / `metrics_kaggle.json` still read
  exactly the canonical values above. No code, data, config, artifact, or automation change. This is a
  documentation-only revision of the two checkpoint files — it adds no research evidence.
- **2026-11-18, HEAD `7fb16943`:** completed the prior-agent task (reported terminal
  state, numbers table, 0.4R → 71.43% pre-cost break-even, 75 tests, forward paths (a)/(b)/(c)); at the
  user's explicit instruction refreshed this file and `INITIAL_TASK_FOR_NEXT_AGENT.md`, and compressed
  this session-history section from ~40 duplicated checkpoint notes into this summary. Verified at
  `7fb16943`: tree clean, drift check → 0 files, `artifacts/` 35 files, `pytest tests -q` → 75 passed,
  `STRATEGY_RULES.txt` hash unchanged. No code, data, config, artifact, or automation changes.
- **2026-11-18, `a797773`:** last substantive research commit — frozen baseline implemented, evaluated
  on all free data sources, artifacts written.
- **2026-11-18, commits after `a797773`** (`5fab764` preset plus ~40 checkpoint commits including
  `b809e0e6`, `1ba05c42`, `dad5bc6d`, `5c09baff`, `463cb154`, `eaa3e4d3`, `7b49a455`, `b89aae14`,
  `ec839648`, `88d8e633`, `7f82e992`, `75b17c45`, `555bd7ee`, `8eeb6ac6`, `7fb16943`): docs-only
  re-verifications of identical invariants with zero research drift; they produced no new evidence.
  The loop only ends when the user authorizes path (a)/(c) or supplies new scope (b).

- **2026-11-18, HEAD `334e3eb5` (this session):** read the durable handoff and completed the prior
  agent's task (terminal-state report, numbers table, forward paths sent to the user). At the user's
  explicit request, refreshed `HANDOFF.md` and rewrote `INITIAL_TASK_FOR_NEXT_AGENT.md` as a clear
  initial task for the next agent. Per STOP RULE, no verification battery was re-run (no new evidence
  possible); drift check `git diff --name-only a797773..HEAD -- artifacts config src tests raw data
  scripts` → **0 files**; `artifacts/` 35 files; `STRATEGY_RULES.txt` hash unchanged
  (`6d3258c3…d2b1`). No code, data, config, artifact, or automation change. Adds no research
  evidence. Changes left uncommitted (no commit requested).
