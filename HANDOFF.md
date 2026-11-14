# NQ ORB — Durable handoff

- **HEAD**: `b89aaed` (`chore(kilo): checkpoint agent session`; checkpoint-only since substantive research commit `5fab764`, 2026-10-31; `a9fc8e9..b89aaed` touches only `HANDOFF.md` + `INITIAL_TASK_FOR_NEXT_AGENT.md`). Working tree clean at session start and end.
- **Timestamp (UTC)**: 2026-11-14T05:33Z (session P).

## TERMINAL STATE — READ FIRST

**The research task is COMPLETE and terminal. No remaining research work exists.** The frozen MNQ 15-min ORB baseline (`STRATEGY_RULES.txt` v1.0, SHA-256 `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`) is final and negative-net on every free dataset available. The free-source search is exhausted: `data/FEASIBILITY_REPORT.md` documents ~30 sweeps through 2026-11-03; every candidate MNQ 1-min/15-min source is paid, key-gated, daily-only, or NQ rather than MNQ.

**Session P (2026-11-14T05:33Z, this session):** completed the prior agent task — read `HANDOFF.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `PROMPT.md`, `STRATEGY_RULES.txt`, `AGENTS.md`; confirmed terminal state read-only (strategy hash re-checked = `6d3258c3…8ad2b1`; all canonical artifacts present; newest monitor artifact `free_data_monitor_202611080209Z.json` dated 2026-11-08, i.e. stalled). Updated `HANDOFF.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` for the next agent. No tests re-run, no hashes re-computed beyond the strategy file, no monitor poll, no strategy/config/raw-data/artifact changes, no automation edits, no commit (handoff edits left uncommitted; controller owns commits). Terminal conclusion unchanged: stop.

**Correct next action is NOT another re-verification.** Do not re-run tests/hashes/monitor checks, do not add checkpoint commits, do not edit `.github/workflows/main.yml`, controller, or automation policy (requires explicit user authorization per `AGENTS.md`; none given). Report terminal state and stop. Legitimate forward paths require an explicit user decision: (a) stop/reduce maintenance automation, (b) run a separately-versioned experiment (e.g. far-side-of-range stop variant, `STRATEGY_RULES.txt` §2.1, as `experiment_farside_stop_v1`), or (c) accept baseline as final.

## Evidence re-verified (from frozen artifacts)

- `STRATEGY_RULES.txt` SHA-256 = `6d3258c3…8ad2b1` (matches).
- axb0306 (`artifacts/metrics_axb0306_full.json`): 60 trades, 42W/18L (70%), 33 long / 27 short, gross -$7,662, **net -$31,637.98**, costs $23,975.98, PF 0.4917, max DD $37,491.80, expectancy -0.0431R.
- Kaggle proxy (`artifacts/metrics_kaggle.json`, 688 trades, 2022-11-16..2025-11-12): 446W/242L (64.8%), 359 long / 329 short, gross -$140,899, **net -$626,525.96**, costs $485,626.96, PF 0.2271, max DD $626,994.56, expectancy -0.0684R, Sharpe -1.68 / Sortino -1.04 (daily), worst day -$4,789.80 (2023-05-12), exposure 8.07%, 2.99 years.
- Chronological splits (train/val/test): -$448,765.02 / -$66,243.22 / -$111,517.72 — all negative net.
- Walk-forward (`artifacts/walk_forward.json`, 8 windows, 150-trade test, step 50): test PF 0.128–0.447, test net -$70,637.24..-$178,375.24 — negative in every window.
- Cost sensitivity: all 12 combos negative (-$487,098.57..-$808,255.35); signal-close sensitivity all negative.
- Driver: costs ($2.87/side + 1-tick adverse slippage) dominate; the 0.4R target needs >71.43% pre-cost win rate; observed rates are below that.
- axb0306 train-split small-sample positive net is noise, not an edge.

## Test/manifest status

- Tests last run: **75 passed in 0.56s** (2026-11-14T02:43Z, venv `/home/runner/work/_temp/orbvenv`). Not re-run this session. CI (`.github/workflows/main.yml:61-62`) only runs the 4 controller/automation test files, not the ORB logic tests (`tests/orb/`).
- Manifest last verified: 20/20 matched (2026-11-13T16:50:32Z). Not re-hashed this session.

## Maintenance-loop observation (corrected)

- `.github/workflows/main.yml:11` still has `cron: "*/5 * * * *"`, and history is checkpoint-only commits through 2026-11-14.
- `research_state/` contains 483 entries (480 `free_data_monitor_*` artifacts, incl. 9 `.err`), but the **newest monitor artifact is `free_data_monitor_202611080209Z.json` (2026-11-08T02:09Z); there are zero monitor artifacts dated after 2026-11-08.** Treat the automation as stalled / not producing new monitor evidence, not as actively accumulating.
- Stopping or changing that automation requires **explicit user authorization** per `AGENTS.md`. None has been given. Do not touch it unilaterally.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with an explicit diff from baseline.
- Do not repeat maintenance re-verification. Report terminal state instead.
- Keep this handoff compact; consolidate rather than append.

(End of file)