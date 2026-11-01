# Initial Task for Next Agent

## Status (session 2026-11-01 — prior task completed + maintenance re-verification, COMPLETE)
- Prior agent task read from HANDOFF.md + INITIAL_TASK_FOR_NEXT_AGENT.md; re-derived evidence rather than trusting prior claims.
- `git status`: working tree clean (branch main, up to date with origin/main, HEAD b14690e).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed.
- SHA-256 recomputed from disk; all six match recorded values exactly (STRATEGY_RULES.txt 6d3258c3…, config 2a6c5ff8…, raw/MNQ_15min.csv f417f22d…, raw/MNQ_1min.csv 129623f4…, raw/MNQ_1min_frontmonth.csv edbadc73…, raw/MNQ_15min_frontmonth.csv 7e129ae3…).
- Canonical artifacts verified: axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD ~$626,994.56.
- Walk-forward artifacts present (artifacts/walk_forward_axb0306.json 3 windows all negative net; artifacts/walk_forward_kaggle.json 8 windows all negative net).
- Free-data sweep re-confirmed: no new genuinely free MNQ 1min/15min source beyond axb0306 (~3 months, single-contract MNQ.M26, unadjusted) and Kaggle front-month (~3 years, unadjusted front-month by max volume); Yahoo daily only. No data purchased; no credentials requested/stored.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; working tree clean.

## Bounded next task
1. **Maintenance only (default).** Re-verify repo state (git status, tests, hashes, artifacts, walk-forward) against HANDOFF.md. Do not change strategy/params/code.
2. **Data monitoring.** If a new genuinely free MNQ 1min/15min source appears, record provenance/hashes (source, URL, retrieval date, symbol/contract, timezone, roll/adjustment method, gaps, SHA-256) before use.
3. **No experiments without approval.** No parameter/strategy changes without a separately named, versioned experiment with an explicit diff from frozen baseline (STRATEGY_RULES.txt v1.0).
4. **Update docs.** If anything changes, update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with evidence.
5. **Blockers:** Research blocked on data depth (axb0306 ~3mo, Kaggle ~3yr front-month) — both negative under full costs; all walk-forward windows negative.

## Test command
- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` (71 passed)

## Hard boundaries (AGENTS.md)
- Historical research and simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
EOF
