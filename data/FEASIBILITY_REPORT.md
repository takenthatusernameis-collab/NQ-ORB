# Free Data Feasibility Report — NQ/MNQ ORB (MNQ showcase)

Date: 2026-10-30
Repo: takenthatusernameis-collab/NQ-ORB

## Tested free sources

### 1) axb0306/cme-futures-ohlc (GitHub, public)
- Repo: https://github.com/axb0306/cme-futures-ohlc
- License/terms: Public repo; data appears sourced from TopstepX via ProjectX Gateway API (stated in README). Not explicitly labeled as exchange redistributable for commercial use, but publicly available on GitHub. Treated as freely accessible; record provenance.
- Symbols present: MNQ, NQ (and others). MNQ has 1min/5min/15min/30min/1h/4h/daily/tick.
- MNQ files observed:
  - MNQ_1min_20260120_20260415.csv
  - MNQ_15min_20260120_20260415.csv
  - MNQ_5min_*, MNQ_30min_*, etc., MNQ_tick_* present
- Format: `datetime,open,high,low,close,volume` (UTC in CSV as stated in repo README: "All timestamps are in UTC.")
- Sample inspection:
  - 1min first rows: 2026-01-20T13:27:00, 13:28:00,...
  - 15min: 2026-01-20T13:15:00, 13:30:00, 13:45:00, 14:00:00,...
- Timezone conversion (UTC->ET): 2026-01-20T14:30:00Z -> 2026-01-20 09:30:00-05:00 (EST). Yes, matches 09:30 ET open.
- Coverage (from filenames): MNQ 1min/15min cover 2026-01-20 to 2026-04-15 (~3 months). MNQ daily goes back to 2025-03-24. This is recent but limited depth (a few months). Not enough for multi-year walk-forward with long out-of-sample; need more history.
- Volume: present.
- Contracts/rolls: Files look like continuous-like series by filename convention; repo says "Structured OHLC dataset..." updated nightly. Need to inspect if continuous adjusted/unadjusted. Roll/adjustment method must be documented before use (see rule 6). If back-adjusted, cannot treat as executable prices blindly.
- Gaps/missing: unknown without full scan.
- Suitability:
  - 15min: sufficient for OR, first break, RVOL (need 20 preceding 15min bars), ATR(14) on 15min.
  - 1min: present (good for intrabar ordering / 15:55 flatten logic). Can test stop/target ordering on 1min if using that resolution.
- Verdict: **Partially sufficient for implementation/test infrastructure** with 1min+15min, but **coverage is short** (Jan-Apr 2026). For a meaningful out-of-sample test we need longer history. Roll/adjustment method now documented (see below): single-contract MNQ.M26, no adjustment.

### 2) FirstRate Data (firstratedata.com)
- Commercial/free sample? Site says "Download Sample" available; full data is paid (subscription mentioned). Not freely downloadable in full without purchase. Cannot rely on free full dataset. Skip for free-data path.

### 3) PortaraCQG
- Commercial. Skip.

### 4) historicalfuturesdata.com
- Has samples (Parquet). Free account mentioned for some data? Says "No account: 10-second samples Free account: all monthly timeframes and CME daily history". MNQ 1min sample exists. Unclear if full history freely downloadable without account/subscription; need to check terms. But samples exist. Still not obviously a bulk free full-history source like GitHub repo.

### 5) Kaggle datasets
- Some NQ datasets exist (e.g. tgtanalytics/nq-futures-1min-bar-2022-2025) - NQ (big contract), not MNQ. Also may have usage terms. But strategy specifies MNQ showcase; better to use MNQ. Coverage varies.

### 6) nqbacktest.online
- Simulator, not bulk historical data download for research pipeline.

## Conclusion on 15:55 ET forced flatten
The axb0306 repo provides MNQ 1-minute bars in UTC. With 1-minute-or-better data we can evaluate intrabar touches and the 15:55 ET flatten exactly (by scanning 1min bars up to 15:55). Session audit (2026-10-31) confirms 15:55 ET 1min bars exist on 60 trading days — the same 60 days that produce trades — so **the forced-flatten exit is fully evaluable** on the axb0306 sample, not marked unverified. The 15:55 fill uses the 15:55 1min bar's open when the bar timestamp equals 15:55, else its close.

## Required performance reporting (added 2026-10-31)
The full AGENTS.md-required metric set is now computed by `runner.compute_metrics` and stored in
`artifacts/metrics_axb0306.json` and `artifacts/metrics_kaggle.json`. Fields added:
- `avg_win_r`, `avg_loss_r`, `avg_win_usd`, `avg_loss_usd` (win/loss splits in R and USD)
- `cagr` (with `capital_convention` and `years_covered`; `None` when net P&L is non-positive)
- `sharpe_r`, `sortino_r` (annualized from per-trade R returns, factor sqrt(252), per-trade frequency)
- `worst_day_usd`/`worst_day_date`, `best_day_usd`/`best_day_date`
- `monthly_net_pnl`, `yearly_net_pnl` dictionaries
- `exposure_pct` (bars held / 27 possible 15-min bars per session)
- `signal_close_entry_sensitivity` (separate scenario only, never mixed with primary)

Baseline axb0306 (cost-aware, trade counts unchanged): avg_win_r 0.377R, avg_loss_r 1.024R
(break-even requires win rate > 1/(1+0.4) = 71.43%; observed 70% but losses are ~2.7x wins in R,
so expectancy is negative). Sharpe -1.06, Sortino -0.67, worst day 2026-01-27 (-$3,811.28),
exposure 0.103% of session bars. Monthly: Jan +$697.96, Feb +$2,215.78, Mar -$24,373.58,
Apr -$10,178.14. Signal-close entry sensitivity is also negative across all slippage levels.

Baseline Kaggle front-month: avg_win_r 0.380R, avg_loss_r 1.030R, Sharpe -1.68, Sortino -1.04,
worst day 2023-05-12 (-$4,789.80), exposure 0.081%. All 36 months negative except 2025-09 (+$1,803.20).

