# Initial Task for Next Agent — NQ ORB

## Current priority
Maintenance/documentation. Free-data search re-checked MarketParquet (1-min is paid; only daily free), FirstRate Data (paid subscription), Portara (paid), Yahoo Finance (daily only), Kaggle (NQ only, not MNQ). No new genuinely free MNQ 1-min/15-min source located. Existing free sources remain axb0306 (~3 months) and Kaggle front-month (~3 years, unadjusted). Do not change strategy rules or parameters.

## Frozen baseline (do not modify)
- STRATEGY_RULES.txt v1.0
- config/orb_mnq_15m_showcase.yaml
- Baselines: axb0306 = 60 trades, net -$31,637.98; Kaggle front-month = 688 trades, net -$626,525.96

## Required next actions
1. Re-run full test suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` (expect 66 passed).
2. Re-verify raw data hashes (unchanged).
3. Continue searching for genuinely free MNQ 1-min/15-min sources; document provenance and sha256 hashes before use. Do not purchase data. If downloaded, re-run chronological splits and cost sensitivity across full periods.
4. Update FEASIBILITY_REPORT.md, HANDOFF.md, and this file with evidence.

## Constraints
- No parameter optimization, no strategy-rule changes, no broker integration, no live/paper orders.
- Historical research/simulation only. Do not purchase data.
- Do not present synthetic results as market evidence.
- Distinguish implementation tests from empirical evaluation.

## Verification command
`PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` (expect 66 passed)
