# Initial Task for Next Agent

## Status (this session 2026-11-01 — engine re-run + funnel cross-check)

- Read durable handoff (HANDOFF.md) + initial task + STRATEGY_RULES.txt v1.0 + PROMPT.md + AGENTS.md. Re-derived evidence rather than trusting prior claims.
- Prior agent task (maintenance/documentation re-verification) confirmed complete: no implementation work required beyond maintenance; frozen baseline preserved.
- Environment note: this session installed pandas 3.1.0 + pytest 9.2.0 via pip3 (previously reported as unavailable). Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 66 passed in 0.94s.
- SHA-256 re-computed, all match recorded values: STRATEGY_RULES.txt v1.0 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4.
- Fresh engine re-run (not a stored copy) for both sources, byte-diffed vs canonical artifacts:
  - axb0306: trades SHA-256 ce389da2488474a6d0d994cf99bb1e6509761d80f85986f1f8da3e1738b6a364 (IDENTICAL), metrics SHA-256 e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f (IDENTICAL).
  - kaggle: trades SHA-256 7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5 (IDENTICAL), metrics SHA-256 a6ae100685ea30aa2392122fdf9830ccbaad5d25a22039db7e7521a0b12c1af1 (IDENTICAL).
- Independent funnel cross-check re-run: 932 trading dates, 771 OR-built, 765 first breakouts, 688 pass filters -> engine trade count 688, matches exactly.
- Verify artifacts deleted after comparison; working tree clean (HEAD 1b6408c). Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no commit created.
- No new free MNQ 1min/15min source identified; blockers unchanged.

## Canonical artifacts (source of truth — do not treat as proof of edge)

- artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json — axb0306: 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.492, max DD $37,491.80.
- artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json — Kaggle front-month: 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.227, max DD ~$626,994.56.
- Both baselines negative under full costs; costs dominate.

## Bounded next task (carried forward unchanged)

1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes (source, URL, retrieval date, symbol/contract, timezone, roll/adjustment method, SHA-256) before use.
2. No parameter/strategy changes without a separately named, versioned experiment with an explicit diff from the frozen baseline (STRATEGY_RULES.txt v1.0).
3. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods; preserve a final untouched out-of-sample interval.
4. Keep FEASIBILITY_REPORT.md, HANDOFF.md, and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.

## Test command

- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` (prior sessions: 66 passed). pandas+pytest are installable via pip3 in this environment if missing; do not treat inability to run as a code failure.

## Blockers

- History depth insufficient for robust walk-forward/OOS: axb0306 ~3 months (single-contract MNQ.M26, no roll, no adjustment); Kaggle front-month ~3 years (unadjusted front-month by max volume). No multi-year free MNQ 1min/15min beyond these.
- Results negative under full costs on both available samples (costs dominate).
- axb0306 roll/adjustment method: single-contract MNQ.M26, no roll inside the sample; repo update script hard-codes one contract ID — re-verify hash and price continuity before using any re-downloaded file.

## Hard boundaries (AGENTS.md)

- Historical research and simulation only. No broker integration, order routing, live trading, paper-trading execution against a broker, or deployment.
- Never request, add, print, or persist broker/API credentials.
- Do not purchase data or use paid/proprietary services. Prefer freely accessible datasets; never bypass access controls or terms.
- Do not launch nested Kilo sessions, duplicate scheduled workflows, or additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy unless explicitly authorized.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal a failure.