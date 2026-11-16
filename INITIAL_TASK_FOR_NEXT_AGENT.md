# Initial Task for Next Agent

## Context
NQ ORB research is **COMPLETE and TERMINAL**. Frozen MNQ 15-min ORB baseline is final and negative-net on every available free dataset (axb0306 and Kaggle proxy). 1-minute experiment `orb_mnq_1m_wf_v1` did not change canonical results. Free-source search is exhausted (`data/FEASIBILITY_REPORT.md`).

## Verified state (2026-11-16, verification #59, HEAD `3eaaeb8`)
- `STRATEGY_RULES.txt` v1.0 frozen — SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`
- Baseline commit `5fab764`; last substantive research commit `a797773`
- `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` → empty
- `artifacts/`: 35 files, no `*manifest*`
- Canonical metrics unchanged:
  - **axb0306** (`artifacts/metrics_axb0306.json`): 60 trades (42W/18L, 70.0%), long 33 / short 27, net PnL -$31,637.98, PF 0.4917, avg R -0.0431
  - **Kaggle** (`artifacts/metrics_kaggle.json`): 688 trades (446W/242L, 64.83%), long 359 / short 329, net PnL -$626,525.96, PF 0.2271, avg R -0.0684
- `python3 -m pytest` not available in this environment (no module named pytest); last recorded full suite run in prior sessions: 75 passed

## Required action
**Do not start autonomous research and do not create handoff-only checkpoints on generic prompts.** Report terminal state and await explicit user decision.

Legitimate forward paths (only with explicit user authorization):
- **(a)** Stop/reduce maintenance automation (`.github/workflows/main.yml:11`, cron) — requires explicit auth for that exact change
- **(b)** Run a separately versioned, named experiment with explicit diff from frozen baseline (e.g. far-side-of-range stop per `STRATEGY_RULES.txt` §2.1)
- **(c)** Accept baseline as final

## Hard constraints
- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

## Verification commands
```bash
git status --short
sha256sum STRATEGY_RULES.txt
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
ls artifacts | wc -l
python3 -m pytest  # if pytest installed
```
