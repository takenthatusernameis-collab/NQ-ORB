# Initial Task for Next Agent

## Status (session 2026-11-02 — maintenance re-verification, COMPLETE)
- Prior agent task read from HANDOFF.md + INITIAL_TASK_FOR_NEXT_AGENT.md; re-derived evidence rather than trusting prior claims.
- `git status`: clean (branch main, up to date with origin/main, HEAD 924f82d).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; working tree clean.

## Bounded next task
1. **Maintenance only (default).** Re-verify repo state (git status, hashes, artifacts, walk-forward). Run tests if needed (`PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q`).
2. **Data monitoring.** If a new genuinely free MNQ 1min/15min source appears, record provenance/hashes before use.
3. **No experiments without approval.** No parameter/strategy changes without a separately named, versioned experiment with an explicit diff from frozen baseline (STRATEGY_RULES.txt v1.0).
4. **Update docs.** Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with evidence if anything changes.
5. **Blockers:** Research blocked on data depth (axb0306 ~3mo single-contract, Kaggle ~3yr front-month unadjusted); both negative under full costs; all walk-forward windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.

## Test command
- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` (71 passed)

## Hard boundaries (AGENTS.md)
- Historical research and simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
