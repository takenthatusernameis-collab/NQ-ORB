# Initial Task for Next Agent

## Status (session 2026-11-05 — maintenance re-verification pass COMPLETE, 0450b8a)

- Branch main; 0450b8a (chore(kilo): checkpoint agent session); working tree clean (`git status --short` empty, no untracked files). origin/main == 0450b8a. Recent commits: 0450b8a, 06fc22e, f98b75c, f3f5313, f06e98b.
- SHA-256 re-verified from disk (2026-11-05): all 6 tracked file hashes match recorded values.
- Artifacts: 25 entries in artifacts/ (24 JSON files parse cleanly, 0 parse errors).
- Walk-forward/baselines unchanged from prior verified artifacts (axb0306 3 windows all negative; Kaggle 8 windows all negative; axb0306 60 trades net -$31637.98; Kaggle 688 trades net -$626525.96).
- Raw date ranges unchanged: MNQ_15min.csv 2026-01-20T13:15 → 2026-04-15T23:15; MNQ_1min.csv 2026-01-20T13:27 → 2026-04-15T23:29; front-month files end 2025-11-12T23:45/23:59.
- Tests: pytest available; 71 passed/0 failed.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data re-scan: no new genuinely free MNQ 1min/15min full-history source found.

## Tasks (maintenance only)

1. Re-verify repo state, file hashes, artifacts, walk-forward, tests if available.
2. Data monitoring for genuinely free MNQ 1min/15min source; record provenance+SHA-256 before use.
3. No experiments without approval.
4. Update HANDOFF.md and this file with concrete evidence if anything changes.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both baselines negative under full costs; all walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- axb0306 roll/adjustment: single-contract MNQ.M26, no roll inside sample.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.

## Why this task

Maintenance/re-verification only. Do NOT tune stops/targets/filters/sizing/session times — STRATEGY_RULES.txt v1.0 frozen. Only (a) verify frozen baseline intact/reproducible, (b) watch for genuinely free MNQ 1min/15min data (provenance+SHA256 before use), (c) refresh HANDOFF.md/this file.
