# Initial Task for Next Agent

## Status (session 2026-11-01 — maintenance re-verification, COMPLETE)
- Prior agent task read from HANDOFF.md + INITIAL_TASK_FOR_NEXT_AGENT.md; re-derived evidence rather than trusting prior claims.
- Independently re-verified this session:
  - Full suite `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 66 passed.
  - SHA-256 hashes verified unchanged and match HANDOFF.md exactly: STRATEGY_RULES.txt v1.0 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; config/orb_mnq_15m_showcase.yaml `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; raw/MNQ_15min.csv `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; raw/MNQ_1min.csv `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; raw/MNQ_1min_frontmonth.csv `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; raw/MNQ_15min_frontmonth.csv `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`.
  - Canonical artifacts verified: axb0306 60 trades / 70.0% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.492 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.227 / max DD ~$626,994.56.
  - Free-data sweep re-confirmed: no new genuinely free MNQ 1min/15min source beyond axb0306 (~3 months, single-contract MNQ.M26, unadjusted) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance daily only; all other candidates paid/key-gated. No data purchased; no credentials requested/stored.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; working tree clean.

## Bounded next task
1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes (source, URL, retrieval date, symbol/contract, timezone, roll/adjustment method, SHA-256) in data/FEASIBILITY_REPORT.md before use.
2. No parameter/strategy changes without a separately named, versioned experiment with an explicit diff from the frozen baseline (STRATEGY_RULES.txt v1.0).
3. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods; preserve a final untouched out-of-sample interval.
4. Keep FEASIBILITY_REPORT.md, HANDOFF.md, and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.

## Test command
- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` (66 passed).

## Blockers
- History depth insufficient for robust walk-forward/OOS: axb0306 ~3 months (single-contract MNQ.M26, unadjusted); Kaggle front-month ~3 years (unadjusted front-month by max volume). No multi-year free MNQ 1min/15min beyond these.
- Results negative under full costs on both available samples (costs dominate): axb0306 net -$31,637.98 (PF 0.492); Kaggle net -$626,525.96 (PF 0.227).
- axb0306 roll/adjustment method: single-contract MNQ.M26, no roll inside the sample; repo update script hard-codes one contract ID — re-verify hash and price continuity before using any re-downloaded file.

## Hard boundaries (AGENTS.md)
- Historical research and simulation only. No broker integration, order routing, live trading, paper-trading execution against a broker, or deployment.
- Never request, add, print, or persist broker/API credentials.
- Do not purchase data or use paid/proprietary services. Prefer freely accessible datasets; never bypass access controls or terms.
- Do not launch nested Kilo sessions, duplicate scheduled workflows, or additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy unless explicitly authorized.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal a failure.
