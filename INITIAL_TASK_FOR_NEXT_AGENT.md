# Initial Task for Next Agent

## Prior task completed (this session 2026-11-01 — independent re-verification, fresh engine re-run)

- Read durable handoff (HANDOFF.md) + initial task + STRATEGY_RULES.txt v1.0 + PROMPT.md + AGENTS.md + data/FEASIBILITY_REPORT.md; re-derived evidence rather than trusting prior claims.
- Full suite green: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 66 passed.
- Working tree clean (HEAD 6f434dd). No code/strategy/parameter changes; frozen baseline preserved; no broker integration.
- Frozen STRATEGY_RULES.txt v1.0 hash 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1 preserved; config/orb_mnq_15m_showcase.yaml hash 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4 unchanged.
- Raw data hashes all match recorded values: MNQ_15min.csv f417f22d…, MNQ_1min.csv 129623f4…, MNQ_1min_frontmonth.csv edbadc73…, MNQ_15min_frontmonth.csv 7e129ae3….
- Fresh engine re-run (not a stored copy) for both sources, byte-diffed vs canonical artifacts:
  - axb0306: metrics IDENTICAL, trades IDENTICAL (sha256 ce389da2488474a6d0d994cf99bb1e6509761d80f85986f1f8da3e1738b6a364).
  - kaggle: metrics IDENTICAL; trades file SHA-256 identical (7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5).
- Verify artifacts deleted after comparison.
- Independent funnel cross-check re-run: 932 trading dates, 771 OR-built, 765 first breakouts, 688 pass RVOL+ATR filters -> engine trade count 688, matches exactly.
- No new free MNQ 1min/15min source; blockers unchanged.

## Canonical artifacts (source of truth — do not treat as proof of edge)
- artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json — axb0306: 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.492, max DD $37,491.80.
- artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json — Kaggle front-month: 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.227, max DD ~$626,994.56.
- Both baselines negative under full costs; costs dominate.

## Bounded next task

1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes (source, URL, retrieval date, symbol/contract, timezone, roll/adjustment method, SHA-256) before use.
2. No parameter/strategy changes without a separately named, versioned experiment with an explicit diff from the frozen baseline (STRATEGY_RULES.txt v1.0).
3. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods; preserve a final untouched out-of-sample interval.
4. Keep FEASIBILITY_REPORT.md, HANDOFF.md, and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.

## Test command
`PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` (expect 66 passed).

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
