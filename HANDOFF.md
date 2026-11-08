## Durable state (authoritative snapshot)
- **Frozen baseline**: `STRATEGY_RULES.txt` v1.0 — SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`. No silent baseline changes.
- **Baseline results (unchanged)**: axb0306 net **-$31,637.98**, win 70%, PF 0.4917; Kaggle net **-$626,525.96**, win 64.8%, PF 0.2271. Walk-forward negative (axb0306 3 windows, Kaggle 8 windows).
- **Data coverage (axb0306/cme-futures-ohlc)**: single-contract `MNQ.M26`, no roll inside sample 2026-01-20..2026-04-15. Latest observed free 1min/15min coverage ends **2026-04-15** (no extension observed). 15-min bars alone are insufficient for exact 15:55 ET exit evidence.
- **Tracked hashes (re-verified 2026-11-08T18:37Z, all MATCH)**:
  - `STRATEGY_RULES.txt` `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`
  - `config/orb_mnq_15m_showcase.yaml` `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`
  - `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`
  - `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`
  - `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`
  - `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`
  - `research_state/free_data_monitor_20261108T060017Z.json` `3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f`
- **Environment**: `pytest` unavailable (`No module named pytest`, Python 3.12.3). Prior verified test baseline: 71 passed (2026-11-06T21:11Z).
- **Loop status**: free-data maintenance monitoring loop **stopped at 2026-11-08T06:00Z deadline**. **No further polling unless explicitly directed by user/controller.**

## Verification ledger
Full per-session history preserved in git (`git log -- HANDOFF.md`). Prior redundant verification-only checkpoint entries (2026-11-08 06:03Z–18:36Z) trimmed for readability; each confirmed clean tree at session HEAD, all 7 tracked SHA-256 MATCH, loop stopped, coverage ends 2026-04-15, baselines unchanged, `pytest` unavailable, no code/strategy/data/raw/artifact/workflow changes, no pending work.

- **2026-11-08T06:00Z (deadline)**: maintenance loop stopped. Final monitor ledger `research_state/free_data_monitor_20261108T060017Z.json` `3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f`; axb0306 MNQ 1min/15min coverage ends 2026-04-15, no extension observed.
- **2026-11-08T18:34Z (prior)**: re-verified at HEAD `337f4fd926bbdf74c20d14ea5fdff440f9751e8b`; all 7 tracked SHA-256 MATCH.
- **2026-11-08T18:36Z (prior)**: re-verified at HEAD `34b8b4a632bd7ae59ec9c58b121e6dc1ec0678c5`; all 7 tracked SHA-256 MATCH.
- **2026-11-08T18:37Z (prior)**: completed prior agent task from durable handoff — re-verified state. `git status --short` clean at HEAD `4f9333b291d065f6f94e01aca8893d822a297706`; all 7 tracked SHA-256 MATCH (re-verified via `sha256sum`). Loop remains stopped; latest free MNQ coverage ends 2026-04-15; baselines unchanged; `pytest` unavailable. No code/strategy/data/raw/artifact/workflow changes. No pending work.
- **2026-11-08T18:45Z (this session)**: completed prior agent task from durable handoff — re-verified state. `git status --short` clean at HEAD `824bdf332829e72ea825965ddd762e41fff3c4d4`; all 7 tracked SHA-256 MATCH (re-verified via `sha256sum`): STRATEGY_RULES `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`, showcase config `2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4`, `raw/MNQ_15min.csv` `f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37`, `raw/MNQ_1min.csv` `129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99`, `raw/MNQ_1min_frontmonth.csv` `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`, `raw/MNQ_15min_frontmonth.csv` `7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4`, monitor ledger `research_state/free_data_monitor_20261108T060017Z.json` `3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f`. Loop remains stopped (06:00Z deadline); latest free MNQ coverage ends 2026-04-15 (axb0306/cme-futures-ohlc, MNQ.M26); baselines unchanged (axb0306 net -$31,637.98, Kaggle net -$626,525.96, walk-forward negative); `pytest` unavailable (Python 3.12.3, `No module named pytest`). No code/strategy/data/raw/artifact/workflow changes. No pending work. `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` updated.
