# Initial Task for Next Agent

## Status (session 2026-11-01 — prior task completed + live free-data sweep + handoff refresh, COMPLETE)
- Prior agent task read from HANDOFF.md + INITIAL_TASK_FOR_NEXT_AGENT.md; re-derived evidence rather than trusting prior claims.
- `git status`: working tree clean (branch main, HEAD 9be29de).
- Full suite `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed.
- SHA-256 hashes verified unchanged and match HANDOFF.md exactly: STRATEGY_RULES.txt v1.0 `6d3258c3...`; config/orb_mnq_15m_showcase.yaml `2a6c5ff8...`; raw/MNQ_15min.csv `f417f22d...`; raw/MNQ_1min.csv `129623f4...`; raw/MNQ_1min_frontmonth.csv `edbadc73...`; raw/MNQ_15min_frontmonth.csv `7e129ae3...`.
- Baselines re-run from a fresh process and byte-diffed against committed artifacts: `git diff --stat artifacts/` EMPTY. axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD ~$626,994.56.
- Walk-forward re-derived and byte-diffed: `git diff --stat artifacts/walk_forward_*.json` EMPTY. axb0306 3 windows all negative net (-$10,053.14 .. -$23,058.98); Kaggle 6 windows all negative net (-$70,637.24 .. -$114,820.72).
- Independent ledger-integrity spot-check (throwaway script, deleted): zero multi-trade days on both samples; latest exit 10:00 ET on both (<= 15:55 ET forced-exit bound); risk_points == 0.4*atr14 to within 0.0001 ticks on all 748 trades; exit-reason splits axb0306 42 target / 12 stop / 6 stop_first_ambiguous, Kaggle 478 / 130 / 80; long/short axb0306 33/27, Kaggle 359/329.
- Live free-data sweep (2026-11-01) re-confirmed: no new genuinely free MNQ 1min/15min source beyond axb0306 (~3 months, single-contract MNQ.M26, unadjusted, no roll) and Kaggle front-month (~3 years, unadjusted front-month by max volume); Yahoo daily only. FinzData $49, FirstRate $99.95/yr, MarketParquet $79, historicalfuturesdata.com $59/yr, Databento key-gated + $125 expiring credit, Barchart Premier-only, broker platforms require funded/demo account, CME DataMine priced per dataset. dbn-cache/Databento free tier is the only free path to new MNQ 1min bars and requires a Databento API key (key-gated) — no credentials requested, none stored. No data purchased.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; working tree clean.

## Bounded next task
1. Maintain documentation; if a new free MNQ 1min/15min source appears, record provenance/hashes (source, URL, retrieval date, symbol/contract, timezone, roll/adjustment method, SHA-256) before use.
2. No parameter/strategy changes without a separately named, versioned experiment with an explicit diff from the frozen baseline (STRATEGY_RULES.txt v1.0).
3. If longer free history is obtained, re-run chronological splits and cost sensitivity across full periods; preserve a final untouched out-of-sample interval.
4. Keep HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md updated with evidence.
5. The research task is effectively blocked on data depth, not code — the next agent's highest-value action is a bounded free-data re-sweep, not parameter fitting.

## Test command
- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` (71 passed).
- Re-derive baselines: `python3 src/orb/runner.py --source axb0306 --prefix axb0306` and `--source kaggle --prefix kaggle`, then diff `artifacts/trades_*.json` / `artifacts/metrics_*.json` against committed values.
- Re-derive walk-forward: `python3 scripts/walk_forward.py --source axb0306 --window-trades 20 --step-trades 10` and `--source kaggle --window-trades 150 --step-trades 50`.

## Blockers
- History depth insufficient for robust walk-forward/OOS: axb0306 ~3 months (single-contract MNQ.M26, unadjusted); Kaggle front-month ~3 years (unadjusted front-month by max volume). No multi-year free MNQ 1min/15min beyond these.
- Results negative under full costs on both available samples (costs dominate): axb0306 net -$31,637.98 (PF 0.4917); Kaggle net -$626,525.96 (PF 0.2271). All walk-forward test windows negative on both sources.
- axb0306 roll/adjustment method: single-contract MNQ.M26, no roll inside the sample; repo update script hard-codes one contract ID — re-verify hash and price continuity before using any re-downloaded file.

## Hard boundaries (AGENTS.md)
- Historical research and simulation only. No broker integration, order routing, live trading, paper-trading execution against a broker, or deployment.
- Never request, add, print, or persist broker/API credentials.
- Do not purchase data or use paid/proprietary services. Prefer freely accessible datasets; never bypass access controls or terms.
- Do not launch nested Kilo sessions, duplicate scheduled workflows, or additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy unless explicitly authorized.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal a failure.