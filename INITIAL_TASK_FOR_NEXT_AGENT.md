# Initial Task for Next Agent

## Context

The NQ ORB research is **COMPLETE and TERMINAL**. The frozen MNQ 15-min ORB baseline is final and negative-net on every available free dataset (axb0306 and Kaggle proxy). The 1-minute experiment `orb_mnq_1m_wf_v1` did not change canonical results. Free-source search is exhausted (see `data/FEASIBILITY_REPORT.md`).

## Current State (verified this session, HEAD `03a2c90`)

- **STRATEGY_RULES.txt** v1.0 frozen (SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`)
- **Baseline commit**: `5fab764`; **Last substantive research commit**: `a797773`
- **Working tree**: clean (`git status --short` empty); `git diff a797773..HEAD` on artifacts/config/src/tests/raw/data/scripts is empty
- **Artifacts**: 35 files in `artifacts/`, no manifest, metrics unchanged
- **Tests**: 75 passed (full suite green, ~0.73s)
- **Canonical metrics**:
  - axb0306: 60 trades, 70.0% win rate, net -$31,637.98, PF 0.4917, avg R -0.0431
  - Kaggle: 688 trades, 64.8% win rate, net -$626,525.96, PF 0.2271, avg R -0.0684

## Your Task

**Do not start autonomous research and do not add handoff-only checkpoints on generic prompts.** The correct action is to **report terminal state and await explicit user decision**. Repeated doc-only checkpoints add no new state.

Legitimate forward paths (require explicit user authorization):
- **(a)** Stop/reduce maintenance automation (cron at `.github/workflows/main.yml:11`)
- **(b)** Run a separately-versioned named experiment with explicit diff from baseline (e.g., far-side-of-range stop per `STRATEGY_RULES.txt` §2.1)
- **(c)** Accept baseline as final

## Hard Constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

## Verification Commands (for reference)

```bash
git status --short                              # should be clean
sha256sum STRATEGY_RULES.txt                    # should match frozen hash
git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts  # empty
ls artifacts | wc -l                            # 35
python3 -m pytest                               # 75 passed
```

## Expected Output

Report terminal state verification and present the three forward paths (a)/(b)/(c) for user decision. Do not proceed without explicit user direction.