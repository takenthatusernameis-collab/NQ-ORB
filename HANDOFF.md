# NQ ORB — Durable Handoff
Date: 2026-11-01
Repository: takenthatusernameis-collab/NQ-ORB
Status: Independent re-verification complete; frozen baseline preserved; baselines reproduce byte-for-byte; no new free MNQ 1min/15min source.

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

## Canonical artifacts (source of truth)
- artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json — axb0306: 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.492, max DD $37,491.80.
- artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json — Kaggle front-month: 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.227, max DD ~$626,994.56.
- Historical (retained, not canonical): trades_baseline.json, metrics.json, trades_axb0306_full.json, metrics_axb0306_full.json.

## Session log (2026-11-01 — independent re-verification)
- Prior agent task read from HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md; re-derived evidence rather than trusting prior claims.
- Full test suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 66 passed.
- Raw data hashes re-computed (sha256sum): all four match recorded values.
- Frozen baseline hashes re-computed: STRATEGY_RULES.txt v1.0 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4.
- Fresh engine re-run (not a stored copy) for both sources, then byte-diffed vs canonical artifacts:
  - axb0306: metrics IDENTICAL, trades IDENTICAL.
  - kaggle: metrics IDENTICAL; trades file SHA-256 identical (7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5).
- Independent funnel cross-check re-run: 932 trading dates, 771 OR-built, 765 first breakouts, 688 pass filters -> engine trade count 688, matches exactly.
- Verify artifacts deleted after comparison; working tree clean (HEAD 067d706). Frozen baseline preserved; no code/strategy/parameter changes; no broker integration.
- Prior agent task complete: maintenance/documentation pass independently re-verified; no implementation work required beyond maintenance.

## Prior sessions (2026-10-30 through 2026-11-01)
All prior maintenance-verification sessions verified the same frozen state (full suite green, raw + baseline hashes unchanged, baselines intact). Full per-session log retained in git history of this file.

## Next bounded task
1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes before use.
2. No parameter/strategy changes without a separately versioned experiment (frozen baseline preserved).
3. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods.
4. Keep FEASIBILITY_REPORT.md, HANDOFF.md, and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.