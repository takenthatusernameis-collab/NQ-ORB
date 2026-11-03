# Initial Task for Next Agent

# Initial Task for Next Agent

## Status (session 2026-11-03 — maintenance re-verification, sixty-first pass, COMPLETE)
- On branch main; working tree clean; up to date with origin/main; HEAD c482b7d (chore(kilo): checkpoint agent session).
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1, config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4, raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37, raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99, raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7, raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Raw date ranges re-checked from disk: axb0306 series ends 2026-04-15 (1min last bar 2026-04-15T23:29, 15min last bar 2026-04-15T23:15); Kaggle front-month ends 2025-11-12 (1min 2025-11-12T23:59, 15min 2025-11-12T23:45). Unchanged from prior captures.
- Canonical artifacts verified present + parseable; walk-forward artifacts verified programmatically (all windows negative on both sources).
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; working tree clean.
- Free-data re-sweep: no new genuinely free MNQ 1min/15min source found. No data purchased; no credentials requested/stored.

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
This is a maintenance/re-verification session, not a feature session. Do NOT tune stops, targets, filters, sizing, or session times — STRATEGY_RULES.txt v1.0 is frozen. The only authorized work is (a) re-verifying the frozen baseline is intact and reproducible, (b) watching for a new genuinely free MNQ 1min/15min data source (record provenance + SHA-256 before any use), and (c) refreshing HANDOFF.md / this file. All prior baselines are negative under full costs across every walk-forward window; the constraint is data depth (~3 months axb0306, ~3 years Kaggle front-month), not code.
