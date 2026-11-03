# Initial Task for Next Agent

## Status (session 2026-11-03 — maintenance re-verification, fourteenth pass, COMPLETE)
- On branch main; working tree clean; up to date with origin/main; HEAD 8f16053.
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all windows negative on both sources (axb0306 3/3, Kaggle 8/8).
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; working tree clean.

## Bounded default task
1. **Maintenance only.** Re-verify repo state (git status, file hashes, canonical artifacts, walk-forward artifacts). Run tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q`.
2. **Data monitoring only.** If a new genuinely free MNQ 1min/15min source appears, record provenance + file hashes before any use. Known free sources: axb0306 (~3 months, single-contract MNQ.M26, unadjusted) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Do not purchase data; never store credentials.
3. **No experiments without approval.** No parameter/strategy/rule changes without a separately named, versioned experiment with an explicit diff from frozen STRATEGY_RULES.txt v1.0.
4. **Update docs.** Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence if anything changes.

## Test command
- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` (71 passed)

## Hard boundaries (AGENTS.md)
- Historical research and simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work
- Research blocked on data depth; both baselines negative under full costs; all walk-forward windows negative. Highest-value action remains a bounded free-data re-sweep, not parameter fitting.
- axb0306 roll/adjustment method: single-contract MNQ.M26, no roll inside the sample; repo update script hard-codes one contract ID — re-verify hash and price continuity before using any re-downloaded file.
- Kaggle front-month sample ends 2025-11-12; the final ~2.9 months (2025-08-29 onward, 38 trades) are the preserved untouched out-of-sample interval. No free source extends this without purchase.

## Why this task (for the next agent)
This is a maintenance/re-verification session, not a feature session. Do NOT tune stops, targets, filters, sizing, or session times — STRATEGY_RULES.txt v1.0 is frozen. The only authorized work is (a) re-verifying the frozen baseline is intact and reproducible, (b) watching for a new genuinely free MNQ 1min/15min data source (record provenance + SHA-256 before any use), and (c) refreshing HANDOFF.md / this file. All prior baselines are negative under full costs across every walk-forward windows; the constraint is data depth (~3 months axb0306, ~3 years Kaggle front-month), not code.
