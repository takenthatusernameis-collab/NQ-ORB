# Initial task for next agent

Read `HANDOFF.md` first. Current priority is maintenance/documentation; the frozen baseline is preserved.

## State verified this session (2026-11-01br)

- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 66 passed in 0.61s.
- Baselines (artifacts/metrics_axb0306.json, artifacts/metrics_kaggle.json):
  - axb0306: 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.492, max DD $37,491.80.
  - Kaggle front-month: 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.227, max DD $626,994.56.
- Raw data hashes unchanged:
  - raw/MNQ_15min.csv: f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37
  - raw/MNQ_1min.csv: 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99
  - raw/MNQ_15min_frontmonth.csv: 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4
  - raw/MNQ_1min_frontmonth.csv: edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7
- Frozen baseline hashes unchanged:
  - STRATEGY_RULES.txt: 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1
  - config/orb_mnq_15m_showcase.yaml: 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4
- Working tree clean except for HANDOFF.md, INITIAL_TASK_FOR_NEXT_AGENT.md, and data/FEASIBILITY_REPORT.md (all updated this session). No transient verify artifacts in artifacts/.

## Prior agent task — complete

Verified tests pass, all hashes unchanged, baselines intact (re-run fresh and diffed field-by-field plus full trade ledgers: byte-identical). Free-data sweep confirmed no new genuinely free MNQ 1min/15min source. Frozen baseline preserved; no code/strategy/parameter changes; no broker integration. data/FEASIBILITY_REPORT.md updated with this session's sweep entry.

## Bounded next steps

1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes (and update data/FEASIBILITY_REPORT.md if present) before use.
2. Do not change frozen rules/params without a separately named, versioned experiment with an explicit diff from the frozen baseline (STRATEGY_RULES.txt v1.0).
3. If longer free MNQ 1min/15min history is obtained, re-run chronological train/validation/test splits and cost sensitivity across full periods; preserve a final untouched test interval.
4. Keep HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence after each session.

## Hard constraints (do not violate)

- Do not purchase data or use paid/proprietary services; no broker/API credentials ever.
- No broker integration, order routing, live trading, or paper-trading execution against a broker.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history.
- Never fabricate bars, fills, timestamps, or missing data; report limitations honestly.

## Next agent task

Continue maintenance/documentation. Verify tests pass and hashes match (see state above). If a new free MNQ 1min/15min source appears, record provenance/hashes before use and update data/FEASIBILITY_REPORT.md if present. Otherwise keep HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md current with evidence after each session. No implementation work is required unless the user changes scope.