## Deterministic test coverage (2026-10-31)
`tests/orb/test_orb_logic.py` now covers, with synthetic fixtures: opening-range construction,
first-breakout only, both regime filters (RVOL excludes breakout bar, ATR% floor/ceiling), both
directions, stop/target math (0.4R long and short), tick rounding to 0.25, position sizing floor/skip,
one-trade-per-day, 15:00 entry cutoff, 15:55 forced flatten via 1min data, wick-without-close not a
breakout, DST spring-forward and fall-back conversions, ambiguous intrabar touch (stop-first),
contract-roll edge cases (no cross-contract contamination), config field defaults, plus numeric
verification that the RVOL denominator excludes the breakout bar, that a failed first breakout
blocks any second breakout the same day, and that the full required-metric set plus the
signal-close entry sensitivity are produced. Full suite: `python -m pytest tests -q` -> 63 passed.

## Free-data search (expanded, 2026-10-31)
- Searched for additional free MNQ 1min/15min sources (Kaggle, GitHub, public repos). Found Kaggle dataset `brandenmorris/mnq-1-minute-data-5132025-11122025` (Databento GLBX.MDP3) cached locally; built front-month unadjusted series (2022-11-16..2025-11-12) with hashes recorded below and in artifacts. Other MNQ-specific long free 1min sources not located in this environment; NQ (big contract) datasets exist but are not MNQ. No paid data purchased.
- axb0306/cme-futures-ohlc remains the other source (~2026-01-20..2026-04-15). Both documented with roll methods.

## Blockers / gaps
1. **Limited history**: ~3 months of 1min/15min for MNQ (Jan 20 - Apr 15 2026). Insufficient for robust walk-forward/OOS; need longer free history.
2. **Continuous contract method — RESOLVED 2026-10-31**: axb0306 is single-contract (MNQ.M26), no roll, no adjustment (see above). Kaggle is unadjusted front-month by max volume. No back-adjustment in either source.
3. **NQ vs MNQ**: Must use MNQ ($2/point). Have MNQ.
4. **Exact contract months/rolls**: axb0306 = MNQ.M26 only, no roll in sample (verified). Kaggle = front-month by max volume, 100% dominance (verified).

## Recommendation
Proceed to implement infrastructure using this free source as a **test dataset** to validate logic, but **do not claim full empirical validation** due to limited history. Try to find longer free MNQ history (e.g. Topstep-style public samples, other GitHub repos, or Kaggle MNQ if exists). Document everything. Do not purchase data.

## Raw data hashes (SHA-256)
- raw/MNQ_15min.csv: f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37 (5609 lines incl header)
- raw/MNQ_1min.csv: 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99 (84078 lines incl header)
- raw/MNQ_1min_frontmonth.csv: edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7
- raw/MNQ_15min_frontmonth.csv: 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4
- source (Kaggle GLBX MDP3): glbx-mdp3-20221116-20251112.ohlcv-1m.csv cached at /home/runner/work/_temp/kilo-home/.cache/kagglehub/datasets/brandenmorris/mnq-1-minute-data-5132025-11122025/versions/1/MNQ_OHLCV_5-13-2025--11-12-2025/ (hash recorded via build script)

## Reproducibility verification (session 2026-10-31o)

Both baselines were re-run from scratch (fresh process, same raw CSVs, same frozen
config) and compared field-by-field against the stored canonical artifacts. All
numeric metric fields are byte-identical, confirming deterministic execution.

- `python src/orb/runner.py --prefix axb0306_verify --source axb0306`
- `python src/orb/runner.py --prefix kaggle_verify --source kaggle`
- Comparison: `artifacts/metrics_axb0306.json` vs `metrics_axb0306_verify.json`,
  `artifacts/metrics_kaggle.json` vs `metrics_kaggle_verify.json`.
- Matched fields (both sources): trade_count, win_rate, gross_pnl, net_pnl, costs,
  avg_r, expectancy_usd, profit_factor, max_drawdown_usd, sharpe_r, sortino_r,
  exposure_pct, and the full cost-sensitivity grid (12 scenarios each).
- Reproduced baselines unchanged:
  - axb0306: 60 trades, 70.0% WR, gross -$7,662.00, net -$31,637.98, PF 0.492.
  - Kaggle front-month: 688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.227.

## Independent signal-funnel cross-check (session 2026-10-31o)

`scripts/diag_signal_funnel.py` re-implements the filter chain independently from
`BacktestEngine.run` (separate code path) and counts trades per stage on the
Kaggle front-month series:

- 932 trading dates; 771 with an OR built (161 no-OR days excluded).
- 765 days with a first close-beyond-range breakout.
- 688 pass RVOL>=1.0 AND 0.10%<=ATR%<=0.60%.
- 688 pass the <15:00 cutoff, 688 pass sizing (>=1 contract), 688 have a next-bar
  open entry.
- **Engine trade count: 688 — matches the independent funnel exactly.**

A matching independent funnel run on the axb0306 sample (61 OR days, 61 first
breakouts, 60 pass filters) also matches the engine's 60 trades. The 1-trade-per-day
and first-breakout-only rules are the only reason counts fall below the breakout
count, and they are enforced identically in both paths.

Ledger integrity checks (both samples): zero exits past 15:55 ET, zero days with
more than one trade, and stop/target prices within 0.125 index points (half a tick)
of the exact 0.4R formula — the residual is tick rounding, as required by the spec.

## Continuous contract / roll method documentation

