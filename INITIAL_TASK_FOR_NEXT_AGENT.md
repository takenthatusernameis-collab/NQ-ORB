# Initial task for next agent (2026-10-31as)

Read HANDOFF.md first. Current priority: maintenance/documentation only (no new genuinely free MNQ 1min/15min sources found beyond axb0306 and Kaggle front-month; Yahoo daily only; MarketParquet/historicalfuturesdata.com/FirstRate/Portara excluded as paid).

## Verification checklist (completed this session, 2026-10-31as)
1. Full test suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` -> 66 passed.
2. Both baselines re-run from scratch and compared byte-identical to canonical artifacts:
   - axb0306: 60 trades net -$31,637.98 / gross -$7,662.00 / PF 0.49167 / WR 70.0%
   - Kaggle front-month: 688 trades net -$626,525.96 / gross -$140,899.00 / PF 0.22709 / WR 64.8256%
   Determinism re-confirmed.
3. Raw data hashes verified unchanged:
   - raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37
   - raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99
   - raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4
   - raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7
4. No code/strategy/parameter changes; frozen baseline preserved; no data purchased; no broker integration; no live/paper orders.

## Constraints
- Follow AGENTS.md (historical/simulation only, no broker integration, no credentials, no paid data).
- Frozen baseline: STRATEGY_RULES.txt v1.0, config/orb_mnq_15m_showcase.yaml unchanged.
- Preserve evidence; update FEASIBILITY_REPORT.md if new provenance appears.
- Do not commit changes unless explicitly asked.

## Next bounded task
1. Maintain documentation; if a new genuinely free MNQ 1min/15min source appears, record provenance/hashes before use.
2. No parameter/strategy changes without a separately versioned experiment (frozen baseline preserved).
3. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods.
4. Keep FEASIBILITY_REPORT.md, HANDOFF.md, and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.
