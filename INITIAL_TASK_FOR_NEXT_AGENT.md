# Initial task for next agent (2026-10-31am)

Read HANDOFF.md first. Current priority: maintenance/documentation only (no new genuinely free MNQ 1min/15min sources found beyond axb0306 and Kaggle front-month; Yahoo daily only; MarketParquet/historicalfuturesdata.com/FirstRate/Portara excluded as paid).

## Verification checklist
1. Run full test suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` (expect 66 passed).
2. Re-run both baselines from scratch for determinism:
   - `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python src/orb/runner.py --source axb0306 --prefix axb0306_verify`
   - `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python src/orb/runner.py --source kaggle --prefix kaggle_verify`
   Compare all metric fields against stored canonical artifacts:
   - axb0306: 60 trades net -$31,637.98 / gross -$7,662.00 / PF 0.49167 / WR 70.0%
   - Kaggle front-month: 688 trades net -$626,525.96 / gross -$140,899.00 / PF 0.22709 / WR 64.8256%
3. Verify raw data hashes unchanged:
   - raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37
   - raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99
   - raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4
   - raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7
4. If no new data/code changes needed, just update HANDOFF.md and this file with evidence. Do not change strategy/parameters (frozen baseline). Do not purchase data/add credentials/enable live trading.

## Constraints
- Follow AGENTS.md (historical/simulation only, no broker integration, no credentials, no paid data).
- Frozen baseline: STRATEGY_RULES.txt v1.0, config/orb_mnq_15m_showcase.yaml unchanged.
- Preserve evidence; update FEASIBILITY_REPORT.md if new provenance appears.
- Next bounded task: maintain documentation; record provenance/hashes for any genuinely free MNQ 1min/15min source before use; no parameter/strategy changes without a separately versioned experiment.
