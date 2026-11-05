# Initial Task for Next Agent

## Status (maintenance re-verification COMPLETE — 2026-11-05 09:24 UTC, this session)

- Branch `main`; HEAD at `5f23823` (2026-11-05, `chore(kilo): checkpoint agent session`), which touched only `HANDOFF.md`/`INITIAL_TASK_FOR_NEXT_AGENT.md`; code/data state unchanged from `707575c`. Working tree clean before handoff edits; handoff/task-file edits only during this session.
- SHA-256 re-verified from disk (all 6 **MATCH**): `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`, `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`, `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`, `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`, `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`, `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`.
- Artifacts: **24** JSON files parse cleanly (0 parse errors).
- Baselines unchanged (`metrics_*_full.json` / `metrics_verify_*`): `axb0306` net `-$31637.98`, win rate `70%`, profit factor `0.4917`; Kaggle net `-$626525.96`, win rate `64.8%`, profit factor `0.2271`. Prior verified walk-forward: `axb0306` 3 windows all negative; Kaggle 8 windows all negative.
- Raw rows unchanged (2026-11-05): `MNQ_15min` 5609; `MNQ_1min` 84078; `MNQ_1min_frontmonth` 1059205; `MNQ_15min_frontmonth` 70615 (total 1219507).
- Tests: `python3 -m pytest -q` → **71 passed, 0 failed** (0.88s, 2026-11-05 09:24 UTC).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring (2026-11-05 09:24 UTC bounded sweep): GitHub API `https://api.github.com/repos/axb0306/cme-futures-ohlc/contents/MNQ` lists 1min/15min only through 2026-04-15 (`MNQ_1min_20260120_20260415.csv` 4904282 bytes sha `946c6b76d685…`; `MNQ_15min_20260120_20260415.csv` 333668 bytes sha `7df047964034…`) — **no extension beyond 2026-04-15**. Latest commit on MNQ path `60abd3fb6369` dated 2026-04-15T23:34:55Z — unchanged. No new genuinely free MNQ 1min/15min full-history source located.

## Tasks (maintenance only)

1. Re-verify repo state, file hashes, artifacts, and run tests if available (`python3 -m pytest -q`). Record any drift with concrete evidence.
2. Bounded free-data monitoring for a genuinely free MNQ 1min/15min full-history source that extends beyond 2025-11-12 (front-month) and/or provides longer MNQ.M26 context; **record provenance + SHA-256 before use**. Do not purchase data or bypass access controls/terms.
3. No experiments/tuning without explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0. Do not optimize thresholds, stops, targets, entry rules, or session times.
4. Update `HANDOFF.md` and this file with concrete evidence if anything changes (hashes, test counts, artifacts, new data candidates, blockers).

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.

## Blockers / next concrete work

- Research blocked on data depth; both baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through 2026-04-15.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.
- If a genuinely free MNQ 1min/15min source with longer history is found (**record provenance + SHA-256 before use**), the next concrete task is a re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning. Recompute metrics independently from the trade ledger and store configs/hashes/ledger/summary/validation artifacts.
