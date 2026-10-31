# Artifacts — NQ ORB

Canonical backtest outputs. All runs use the frozen `STRATEGY_RULES.txt` v1.0 /
`config/orb_mnq_15m_showcase.yaml` preset (no parameter changes).

## Canonical artifacts (source of truth)

| File | Source | Description |
|------|--------|-------------|
| `trades_axb0306.json` | axb0306/cme-futures-ohlc | Per-trade ledger (60 trades) |
| `metrics_axb0306.json` | axb0306 | Full required-metric set |
| `trades_kaggle.json` | Kaggle front-month | Per-trade ledger (688 trades) |
| `metrics_kaggle.json` | Kaggle | Full required-metric set |

## Freshly reproduced verification copies

The `_verify` files are re-runs produced from the same raw CSVs to demonstrate
reproducibility. Core metric fields (`trade_count`, `win_rate`, `gross/net P&L`,
`costs`, `avg_r`, `expectancy`, `profit_factor`, `max_drawdown`, `Sharpe`,
`Sortino`, `exposure`, cost grid, signal-close sensitivity) and the per-trade
ledgers are byte-identical to canonical on every re-run. The non-`_verify`
files remain canonical.

## Canonical refresh (2026-10-31)

The canonical `metrics_axb0306.json` / `metrics_kaggle.json` were regenerated
from the deterministic current engine (`src/orb/runner.py`). All core metric
fields are unchanged from the previously stored values; the refresh adds
breakdown fields that the engine now emits (`long_short_split`, per-split
long/short breakdowns inside `chronological_splits`). Trade ledgers
(`trades_axb0306.json`, `trades_kaggle.json`) were already byte-identical and
were not modified. Verification copies retained.

| File | Re-run of |
|------|-----------|
| `trades_axb0306_verify.json` | `trades_axb0306.json` |
| `metrics_axb0306_verify.json` | `metrics_axb0306.json` |
| `trades_kaggle_verify.json` | `trades_kaggle.json` |
| `metrics_kaggle_verify.json` | `metrics_kaggle.json` |

## Historical (retained, not canonical)

- `trades_baseline.json`, `trades_full.json`, `metrics.json` — earliest baseline
  outputs from the initial implementation session; superseded by `_axb0306`.
- `trades_axb0306_full.json`, `metrics_axb0306_full.json` — intermediate full
  ledger before the final metric set was added; superseded by `_axb0306`.

All historical files are retained for auditability; nothing has been deleted.

## Data provenance

Raw data lives in `raw/` (never committed). SHA-256 hashes and source details are
in `data/FEASIBILITY_REPORT.md`.