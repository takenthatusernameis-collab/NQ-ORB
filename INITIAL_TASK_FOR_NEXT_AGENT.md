# Initial Task for Next Agent — NQ ORB

## Current State: TERMINAL

The NQ/MNQ opening-range-breakout research is **complete and frozen**. All verification checks pass:

- **Strategy rules**: `STRATEGY_RULES.txt` v1.0 frozen (SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`)
- **Zero drift**: No research/source changes since last substantive commit `a797773`
- **Artifacts**: 35 files, no manifests, canonical metrics unchanged
- **Results**: Baseline negative-net on every free dataset tested
  - **axb0306** (60 trades, 2026-01 to 2026-04): net -$31,638, PF 0.49, avg R -0.043
  - **Kaggle** (688 trades, 2022-11 to 2025-11): net -$626,526, PF 0.23, avg R -0.068
- **Data**: Free sources exhausted; no paid/proprietary data used
- **Tests**: 75 passed (last recorded in pytest-available environments)

## Your Task

**Do not start autonomous research.** Do not create handoff-only checkpoints on generic prompts.

Report the terminal state above and **await explicit user decision** on one of three legitimate forward paths:

| Path | Description | Requires |
|------|-------------|----------|
| **(a)** | Stop/reduce maintenance automation (`.github/workflows/main.yml:11`, cron) | Explicit auth for that exact change |
| **(b)** | Run a separately versioned, named experiment with explicit diff from frozen baseline (e.g. far-side-of-range stop per `STRATEGY_RULES.txt` §2.1) | Explicit user authorization + named experiment design |
| **(c)** | Accept baseline as final | Explicit user confirmation |

## Hard Constraints (Non-Negotiable)

- Historical research/simulation only — no broker/live/paper execution, no credentials, no paid data
- Never modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts
- Any strategy change = separately named, versioned experiment with explicit diff from baseline
- Never edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change

## Verification Commands (run to confirm state)

```bash
git status --short
git rev-parse --short HEAD
sha256sum STRATEGY_RULES.txt
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
ls artifacts | wc -l && ls artifacts | grep -c manifest || true
python3 -m pytest -q  # if pytest installed
```

## Reference Files

- `HANDOFF.md` — this durable handoff (updated this session)
- `STRATEGY_RULES.txt` — frozen strategy definition
- `PROMPT.md` — research workflow definition
- `artifacts/metrics_axb0306.json` — primary dataset metrics
- `artifacts/metrics_kaggle.json` — proxy dataset metrics
- `data/FEASIBILITY_REPORT.md` — data sourcing evidence