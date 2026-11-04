# Initial Task for Next Agent

## Status (session 2026-11-04 — maintenance re-verification pass COMPLETE, HEAD 7ab124e)

- Branch main; HEAD 7ab124e (chore(kilo): checkpoint agent session); working tree clean (`git status --short` empty); fetched origin --prune; up to date with origin/main. Recent commits: 7ab124e, 7287ad5, 4d00661, b007093, c33d275.
- SHA-256 verified from disk (2026-11-04): all six tracked file hashes match recorded values (STRATEGY_RULES.txt, config/orb_mnq_15m_showcase.yaml, raw/MNQ_15min.csv, raw/MNQ_1min.csv, raw/MNQ_1min_frontmonth.csv, raw/MNQ_15min_frontmonth.csv).
- Tests: pandas + pytest installed for verification; full suite `python3 -m pytest tests/` = 71 passed, 0 failed.
- Artifacts: 21 files in artifacts/ (README.md); 20 JSON parse cleanly. Walk-forward axb0306 3/3 test windows negative (-$10053.14, -$21922.10, -$23058.98). Walk-forward Kaggle 8/8 test windows negative (-$178375.24, -$173264.64, -$168315.48, -$134617.64, -$122071.62, -$70637.24, -$104755.42, -$114820.72).
- Baselines from canonical artifacts: axb0306 net -$31,637.98, 60 trades (70.0% WR); Kaggle front-month net -$626,525.96, 688 trades (64.83% WR).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data re-scan (2026-11-04): Kaggle brandenmorris MNQ (CC BY 4.0) still capped at 2025-11-12 (no newer file on dataset page); final ~2.9 months remain untouched OOS. axb0306 ends 2026-04-15 (stale). Paid/key-gated candidates unchanged. No genuinely free MNQ 1min/15min source found to extend coverage.

## Tasks (maintenance only)

1. **Re-verify** repo state (`git status`/`git log`/`git fetch origin --prune`), file hashes vs recorded values (the six tracked files listed in HANDOFF.md), canonical artifacts parseable, walk-forward present and all test windows negative. Run tests (`python3 -m pytest tests/`) if available.
2. **Optional reproducibility**: re-run both baselines from scratch (`python3 src/orb/runner.py --source axb0306 --prefix <name>` and `--source kaggle --prefix <name>`) and confirm metrics/trades match canonical artifacts. Remove any copies after comparison.
3. **Data monitoring**: watch for a new genuinely free MNQ 1min/15min source. If found, record source/license/access constraints, retrieval time, contract symbols/months, session timezone, bar timestamps, gaps, roll rules, adjustment method, and SHA-256 before any use. Known free: axb0306 (stale, ends 2026-04-15) and Kaggle front-month (ends 2025-11-12). All other candidates paid/key-gated/limited.
4. **No experiments without approval**: no parameter/strategy/rule changes without separately named, versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0.
5. **Update docs**: update HANDOFF.md and this file with concrete evidence if anything changes.

## Hard boundaries (AGENTS.md)

- Historical research and simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both baselines negative under full costs; all walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- axb0306 roll/adjustment: single-contract MNQ.M26, no roll inside sample; verify hash/continuity before re-downloading.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.

## Why this task

Maintenance/re-verification only. Do NOT tune stops/targets/filters/sizing/session times — STRATEGY_RULES.txt v1.0 frozen. Only (a) verify frozen baseline intact/reproducible, (b) watch for genuinely free MNQ 1min/15min data (provenance+SHA256 before use), (c) refresh HANDOFF.md/this file.
