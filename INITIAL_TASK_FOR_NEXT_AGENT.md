# Initial task for next agent

Read `HANDOFF.md` first. Current priority is maintenance/documentation (frozen baseline preserved).

## Evidence to verify (as of 2026-10-31u)
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` should pass (66 passed).
- Baselines (artifacts/metrics_axb0306.json, artifacts/metrics_kaggle.json): axb0306 60 trades net -$31,637.98; Kaggle front-month 688 trades net -$626,525.96.
- Raw data hashes unchanged:
  - MNQ_15min f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37
  - MNQ_1min 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99
  - MNQ_15min_frontmonth 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4
  - MNQ_1min_frontmonth edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7
- No new free MNQ 1min/15min sources beyond axb0306 and Kaggle front-month (Yahoo daily only). No data purchased.
- Fresh re-run reproducibility: `python src/orb/runner.py --source axb0306` and `--source kaggle` reproduce the canonical artifacts byte-for-byte.

## Bounded next steps
1. If a new free MNQ 1min/15min source appears, record provenance/hashes and update FEASIBILITY_REPORT before use.
2. Do not change frozen rules/params without a separately versioned experiment.
3. If longer free history obtained, re-run chronological splits/cost sensitivity across full periods.
4. Keep HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.

Do not purchase data, add credentials, enable live trading, or edit controller/workflow files without explicit authorization.