# NQ ORB — Durable handoff

- **HEAD**: `07a4ca3` (= origin/main, clean `main...origin/main`; working tree clean at session start). No research/data/config/artifact files changed by this session. The `*/5 * * * *` loop is still active and stopping it requires explicit user authorization.
- **Timestamp (UTC)**: 2026-11-13T11:56:23Z
- **Last sanity check (UTC)**: 2026-11-13T11:56:23Z (this session) — terminal-state confirmation only, no maintenance re-verification. Verified clean branch/tree (`07a4ca3` == origin/main), `STRATEGY_RULES.txt` SHA `6d3258c3…` unchanged, and baseline metrics re-read from canonical artifacts (axb0306 net -$31,637.98 PF 0.4917; Kaggle net -$626,525.96 PF 0.2271). Full suite/manifest not re-run per terminal-state directive (last full: **75 passed in 0.91s** at 2026-11-13T11:53:44Z; manifest 20/20 matched at 2026-11-13T11:01:40Z). No frozen/research/data/artifact files touched; durable handoff files refreshed only; **no commit added**.

## TERMINAL STATE — READ FIRST

**The research task is COMPLETE. The frozen baseline is final and negative-net.** There is no remaining research work that can be done on the current free-data ceiling (see `data/FEASIBILITY_REPORT.md` — the free-source search has been exhaustively re-run dozens of times across 2026-10-31..2026-11-03 with no new source; every candidate is paid, key-gated, daily-only, or NQ big-contract, not MNQ).

**This repository is in a degenerate maintenance loop and it must be broken.** Evidence:
- The `.github/workflows/main.yml` runs on `cron: "*/5 * * * *"` and spawns a sequential Kilo session each activation.
- Each Kilo session performs an identical "maintenance re-verification" (tests + hash manifest + monitor check) and the workflow commits a `chore(kilo): checkpoint agent session` checkpoint.
- Since 2026-11-01 there have been **0 real research commits** (last substantive research commits: `5fab764` and `ce861a2`, both 2026-10-31). As of 2026-11-13T11:52:58Z there are **2,498 commits since 2026-11-01**, of which **2,207** are `chore(kilo): checkpoint agent session`; all remaining non-checkpoint commits are handoff re-verification, diagnostics-capture, or free-data-monitor bookkeeping — none add research evidence.
- The `HANDOFF.md` session log and commit history are bloating with near-identical entries that add no information. This handoff was consolidated (2026-11-13T09:44:56Z) to remove that bloat while preserving all substantive facts.

**Correct next action is NOT another re-verification.** The research is done and verified. Re-running the maintenance check in perpetuity consumes the workflow budget and produces no evidence. The proper way to stop the loop is to change the automation (`main.yml` schedule or a terminal no-op state), which **requires explicit user authorization** per `AGENTS.md` ("Do not edit `.github/workflows/main.yml` … unless the user explicitly authorizes that exact change"). No such authorization has been given. Until it is, this file records the terminal state so the next agent does not repeat the loop.

## Research status (frozen)

- **Strategy**: `STRATEGY_RULES.txt` v1.0 (MNQ 15-min ORB showcase, 09:30–09:45 ET OR, first-breakout-only, RVOL>=1.0 + ATR% 0.10–0.60%, 0.4×ATR stop, 0.4R target, $3000 risk, 15:00 ET cutoff, 15:55 ET flatten, 1 trade/day, 126 lines). No parameter changes.
- **Data**: axb0306 MNQ (2026-01-20..2026-04-15, 60 complete days; raw `MNQ_{15min,1min}.csv`) and kaggle front-month proxy (2022-11-16..2025-11-12, 688 days; raw `MNQ_{15min,1min}_frontmonth.csv`). 1-min audits: `research_state/1m_audit_{axb0306,kaggle}.json`. Free-data search exhausted (`data/FEASIBILITY_REPORT.md`); 06:00Z monitor stopped.
- **Results (negative net, evidence not edge)** — re-verified against `artifacts/metrics_*.json` this session:
  - axb0306 (`artifacts/metrics_axb0306_full.json`): 60 trades, 42W/18L (70% win), gross -$7,662, **net -$31,637.98**, costs $23,975.98, PF 0.4917, max DD $37,491.80, long 33 / short 27.
  - Kaggle (`artifacts/metrics_kaggle.json`): 688 trades, 446W/242L (64.8% win), gross -$140,899, **net -$626,525.96**, costs $485,626.96, PF 0.2271, max DD $626,994.56, long 359 / short 329.
  - Chronological train/val/test and date-based walk-forward splits are all negative net (see artifacts). Do not present as profitable.
  - Driver: costs (commissions + fees $2.87/side, 1-tick adverse slippage) dominate; the 0.4R target needs >71.43% pre-cost win rate and observed rates are below that. Cost sensitivity (slip ×0.5–2.0, cost ×0.8–1.2) stays negative across the board.

