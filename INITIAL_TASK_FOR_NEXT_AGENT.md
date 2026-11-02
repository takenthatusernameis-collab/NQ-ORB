# Initial Task for Next Agent

## Status (session 2026-11-02 — maintenance re-verification, COMPLETE)
- Prior agent task read from HANDOFF.md + INITIAL_TASK_FOR_NEXT_AGENT.md; re-derived evidence rather than trusting prior claims.
- On branch main; working tree clean; up to date with origin/main (HEAD e3df816).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed.
- SHA-256 recomputed from disk; all six hashes match recorded values exactly (STRATEGY_RULES.txt 6d3258c3...; config 2a6c5ff8...; raw/MNQ_15min.csv f417f22d...; raw/MNQ_1min.csv 129623f4...; raw/MNQ_1min_frontmonth.csv edbadc73...; raw/MNQ_15min_frontmonth.csv 7e129ae3...).
- Canonical artifacts verified from disk: axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD ~$626,994.56.
- Walk-forward artifacts present (artifacts/walk_forward_axb0306.json 3 windows all negative net; artifacts/walk_forward_kaggle.json 8 windows all negative net).
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
- No new genuinely free MNQ 1min/15min source found beyond axb0306 and Kaggle front-month; Yahoo Finance is daily only; Databento/DBN-cache requires a key (key-gated, no credentials stored).
- If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods; preserve a final untouched OOS interval.