### axb0306/cme-futures-ohlc (2026-01-20 to 2026-04-15) — ROLL METHOD NOW DOCUMENTED (2026-10-31)
- Inspected the repo's `update_data.py` (raw, fetched 2026-10-31). It authenticates to TopstepX via the ProjectX Gateway API (`/Auth/loginKey`, `/History/retrieveBars`) and downloads **a single fixed contract ID per symbol**. For MNQ the contract is `CON.F.US.MNQ.M26` (June 2026), with the code comment `# Current front-month contracts (update when contracts roll)`.
- **There is no roll logic and no back-adjustment.** The script appends new bars to one CSV and renames it with the updated end date. The series is therefore **single-contract, unadjusted** — not a continuous/rolled series. Prices are actual traded prices of MNQ.M26, satisfying STRATEGY_RULES.txt rule 6 (do not treat back-adjusted prices as executable fills).
- **Empirical verification (2026-10-31)**: scanned the sample for roll signatures.
  - 0 bars with |close-to-close| move > 2% (a roll gap would produce one).
  - Daily volume profile is stable across the sample (~1.0-2.3M/day) with no liquidity collapse; the 2026-03-10 MNQ front-month roll date shows no discontinuity.
  - Conclusion: **no roll occurs inside 2026-01-20..2026-04-15**; the whole sample is one contract (MNQ.M26). The `M26` code comment in the script is consistent with a June 2026 expiry that has not yet rolled in this window.
- **Caveat**: because the script hard-codes one contract ID and says "update when contracts roll", any future roll is a manual edit. If the repo is re-fetched after a roll, a new contract ID could silently appear in the same filename and create an unannounced discontinuity. Re-verify the hash and price continuity before using any re-downloaded file.
- **Baseline use**: the axb0306 baseline (60 trades) runs on this single-contract, unadjusted series. No roll bridging, no volume mixing across contracts.

### Kaggle brandenmorris/mnq-1-minute-data (5-13-2025 to 11-12-2025, Databento GLBX.MDP3)
- Source: Databento GLBX.MDP3 ohlcv-1m schema, symbol MNQ.FUT, stype_in=parent.
- Raw data is per-contract (instrument_id) with NO roll adjustment.
- Roll method: front-month selected per calendar date by maximum daily volume across contracts; front-month dominance is 100% on every date in the sample (verified), so selection is unambiguous.
- No adjustment applied: prices are actual traded prices, satisfying STRATEGY_RULES.txt requirement that back-adjusted prices must not be treated as executable fills.
- Outputs: raw/MNQ_1min_frontmonth.csv, raw/MNQ_15min_frontmonth.csv (aggregated from 1min).
- Hashes as above.

## Session / coverage audit (2026-10-31, axb0306)
- 15min: 74 calendar days present; 61 have a 09:30 ET bar; 60 have a 15:45 ET bar; **60 trading days have the complete 09:30-16:00 ET window (27 consecutive 15min bars)**. One day (2026-02-16) has only 14 bars (partial) and is excluded by the engine's OR requirement.
- 1min: bars exist at 15:55 ET on 60 trading days, so the forced-flatten exit is evaluable on exactly the same 60 days that produce trades.
- 2026-04-03 ends at 09:14 ET (555 bars) — an early-termination day, no OR bar, correctly skipped.
- DST: 2026-03-09 (spring forward) and 2026-11-01 (fall back) conversions verified; the sample spans the 2026-03-09 transition with full bars on both sides.

## Baseline comparison (cost-aware, MNQ showcase preset)
- axb0306 (2026-01-20..2026-04-15, single-contract MNQ.M26, no roll/no adjustment, 1min+15min): 60 trades, 42W/18L (70.0%), gross -$7,662.00, net -$31,637.98, total costs $23,975.98, avg R -0.0431, expectancy -$527.30/trade, PF 0.492, max DD $37,491.80, longs 33 (-$17,601.84), shorts 27 (-$14,036.14). Chrono splits (train/val/test) on limited sample show train positive in gross but all negative net; OOS negative. Artifacts: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json.
- Kaggle front-month (2022-11-16..2025-11-12, unadjusted front-month by max volume, 1min+15min): 688 trades, 446W/242L (64.83%), gross -$140,899.00, net -$626,525.96, total costs $485,626.96, avg R -0.0684, expectancy -$910.65/trade, PF 0.227, max DD ~$626,994.56, longs 359 (-$287,054.04), shorts 329 (-$339,471.92). Artifacts: artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json.
- Differences: Kaggle provides much longer history (3 years) and uses unadjusted front-month selection (cleaner for executable fills); axb0306 is a shorter recent single-contract sample (MNQ.M26, no roll, no adjustment). Both show negative net performance under full costs with this preset on available samples; Kaggle has larger drawdowns in absolute terms due to more trades/longer period. No multi-year free MNQ 1min/15min coverage exists beyond these sources; history depth remains a blocker for robust walk-forward/OOS.
- Note: Results are from short/limited free samples only; not proof of edge. Costs (commissions+fees $2.87/side, slippage 1 tick adverse) dominate in both cases.

## Free-data search update (2026-10-31)
- MarketParquet (marketparquet.com): PAID ("From $79"), not free. Excluded per no-purchase policy.
- historicalfuturesdata.com: PAID (pricing page present), not free. Excluded.
- No new free MNQ 1-min/15-min source located. Existing free sources remain axb0306 (~3 months) and Kaggle front-month (~3 years, unadjusted).

