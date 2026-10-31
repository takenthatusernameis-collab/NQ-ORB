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
- axb0306 (2026-01-20..2026-04-15, unverified continuous, 1min+15min): 60 trades, 42W/18L (70.0%), gross -$7,662.00, net -$31,637.98, total costs $23,975.98, avg R -0.0431, expectancy -$527.30/trade, PF 0.492, max DD $37,491.80, longs 33 (-$17,601.84), shorts 27 (-$14,036.14). Chrono splits (train/val/test) on limited sample show train positive in gross but all negative net; OOS negative. Artifacts: artifacts/metrics.json, artifacts/trades_full.json.
- Kaggle front-month (2022-11-16..2025-11-12, unadjusted front-month by max volume, 1min+15min): 688 trades, 446W/242L (64.83%), gross -$140,899.00, net -$626,525.96, total costs $485,626.96, avg R -0.0684, expectancy -$910.65/trade, PF 0.227, max DD ~$626,994.56, longs 359 (-$287,054.04), shorts 329 (-$339,471.92). Artifacts: artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json.
- Differences: Kaggle provides much longer history (3 years) and uses unadjusted front-month selection (cleaner for executable fills); axb0306 is shorter recent sample with unverified continuous series. Both show negative net performance under full costs with this preset on available samples; Kaggle has larger drawdowns in absolute terms due to more trades/longer period. No multi-year free MNQ 1min/15min coverage exists beyond these sources; history depth remains a blocker for robust walk-forward/OOS.
- Note: Results are from short/limited free samples only; not proof of edge. Costs (commissions+fees $2.87/side, slippage 1 tick adverse) dominate in both cases.
