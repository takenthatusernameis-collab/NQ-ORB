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
- Verdict: **Partially sufficient for implementation/test infrastructure** with 1min+15min, but **coverage is short** (Jan-Apr 2026). For a meaningful out-of-sample test we need longer history. Also need to confirm continuous contract method and whether 15:55 exits can be evaluated exactly with 1min data (yes, 1min bars exist).

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
The axb0306 repo provides MNQ 1-minute bars in UTC. With 1-minute-or-better data we can evaluate intrabar touches and the 15:55 ET flatten exactly (by scanning 1min bars up to 15:55). So **15:55 flatten is testable with 1min data from this source** if we handle timezone correctly and have continuous contract methodology documented.

## Blockers / gaps
1. **Limited history**: ~3 months of 1min/15min for MNQ (Jan 20 - Apr 15 2026). Insufficient for robust walk-forward/OOS; need longer free history.
2. **Continuous contract method unknown**: Need to inspect repo more (update_data.py, config) and sample data around rolls? Or check if it's back-adjusted. Must record adjustment method.
3. **NQ vs MNQ**: Must use MNQ ($2/point). Have MNQ.
4. **Exact contract months/rolls**: Need to see if individual contracts or continuous; filename suggests continuous series? "MNQ_1min_..." without contract month in name like MNQH26 - could be continuous. Repo says "continuous data series and individual futures contracts" - need to look up how files are structured.

## Recommendation
Proceed to implement infrastructure using this free source as a **test dataset** to validate logic, but **do not claim full empirical validation** due to limited history. Try to find longer free MNQ history (e.g. Topstep-style public samples, other GitHub repos, or Kaggle MNQ if exists). Document everything. Do not purchase data.
