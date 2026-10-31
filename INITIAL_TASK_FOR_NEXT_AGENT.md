# Initial task for next agent — NQ ORB

Date: 2026-10-31

## Current state (read HANDOFF.md first)
- Frozen baseline preserved: `STRATEGY_RULES.txt` v1.0, `config/orb_mnq_15m_showcase.yaml` unchanged. No strategy/parameter changes.
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` -> 66 passed (latest session 2026-10-31az).
- Raw data hashes verified unchanged: MNQ_15min f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; MNQ_1min 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; Kaggle front-month 15min 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4; 1min edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7.
- Canonical baselines (deterministic, cost-aware, byte-identical to `artifacts/metrics_axb0306.json` and `artifacts/metrics_kaggle.json` on all 41 fields):
  - axb0306: 60 trades, net -$31,637.98 (gross -$7,662.00, PF 0.49167, WR 70.0%, max DD $37,491.80)
  - Kaggle front-month: 688 trades, net -$626,525.96 (gross -$140,899.00, PF 0.22709, WR 64.8256%, max DD ~$626,994.56)
- Free-data state (session 2026-10-31az web sweep): only axb0306 (~3 months, single-contract MNQ.M26 unadjusted) and Kaggle front-month (~3 years, unadjusted front-month by max volume) are genuinely free. Yahoo daily only. PAID / key-gated and therefore excluded: FirstRate Data ($99.95/yr), FinzData ($29 one-time MNQ intraday), historicalfuturesdata.com, TickTradingData, Portara, Databento (key-gated, unadjusted continuous), MarketParquet (free tier only ~1yr daily + small intraday sample pack). Kaggle brandenmorris MNQ 1min 5/13/2025-11/12/2025 is the same Databento GLBX.MDP3 source family as the existing Kaggle front-month dataset; not separately downloaded to avoid duplicate provenance. tgtanalytics NQ 1min is the big NQ contract, not MNQ. No data purchased.

## Priority (maintenance/documentation only; do not change baseline)
1. **Free data sweep**: If any genuinely free MNQ 1min/15min source appears, download with provenance (URL/repo, retrieval time, license), compute sha256 hashes for raw CSVs, update `data/FEASIBILITY_REPORT.md`, and record in `HANDOFF.md` before using. Exclude paid/key-gated sources.
2. **Integrity checks**: On each verification session, re-run tests, re-verify raw hashes, and confirm canonical baselines match `artifacts/metrics_axb0306.json` and `artifacts/metrics_kaggle.json` byte-identically (re-run via `src/orb/runner.py --source axb0306 --prefix <tag>` and `--source kaggle --prefix <tag>`, then delete check artifacts).
3. **Evidence hygiene**: Keep `data/FEASIBILITY_REPORT.md`, `HANDOFF.md`, and this file updated with commands/results/hashes/blockers/next task.
4. **No baseline changes**: No parameter/strategy/rule changes without a separately named versioned experiment with explicit diff from frozen baseline. No broker integration, no live/paper orders, no data purchases.

## Suggested commands
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q`
- Hashes: `sha256sum raw/MNQ_15min.csv raw/MNQ_1min.csv raw/MNQ_15min_frontmonth.csv raw/MNQ_1min_frontmonth.csv`
- Baselines: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python src/orb/runner.py --source axb0306 --prefix axb0306_check && PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python src/orb/runner.py --source kaggle --prefix kaggle_check` (compare to canonical, delete check artifacts)

## Blockers
- History depth limited (axb0306 ~3m single-contract unadjusted; Kaggle front-month ~3y unadjusted). Insufficient for robust walk-forward/OOS.
- Costs dominate (both samples negative under full costs).
- axb0306 continuous/roll adjustment undocumented; Kaggle is front-month unadjusted.

Complete the above maintenance, update `HANDOFF.md`, update this file, and leave evidence.

## Session verification (2026-10-31ay)
- Tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python -m pytest tests -q` -> 66 passed.
- Raw hashes verified unchanged: MNQ_15min f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; MNQ_1min 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; Kaggle front-month 15min 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4; 1min edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7.
- Baselines re-run from scratch (`src/orb/runner.py --source axb0306 --prefix axb0306_check` and `--source kaggle --prefix kaggle_check`); all 41 metric fields byte-identical to canonical artifacts `artifacts/metrics_axb0306.json` and `artifacts/metrics_kaggle.json`: axb0306 60 trades net -$31,637.98 / PF 0.49167 / WR 70.0%; Kaggle front-month 688 trades net -$626,525.96 / PF 0.22709 / WR 64.8256%. Determinism confirmed; check artifacts removed.
- Free-data sweep (2026-10-31): MarketParquet re-inspected live — free tier is daily-only (last 1yr) + 30-symbol 1-week intraday sample pack; full MNQ 1-min archive is $79 one-time (PAID, excluded). historicalfuturesdata.com re-inspected live — MNQ 1-min is $59/yr per bar size; free tier is only a latest-month 10sec sample (PAID, excluded). infoway.io requires API key signup (unverified historical depth; not used). GitHub re-scan: NQ 1m samples are US equities, not MNQ. Kaggle tgtanalytics/nq-futures-1min-bar-2022-2025 and youneseloiarm/nasdaq-cme-future-nq are NQ big contract ($20/point), not MNQ — excluded per STRATEGY_RULES.txt. No new genuinely free MNQ 1min/15min source located. No data purchased; no credentials requested or stored.
- Frozen baseline preserved (STRATEGY_RULES.txt v1.0, config/orb_mnq_15m_showcase.yaml unchanged); no code/strategy/parameter changes; no broker integration; no live/paper orders.
- Updated `data/FEASIBILITY_REPORT.md` with the 2026-10-31ay free-data sweep section, plus HANDOFF.md and this file.