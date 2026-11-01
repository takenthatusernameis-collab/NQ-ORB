# Initial task for next agent

Read `HANDOFF.md` first. Current priority is maintenance/documentation; the frozen baseline is preserved.

## State verified this session (2026-11-01k)

- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 66 passed in 0.93s.
  - Note: pytest 9.2.0 + pandas + numpy were installed to the user site this session (`pip install pytest pandas numpy`); the base environment did not have pytest. Re-run the same command; do not re-install unless the environment is reset.
- Baselines (artifacts/metrics_axb0306.json, artifacts/metrics_kaggle.json):
  - axb0306: 60 trades, 70.0% WR, gross -$7662.00, net -$31637.98, PF 0.4917, max DD $37491.80.
  - Kaggle front-month: 688 trades, 64.83% WR, gross -$140899.00, net -$626525.96, PF 0.2271, max DD ~$626994.56.
- Raw data hashes unchanged:
  - raw/MNQ_15min.csv: f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37
  - raw/MNQ_1min.csv: 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99
  - raw/MNQ_15min_frontmonth.csv: 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4
  - raw/MNQ_1min_frontmonth.csv: edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7
- Frozen baseline hashes unchanged:
  - STRATEGY_RULES.txt: 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1
  - config/orb_mnq_15m_showcase.yaml: 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4
- Working tree clean. No code/strategy/parameter changes; frozen baseline preserved.

## Prior agent task — complete

Verified tests pass, all hashes unchanged, baselines intact. Free-data sweep re-run (GitHub API axb0306/cme-futures-ohlc commits on path=MNQ + live MNQ directory listing, Kaggle brandenmorris dataset page, live websearch for free MNQ 1min/15min download, Yahoo Finance, Databento, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate, TickTradingData, infoway.io, CME DataMine, investing.com, thinridge.io, getdata.finance, kibot, quantnet, arXiv 2605.04004): **no new genuinely free MNQ 1min/15min source**.
- axb0306 MNQ history still ends 2026-04-15 (commit 60abd3fb…, unchanged since prior session audit); MNQ directory still exactly 8 files (15min/1h/1min/30min/4h/5min/daily/tick), no new intraday files, no history extension.
- Kaggle brandenmorris dumps still end 2025-11-12 and are marked "Updated a year ago" — no extension. All other MNQ hits are NQ (big contract, $20/point) or paid/key-gated.
- All paid candidates re-confirmed paid/key-gated (historicalfuturesdata.com $59/yr per bar size, FirstRate $99.95/yr, Portara paid, MarketParquet $79 one-time, Databento key-gated + $125 credit expiring, thinridge.io uses FirstRate paid data, getdata.finance paid, kibot $520, quantnet personal sale, CME DataMine purchase-only, investing.com daily-only, Yahoo daily-only). No data purchased; no credentials requested or stored. HANDOFF.md updated.

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