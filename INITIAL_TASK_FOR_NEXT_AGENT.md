# Initial Task for Next Agent — NQ ORB

## Context
Research is in **terminal COMPLETE state**. Frozen MNQ 15-min ORB baseline (`STRATEGY_RULES.txt` v1.0, SHA `6d3258c3…8ad2b1`) is negative-net on every freely available dataset; free MNQ 1-min/15-min search exhausted.

- axb0306 (NQ 15-min): 60 trades, net **-$31,637.98**
- Kaggle proxy (MNQ 15-min): 688 trades, net **-$626,525.96**
- 1-min experiment `orb_mnq_1m_wf_v1`: **byte-identical** to 15m; all splits/walk-forward/12 cost-sensitivity combos negative
- Drift re-confirmed 2026-11-14T09:39Z: clean tree, SHA match, no non-doc commits since `a797773` (HEAD `4724faa`)

## Task
**Do nothing unless the user explicitly directs one of:**
1. **Stop/reduce maintenance automation** — change `*/5 * * * *` in `.github/workflows/main.yml` (explicit user authorization required)
2. **Run a separately-versioned experiment** — e.g. far-side-of-range stop (`STRATEGY_RULES.txt` §2.1) as `experiment_farside_stop_v1` with explicit diff from baseline
3. **Accept baseline as final** — archive project

## Constraints
- Do not re-run tests, re-hash, re-verify drift, or add checkpoint commits
- Do not edit `.github/workflows/main.yml`, controller, or automation policy without explicit authorization
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts
- Any strategy change = separately named, versioned experiment with explicit diff
- Historical research/simulation only; no broker/live execution, no credentials, no paid data

## If verification is explicitly required
```bash
git status --porcelain
sha256sum STRATEGY_RULES.txt
git log --oneline a797773..HEAD -- src/ config/ scripts/ tests/ raw/ data/ artifacts/
```
Expect: clean tree, SHA `6d3258c3…8ad2b1`, empty log.

**Default:** report terminal state and await user decision. Do not create work.