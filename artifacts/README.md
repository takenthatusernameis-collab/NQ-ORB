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

The `_verify` files are byte-equivalent (in all metric fields) re-runs produced in
session 2026-10-31o from the same raw CSVs. They exist to demonstrate
reproducibility; the non-`_verify` files above remain canonical.

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