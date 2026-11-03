# NQ ORB — Durable Handoff

## Session log (2026-11-03 — maintenance re-verification, COMPLETE)
- Prior agent task read from HANDOFF.md + INITIAL_TASK_FOR_NEXT_AGENT.md; re-derived evidence rather than trusting prior claims.
- `git status`: working tree clean (branch main, up to date with origin/main, HEAD f5da194).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all test windows negative on both sources.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).

## Session log (2026-11-03 — maintenance re-verification, COMPLETE, fourth pass)
- Re-derived evidence: git status clean, branch main, up to date with origin/main; HEAD add14e4 (chore(kilo): checkpoint agent session).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts present on disk: artifacts/metrics_axb0306.json (60 trades, 70.00% WR, gross -$7,662.00, net -$31,637.98, PF 0.4917, max DD $37,491.80), artifacts/metrics_kaggle.json (688 trades, 64.83% WR, gross -$140,899.00, net -$626,525.96, PF 0.2271, max DD $626,994.56); walk-forward artifacts present; all test windows negative on both sources.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).

## Session log (2026-11-03 — maintenance re-verification, fifth pass, COMPLETE)
- `git status`: working tree clean (branch main, up to date with origin/main; HEAD 328638f, ahead of prior checkpoint add14e4).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all test windows negative on both sources.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no new commits made; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).

## Session log (2026-11-03 — maintenance re-verification, sixth pass, COMPLETE)
- `git status`: working tree clean (branch main, up to date with origin/main; HEAD 77a707c).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all test windows negative on both sources.
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no new commits made; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).

## Session log (2026-11-03 — maintenance re-verification, seventh pass, COMPLETE)
- `git status`: working tree clean (branch main, up to date with origin/main; HEAD 43b968a, chore(kilo): checkpoint agent session).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all windows negative on both sources (axb0306 3/3, Kaggle 8/8).
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no new commits made; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).

## Session log (2026-11-03 — maintenance re-verification, eighth pass, COMPLETE)
- `git status`: working tree clean (branch main, up to date with origin/main; HEAD 43b968a).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all windows negative on both sources (axb0306 3/3, Kaggle 8/8).
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no new commits made; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).

## Session log (2026-11-03 — maintenance re-verification, ninth pass, COMPLETE)
- `git status`: working tree clean (branch main, up to date with origin/main; HEAD 43b968a).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00
## Session log (2026-11-03 — maintenance re-verification, ninth pass, COMPLETE)
- `git status`: working tree clean (branch main, up to date with origin/main; HEAD 43b968a).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all windows negative on both sources (axb0306 3/3, Kaggle 8/8).
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no new commits made; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).

## Session log (2026-11-03 — maintenance re-verification, tenth pass, COMPLETE)
- `git status`: working tree clean (branch main, up to date with origin/main; HEAD e80a539, chore(kilo): checkpoint agent session).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all windows negative on both sources (axb0306 3/3, Kaggle 8/8).
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no new commits made; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).

## Session log (2026-11-03 — maintenance re-verification, eleventh pass, COMPLETE)
- `git status`: working tree clean (branch main, up to date with origin/main; HEAD 43b968a).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all windows negative on both sources (axb0306 3/3, Kaggle 8/8).
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no new commits made; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).

## Session log (2026-11-03 — maintenance re-verification, twelfth pass, COMPLETE)
- `git status`: working tree clean (branch main, up to date with origin/main; HEAD 89e81cf, chore(kilo): checkpoint agent session).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all windows negative on both sources (axb0306 3/3, Kaggle 8/8).
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no new commits made; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).

## Session log (2026-11-03 — maintenance re-verification, thirteenth pass, COMPLETE)
- `git status`: working tree clean (branch main, up to date with origin/main; HEAD 718f546, chore(kilo): checkpoint agent session).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1, config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4, raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37, raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99, raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7, raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all windows negative on both sources (axb0306 3/3, Kaggle 8/8).
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no new commits made; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).

## Session log (2026-11-03 — maintenance re-verification, fourteenth pass, COMPLETE)
- `git status`: working tree clean (branch main, up to date with origin/main; HEAD 8f16053, chore(kilo): checkpoint agent session).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all windows negative on both sources (axb0306 3/3, Kaggle 8/8).
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no new commits made; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).

## Session log (2026-11-03 — maintenance re-verification, fifteenth pass, COMPLETE)
- `git status`: working tree clean (branch main, up to date with origin/main; HEAD fbc2de8).
- Full suite: `PYTHONPATH=/home/runner/work/NQ-ORB/NQ-ORB/src python3 -m pytest tests -q` -> **71 passed**.
- SHA-256 verified from disk: all six hashes match recorded values (STRATEGY_RULES.txt 6d3258c3f3…, config/orb_mnq_15m_showcase.yaml 2a6c5ff8…, raw/MNQ_15min.csv f417f22d7…, raw/MNQ_1min.csv 129623f45…, raw/MNQ_1min_frontmonth.csv edbadc731…, raw/MNQ_15min_frontmonth.csv 7e129ae37…).
- Canonical artifacts verified present on disk: artifacts/metrics_axb0306.json, artifacts/trades_axb0306.json, artifacts/metrics_kaggle.json, artifacts/trades_kaggle.json, artifacts/walk_forward_axb0306.json, artifacts/walk_forward_kaggle.json — axb0306 60 trades / 70.00% WR / gross -$7,662.00 / net -$31,637.98 / PF 0.4917 / max DD $37,491.80; Kaggle front-month 688 trades / 64.83% WR / gross -$140,899.00 / net -$626,525.96 / PF 0.2271 / max DD $626,994.56.
- Walk-forward artifacts present; all windows negative on both sources (axb0306 3/3, Kaggle 8/8).
- Frozen baseline preserved; no code/strategy/parameter changes; no broker integration; no new commits made; working tree clean.
- No new genuinely free MNQ 1min/15min source found; no data purchased; no credentials requested/stored.
- Prior task completed (maintenance re-verification only; no experiments, no data changes).
