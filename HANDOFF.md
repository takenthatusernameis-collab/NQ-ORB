# Handoff

## Mission

Build and rigorously evaluate a reproducible NQ/MNQ opening-range-breakout research implementation. `STRATEGY_RULES.txt` is the authoritative, frozen strategy definition. Historical research and simulation only — no broker integration, no live/paper trading, no deployment. No secrets, no paid data, no bypassing access controls.

## Current durable state (maintenance re-verification pass — 35cb08b)

- Branch: main. Working tree clean (`git status --short` empty, no untracked files); HEAD at 35cb08b (chore(kilo): checkpoint agent session). origin/main == 35cb08b. Recent commits: 35cb08b, af3673b, 3aa9f09, 0450b8a, 06fc22e, f98b75c.
- SHA-256 re-verified from disk (2026-11-05): all 6 tracked file hashes match recorded values:
  - STRATEGY_RULES.txt 6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1 — MATCH
  - config/orb_mnq_15m_showcase.yaml 2a6c5ff82b810663f0bd20259b80397a220dc36b120ff823f9c63974148391e4 — MATCH
  - raw/MNQ_15min.csv f417f22d7c933920636b15ce1ac47a657149ecbe8c087300a029a0372fc4ce37 — MATCH
  - raw/MNQ_1min.csv 129623f45308a98a1a345473ac5fe4d03d5d53f7dd177a608d946eb3d3d6ea99 — MATCH
  - raw/MNQ_1min_frontmonth.csv edbadc731ed90c9e0425cf2f7d6c69e72c9f643c0b8c388dec009fb2e3e613e7 — MATCH
  - raw/MNQ_15min_frontmonth.csv 7e129ae37f1ae62bd8d8209b1e5ea90521ffbb847d58ff3a0a6f27afdd3a9ef4 — MATCH
- Canonical artifacts: 25 entries in artifacts/ (24 JSON files parse cleanly, 0 parse errors; README.md is included in directory listing).
- Determinism/walk-forward/baselines unchanged from prior verified artifacts (axb0306 3 windows all negative; Kaggle 8 windows all negative; axb0306 60 trades net -$31637.98; Kaggle 688 trades net -$626525.96).
- Raw date ranges unchanged (MNQ_15min.csv 5608 rows 2026-01-20T13:15 → 2026-04-15T23:15; MNQ_1min.csv 84077 rows 2026-01-20T13:27 → 2026-04-15T23:29; MNQ_1min_frontmonth.csv 1059204 rows → 2025-11-12T23:59; MNQ_15min_frontmonth.csv 70614 rows → 2025-11-12T23:45).
- Tests: pytest available; 71 passed/0 failed (session 2026-11-05 re-verification pass, 0.95s).
- Frozen baseline preserved; no code/strategy/parameter changes; no data purchased; no credentials requested or stored.
- Free-data monitoring (re-swept 2026-11-05): unchanged — no new genuinely free MNQ 1min/15min full-history source found. Candidates evaluated: FirstRate Data, Portara, Kibot, MarketParquet full archive = paid; Yahoo Finance (NQ=F/MNQ=F) = daily only + 1min limited to last 30d and 8 bars/request, unadjusted contract-switching; MarketParquet free = last ~365d daily + intraday sample pack only (Apr 6-10 2026); Databento = $125 credit expiring in 6mo, unadjusted continuous series, UTC timestamps; Kaggle uploads = unknown provenance/licence; getdata-finance GitHub = 1m sample only (2026-04-01 → 2026-09-02, E-mini NQ not MNQ), full archive behind getdata.finance. None meets the free + 1min/15min + full-history bar.

## Prior task (completed 2026-11-05, this session — maintenance re-verification — 35cb08b)

Maintenance re-verification completed: verified git state (working tree clean, 35cb08b == main == origin/main; only diff from af3673b is the two handoff files). Re-verified SHA-256 hashes from disk; all 6 tracked file hashes match recorded values. Confirmed artifacts parse cleanly (25 entries, 24 JSON files, 0 parse errors). Ran pytest (71 passed/0 failed). Walk-forward/baselines unchanged from artifacts. Raw date ranges re-checked by row count. Free-data re-sweep performed (8+ sources evaluated, none qualifies). No data purchased; no credentials requested/stored. Updated HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md.

## Next agent (immediate)

See INITIAL_TASK_FOR_NEXT_AGENT.md. Maintenance/re-verification only: verify repo state/hashes/artifacts/tests if available, monitor for genuinely free MNQ 1min/15min data (record provenance+SHA-256 before use), do not tune/change strategy without separately named versioned experiment with explicit diff from frozen STRATEGY_RULES.txt v1.0. Update HANDOFF.md and INITIAL_TASK_FOR_NEXT_AGENT.md with concrete evidence.

## Hard boundaries (AGENTS.md)

- Historical research/simulation only. No broker integration/order routing/live trading/paper trading/deployment.
- Never request/add/print/persist broker/API credentials.
- Do not purchase data or use paid/proprietary services; prefer freely accessible datasets; never bypass access controls/terms.
- Do not launch nested Kilo sessions/duplicate scheduled workflows/additional GitHub Actions activations.
- Do not edit `.github/workflows/main.yml`, controller helper code, permissions, or automation policy without explicit authorization.
- Do not delete research evidence, overwrite raw data, or reset/rewrite Git history to conceal failure.
