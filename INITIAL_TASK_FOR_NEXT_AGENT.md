# Initial task for next agent

Read `HANDOFF.md` first. Current priority is maintenance/documentation (frozen baseline preserved).

## State to verify (as of 2026-10-31bn)

- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` should pass (66 passed).
- Baselines (artifacts/metrics_axb0306.json, artifacts/metrics_kaggle.json):
  - axb0306: 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.492, max DD $37,491.80, Sharpe -1.056, Sortino -0.668, exposure 0.103%.
  - Kaggle front-month: 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.227, max DD $626,994.56, Sharpe -1.680, Sortino -1.042, exposure 0.081%.
- Raw data hashes unchanged:
  - raw/MNQ_15min.csv: f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37
  - raw/MNQ_1min.csv: 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99
  - raw/MNQ_15min_frontmonth.csv: 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4
  - raw/MNQ_1min_frontmonth.csv: edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7
- Frozen baseline hashes:
  - STRATEGY_RULES.txt: 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1
  - config/orb_mnq_15m_showcase.yaml: 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4
- No transient verify artifacts in artifacts/ (only canonical + historical).

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

## Session task (2026-10-31bn)

Maintenance session. No new implementation work was required. Verified:
- Full test suite: 66 passed.
- Raw data hashes unchanged across all 4 files.
- Frozen baseline hashes unchanged (STRATEGY_RULES.txt, config/orb_mnq_15m_showcase.yaml).
- Both baselines re-run fresh (`--prefix verify_axb`, `--prefix verify_kag`) and diffed field-by-field + full trade-ledger byte-identical against canonical artifacts.
- artifacts/ contains only canonical + historical files (no transient verify_* artifacts); matches artifacts/README.md.
- Free-data sweep re-run (GitHub API repo commits + MNQ path listing, Kaggle dataset search, Yahoo Finance, Databento GLBX.MDP3, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate, TickTradingData, infoway.io, CME DataMine, investing.com, thinridge.io, arXiv 2605.04004, getdata.finance, kibot, quantnet): **no new genuinely free MNQ 1min/15min source**.
  - GitHub: axb0306/cme-futures-ohlc most recent commit on the MNQ path is still `60abd3fb…` dated 2026-04-15T23:34:55Z — unchanged since prior session audit. No new intraday MNQ files, no extension of history.
  - Kaggle: `brandenmorris/mnq-1-minute-data-5132025-11122025` remains the only free MNQ 1-min source (ends 2025-11-12, already ingested). All other MNQ hits are NQ (big contract, $20/point) or paid/key-gated.
  - All paid candidates re-confirmed paid/key-gated: FinzData $49 one-time, FirstRate $99.95/yr, historicalfuturesdata.com $59/yr per bar size, MarketParquet $79, TickTradingData €200, Kibot $520, Databento key-gated + credit-based, CME DataMine purchase-only, investing.com daily-only, getdata.finance paid, quantnet personal sale. No data purchased; no credentials requested or stored.
- No data purchased, no code/strategy/parameter changes, frozen baseline preserved, no broker integration.

## Next agent task

Continue maintenance/documentation. If a new free MNQ 1min/15min source appears, record provenance/hashes before use and update data/FEASIBILITY_REPORT.md. Otherwise keep HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md current with evidence after each session.