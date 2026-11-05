# Initial Task for Next Agent

## Status (maintenance re-verification COMPLETE — 2026-11-05T14:26Z, this session)

- Branch `main`; HEAD `a7aae67` at verification (checkpoint drift only; no strategy/code/data drift). `git status --short` clean before edits.
- All 6 tracked SHA-256 hashes **MATCH** (unchanged). Artifacts: **24** JSON files parse cleanly. `python3 -m pytest -q` → **71 passed, 0 failed** (0.65s, 2026-11-05T14:26Z).
- Free-data monitoring (2026-11-05T14:26Z): GitHub API `axb0306` MNQ path latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` — **no extension beyond 2026-04-15**. No genuinely free MNQ 1min/15min full-history source found. No data purchased; no credentials requested/stored; no code/strategy/parameter changes.


## Status (maintenance re-verification COMPLETE — 2026-11-05T13:45Z, this session)

- Branch `main`; HEAD `b2e3868` at verification (checkpoint drift only; no strategy/code/data drift). `git status --short` clean before edits.
- All 6 tracked SHA-256 hashes **MATCH** (unchanged). Artifacts: **24** JSON files parse cleanly. `python3 -m pytest -q` → **71 passed, 0 failed** (0.64s, 2026-11-05T13:45Z).
- Free-data monitoring (2026-11-05T13:45Z): GitHub API `axb0306` MNQ path latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` — **no extension beyond 2026-04-15**. No genuinely free MNQ 1min/15min full-history source found. No data purchased; no credentials requested/stored; no code/strategy/parameter changes.

## Status (maintenance re-verification COMPLETE — 2026-11-05T13:43Z, this session) (prior)

- Branch `main`; HEAD `3f63cdd` at verification (checkpoint commits present; no strategy/code/data drift observed). `git status --short` clean before edits.
- SHA-256 re-verified from disk (all **MATCH**):
  - `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` (126 lines)
  - `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4` (77 lines)
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37` (5609 lines)
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99` (84078 lines)
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7` (1059205 lines)
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4` (70615 lines)
- Artifacts: **24** JSON files parse cleanly (0 parse errors). `artifacts/metrics_axb0306.json` SHA-256 `e06f9dd065963f60209353da8e15d2e8246651a1dfc636fab1948bec6296f93f` (9055 bytes).
- Baselines unchanged (from verified artifacts): axb0306 net **-$31637.98**, win rate **70%**, profit factor **0.4917**; Kaggle net **-$626525.96**, win rate **64.8%**, profit factor **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L.
- Tests: `python3 -m pytest -q` → **71 passed, 0 failed** (0.66s, 2026-11-05T13:43Z).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring (2026-11-05T13:43Z, this session):
  - GitHub API `repos/axb0306/cme-futures-ohlc/commits?path=MNQ&per_page=3` → latest MNQ-path commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` `2026-04-15T23:34:55Z` (priors 2026-04-14/13) — **no extension beyond 2026-04-15**.
  - Bounded web sweep (2026-11-05): paid/proprietary — MarketParquet MNQ full 1-min archive 2019-05-06..2026-10-23 ($79 one-time; free = ~365d daily + Apr 6–10 2026 intraday sample pack), FirstRate Data MNQ intraday 2019-05-05..2026-11-02 (purchase + $99.95/yr updates), Portara MNQ 1-min full ~199.6 MB (paid), Kibot All Futures Continuous+individual 1-min ($820 bundle / paid), FinzData/Barchart Premier/CME DataMine/Databento GLBX.MDP3 (credits/usage, not unrestricted free full history) — **not used/purchased**. Free but intraday-inadequate: Yahoo `MNQ=F`/`NQ=F` (1-min last ~30d, 5-min 60d, 1h 730d), MarketParquet free (~365d daily + sample week), Barchart free (2y daily only). Kaggle `tgtanalytics/nq-futures-1min-bar-2022-2025` ends 2025-11-12 (no newer upload observed); `brandenmorris/mnq-1-minute-data-5132025-11122025` narrow 2025 slice only. **No genuinely free MNQ 1min/15min full-history source extending beyond 2026-04-15 found.**

## Tasks (maintenance only — do in order)

1. **Re-verify repo state.** Run `git status --short` (expect clean), re-compute all 6 tracked SHA-256 hashes against the recorded values above, confirm `ls artifacts/*.json | wc -l` = 24 and `python3 -m pytest -q` = 71 passed / 0 failed. Record any drift with concrete evidence.
2. **Bounded free-data monitoring.** Check for a genuinely free MNQ 1min/15min full-history source that extends beyond 2026-04-15 (current latest free coverage). **Record provenance + SHA-256 before use.** Do not purchase data or bypass access controls/terms.
3. **No experiments/tuning.** Do not optimize thresholds, stops, targets, entry rules, or session times. Any change requires explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0.
4. **Update handoff files.** Update `HANDOFF.md` and this file with concrete evidence if anything changes (hashes, test counts, artifacts, new data candidates, blockers).

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through 2026-04-15.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- If a genuinely free MNQ 1min/15min source with longer history is found (**record provenance + SHA-256 before use**), the next concrete task is a re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning. Recompute metrics independently from the trade ledger and store configs/hashes/ledger/summary/validation artifacts.

(End of file)
