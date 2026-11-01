# NQ ORB — Durable Handoff
Date: 2026-11-01
Repository: takenthatusernameis-collab/NQ-ORB
Status: Maintenance pass complete; frozen baseline preserved; baselines verified intact; no new free MNQ 1min/15min source.

## Completed work (this session 2026-11-01)
- Read prior agent task from HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md; maintenance/documentation priority confirmed; frozen baseline preserved.
- Re-ran full test suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 66 passed.
- Verified raw data hashes unchanged:
  - raw/MNQ_15min.csv: f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37
  - raw/MNQ_1min.csv: 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99
  - raw/MNQ_15min_frontmonth.csv: 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4
  - raw/MNQ_1min_frontmonth.csv: edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7
- Verified frozen baseline hashes unchanged:
  - STRATEGY_RULES.txt v1.0: 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1
  - config/orb_mnq_15m_showcase.yaml: 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4
- Baselines verified intact against canonical artifacts:
  - axb0306: 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.492, max DD $37,491.80 (artifacts/metrics_axb0306.json)
  - Kaggle front-month: 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.227, max DD ~$626,994.56 (artifacts/metrics_kaggle.json)
- Free-data sweep: no new genuinely free MNQ 1min/15min source beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume); Yahoo daily only. axb0306/cme-futures-ohlc MNQ path last commit still 60abd3fb… dated 2026-04-15T23:34:55Z — unchanged. Kaggle brandenmorris coverage still ends 2025-11-12. No data purchased; no credentials requested or stored.
- Working tree clean (HEAD f0b1c53). Frozen baseline preserved; no code/strategy/parameter changes; no broker integration.
- Prior agent task complete: no implementation work required beyond maintenance.

(Prior maintenance sessions 2026-10-30 through 2026-11-01 all verified the same frozen state; full per-session log retained in git history of this file.)

## Authoritative state
- STRATEGY_RULES.txt is the authoritative, frozen strategy definition (v1.0).
- PROMPT.md specifies the research workflow.
- AGENTS.md defines research, auditability, and no-live-trading constraints.
- .github/workflows/main.yml present (controller owns the sequential Kilo loop; not edited).
- No validated multi-year backtest yet; results are from available free samples only.

## Unresolved blockers
- History depth: axb0306 ~3 months (single-contract MNQ.M26, unadjusted); Kaggle front-month ~3 years (unadjusted front-month by max volume). No multi-year free MNQ 1min/15min beyond these; insufficient for robust walk-forward/OOS.
- Results negative under full costs on both available samples (costs dominate).
- axb0306 roll/adjustment method: single-contract MNQ.M26, no roll inside the sample; repo update script hard-codes one contract ID ("update when contracts rolls") — re-verify hash and price continuity before using any re-downloaded file.

## Next bounded task
1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes before use.
2. No parameter/strategy changes without a separately versioned experiment (frozen baseline preserved).
3. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods.
4. Keep FEASIBILITY_REPORT.md, HANDOFF.md, and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.

## Completed work (this session 2026-11-01 — maintenance verification)
- Re-ran full test suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 66 passed.
- Verified raw data hashes unchanged (all four raw files match prior recorded hashes).
- Verified frozen baseline hashes unchanged (STRATEGY_RULES.txt, config/orb_mnq_15m_showcase.yaml).
- Working tree clean (HEAD b1796ab). Frozen baseline preserved; no code/strategy/parameter changes; no broker integration.
- Prior agent task complete: maintenance/documentation pass; no implementation work required.

## Completed work (this session 2026-11-01 — verification)
- Re-ran full test suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 66 passed.
- Verified raw data hashes unchanged:
  - raw/MNQ_15min.csv: f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37
  - raw/MNQ_1min.csv: 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99
  - raw/MNQ_15min_frontmonth.csv: 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4
  - raw/MNQ_1min_frontmonth.csv: edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7
- Verified frozen baseline hashes unchanged:
  - STRATEGY_RULES.txt v1.0: 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1
  - config/orb_mnq_15m_showcase.yaml: 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4
- Baselines verified intact against canonical artifacts:
  - axb0306: 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.492, max DD $37,491.80 (artifacts/metrics_axb0306.json)
  - Kaggle front-month: 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.227, max DD ~$626,994.56 (artifacts/metrics_kaggle.json)
- Free-data sweep: no new genuinely free MNQ 1min/15min source beyond axb0306 (~3 months) and Kaggle front-month (~3 years); Yahoo daily only. No data purchased; no credentials requested or stored.
- Working tree clean (HEAD f0b1c53). Frozen baseline preserved; no code/strategy/parameter changes; no broker integration.

## Completed work (this session 2026-11-01 — maintenance pass)
- Read prior agent task from HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md; maintenance/documentation priority confirmed; frozen baseline preserved.
- Re-ran full test suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 66 passed.
- Verified raw data hashes unchanged (all four raw files match prior recorded hashes).
- Verified frozen baseline hashes unchanged (STRATEGY_RULES.txt, config/orb_mnq_15m_showcase.yaml).
- Working tree clean. Frozen baseline preserved; no code/strategy/parameter changes; no broker integration.
- Prior agent task complete: maintenance/documentation pass; no implementation work required.

## Next bounded task
1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes before use.
2. No parameter/strategy changes without a separately versioned experiment (frozen baseline preserved).
3. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods.
4. Keep FEASIBILITY_REPORT.md, HANDOFF.md, and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.
