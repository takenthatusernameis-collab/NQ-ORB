# Initial task for next agent — NQ ORB

Date: 2026-10-31

## Current state (read HANDOFF.md first)
- Frozen baseline preserved: `STRATEGY_RULES.txt` v1.0, `config/orb_mnq_15m_showcase.yaml` unchanged. No strategy/parameter changes.
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` -> 66 passed.
- Raw data hashes unchanged: MNQ_15min f417f22d..., MNQ_1min 129623f4..., Kaggle front-month 15min 7e129ae3..., 1min edbadc73....
- Canonical baselines (deterministic, cost-aware): axb0306 60 trades, net -$31,637.98 (gross -$7,662.00, PF 0.492, WR 70.0%); Kaggle front-month 688 trades, net -$626,525.96 (gross -$140,899.00, PF 0.227, WR 64.83%). Artifacts match byte-for-byte on re-run.
- Free-data search: only axb0306 (~3 months, single-contract MNQ.M26 unadjusted) and Kaggle front-month (~3 years, unadjusted front-month by max volume) are genuinely free. Yahoo daily only. MarketParquet/historicalfuturesdata.com/Portara/FirstRate excluded as paid. No longer free MNQ 1min/15min sources found.

## Priority (maintenance/documentation only; do not change baseline)
1. **Free data sweep**: If any genuinely free MNQ 1min/15min source appears, download with provenance (URL/repo, retrieval time, license), compute sha256 hashes for raw CSVs, update `data/FEASIBILITY_REPORT.md`, and record in `HANDOFF.md` before using. Exclude paid sources.
2. **Integrity checks**: On each verification session, re-run tests, re-verify raw hashes, and confirm canonical baselines match `artifacts/metrics_axb0306.json` and `artifacts/metrics_kaggle.json` (byte-for-byte). Re-run baselines via `src/orb/runner.py` if artifacts ever look stale.
3. **Evidence hygiene**: Keep `data/FEASIBILITY_REPORT.md`, `HANDOFF.md`, and this file updated with commands/results/hashes/blockers/next task. Add notes to `artifacts/README.md` if new artifact classes appear.
4. **No baseline changes**: No parameter/strategy/rule changes without a separately named versioned experiment with explicit diff from frozen baseline. No broker integration, no live/paper orders, no data purchases.

## Suggested commands
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q`
- Hashes: `sha256sum raw/MNQ_*.csv raw/MNQ_*frontmonth.csv`
- Baselines: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python src/orb/runner.py --source axb0306 --prefix axb0306_verify && PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python src/orb/runner.py --source kaggle --prefix kaggle_verify`

## Blockers
- History depth limited (axb0306 ~3m, Kaggle front-month ~3y unadjusted). Insufficient for robust walk-forward/OOS.
- Costs dominate (both samples negative under full costs).
- axb0306 continuous/roll adjustment undocumented; Kaggle is front-month unadjusted.

Complete the above maintenance, update `HANDOFF.md`, update this file, and leave evidence.
