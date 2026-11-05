# Initial Task for Next Agent

## Status (session 2026-11-05 — maintenance re-verification pass COMPLETE, HEAD 6e71e87)

- Branch main; HEAD 6e71e87 (chore(kilo): checkpoint agent session); working tree clean (`git status --short` empty, no untracked files). Recent commits: 6e71e87, 55f9677, 7f2ad6e, 36be7a0, 9f0eb8e, a7c4c55, 8930346.
- SHA-256 verified from disk (2026-11-05): all six tracked file hashes match recorded values.
- Artifacts: 21 files in artifacts/ (README.md + 20 JSON); all JSON parse cleanly (0 parse errors).
- Walk-forward verified from artifacts: axb0306 3 windows, all test_net_pnl negative ([-10053.14, -21922.10, -23058.98]). Kaggle 8 windows, all test_net_pnl negative ([-178375.24, -173264.64, -168315.48, -134617.64, -122071.62, -70637.24, -104755.42, -114820.72]).
- Baselines verified: axb0306_full 60 trades, 70.0% WR, net -$31,637.98; Kaggle front-month 688 trades, 64.8256% WR, net -$626,525.96.
- Raw date ranges unchanged: axb0306 ends 2026-04-15T23:15:00/23:29:00 (stale); Kaggle front-month ends 2025-11-12T23:59:00/23:45:00.
- Tests: `python3 -m pytest tests/` = 71 passed, 0 failed (pytest 9.2.0 available this session).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring re-scan (2026-11-05): unchanged — no new genuinely free MNQ 1min/15min source found.

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

(End of file)