## SHA-256 manifest (20 key files, recomputed and verified 2026-11-13T09:44:56Z — 20/20 match)

| File | SHA-256 |
|---|---|
| STRATEGY_RULES.txt | 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1 |
| config/orb_mnq_15m_showcase.yaml | 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4 |
| config/orb_mnq_1m_wf_v1.yaml | ad745900a1b9adf2ef65a591eb24aa435670ac797525077d58775e53618f845b |
| data/FEASIBILITY_REPORT.md | a0a0f88eaeb0b63882d00557d6b740bb732a41b30e56ab4c5f45ce73e79bab1b |
| raw/MNQ_15min.csv | f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37 |
| raw/MNQ_15min_frontmonth.csv | 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4 |
| raw/MNQ_1min.csv | 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99 |
| raw/MNQ_1min_frontmonth.csv | edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7 |
| research_state/1m_audit_axb0306.json | 3aac07d224662c7ef514cc0e7df4a1236bcb5be312b5dc88f70a74533cb8a706 |
| research_state/1m_audit_kaggle.json | 277346323e2375485abd053d3587736778eaaae64e0b12494ae71eeb588f6041 |
| research_state/free_data_monitor_20261108T060017Z.json | 3f90bc19548bb0d3e574644dc86e7e42fd75361f63dc22ca51bec1cc977c776f |
| artifacts/README.md | 90792fb6b81103641187aad1e00dd8828446c6c62a1d192d2204f913e619552f |
| artifacts/metrics_axb0306_full.json | dddaefa2aaa23df2f34b10d5dee0220a08d6cfe6e86f9e39a19e6f912ee22f8f |
| artifacts/metrics_kaggle.json | a6ae100685ea30aa2392122fdf9830ccbaad5d25a22039db7e7521a0b12c1af1 |
| artifacts/trades_axb0306_full.json | 43672bbfe6e1198e24f412cc5c0c3bd1a7287253af493390ea1977fb12d7f115 |
| artifacts/trades_kaggle.json | 7251e4a93a298352dbd7b09b1505567a8a4d0fc8fb7dbc9a573bc110fb818aa5 |
| artifacts/walk_forward_axb0306.json | a91cf29d4dd64ff3e690bba742c3c8e0f17079f0658bd4622cae67d4a73fff79 |
| artifacts/walk_forward_kaggle.json | cf8419973d2dbbeaea6b855ea6f483a4b469e61874334fbf3dfdebb4c7cda1a7 |
| artifacts/walk_forward_date_60_20_20_axb0306.json | f05c44b0b129ef96118e2f57b3a4a41531292efd3976ac0394bb6b8b948a5546 |
| artifacts/walk_forward_date_60_20_20_kaggle.json | eac749dc112a31df57e366203efa378e0ba5528ac6c4ee878a22bf0557781355 |

**Manifest note:** `artifacts/metrics_axb0306_full.json` on-disk authoritative hash is `dddaefa2aaa23df2f34b10d5dee0220a08d6cfe6e86f9e39a19e6f912ee22f8f` (unchanged). Recomputed and verified 20/20 match 2026-11-13T11:01:40Z (unchanged since).

## Session log (consolidated — near-identical entries collapsed)

