# Initial Task for Next Agent — NQ ORB

## Status: terminal COMPLETE — do nothing by default

Research is in terminal COMPLETE state. Frozen MNQ 15-min ORB baseline (`STRATEGY_RULES.txt` v1.0, SHA `6d3258c3…8ad2b1`) is negative-net on every freely available dataset; free MNQ 1-min/15-min search exhausted. Drift re-confirmed 2026-11-14T11:19Z: clean tree, SHA match, no non-doc commits since `a797773` (HEAD `a57f9ae`).

Key results:
- axb0306 (NQ 15-min): 60 trades, net **-$31,637.98**
- Kaggle proxy (MNQ 15-min): 688 trades, net **-$626,525.96**
- 1-min experiment `orb_mnq_1m_wf_v1`: byte-identical to 15m; all splits/walk-forward/12 cost-sensitivity combos negative

## Task

**Default: report terminal state and await an explicit user decision. Do not create work, do not re-verify, do not add checkpoint commits.**

Only act if the user explicitly directs one of:

1. **Stop/reduce maintenance automation** — change `*/5 * * * *` in `.github/workflows/main.yml` (explicit user authorization required; do not edit without it).
2. **Run a separately-versioned experiment** — e.g. far-side-of-range stop (`STRATEGY_RULES.txt` §2.1) as `experiment_farside_stop_v1`, with an explicit diff from the frozen baseline.
3. **Accept baseline as final** — archive the project.

## Constraints

- Do not re-run tests, re-hash, re-verify drift, or add checkpoint commits.
- Do not edit `.github/workflows/main.yml`, controller, or automation policy without explicit authorization.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts.
- Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Historical research/simulation only; no broker/live execution, no credentials, no paid data.

## If verification is explicitly required

```bash
git status --porcelain
sha256sum STRATEGY_RULES.txt
git log --oneline a797773..HEAD -- src/ config/ scripts/ tests/ raw/ data/ artifacts/
```

Expect: clean tree, SHA `6d3258c3…8ad2b1`, empty log.
