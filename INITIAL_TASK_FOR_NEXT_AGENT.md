# Initial Task for Next Agent

## Status (session 2026-11-01 — full re-verification + live free-data re-sweep, COMPLETE)
- Prior agent task read from HANDOFF.md + INITIAL_TASK_FOR_NEXT_AGENT.md; re-derived evidence rather than trusting prior claims.
- `git status`: working tree clean (branch main, up to date with origin/main, HEAD f2ff8a4).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> 71 passed.
- SHA-256 recomputed from disk; all six match recorded values exactly (STRATEGY_RULES.txt 6d3258c3…, config 2a6c5ff8…, raw/MNQ_15min.csv f417f22d…, raw/MNQ_1min.csv 129623f4…, raw/MNQ_1min_frontmonth.csv edbadc73…, raw/MNQ_15min_frontmonth.csv 7e129ae3…).
- Baselines re-run from a fresh process and byte-diffed: metrics IDENTICAL for both sources; trades SHA-256 identical (axb0306 ce389da2…, kaggle 7251e4a9…). Throwaway verify_* outputs deleted; committed tree restored; working tree clean.
- Walk-forward re-derived and byte-diffed: `git diff --stat` EMPTY for both artifacts/walk_forward_axb0306.json and artifacts/walk_forward_kaggle.json. axb0306 3 windows all negative net (-$10,053.14 .. -$23,058.98); kaggle 8 windows all negative net (-$178,375.24 .. -$70,637.24).
- Ledger integrity re-verified directly from canonical artifacts: zero multi-trade days; latest exit 10:00 ET on both (<= 15:55 ET); risk_points == 0.4*atr14 to within 0.0001 ticks on all 748 trades; atr_pct within [0.10, 0.60]; rvol >= 1.0; exit-reason splits target/stop/stop_first_ambiguous only (axb0306 42/12/6, kaggle 478/130/80); long/short axb0306 33/27, kaggle 359/329.
- Live free-data sweep (2026-11-01): GitHub API confirms axb0306/cme-futures-ohlc MNQ path latest commit still `60abd3fb…` 2026-04-15T23:34:55Z and the MNQ/ directory still holds exactly the same 8 files (no intraday extension). Re-downloaded both live files and re-hashed: raw/MNQ_1min.csv 129623f45308… and raw/MNQ_15min.csv f417f22d… — both byte-identical to the committed local copies (no silent upstream change). Live websearch re-scan: Kaggle brandenmorris MNQ unchanged (CC BY 4.0, Databento GLBX.MDP3, 2022-11-16..2025-11-12, 11.76 GB v1, already ingested); tgtanalytics NQ 1min 2022-2025 is the big NQ contract ($20/point), excluded; youneseloiarm Nasdaq-CME-Future-NQ is NQ, excluded; vbloise Micro Emini NASDAQ is daily only, excluded; MarketParquet MNQ 1-min continuous ratio-adjusted 2019-05-06..2026-10-23 is $79 one-time (free tier = ~1yr daily + small intraday sample pack only); Portara MNQ intraday $220+ paid; Databento GLBX.MDP3 MNQ key-gated + credit-based; Yahoo Finance / investing.com daily only; CME DataMine priced per dataset. dbn-cache / Databento free tier is the only genuinely free path to new MNQ 1min bars and requires a Databento API key (key-gated) — no credentials requested, none stored. No new genuinely free MNQ 1min/15min source found; no data purchased.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; working tree clean.

## Bounded next task
1. **Maintenance only (default).** Re-verify repo state (git status, tests, hashes, artifacts, walk-forward) against HANDOFF.md. Do not change strategy/params/code.
2. **Data monitoring.** If a new genuinely free MNQ 1min/15min source appears, record provenance/hashes (source, URL, retrieval date, symbol/contract, timezone, roll/adjustment method, gaps, SHA-256) before use.
3. **No experiments without approval.** No parameter/strategy changes without a separately named, versioned experiment with an explicit diff from frozen baseline (STRATEGY_RULES.txt v1.0).
4. **Update docs.** If anything changes, update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with evidence.
5. **Blockers:** Research blocked on data depth (axb0306 ~3mo, Kaggle ~3yr front-month) — both negative under full costs; all walk-forward windows negative.

## Test command
- `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` (71 passed)

## Hard boundaries (AGENTS.md)
- Historical research and simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