- **2026-11-13T11:56:23Z (this session)**: Terminal-state confirmation at HEAD `07a4ca3` (= origin/main, clean `main...origin/main`). Read prior durable handoff/task and completed it: research COMPLETE (terminal), frozen baseline final negative-net, free-data search exhausted. Per directive, did not re-run suite/manifest; verified clean state, `STRATEGY_RULES.txt` SHA `6d3258c3…` unchanged, and canonical metrics (axb0306 60 trades net -$31,637.98 PF 0.4917; Kaggle 688 trades net -$626,525.96 PF 0.2271). No frozen/research/data/artifact files touched. Durable handoff files refreshed only; **no commit added**. Loop/commit bloat persists; stopping `.github/workflows/main.yml` `*/5 * * * *` requires explicit user authorization.
- **2026-11-13T11:53:44Z (prior session)**: Terminal-state confirmation at HEAD `07a4ca3`. Verified clean state/hash/metrics; suite re-run once: **75 passed in 0.91s**. No commit added.
- **2026-11-13T11:51:20Z (prior session)**: Terminal-state confirmation at HEAD `2624bcd`; no re-run per directive. No commit added.
- **2026-11-13T11:49:31Z (prior session)**: Terminal-state confirmation at HEAD `dbca432` (= origin/main, clean `main...origin/main`, working tree clean at start and end). Read the prior durable handoff/task and completed it: confirmed the research task is COMPLETE (terminal state), the frozen baseline is final negative-net, and the free-data search is exhausted. Per the handoff's explicit "do not repeat maintenance re-verification" directive, the full suite/manifest were **not** re-run; verified instead clean branch/tree (`dbca432` == origin/main), `STRATEGY_RULES.txt` SHA `6d3258c3…` unchanged, and canonical metrics (axb0306 60 trades net -$31,637.98 PF 0.4917; Kaggle 688 trades net -$626,525.96 PF 0.2271). A new checkpoint commit (`dbca432`) landed since the previous handoff write; the `*/5 * * * *` loop is still active and stopping it requires explicit user authorization — not attempted. No frozen/research/data/artifact files touched. **No commit added.**
- **2026-11-13T11:01:40Z (prior session)**: Terminal-state confirmation at HEAD `5024077` (= origin/main, clean `main...origin/main`, working tree clean at start and end). Prior task COMPLETE (terminal state). Full suite re-run once: **75 passed in 1.02s**; 20/20 manifest hashes matched; `STRATEGY_RULES.txt` SHA `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1` unchanged. Baseline re-confirmed from artifacts (axb0306 net -$31,637.98 PF 0.4917; Kaggle net -$626,525.96 PF 0.2271). Quantified commit bloat: 2,501 commits since 2026-11-01, 2,207 checkpoints, 0 research commits. No frozen/research/data/artifact files touched. **No commit added**. Durable handoff files refreshed in working tree only.
- **2026-11-13T10:48:44Z–10:59:11Z (consolidated prior sessions)**: Series of terminal-state one-time confirmations at advancing controller-checkpoint HEADs (through `e611840`); each confirmed clean tree/branch and unchanged strategy hash, no new evidence. Last full check before this session 2026-11-13T10:48:44Z (75 passed, 20/20). No commits by those sessions.
- **2026-11-13T04:37Z–09:43Z (consolidated prior sessions, ~60+ near-identical)**: Long series of terminal-state one-time confirmations at advancing controller-checkpoint HEADs (through `9c0a984`). Each confirmed clean state and unchanged strategy SHA; most re-ran suite once (**75 passed**, 0.55–0.98s) and 20/20 manifest; some relied on last recorded check. No new evidence, no commits. Consolidated to reduce handoff bloat.
- **2026-11-13T01:04:05Z**: Maintenance re-verification at HEAD `6c08091`: 75 passed, 20/20 manifest matched. Diagnosed degenerate maintenance loop (0 real research commits since 2026-11-01; thousands of checkpoint commits; workflow `*/5 * * * *`). Recorded terminal state.
- **2026-11-01 (multiple sessions)**: Independent re-verification runs; baselines re-run byte-identical (axb0306 net -$31,637.98 PF 0.492; Kaggle net -$626,525.96 PF 0.227); independent signal-funnel cross-check matched engine (688 trades); full suite 66 passed; free-data sweep found no new source.
- **Earlier sessions (2026-11-08..2026-11-12)**: ~900+ handoff-only checkpoint commits with identical passing re-verification results; no research value. See TERMINAL STATE and `data/FEASIBILITY_REPORT.md`.

## Test status

- Last full sanity check **75 passed in 0.91s** (`/tmp/kilo-verify-venv/bin/python -m pytest tests/ -q`; 2026-11-13T11:53:44Z). Manifest 20/20 matched at 2026-11-13T11:01:40Z. This session (2026-11-13T11:56:23Z) did not re-run suite/manifest per terminal-state directive; verified clean state, strategy SHA, and baseline metrics only. No commit; HEAD `07a4ca3` == origin/main.

## Standing constraints

- Historical research/simulation only. No broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, configs, raw data, or canonical artifacts. Any strategy change must be a separately named, versioned experiment with explicit diff from baseline.
- **Do not repeat the maintenance re-verification loop.** The research is complete and the baseline is final (negative net). Re-running tests/hashes/monitor checks every few minutes adds no evidence and bloats the repo. If asked to "continue", report the terminal state instead of re-verifying.
- Stopping the automation (`.github/workflows/main.yml` `*/5 * * * *` schedule, or adding a terminal no-op) requires explicit user authorization per `AGENTS.md`. Do not change it without that authorization.
