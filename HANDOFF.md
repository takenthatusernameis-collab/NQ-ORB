# NQ ORB — Durable handoff

## Status: terminal research complete; awaiting user decision

**This session (2026-11-16, Kilo, verification #62):** Completed prior agent task (read durable handoff, verified terminal state, refreshed handoff and initial task message) at explicit user request. Independently re-verified current working tree (HEAD `d4b33a3`; `git status --short` clean before this doc refresh). All checks pass: `sha256sum STRATEGY_RULES.txt` = `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` empty (0 lines); `ls artifacts | wc -l` = 35, no `*manifest*`; canonical metrics re-read from artifacts JSON unchanged (axb0306 trade_count=60, wins=42, losses=18, win_rate=0.70, long_trades=33, short_trades=27, net_pnl=-31637.98, PF=0.4917, avg_r=-0.0431; Kaggle trade_count=688, wins=446, losses=242, win_rate=0.6483, long_trades=359, short_trades=329, net_pnl=-626525.96, PF=0.2271, avg_r=-0.0684). `python3 -m pytest` unavailable in this environment (no module named pytest), so test suite was not run this session (last recorded passing suite in prior sessions: 75 passed). No research/data/test/automation source changes made. State remains terminal; forward paths (a)/(b)/(c) require explicit user decision.

## Verified terminal state (canonical)

- `STRATEGY_RULES.txt` v1.0 frozen — SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`
- Baseline commit: `5fab764` (frozen showcase preset). Last substantive research commit: `a797773`
- `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` → empty (no research/data/test/automation source drift since last substantive commit)
- `artifacts/`: 35 files, no `*manifest*`
- Canonical metrics (from artifacts JSON):
  - **axb0306** (`artifacts/metrics_axb0306.json`): 60 trades (42W/18L, 70.0%), long 33 / short 27, net PnL -$31,637.98, costs $23,975.98, PF 0.4917, avg R -0.0431
  - **Kaggle** (`artifacts/metrics_kaggle.json`, proxy): 688 trades (446W/242L, 64.83%), long 359 / short 329, net PnL -$626,525.96, costs $275,113.96, PF 0.2271, avg R -0.0684
- 1-minute experiment `orb_mnq_1m_wf_v1` did not change canonical results (artifacts preserved). Baseline negative-net on every available free dataset.
- Raw data hashes (per `data/FEASIBILITY_REPORT.md`): `raw/MNQ_15min.csv` f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; `raw/MNQ_1min.csv` 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99
- Free-source search exhausted (`data/FEASIBILITY_REPORT.md`). No paid/proprietary data used.

## Prior session trail (condensed)

Repeated independent verifications (#3–#62, 2026-11-16, Kilo sessions) consistently confirmed frozen rules hash, zero research-source drift vs `a797773`, 35 artifacts/no manifests, and unchanged canonical metrics. Full test suite last recorded passing in environments with pytest: **75 passed**. Many recent environments lack pytest (`python3 -m pytest` unavailable). Prior detailed per-session entries were checkpoint-only and carried no research changes; this condensed handoff preserves essential evidence while reducing repetition.

## Required action for next agent

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
git rev-parse --short HEAD
sha256sum STRATEGY_RULES.txt
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts
ls artifacts | wc -l && ls artifacts | grep -c manifest || true
python3 -m pytest -q  # if pytest installed
```
