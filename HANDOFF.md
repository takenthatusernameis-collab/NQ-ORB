# Handoff

## Mission
Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (verified 2026-11-03 — maintenance re-verification, one-hundred-and-sixth pass, COMPLETE)
- Branch: main (up to date with origin/main). HEAD: 8b712e5 (chore(kilo): checkpoint agent session). Working tree clean. `git fetch origin` this pass: local HEAD 8b712e5 == origin/main 8b712e5, no upstream drift (previous HEAD dcc7cbb also present in log; remote is at 8b712e5).
- All tests: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed in 0.71s**.
- SHA-256 (recomputed from disk this pass, all six match recorded values): STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1; config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4; raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37; raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99; raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7; raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4.
- Canonical artifacts (present + parseable): artifacts/metrics_axb0306.json (60 trades, 70.00% WR, gross -$7,662.00, net -$31,637.98, PF 0.49167, max DD $37,491.80), artifacts/metrics_kaggle.json (688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.22709, max DD $626,994.56). artifacts/trades_axb0306.json (SHA-256 ce389da2488474a6d0d994cf99bb1e6509761d80f85986f1f8da3e1738b6a364), artifacts/trades_kaggle.json (SHA-256 7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5) also present.
- Walk-forward (axb0306, 3 windows): [20,40] test net -$10,053.14; [30,50] -$21,922.10; [40,60] -$23,058.98 — all negative. (Kaggle front-month, 8 windows): [150,300] -$178,375.24, [200,350] -$173,264.64, [250,400] -$168,315.48, [300,450] -$134,617.64, [350,500] -$122,071.62, [400,550] -$70,637.24, [450,600] -$104,755.42, [500,650] -$114,820.72 — all negative.
- Raw date ranges: axb0306 ends 2026-04-15 (1min last 2026-04-15T23:29, 15min last 2026-04-15T23:15); Kaggle front-month ends 2025-11-12 (1min 2025-11-12T23:59, 15min 2025-11-12T23:45). Final ~2.9 months of Kaggle (from 2025-08-29 onward, ~38 trades, net -$21,472.00) are the preserved untouched out-of-sample interval.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no data purchased; no credentials requested/stored. No new genuinely free MNQ 1min/15min source found this pass.

## Prior task
Maintenance re-verification (one-hundred-and-sixth pass): re-verified repo state vs remote (clean, up to date with origin/main at 8b712e5), recomputed all six file hashes (all match), confirmed canonical artifacts parseable with correct metrics and trade ledger SHA-256 identical, verified walk-forward artifacts present (all negative), re-ran full test suite (71 passed). Completed this pass.

## Next agent (immediate)
See INITIAL_TASK_FOR_NEXT_AGENT.md. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available, monitor for genuinely free MNQ 1min/15min data (record provenance+hash before use), do not tune/change strategy without separately named versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0. Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence.

(End of file)
