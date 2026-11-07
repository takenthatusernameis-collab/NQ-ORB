# Handoff

## Current session verification (2026-11-07T00:51:31Z, this session)

- `git status --short` at start: clean (no tracked/untracked changes) — no code/strategy/data/raw/artifact changes.
- All 6 tracked SHA-256 hashes **MATCH**:
  - `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`
  - `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`
- `python3 scripts/free_data_monitor.py` executed → `research_state/free_data_monitor_20261107T005131Z.json` (file SHA-256 `edc441c25a54ac5a350070f43ba59b6bfe1ff8dd3c60d576aef441bb314d5fec`, `checked_at_utc` `2026-11-07T00:51:31.974005+00:00`, **14 candidates**, JSON valid).
- axb0306/cme-futures-ohlc: verdict `free`; latest commit `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z`; MNQ 1min/15min coverage ends **2026-04-15**, **no extension observed** (re-verified).
- No code/strategy/data/raw/artifact changes this session.

## Current durable state (as of 2026-11-07T00:51:31Z)

- Baselines unchanged: axb0306 net **-$31637.98**, win **70%**, PF **0.4917**; Kaggle net **-$626525.96**, win **64.8%**, PF **0.2271**. Prior verified walk-forward: axb0306 3 windows all negative net P&L; Kaggle 8 windows all negative net P&L. Frozen baseline preserved (`STRATEGY_RULES.txt` v1.0).

## Next agent (immediate)

Repeat the bounded maintenance loop (re-verify state, run `scripts/free_data_monitor.py`, record evidence, no tuning). Latest completed: **2026-11-07T00:51:31Z** (ledger `research_state/free_data_monitor_20261107T005131Z.json`, SHA-256 `edc441c25a54ac5a350070f43ba59b6bfe1ff8dd3c60d576aef441bb314d5fec`, checked `2026-11-07T00:51:31.974005+00:00`, 14 candidates; axb0306 `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z`, free, MNQ 1min/15min ends 2026-04-15, no extension).

**Initial task message for next agent:** Read HANDOFF.md. Run `git status --short` (expect only untracked `research_state/free_data_monitor_*.json` ledgers, or clean). Verify all 6 tracked SHA-256 hashes match (STRATEGY_RULES.txt `6d3258c3...`; `config/orb_mnq_15m_showcase.yaml` `2a6c5ff8...`; `raw/MNQ_15min.csv` `f417f22d...`; `raw/MNQ_1min.csv` `129623f4...`; `raw/MNQ_1min_frontmonth.csv` `edbadc73...`; `raw/MNQ_15min_frontmonth.csv` `7e129ae3...`). Run `python3 scripts/free_data_monitor.py`; save output to a new timestamped ledger in `research_state/`; record file SHA-256, checked_at_utc, candidate count, axb0306 latest commit/date; confirm no extension beyond 2026-04-15. Do not tune parameters, change strategy logic, or touch raw data/artifacts. Update HANDOFF.md with the new session verification and write the next agent's initial task message.

## Prior maintenance verifications (evidence preserved)

