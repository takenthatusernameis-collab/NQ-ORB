# Initial task for next agent

Read `HANDOFF.md` first. Current priority is maintenance/documentation (frozen baseline preserved).

## State to verify (as of 2026-10-31ap)

- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` should pass (66 passed).
- Baselines (artifacts/metrics_axb0306.json, artifacts/metrics_kaggle.json): axb0306 60 trades net -$31,637.98 / PF 0.492 / max DD $37,491.80 / WR 70.0%; Kaggle front-month 688 trades net -$626,525.96 / PF 0.227 / max DD ~$626,994.56 / WR 64.83%.
- Raw data hashes unchanged:
  - raw/MNQ_15min.csv: f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37
  - raw/MNQ_1min.csv: 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99
  - raw/MNQ_15min_frontmonth.csv: 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4
  - raw/MNQ_1min_frontmonth.csv: edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7
- Frozen baseline preserved: STRATEGY_RULES.txt v1.0 and config/orb_mnq_15m_showcase.yaml unchanged; no code/strategy/parameter changes.

## Bounded next steps

1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes (and update data/FEASIBILITY_REPORT.md) before use.
2. Do not change frozen rules/params without a separately named, versioned experiment with an explicit diff from the frozen baseline.
3. If longer free MNQ 1min/15min history is obtained, re-run chronological train/validation/test splits and cost sensitivity across full periods.
4. Keep HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence after each session.

## Hard constraints (do not violate)

- Do not purchase data or use paid/proprietary services; no broker/API credentials ever.
- No broker integration, order routing, live trading, or paper-trading execution against a broker.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history.
