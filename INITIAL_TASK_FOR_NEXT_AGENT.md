# Initial Task for Next Agent

## Status (session 2026-11-02 — maintenance re-verification, COMPLETE)
- Prior agent task read from HANDOFF.md + INITIAL_TASK_FOR_NEXT_AGENT.md; re-derived evidence rather than trusting prior claims.
- `git status`: working tree clean (branch main, up to date with origin/main, HEAD 54953bd).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed.
- SHA-256 recomputed from disk; all six hashes match recorded values exactly (STRATEGY_RULES.txt, config/orb_mnq_15m_showcase.yaml, raw/MNQ_15min.csv, raw/MNQ_1min.csv, raw/MNQ_1min_frontmonth.csv, raw/MNQ_15min_frontmonth.csv).
- Canonical artifacts verified from disk: axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD ~$626,994.56.
- Walk-forward artifacts present (artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json): all test windows negative on both sources.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; working tree clean.

## Bounded next task
1. **Maintenance only (default).** Re-verify repo state (git status, hashes, artifacts, walk-forward). Run tests if needed (`PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q`).
2. **Data monitoring.** If a new genuinely free MNQ 1min/15min source appears, record provenance/hashes before use (only axb0306 ~3mo single-contract MNQ.M26 unadjusted and Kaggle front-month ~3yr unadjusted front-month by max volume are known free sources).
3. **No experiments without approval.** No parameter/strategy changes without a separately named, versioned experiment with an explicit diff from frozen baseline (STRATEGY_RULES.txt v1.0).
4. **Update docs.** Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with evidence if anything changes.
5. **Blockers:** Research blocked on data depth; both negative under full costs; all walk-forward windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.

## Test command
- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` (71 passed)

## Hard boundaries (AGENTS.md)
- Historical research and simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.