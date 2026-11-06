# Handoff

## Current durable state (maintenance re-verification — 2026-11-06T13:44Z, this session)

- Session verification (2026-11-06T13:44Z, repo clean before edits): `git status --short` **clean** before edits (exit 0). All 6 tracked SHA-256 hashes **MATCH** (`STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`). 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed, 0 failed** (exit 0, 0.94s). No code/strategy/data/raw/artifact changes.
- Free-data monitoring (2026-11-06T13:44Z, `scripts/free_data_monitor.py`): ledger `research_state/free_data_monitor_2026-11-06T1344Z.json` (checked_at_utc `2026-11-06T13:40:14.164082+00:00`, file SHA-256 `ff3b46a58fbeab78792e4ba0f6ea163698ef3c790c3e72e34f7d7a75d60e7c81`, 14 candidates, JSON valid). `axb0306/cme-futures-ohlc` verdict **free**; latest MNQ 1min/15min coverage observed ends **2026-04-15** — **no extension beyond 2026-04-15**. **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified artifacts): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

## Prior maintenance verifications (evidence preserved in ledgers/commits)

- 2026-11-06T13:39Z: ledger `research_state/free_data_monitor_2026-11-06T1339Z.json` SHA-256 `9567e788329ddb57a8b1b2872a8f2c4fd79a0a70fb4d2cf3a7f07a4028be43a1`; checked `2026-11-06T13:39:25Z`, 14 candidates; hashes/artifacts/tests unchanged (71 passed); axb0306 MNQ ends 2026-04-15.
- 2026-11-06T13:36Z: ledger `research_state/free_data_monitor_2026-11-06T1336Z.json` SHA-256 `f969db20169776708e832c1d0fad44878285927d67ee3df6f2cfc2e94c93182c`; checked `2026-11-06T13:36:31Z`, 14 candidates; hashes/artifacts/tests unchanged (71 passed); axb0306 MNQ ends 2026-04-15.
- 2026-11-06T13:35Z: ledger `research_state/free_data_monitor_2026-11-06T1335Z.json` SHA-256 `46edb12d21994bd542031a957ddb346230e8306ce5b8aba1be8616abf8edb079`; checked `2026-11-06T13:35:34Z`, 14 candidates; hashes/artifacts/tests unchanged (71 passed); axb0306 MNQ ends 2026-04-15.
- 2026-11-06T12:48Z/12:41Z/12:34Z/12:33Z and earlier 2026-11-06 sessions: equivalent re-verifications with ledgers in `research_state/`; axb0306 ends 2026-04-15.

- Session verification (2026-11-06T11:51Z, repo clean before edits): `git status --short` **clean** before edits (exit 0). All 6 tracked SHA-256 hashes **MATCH** (full): `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`; `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`; `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`; `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`; `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`. 24 `artifacts/*.json`, 0 parse errors. `python3 -m pytest -q` **71 passed, 0 failed** (exit 0, 0.88s). No code/strategy/data/raw/artifact changes.
- Free-data monitoring (2026-11-06T11:51Z, `scripts/free_data_monitor.py`): ledger `research_state/free_data_monitor_2026-11-06T1151Z.json` (checked_at_utc `2026-11-06T11:51:35.460776+00:00`, file SHA-256 `04d097ca79953f3ba06f2e89f8149f87bccb103ec62b4cce0a518e4ca416c4de`, 14 candidates, JSON valid). `axb0306/cme-futures-ohlc` verdict **free**; latest MNQ 1min/15min coverage observed ends **2026-04-15** (no extension observed). **No genuinely free MNQ 1min/15min full-history source beyond 2026-04-15** found. No data purchased; no credentials requested/stored; no access controls bypassed.
- Baselines unchanged (verified artifacts): axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0). No code/strategy/parameter/data/raw/artifact changes.

- 2026-11-06T12:34Z: ledger `research_state/free_data_monitor_2026-11-06T1234Z.json` SHA-256 `a8ac0732e55b6728a5bae4a0a0d8f2663c13c85be3f0c8d16cc7bd95f6db21ae`; checked `2026-11-06T12:34:32Z`, 14 candidates; hashes/artifacts/tests unchanged (71 passed); axb0306 ends 2026-04-15.

- 2026-11-06T12:33Z: ledger `research_state/free_data_monitor_2026-11-06T1233Z.json` SHA-256 `e7aadff289f8a7bdf213f94e024725b64ce08be42bafb741d4cb7c4bc0a3a20e`; checked `2026-11-06T12:33:43Z`, 14 candidates; hashes/artifacts/tests unchanged (71 passed); axb0306 ends 2026-04-15.
- 2026-11-06T11:46Z: ledger `research_state/free_data_monitor_2026-11-06T114618Z.json` SHA-256 `1a780dd8fbfcba899669b972b663a05433f9bf51a17f14e0f189855586352660`; hashes/artifacts/tests unchanged; axb0306 ends 2026-04-15.
- 2026-11-06T11:44Z: ledger `research_state/free_data_monitor_2026-11-06T114400Z.json` SHA-256 `10bee75ec11280f20eea563c871b18b2d6f974d317b5464765e12149fd3b97a5`; unchanged.
- 2026-11-06T11:41Z: ledger `research_state/free_data_monitor_2026-11-06T114115Z.json` SHA-256 `c7929992196304d0d653000728a463aa02956add6ac2b951245a67fc49eb9152`; independent sweep reconfirmed no free 1m/15m full-history extension.
- Earlier 2026-11-06 maintenance sessions (11:38Z/11:32Z/10:45Z, etc.) recorded equivalent re-verifications with ledgers in `research_state/`.

## Mission
Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Blockers / durable constraints
- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through **2026-04-15** (re-verified 2026-11-06T13:36Z).
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.

## Next agent (immediate)
Repeat the same bounded maintenance loop (re-verify state, run `scripts/free_data_monitor.py`, record evidence, no tuning). Latest completed: **2026-11-06T13:44Z** (ledger `research_state/free_data_monitor_2026-11-06T1344Z.json`, file SHA-256 `ff3b46a58fbeab78792e4ba0f6ea163698ef3c790c3e72e34f7d7a75d60e7c81`, checked `2026-11-06T13:40:14Z`, 14 candidates; axb0306 MNQ 1min/15min ends 2026-04-15).

1. Re-verify repo state: `git status --short` (clean before edits), all 6 tracked SHA-256 hashes against values in `HANDOFF.md`, confirm `ls artifacts/*.json | wc -l` (24, 0 parse errors), `python3 -m pytest -q` (**71 passed, 0 failed**; install missing deps if needed). Record any drift with concrete evidence.
2. Bounded free-data monitoring for a genuinely free MNQ 1min/15min full-history source extending beyond **2026-04-15** (`axb0306/cme-futures-ohlc` latest). **Record provenance + SHA-256 before use.** Do not purchase data or bypass access controls/terms. Run `python3 scripts/free_data_monitor.py > research_state/free_data_monitor_<UTCstamp>.json` each session.
3. No experiments/tuning without explicit approval and a separately named, versioned experiment with an explicit diff from frozen `STRATEGY_RULES.txt` v1.0.
4. Update `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with concrete evidence if anything changes. Commit durably.

## Next concrete work (if a genuinely free MNQ 1min/15min source with longer history is found)
Re-baseline run with the frozen preset and an updated walk-forward/OOS split — **not** parameter tuning. Recompute metrics independently from the trade ledger and store configs/hashes/ledger/summary/validation artifacts. Record provenance + SHA-256 before use.

## Hard boundaries (AGENTS.md)
- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
