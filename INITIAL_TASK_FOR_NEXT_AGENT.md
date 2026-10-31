# Initial task for next agent (2026-10-31ah2)

Read HANDOFF.md first. Current priority: maintenance/documentation only (no new free MNQ 1min/15min sources found beyond axb0306 and Kaggle front-month; Yahoo daily only; MarketParquet/historicalfuturesdata.com/Portara/FirstRate excluded as paid).

## Verification checklist
1. Run full test suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` (expect 66 passed).
2. Verify baselines against artifacts: axb0306 60 trades net -$31,637.98 / gross -$7,662.00; Kaggle front-month 688 trades net -$626,525.96 / gross -$140,899.00. Confirm hashes unchanged for raw MNQ_15min/MNQ_1min and Kaggle front-month files.
3. If no new data/code changes needed, just update HANDOFF.md and this file with evidence. Do not change strategy/parameters (frozen baseline). Do not purchase data/add credentials/enable live trading.

## Constraints
- Follow AGENTS.md (historical/simulation only, no broker integration, no credentials, no paid data).
- Frozen baseline: STRATEGY_RULES.txt v1.0, config/orb_mnq_15m_showcase.yaml unchanged.
- Preserve evidence; update FEASIBILITY_REPORT.md if new provenance appears.
- Next bounded task: maintain documentation; record provenance/hashes for any genuinely free MNQ 1min/15min source before use; no parameter/strategy changes without a separately versioned experiment.