- 2026-11-07T00:51:31Z: ledger `research_state/free_data_monitor_20261107T005131Z.json` SHA-256 `edc441c25a54ac5a350070f43ba59b6bfe1ff8dd3c60d576aef441bb314d5fec` (checked `2026-11-07T00:51:31.974005+00:00`), 14 candidates, `git status` clean at start, all 6 hashes match, axb0306 `60abd3fb6369c6ce0b6a4a65b0f2562fc96b1264` dated `2026-04-15T23:34:55Z`, MNQ 1min/15min ends 2026-04-15 (no extension). No code/strategy/data/raw/artifact changes.
- 2026-11-07T00:49:52Z: ledger `research_state/free_data_monitor_20261107T004952Z.json` SHA-256 `e3a825eb10b32216fd171ca0357e62333e8d79e794bb9e3df18e3daad8a71fcc` (checked `2026-11-07T00:49:52.697886+00:00`), 14 candidates, `git status` showed only this session's untracked ledger at start, all 6 hashes match, axb0306 free, MNQ 1min/15min ends 2026-04-15 (no extension). No code/strategy/data/raw/artifact changes.
- 2026-11-07T00:49Z: ledger `research_state/free_data_monitor_20261107T004906Z.json` SHA-256 `689d20de4fbf0198125a45032c41b75bc80df8349311e9d9189538ab932a7937` (checked `2026-11-07T00:49:06.321793+00:00`), 14 candidates, git clean at start, all 6 hashes match, axb0306 `60abd3fb...` dated `2026-04-15T23:34:55Z`, MNQ 1min/15min ends 2026-04-15 (no extension). No code/strategy/data/raw/artifact changes.
- 2026-11-07T00:47Z: ledger `research_state/free_data_monitor_20261107T004700Z.json` SHA-256 `e2464fdc2506414efb6a09bca02872d952e2932e3940469bd39dfcedfe8fcd15` (checked `2026-11-07T00:47:00.739871+00:00`), 14 candidates, `git status` showed only prior untracked ledger at start, all 6 hashes match, axb0306 `60abd3fb...` dated `2026-04-15T23:34:55Z`, MNQ 1min/15min ends 2026-04-15 (no extension). `pytest` unavailable (prior verified 71 passed). No code/strategy/data/raw/artifact changes.
- 2026-11-07T00:45Z: ledger `research_state/free_data_monitor_20261107T004504Z.json` SHA-256 `aaaa2c8f86c240ce5f924ccc0291221510c73329abf6a370c0d923c977a4dd0b` (checked `2026-11-07T00:45:04.885336+00:00`), 14 candidates, git clean at start, all 6 hashes match, axb0306 ends 2026-04-15 (no extension). No code/strategy/data/raw/artifact changes.
- 2026-11-07T00:41Z: ledger `research_state/free_data_monitor_20261107T004137Z.json` SHA-256 `be233ad84a05a49f9295422fdfc8a915fd719305a9b20afd6102398921f493dc` (checked `2026-11-07T00:41:37.079300+00:00`), 14 candidates, git clean at start, all 6 hashes match, axb0306 ends 2026-04-15 (no extension). No code/strategy/data/raw/artifact changes.
- 2026-11-07T00:39Z: ledger `research_state/free_data_monitor_20261107T003951Z.json` SHA-256 `82be271dc5eb3ac03a37531fd92798adfaf67c2635ed529e901dc4a8090027c5` (checked `2026-11-07T00:39:51.360833+00:00`), 14 candidates, git clean, all 6 hashes match, axb0306 ends 2026-04-15 (no extension). No code/strategy/data/raw/artifact changes.
- 2026-11-06T22:51Z: ledger `research_state/free_data_monitor_20261106T225117Z.json` SHA-256 `f05bf0e426b99ad3505d86f00335aa48974c2003a0d3b78392da03ade356913c` (checked `2026-11-06T22:51:24.973980+00:00`), pytest unavailable in env (prior verified 71 passed), axb0306 ends 2026-04-15.
- 2026-11-06T22:49Z: ledger `research_state/free_data_monitor_20261106T224959Z.json` SHA-256 `391f8509b43e738b5bfb88405a515151e93c1e8269ecd48c849913e72257af47` (checked `2026-11-06T22:49:59+00:00`), pytest unavailable in env (prior verified 71 passed), axb0306 ends 2026-04-15.
- 2026-11-06T22:44Z: ledger `research_state/free_data_monitor_20261106T224426Z.json` SHA-256 `4a05fa9b2c2bd54e99a3ae966cdb7085a17016ef9773141881b7d103a9e47f3f` (checked `2026-11-06T22:44:26.715961+00:00`), pytest unavailable in env (prior verified 71 passed), axb0306 ends 2026-04-15.
- 2026-11-06T21:56Z: ledger `research_state/free_data_monitor_20261106T2156Z.json` SHA-256 `d3915e237cdfa2de1ea1a75010a7add7bbc9b761fb8bf1ba5cd6adfeb6f9df1b` (checked `2026-11-06T21:56:33.089756+00:00`), pytest unavailable in env (prior verified 71 passed), axb0306 ends 2026-04-15.
- 2026-11-06T21:42Z: ledger `research_state/free_data_monitor_20261106T2142Z.json` SHA-256 `5ba009d7327b4bb19e2822f9c55f52f0045b2dcfd83b9b58d233e055ae4ad217` (checked `2026-11-06T21:42:37.370344+00:00`), pytest unavailable in env (prior verified 71 passed), axb0306 ends 2026-04-15.
- 2026-11-06T21:41Z: ledger `research_state/free_data_monitor_20261106T2141Z.json` SHA-256 `6d16ead8bf44cd235768e4ae2bfcc3c33c3c697ba86631843e243b1aae5f535a` (checked `2026-11-06T21:41:31.147691+00:00`), pytest unavailable in env (prior verified 71 passed), axb0306 ends 2026-04-15.
- 2026-11-06T21:11Z: ledger `research_state/free_data_monitor_20261106T211152Z.json` SHA-256 `5cee0bc1f5911b64ad47c66e68ecf8381e5f66f396dafe6e2b5f17def436ab35` (checked `2026-11-06T21:11:52.013146+00:00`), 71 passed, axb0306 ends 2026-04-15.
- 2026-11-06T20:57Z: ledger `research_state/free_data_monitor_20261106T2031Z.json` SHA-256 `771a9137a9e14c09c2f8e49cc2c0c124a212e42efad587efea7f9c21726f14a6` (checked `2026-11-06T20:31:28.534928+00:00`), 71 passed, axb0306 ends 2026-04-15.

## Blockers / durable constraints

- Research blocked on data depth; both frozen baselines negative under full costs; all verified walk-forward test windows negative. Highest-value action remains bounded free-data re-sweep, not parameter fitting.
- `axb0306` roll/adjustment: single-contract `MNQ.M26`, no roll inside sample (2026-01-20..2026-04-15). Latest free 1min/15min coverage observed remains through **2026-04-15**.
- Kaggle front-month ends 2025-11-12; final ~2.9 months preserved as untouched OOS. No free source extends this without purchase.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
