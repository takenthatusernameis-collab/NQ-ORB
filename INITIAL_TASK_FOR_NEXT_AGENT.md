# Initial Task for Next Agent — NQ ORB

## Current State: TERMINAL

The NQ/MNQ opening-range-breakout research is **complete and frozen**. Verified this session (2026-11-16, Kilo) against the working tree:

- `git rev-parse --short HEAD`: `72fb74f` (clean working tree; `a797773` is an ancestor, zero research drift)- **Strategy rules**: `STRATEGY_RULES.txt` v1.0 frozen (SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`)
- **Zero drift**: `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` is empty (no research/source changes since last substantive commit `a797773`)
- **Artifacts**: 35 files in `artifacts/`, no `*manifest*` files
- **Results (canonical, from artifacts JSON)**:
  - **axb0306** (`artifacts/metrics_axb0306.json`, 2026-01–2026-04): 60 trades (42W/18L, 70.0%), long 33/short 27, net -$31,637.98, costs $23,975.98, PF 0.4917, avg R -0.0431
  - **Kaggle** (`artifacts/metrics_kaggle.json`, proxy 2022-11–2025-11): 688 trades (446W/242L, 64.83%), long 359/short 329, net -$626,525.96, costs $275,113.96, PF 0.2271, avg R -0.0684
- **Data**: Free sources exhausted (`data/FEASIBILITY_REPORT.md`); no paid/proprietary data used. Raw hashes recorded in feasibility report.
- **Tests**: Last recorded passing suite in pytest-available environments was **75 passed**. pytest is **not installed** in this environment (`python3 -m pytest -q` reports `No module named pytest`), so the suite could not run here.

## Your Task

**Do not start autonomous research.** Do not create handoff-only checkpoints on generic prompts.

Report the terminal state above and **await explicit user decision** on one of three legitimate forward paths:

| Path | Description | Requires |
|------|-------------|----------|
| **(a)** | Stop/reduce maintenance automation (`.github/workflows/main.yml:11`, cron) | Explicit authorization for that exact change |
| **(b)** | Run a separately versioned, named experiment with explicit diff from frozen baseline (e.g. far-side-of-range stop per `STRATEGY_RULES.txt` §2.1) | Explicit user authorization + named experiment design |
| **(c)** | Accept baseline as final | Explicit user confirmation |

## Hard Constraints (Non-Negotiable)

- Historical research/simulation only — no broker/live/paper execution, no credentials, no paid data
- Never modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts
- Any strategy change = separately named, versioned experiment with explicit diff from baseline
- Never edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change

## Verification Commands

```bash
git status --short
git rev-parse --short HEAD
sha256sum STRATEGY_RULES.txt
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
ls artifacts | wc -l && ls artifacts | grep -c manifest || true
python3 -m pytest -q  # if pytest installed
```

## Reference Files

- `HANDOFF.md` — durable handoff (updated this session)
- `STRATEGY_RULES.txt` — frozen strategy definition
- `PROMPT.md` — research workflow definition
- `artifacts/metrics_axb0306.json` — primary dataset metrics
- `artifacts/metrics_kaggle.json` — proxy dataset metrics
- `data/FEASIBILITY_REPORT.md` — data sourcing evidence