## Free-data search update (2026-10-31bc)
- Databento GLBX.MDP3 MNQ catalog (https://databento.com/catalog/cme/GLBX.MDP3/futures/MNQ): coverage 2019-04-14→present with OHLCV-1m/1m schemas — the deepest MNQ source found. **Not free without credentials**: the historical API requires an API key (`DATABENTO_API_KEY`, 32-char `db-` key obtained on signup) and consumes paid credits at $/GB beyond the $125 signup credit; the `dbn-cache` CLI (`azizuysal/dbn-cache`) also requires the key. The Kaggle brandenmorris dump already used is the same GLBX.MDP3 dataset. Excluded from the free-data path; no download performed; no API key requested or stored.
- FinzData (finzdata.com/futures/mnq): MNQ intraday 1-min/5-min/15-min from 2019-05-05 is a **$49 one-time purchase**; only the last 30 days of daily bars are free. Excluded per no-purchase policy.
- Portara, FirstRate Data, Yahoo Finance re-checked: paid / daily-only. No new genuinely free MNQ 1min/15min source located. No data purchased; no credentials added.

## Free-data search update (2026-10-31au)
- Re-ran the free-data sweep (GitHub, Kaggle, Yahoo Finance, Databento, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate, TickTradingData, infoway.io, CME DataMine, investing.com). No new genuinely free MNQ 1min/15min source located beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance is daily only; all other candidates are paid or key-gated. No data purchased; no credentials requested or stored.
- **FirstRate Data** re-inspected live: MNQ intraday bars 2019-05-05→2026-10-26 (1m/5m/15m/30m/1h/daily, continuous + individual contracts). A sample ZIP is offered, but the full dataset is a **paid bundle** — $99.95/yr annual subscription after 1 free month of updates. Excluded per no-purchase policy; no download performed.
- **FinzData** re-inspected live: MNQ intraday 1m/5m/15m/30m/hourly since 2019-05-05, plus back-adjusted continuous series. Free tier = last 30 days of daily bars only; full history at every bar size is **$29 one-time**. Excluded per no-purchase policy; no download performed; no API key requested.
- **CME Group DataMine** re-inspected: self-service purchase/subscription platform for historical futures datasets (incl. MNQ). Not free. Excluded.
- **investing.com** re-inspected: Micro Nasdaq 100 futures historical data is **daily only** in the free tier. Excluded.
- **arXiv 2605.04004** ("Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures"): a systematic falsification paper using 72,604 five-minute MNQ bars Dec 2021–Aug 2025 (947 complete RTH days) sourced from NinjaTrader. It is **a research paper, not a data source** — no raw bars, no download, no provenance/hashes to record. Cited here only as external corroboration that OHLCV-based MNQ intraday signals underperform after costs; not used as evidence for this repo.
- Baselines re-verified byte-for-byte this session (see HANDOFF.md). Frozen baseline preserved; no code/strategy/parameter changes; no data purchased.

## Free-data search update (2026-10-31aw)
- Re-ran the free-data sweep (GitHub, Kaggle, Yahoo Finance, Databento, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate). No new genuinely free MNQ 1min/15min source located beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance is daily only; all other candidates are paid or key-gated. No data purchased; no credentials requested or stored.
- Canonical artifacts refreshed to match the current deterministic engine output (added `long_short_split` and per-split long/short breakdowns); all core metric fields unchanged. See `artifacts/README.md`.

## Free-data search update (2026-10-31az)
- Re-ran the free-data sweep (GitHub, Kaggle, Yahoo Finance, Databento, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate). No new genuinely free MNQ 1min/15min source located beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance is daily only; all other candidates are paid or key-gated. No data purchased; no credentials requested or stored.
- **Kaggle re-pack duplicate check**: A second Kaggle dataset `brandenmorris/mnq-1m-q4-2022-q4-2025-ts-ohlcv-sym` was located and downloaded via `kagglehub`. Byte-level comparison against the already-ingested `brandenmorris/mnq-1-minute-data-5132025-11122025` (same Databento GLBX.MDP3 source) shows **identical data content** (1,727,376 OHLCV rows, same date range 2022-11-16→2025-11-12, same 40 contract symbols, all numeric columns match) — only the timestamp column name differs (`ts_event` vs `timestamp`). **No new data obtained**; excluded from the free-data path to avoid duplicate ingestion. No raw CSVs added; no hashes to record.
- GitHub search re-run (including `getdata-finance/nq-1m-ohlcv-stocks-historical-data`): that repo's NQ 1m sample is **US equities (NASDAQ-100 stocks), not MNQ futures** — excluded. `SDGDGFSDAD/NQ_FUTURES_1_MIN_PREDICTION` confirms free 1-min NQ/MNQ futures data is not available (its own README states this). No new free MNQ 1min/15min source.
- Baselines re-verified byte-for-byte this session (see HANDOFF.md). Frozen baseline preserved; no code/strategy/parameter changes; no data purchased.

## Free-data search update (2026-10-31ba)
- Re-ran the free-data sweep (GitHub, Kaggle, Yahoo Finance, Databento, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate, **TickTradingData**). No new genuinely free MNQ 1min/15min source located beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance is daily only; all other candidates are paid or key-gated.
- **TickTradingData (ticktradingdata.com)**: MNQ listed with tick-level data since 2019-05-16, but full history is **€200 per instrument** (or €5/month for 1 month of history). Not free. Excluded per no-purchase policy; no download performed; no credentials requested or stored.
- Baselines re-verified byte-for-byte this session (see HANDOFF.md). Frozen baseline preserved; no code/strategy/parameter changes; no data purchased.

## Free-data search update (2026-10-31ay)
- Re-ran the free-data sweep (GitHub, Kaggle, Yahoo Finance, Databento, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate, TickTradingData, infoway.io). No new genuinely free MNQ 1min/15min source located beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance is daily only; all other candidates are paid or key-gated. No data purchased; no credentials requested or stored.
- **MarketParquet (marketparquet.com)** re-inspected live: MNQ 1-min/5-min/30-min/1h continuous ratio-adjusted series 2019-05-06→2026-10-23 (US/Eastern). Free tier is **daily-only for the last 1 year** plus a 30-symbol 1-week intraday sample pack; the full MNQ 1-minute archive is **$79 one-time** ("Complete Archive"). Excluded per no-purchase policy; no download performed.
- **historicalfuturesdata.com** re-inspected live: MNQ 1-min bars are **$59/year per bar size** (annual downloads); free tier is only a latest-month 10-second sample plus daily bars for registered users. Excluded per no-purchase policy; no download performed.
- **infoway.io** requires a free API key signup for MNQ OHLCV; historical depth via kline endpoint is unverified and the service is not a documented bulk free archive. Not used; no key requested or stored.
- **GitHub re-scan** (`getdata-finance/nq-1m-ohlcv-stocks-historical-data`, `SDGDGFSDAD/NQ_FUTURES_1_MIN_PREDICTION`): NQ 1m samples are US equities (NASDAQ-100 stocks), not MNQ futures; the latter's own README confirms free 1-min NQ/MNQ futures data is not publicly available. No new free MNQ 1min/15min source.
- **Kaggle**: `tgtanalytics/nq-futures-1min-bar-2022-2025` and `youneseloiarm/nasdaq-cme-future-nq` are **NQ (big contract, $20/point)**, not MNQ — excluded per STRATEGY_RULES.txt (MNQ $2/point sizing). `brandenmorris/mnq-1-minute-data-5132025-11122025` remains the only free MNQ 1-min Kaggle source and is already ingested as the Kaggle front-month baseline.
- Baselines re-verified byte-for-byte this session (see HANDOFF.md). Frozen baseline preserved; no code/strategy/parameter changes; no data purchased.

## Free-data search update (2026-10-31bb)
- Re-ran the free-data sweep (GitHub, Kaggle, Yahoo Finance, Databento, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate, TickTradingData, infoway.io, CME DataMine, investing.com). No new genuinely free MNQ 1min/15min source located beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance is daily only; all other candidates are paid or key-gated. No data purchased; no credentials requested or stored.
- **FirstRate Data** re-inspected live: MNQ intraday bars 2019-05-05→2026-10-26 (1m/5m/15m/30m/1h/daily, continuous + individual contracts). A sample ZIP is offered, but the full dataset is a **paid bundle** — $99.95/yr annual subscription after 1 free month of updates. Excluded per no-purchase policy; no download performed.
- **FinzData** re-inspected live: MNQ intraday 1m/5m/15m/30m/hourly since 2019-05-05, plus back-adjusted continuous series. Free tier = last 30 days of daily bars only; full history at every bar size is **$29 one-time**. Excluded per no-purchase policy; no download performed; no API key requested.
- **CME Group DataMine** re-inspected: self-service purchase/subscription platform for historical futures datasets (incl. MNQ). Not free. Excluded.
- **investing.com** re-inspected: Micro Nasdaq 100 futures historical data is **daily only** in the free tier. Excluded.
- **arXiv 2605.04004** ("Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures"): a systematic falsification paper using 72,604 five-minute MNQ bars Dec 2021–Aug 2025 (947 complete RTH days) sourced from NinjaTrader. It is **a research paper, not a data source** — no raw bars, no download, no provenance/hashes to record. Cited only as external corroboration that OHLCV-based MNQ intraday signals underperform after costs; not used as evidence for this repo.
- **GitHub re-scan** (`getdata-finance/nq-1m-ohlcv-stocks-historical-data`, `SDGDGFSDAD/NQ_FUTURES_1_MIN_PREDICTION`): NQ 1m samples are US equities (NASDAQ-100 stocks), not MNQ futures; the latter's own README confirms free 1-min NQ/MNQ futures data is not publicly available. No new free MNQ 1min/15min source.
- **Kaggle re-scan**: `tgtanalytics/nq-futures-1min-bar-2022-2025` and `youneseloiarm/nasdaq-cme-future-nq` are **NQ (big contract, $20/point)**, not MNQ — excluded per STRATEGY_RULES.txt (MNQ $2/point sizing). A second Kaggle dataset `brandenmorris/mnq-1m-q4-2022-q4-2025-ts-ohlcv-sym` is a byte-identical duplicate of the already-ingested `brandenmorris/mnq-1-minute-data-5132025-11122025` (same Databento GLBX.MDP3 source, 1,727,376 rows, same date range, only the timestamp column name differs) — **no new data obtained**, excluded to avoid duplicate ingestion.
- **thinridge.io (independent audit)**: MNQ 1-minute continuous bars 2019-05-06→2026-08-14, 2,550,992 bars, tick 0.25 / $2 per point, sourced from FirstRate Data (paid). Confirms the free-data ceiling: nothing free covers years of MNQ 1-minute bars. Not ingested (paid upstream, no-purchase policy).
- Baselines re-verified byte-for-byte this session (see HANDOFF.md). Frozen baseline preserved; no code/strategy/parameter changes; no data purchased.

## Free-data search update (2026-10-31bm)
- Re-ran the free-data sweep (GitHub API repo commits + MNQ directory listing, Kaggle dataset search, Yahoo Finance, Databento GLBX.MDP3, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate, TickTradingData, infoway.io, CME DataMine, investing.com, thinridge.io, arXiv 2605.04004, getdata.finance). **No new genuinely free MNQ 1min/15min source** located beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance is daily only; all other candidates are paid or key-gated. No data purchased; no credentials requested or stored.
- **GitHub re-check (live API)**: axb0306/cme-futures-ohlc most recent commit on the `MNQ` path is still `60abd3fb…` dated **2026-04-15T23:34:55Z** ("Update 2026-04-15: 368 files updated") — unchanged since the prior session audit. No new intraday MNQ files, no extension of history.
- **Kaggle re-scan (live)**: MNQ hits remain `brandenmorris/mnq-1-minute-data-5132025-11122025` (ends 2025-11-12, already ingested) and its byte-identical duplicate `brandenmorris/mnq-1m-q4-2022-q4-2025-ts-ohlcv-sym`. New hits this sweep: `tzamrik/the-bold-play-that-passes-the-funded-challeng-data` (NQ regular-session bars 2022-12-27..2025-12-11, 284,310 rows) and `brtnsmth/intraday-market-data` (3-second multi-asset, no MNQ) — **both are NQ (big contract, $20/point), not MNQ**, excluded per STRATEGY_RULES.txt. `djjain21/nse-bse-and-mcx-f-and-o-historical-data-1-min-and-tick` is Indian NSE/MCX F&O, not MNQ. No new free MNQ 1min/15min source.
- **FirstRate Data** re-inspected live: MNQ intraday bars 2019-05-05→2026-10-26 (1m/5m/15m/30m/1h/daily, continuous + individual contracts). Sample ZIP offered; full dataset is a **paid bundle** ($99.95/yr after 1 free month). Excluded per no-purchase policy.
- **FinzData** re-inspected live: MNQ intraday 1m/5m/15m/30m/hourly since 2019-05-05 plus back-adjusted continuous series. Free tier = last 30 days of daily bars only; full history at every bar size is **$29 one-time**. Excluded per no-purchase policy.
- **Portara** re-inspected: paid (per-contract/continuous purchase, MNQ 1-min from 1999). Excluded.
- **Databento GLBX.MDP3 MNQ**: coverage 2019-04-14→present with OHLCV-1m/1m schemas — deepest MNQ source found, but **not free without credentials** (API key + paid credits beyond $125 signup credit). The Kaggle brandenmorris dump already used is the same GLBX.MDP3 dataset. Excluded from free-data path; no download; no API key requested or stored.
- **thinridge.io** re-inspected: MNQ 1-minute continuous bars 2019-05-06→2026-08-14, 2,550,992 bars, tick 0.25 / $2 per point, sourced from FirstRate Data (paid). Confirms the free-data ceiling. Not ingested (paid upstream, no-purchase policy).
- **getdata.finance** re-inspected: NQ/NAS100 1-minute OHLCV from broker CFD feeds (FXCM/Capital.com mid-quote), free six-month sample per asset, full archive is paid. Not MNQ exchange tape; excluded.
- **arXiv 2605.04004** (v1/v2/v3, latest 2026-09-15): research paper, not a data source. Cited only as external corroboration.
- Baselines re-verified byte-for-byte this session (see HANDOFF.md). Frozen baseline preserved; no code/strategy/parameter changes; no data purchased.

## Free-data search update (2026-10-31bn)
- Re-ran the free-data sweep (GitHub API repo commits + MNQ path listing, Kaggle dataset search, Yahoo Finance, Databento GLBX.MDP3, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate, TickTradingData, infoway.io, CME DataMine, investing.com, thinridge.io, arXiv 2605.04004, getdata.finance, kibot, quantnet). **No new genuinely free MNQ 1min/15min source** located beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance is daily only; all other candidates are paid or key-gated. No data purchased; no credentials requested or stored.
- **GitHub re-check (live API)**: axb0306/cme-futures-ohlc most recent commit on the `MNQ` path is still `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated **2026-04-15T23:34:55Z** ("Update 2026-04-15: 368 files updated") — unchanged since the prior session audit. No new intraday MNQ files, no extension of history.
- **Kaggle re-scan (live)**: MNQ hits remain `brandenmorris/mnq-1-minute-data-5132025-11122025` (ends 2025-11-12, already ingested as the Kaggle front-month baseline) and its byte-identical duplicate `brandenmorris/mnq-1m-q4-2022-q4-2025-ts-ohlcv-sym`. New hits this sweep (`tzamrik/the-bold-play-that-passes-the-funded-challeng-data`, `brtnsmth/intraday-market-data`, `tgtanalytics/nq-futures-1min-bar-2022-2025`, `youneseloiarm/nasdaq-cme-future-nq`, `djjain21/...`) are all **NQ (big contract, $20/point)**, not MNQ — excluded per STRATEGY_RULES.txt. No new free MNQ 1min/15min source.
- **FinzData** re-inspected live: MNQ intraday 1m/5m/15m/30m/hourly since 2019-05-05 plus back-adjusted continuous series. Free tier = last 30 days of daily bars only; full history at every bar size is **$49 one-time**. Excluded per no-purchase policy; no download performed; no API key requested.
- **FirstRate Data** re-inspected live: MNQ intraday bars 2019-05-05→2026-10-26 (1m/5m/15m/30m/1h/daily, continuous + individual contracts). Sample ZIP offered; full dataset is a **paid bundle** ($99.95/yr after 1 free month). Excluded per no-purchase policy.
- **historicalfuturesdata.com** re-inspected live: MNQ 1-min bars are **$59/year per bar size**; free tier is only a latest-month 10-second sample plus daily bars for registered users. Excluded per no-purchase policy.
- **MarketParquet** re-inspected live: MNQ 1-min/5-min/30-min/1h continuous ratio-adjusted series 2019-05-06→2026-10-23. Free tier is daily-only for the last 1 year plus a 30-symbol 1-week intraday sample pack; the full MNQ 1-minute archive is **$79 one-time**. Excluded per no-purchase policy.
- **TickTradingData**: MNQ listed with tick-level data since 2019-05-16, but full history is **€200 per instrument** (or €5/month). Not free. Excluded per no-purchase policy.
- **Kibot**: "All Futures Continuous Contracts 1-Minute Intraday Data" (83 symbols since 2009, incl. MNQ from 2019-05-05) is **$520.00 one-time** with a free sample. Excluded per no-purchase policy.
- **quantnet.com**: personal-sale thread offering MBO/Level-2 MNQ tick data 2022-2026 via Google Drive/AWS S3. Not a free public archive; excluded per no-purchase policy.
- **getdata.finance**: NQ/NAS100 1-minute OHLCV from broker CFD feeds (FXCM/Capital.com mid-quote), free six-month sample per asset, full archive is paid. Not MNQ exchange tape; excluded.
- **Databento GLBX.MDP3 MNQ**: coverage 2019-04-14→present — deepest MNQ source found, but **not free without credentials** (API key + paid credits beyond $125 signup credit). The Kaggle brandenmorris dump already used is the same GLBX.MDP3 dataset. Excluded from free-data path; no download; no API key requested or stored.
- **thinridge.io (independent audit)**: MNQ 1-minute continuous bars 2019-05-06→2026-08-14, 2,550,992 bars, tick 0.25 / $2 per point, sourced from FirstRate Data (paid). Confirms the free-data ceiling. Not ingested (paid upstream, no-purchase policy).
- **arXiv 2605.04004** (v1/v2/v3, latest 2026-09-15): research paper, not a data source. Cited only as external corroboration.
- Baselines re-verified byte-for-byte this session (see HANDOFF.md). Frozen baseline preserved; no code/strategy/parameter changes; no data purchased.

## Independent re-verification (session 2026-11-01)
- Both baselines re-run from a fresh process (`python3 src/orb/runner.py --source axb0306` / `--source kaggle`) and byte-diffed against canonical artifacts: metrics IDENTICAL for both; kaggle trades file SHA-256 identical (7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5). Verify copies deleted after comparison.
- Independent signal-funnel cross-check re-run: 932 trading dates, 771 OR-built, 765 first breakouts, 688 pass RVOL+ATR filters -> engine trade count 688, matches exactly.
- Full suite `python3 -m pytest tests -q` -> 66 passed. Raw data and frozen baseline hashes re-computed, all unchanged.
- Free-data sweep: no new genuinely free MNQ 1min/15min source beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume); Yahoo daily only. No data purchased; no credentials requested or stored.

## Free-data search update (2026-11-01be)
- Re-ran the free-data sweep (GitHub API repo commits + MNQ path listing, Kaggle dataset search, Yahoo Finance, MarketParquet, Databento, historicalfuturesdata.com, Firstrate, Barchart, CME DataMine, dbn-cache). **No new genuinely free MNQ 1min/15min source** located beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance is daily only; all other candidates are paid or key-gated. No data purchased; no credentials requested or stored.
- **GitHub re-check (live API)**: axb0306/cme-futures-ohlc most recent commit on the `MNQ` path is still `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated **2026-04-15T23:34:55Z** ("Update 2026-04-15: 368 files updated") — unchanged since the prior session audit. The `MNQ/` directory listing (live) still contains exactly the same 8 files: `MNQ_15min_20260120_20260415.csv` (blob `7df04796…`), `MNQ_1h_20250321_20260415.csv`, `MNQ_1min_20260120_20260415.csv` (blob `946c6b76…`), `MNQ_30min_20260120_20260415.csv`, `MNQ_4h_20250321_20260415.csv`, `MNQ_5min_20260120_20260415.csv`, `MNQ_daily_20250324_20260414.csv`, `MNQ_tick_20260309_20260415.csv`. No new files, no extension of intraday history.
- **Kaggle re-scan (live)**: MNQ hits remain `brandenmorris/mnq-1-minute-data-5132025-11122025` (ends 2025-11-12, already ingested) and its byte-identical duplicate `brandenmorris/mnq-1m-q4-2022-q4-2025-ts-ohlcv-sym`. The duplicate's Q4-2022..Q4-2025 label overlaps the already-ingested front-month series (raw/MNQ_15min_frontmonth.csv starts 2022-11-16, raw/MNQ_1min_frontmonth.csv starts 2022-11-16) — **no new history**. New hits this sweep (`tgtanalytics/nq-futures-1min-bar-2022-2025`, `youneseloiarm/nasdaq-cme-future-nq`, `sentinelx/nasdaq-5min-historical-data`) are all **NQ (big contract, $20/point)**, not MNQ — excluded per STRATEGY_RULES.txt. No new free MNQ 1min/15min source.
- **Coverage re-verified (local)**: raw/MNQ_15min_frontmonth.csv = 70,614 rows, 2022-11-16T00:00 → 2025-11-12T23:45; raw/MNQ_1min_frontmonth.csv = 1,059,204 rows, 2022-11-16T00:00 → 2025-11-12T23:59. raw/MNQ_15min.csv = 5,608 rows, 2026-01-20T13:15 → 2026-04-15T23:15; raw/MNQ_1min.csv = 84,077 rows, 2026-01-20T13:27 → 2026-04-15T23:29. No extension of either source.
- Baselines re-verified byte-for-byte this session (see HANDOFF.md). Frozen baseline preserved; no code/strategy/parameter changes; no data purchased.

## Free-data search update (2026-11-01br)
- Re-ran the free-data sweep (GitHub API axb0306/cme-futures-ohlc commits on path=MNQ, live websearch for MNQ free intraday download, Kaggle MNQ dataset search, Yahoo Finance, Databento GLBX.MDP3, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate, TickTradingData, infoway.io, CME DataMine, investing.com, thinridge.io, arXiv 2605.04004, getdata.finance, kibot, quantnet). **No new genuinely free MNQ 1min/15min source** located beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance is daily only; all other candidates are paid or key-gated. No data purchased; no credentials requested or stored.
- **GitHub re-check (live API)**: axb0306/cme-futures-ohlc most recent commit on the `MNQ` path is still `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated **2026-04-15T23:34:55Z** ("Update 2026-04-15: 368 files updated") — unchanged since the prior session audit. No new intraday MNQ files, no extension of history.
- **Live websearch re-scan**: MNQ 1-min/15-min free download hits re-confirmed as FirstRate Data ($99.95/yr after 1 free month; free sample ZIP available but not ingested per no-purchase policy), MarketParquet ($79 one-time for intraday archive; free tier daily-only), Kibot (MNQ 1-min 5yr $69.83; all-futures continuous 1-min $520), historicalfuturesdata.com ($59/yr per bar size; free tier = 10-second sample + daily for registered users), Portara (paid per-contract/continuous), Databento (key-gated + credit-based), Yahoo Finance (MNQ=F daily only), investing.com (daily-only). No genuinely free MNQ 1min/15min source.
- Baselines re-verified byte-for-byte this session (see HANDOFF.md). Frozen baseline preserved; no code/strategy/parameter changes; no data purchased.

## Free-data search update (2026-11-01h)
- Re-ran the free-data sweep (GitHub API axb0306/cme-futures-ohlc commits on path=MNQ + live MNQ directory listing, Kaggle brandenmorris datasets, live websearch for free MNQ 1min/15min download, Yahoo Finance, Databento GLBX.MDP3, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate, TickTradingData, infoway.io, CME DataMine, investing.com, thinridge.io, kibot, quantnet, getdata.finance, arXiv 2605.04004). **No new genuinely free MNQ 1min/15min source** located beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance is daily only; all other candidates are paid or key-gated. No data purchased; no credentials requested or stored.
- **GitHub re-check (live API)**: axb0306/cme-futures-ohlc most recent commit on the `MNQ` path is still `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated **2026-04-15T23:34:55Z** ("Update 2026-04-15: 368 files updated") — unchanged since the prior session audit. The `MNQ/` directory listing (live) still contains exactly the same 8 files: `MNQ_15min_20260120_20260415.csv` (blob `7df04796…`), `MNQ_1h_20250321_20260415.csv`, `MNQ_1min_20260120_20260415.csv` (blob `946c6b76…`), `MNQ_30min_20260120_20260415.csv`, `MNQ_4h_20250321_20260415.csv`, `MNQ_5min_20260120_20260415.csv`, `MNQ_daily_20250324_20260414.csv`, `MNQ_tick_20260309_20260415.csv`. No new files, no extension of intraday history.
- **Kaggle re-scan (live)**: brandenmorris's two MNQ datasets ("MNQ 1 Minute Data - 5/13/2025 -- 11/12/2025" and "MNQ-1m-Q4-2022--Q4-2025 (TS OHLCV SYM)") both still marked "Updated a year ago"; coverage still ends **2025-11-12** — no extension of the already-ingested front-month series. All other Kaggle hits remain NQ big contract ($20/point, excluded per STRATEGY_RULES.txt) or non-MNQ. No new free MNQ 1min/15min source.
- **Coverage re-verified (local)**: raw/MNQ_15min_frontmonth.csv = 70,614 rows, 2022-11-16T00:00 → 2025-11-12T23:45; raw/MNQ_1min_frontmonth.csv = 1,059,204 rows, 2022-11-16T00:00 → 2025-11-12T23:59. raw/MNQ_15min.csv = 5,608 rows, 2026-01-20T13:15 → 2026-04-15T23:15; raw/MNQ_1min.csv = 84,077 rows, 2026-01-20T13:27 → 2026-04-15T23:29. No extension of either source.
- Baselines re-verified byte-for-byte this session (see HANDOFF.md). Frozen baseline preserved; no code/strategy/parameter changes; no data purchased.

## Free-data search update (2026-11-01e4)
- Re-ran the free-data sweep (GitHub API axb0306/cme-futures-ohlc commits on path=MNQ + live MNQ directory listing, Kaggle brandenmorris datasets, live websearch for free MNQ 1min/15min download, Yahoo Finance, Databento GLBX.MDP3, FinzData, MarketParquet, historicalfuturesdata.com, Portara, FirstRate, TickTradingData, infoway.io, CME DataMine, investing.com, thinridge.io, kibot, quantnet, getdata.finance, Barchart, arXiv 2605.04004). **No new genuinely free MNQ 1min/15min source** located beyond axb0306 (~3 months, single-contract MNQ.M26, no roll/no adjustment) and Kaggle front-month (~3 years, unadjusted front-month by max volume). Yahoo Finance is daily only; all other candidates are paid or key-gated. No data purchased; no credentials requested or stored.
- **GitHub re-check (live API)**: axb0306/cme-futures-ohlc most recent commit on the `MNQ` path is still `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated **2026-04-15T23:34:55Z** ("Update 2026-04-15: 368 files updated") — unchanged since the prior session audit. The `MNQ/` directory listing (live) still contains exactly the same 8 files: `MNQ_15min_20260120_20260415.csv` (blob `7df04796…`), `MNQ_1h_20250321_20260415.csv`, `MNQ_1min_20260120_20260415.csv` (blob `946c6b76…`), `MNQ_30min_20260120_20260415.csv`, `MNQ_4h_20250321_20260415.csv`, `MNQ_5min_20260120_20260415.csv`, `MNQ_daily_20250324_20260414.csv`, `MNQ_tick_20260309_20260415.csv`. No new files, no extension of intraday history.
- **Kaggle re-scan (live)**: brandenmorris's two MNQ datasets ("MNQ 1 Minute Data - 5/13/2025 -- 11/12/2025" and "MNQ-1m-Q4-2022--Q4-2025 (TS OHLCV SYM)") both still marked "Updated a year ago"; coverage still ends **2025-11-12** — no extension of the already-ingested front-month series. All other Kaggle hits (NQ big contract $20/point, non-MNQ) excluded per STRATEGY_RULES.txt.
- **Barchart** re-inspected: free account = 2 years of daily, 1 download/day; intraday down to 1-minute (about 10 years) needs Premier (paid). Excluded.
- **MarketParquet** re-inspected: MNQ 1-min/5-min/30-min/1h continuous ratio-adjusted series 2019-05-06→2026-10-23, US/Eastern. Free tier = daily-only for last ~365 days + 30-symbol 1-week intraday sample pack; full MNQ 1-minute archive is **$79 one-time**. Excluded per no-purchase policy.
- **historicalfuturesdata.com** re-inspected: MNQ 1-min bars are **$59/year per bar size**; free tier = latest-month 10-second sample + daily for registered users. Excluded.
- **FinzData** re-inspected: MNQ intraday 1m/5m/15m/30m/hourly since 2019-05-05 plus back-adjusted continuous series. Free tier = last 30 days of daily bars only; full history at every bar size is **$49 one-time**. Excluded.
- **FirstRate Data** re-inspected: MNQ intraday bars 2019-05-05→2026-10-26 (1m/5m/15m/30m/1h/daily, continuous + individual contracts). Sample ZIP offered; full dataset is a **paid bundle** ($99.95/yr after 1 free month). Excluded.
- **Databento GLBX.MDP3 MNQ**: coverage 2019-04-14→present — deepest MNQ source found, but **not free without credentials** (API key + paid credits beyond $125 signup credit). The Kaggle brandenmorris dump already used is the same GLBX.MDP3 dataset. Excluded from free-data path; no download; no API key requested or stored.
- **arXiv 2605.04004** (v1/v2/v3, latest 2026-09-15): research paper, not a data source. Cited only as external corroboration.
- Baselines re-verified byte-for-byte this session (see HANDOFF.md). Frozen baseline preserved; no code/strategy/parameter changes; no data purchased.
