# Initial task for next agent

Read the durable handoff first: `HANDOFF.md`. It contains the authoritative current state and the most recent completed work.

## Current priority (maintenance/documentation)
No new free MNQ 1min/15min sources were found beyond axb0306/cme-futures-ohlc and the local Kaggle front-month dataset (brandenmorris/mnq-1-minute-data-5132025-11122025, Databento GLBX.MDP3). Yahoo Finance provides only daily. Paid sources (MarketParquet, historicalfuturesdata.com, Portara, FirstRate) are excluded. Do not purchase data.

## Verification to do (quick)
- Run tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` (expected all passing).
- Confirm raw hashes unchanged: MNQ_15min `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`, MNQ_1min `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`. Kaggle front-month 15min `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`, 1min `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`.
- Confirm baselines intact: axb0306 60 trades net -$31,637.98; Kaggle front-month 688 trades net -$626,525.96 (see artifacts/metrics_axb0306.json, artifacts/metrics_kaggle.json).

## Bounded tasks
1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes before use.
2. No parameter/strategy changes without a separately versioned experiment (frozen baseline preserved: STRATEGY_RULES.txt v1.0, config/orb_mnq_15m_showcase.yaml unchanged).
3. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods.
4. Keep FEASIBILITY_REPORT.md, HANDOFF.md, and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.

## Hard constraints
- Historical research/simulation only. No broker integration, order routing, live/paper execution, credentials.
- Do not purchase data or bypass access controls/terms.
- Do not edit `.github/workflows/main.yml`, controller code, permissions/automation policy without explicit user authorization.
- Do not delete evidence, overwrite raw data, reset/rewrite git history to conceal failure.
