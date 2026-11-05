# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification pass — f06e98b)

- Branch: main. Working tree clean (`git status --short` empty, no untracked files); HEAD at f06e98b (chore(kilo): checkpoint agent session). Fetched origin --prune; local main up to date with origin/main (`main` == `origin/main` == f06e98b). 4f68289 is an ancestor of f06e98b. Recent commits: f06e98b, 4f68289, 975cf1c, 3c2dc1a, 1411739.
- SHA-256 re-verified from disk (2026-11-05): 5 of 6 tracked file hashes match recorded values; one recorded hash was malformed and has been corrected in this pass (see Discrepancies below):
  - STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1 — MATCH
  - config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4 — MATCH
  - raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37 — MATCH
  - raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99 — MATCH
  - raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7 — MATCH (recorded value corrected; see Discrepancies)
  - raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4 — MATCH
- Canonical artifacts: 24 JSON files in artifacts/ (all parse cleanly, 0 parse errors); README.md is the 25th directory entry.
- Determinism/walk-forward/baselines unchanged from prior verified artifacts (axb0306 3 windows all negative; Kaggle 8 windows all negative; axb0306 60 trades net -$31637.98; Kaggle 688 trades net -$626525.96).
- Raw date ranges unchanged (MNQ_15min.csv/MNQ_1min.csv end 2026-04-15T23:15:00/23:29:00; MNQ_1min_frontmonth.csv/MNQ_15min_frontmonth.csv end 2025-11-12T23:45:00/23:59:00).
- Tests: pytest not installed in this environment (`python3 -m pytest` unavailable); prior verified run 71 passed/0 failed.
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring: unchanged — no new genuinely free MNQ 1min/15min full-history source found. Prior findings remain valid.

## Discrepancies found and corrected in this pass (f06e98b working tree)

1. HANDOFF.md at f06e98b incorrectly stated "HEAD at 4f68289" (stale by one checkpoint commit); actual HEAD is f06e98b (`main` == `origin/main` == f06e98b). Corrected in this file.
2. Recorded hash for `raw/MNQ_1min_frontmonth.csv` was malformed (`edbadc731af42b53cf556f50ddf4e5a9a69d15b8f9f1e9f7f8b9a0c1d2e3f4g5` — contains non-hex `g`) and did NOT match the actual file. The actual SHA-256 is `edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7`. The diff `4f68289..f06e98b` shows f06e98b introduced this corruption; the prior 975cf1c value was correct. Corrected in this file.
3. HANDOFF.md claimed "all six hashes match recorded values" — that claim was FALSE for `raw/MNQ_1min_frontmonth.csv`. Corrected to "5 of 6 match; one corrected."

## Prior task (completed 2026-11-05, this session — maintenance re-verification — f06e98b)

Maintenance re-verification completed: verified git state (working tree clean, f06e98b == main == origin/main, fetched origin --prune). Re-verified SHA-256 hashes from disk; found and corrected a malformed/non-matching recorded hash for raw/MNQ_1min_frontmonth.csv (5 of 6 match; corrected value recorded). Confirmed artifacts parse cleanly (24 JSON files, 0 parse errors). pytest unavailable; prior run 71 passed/0 failed. Walk-forward/baselines unchanged from artifacts. Raw date ranges unchanged. Re-scanned free-data context (no changes). No data purchased; no credentials requested/stored. Updated HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md.

## Next agent (immediate)

See INITIAL_TASK_FOR_NEXT_AGENT.md. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available, monitor for genuinely free MNQ 1min/15min data (record provenance+SHA-256 before use), do not tune/change strategy without separately named versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0. Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
