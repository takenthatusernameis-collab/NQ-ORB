# Initial Task for Next Agent

## Prior task completed (this session 2026-11-01 — maintenance verification)
- Test suite green: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 66 passed.
- Raw data hashes unchanged: MNQ_15min f417f22d7c933920...; MNQ_1min 129623f45308a98a...; front-month 15min 7e129ae37f1ae62b...; front-month 1min edbadc731ed90c9e....
- Frozen baseline hashes unchanged: STRATEGY_RULES.txt v1.0 6d3258c3f3af803f...; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663....
- Baselines intact: axb0306 60 trades net -$31,637.98 / PF 0.492 / max DD $37,491.80 / WR 70.0%; Kaggle front-month 688 trades net -$626,525.96 / PF 0.227 / max DD ~$626,994.56 / WR 64.83% (artifacts/metrics_axb0306.json, artifacts/metrics_kaggle.json).
- Working tree clean (HEAD c6c035a). Frozen baseline preserved; no code/strategy/parameter changes; no broker integration.
- Free-data sweep: no new genuinely free MNQ 1min/15min source beyond axb0306 (~3 months, single-contract MNQ.M26) and Kaggle front-month (~3 years); Yahoo daily only.

## Bounded next task
1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes before use.
2. No parameter/strategy changes without a separately versioned experiment (frozen baseline preserved).
3. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods.
4. Keep FEASIBILITY_REPORT.md, HANDOFF.md, and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.

Test command: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` (expect 66 passed).

Blockers: history depth insufficient for robust walk-forward/OOS (axb0306 ~3 months single-contract; Kaggle ~3 years unadjusted front-month); results negative under full costs on both samples (costs dominate); axb0306 has no intra-sample roll — re-verify hash and price continuity before using any re-downloaded file.
