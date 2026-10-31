# Initial Task for Next Agent — NQ ORB

## Current priority
Maintenance/documentation only. No new free MNQ 1min/15min source has been found beyond the two documented sources (axb0306/cme-futures-ohlc and Kaggle brandenmorris/mnq-1-minute-data front-month). Continue verification and documentation; do not change strategy rules or parameters.

## Frozen baseline (do not modify)
- STRATEGY_RULES.txt v1.0
- config/orb_mnq_15m_showcase.yaml
- Baselines: axb0306 = 60 trades, net -$31,637.98; Kaggle front-month = 688 trades, net -$626,525.96

## Required next actions
1. Re-run full test suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` (expect 66 passed).
2. Re-verify raw data hashes:
   - raw/MNQ_15min.csv: f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37
   - raw/MNQ_1min.csv: 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99
   - raw/MNQ_15min_frontmonth.csv: 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4
   - raw/MNQ_1min_frontmonth.csv: edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7
3. Search for new free MNQ 1min/15min sources (GitHub, Kaggle, other public repos). If found, document provenance and hashes in data/FEASIBILITY_REPORT.md before use. Do not purchase data.
4. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods.
5. Update FEASIBILITY_REPORT.md, HANDOFF.md, and this file with evidence.

## Constraints
- No parameter optimization, no strategy-rule changes, no broker integration, no live/paper orders.
- Historical research/simulation only. Do not purchase data.
- Do not present synthetic results as market evidence.
- Distinguish implementation tests from empirical evaluation.

## Verification command
`PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` (expect 66 passed)
