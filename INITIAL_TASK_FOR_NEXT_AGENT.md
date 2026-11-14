# Initial Task for Next Agent — NQ ORB

## Status: prior task COMPLETE — terminal state reported (2026-11-14T21:15Z); research terminal; default action is to do nothing

Durable handoff and this file refreshed 2026-11-14T21:15Z. Arrival drift anchor re-verified read-only: `git status --porcelain` clean; `sha256sum STRATEGY_RULES.txt` == `6d3258c3…8ad2b1`; `git log --oneline a797773..HEAD -- src/ config/ scripts/ tests/ raw/ data/ artifacts/` empty. Full test suite re-run this session: **75 passed in 0.63s** (`python -m pytest -q`). No code/data/config/artifact changes made.

## Your task (initial message)

Report terminal state and stop. There is no outstanding research work. Do not re-run tests/hashes/monitor checks, do not add handoff-only checkpoint cycles, and do not touch `.github/workflows/main.yml`, the controller, or automation policy without explicit user authorization.

Only act if the user explicitly directs one of:

1. **Stop/reduce maintenance automation** — edit `cron` in `.github/workflows/main.yml:11` (requires explicit authorization).
2. **Run a separately-versioned experiment** — e.g. far-side-of-range stop as `experiment_farside_stop_v1` with explicit diff from baseline, deterministic tests, chronological splits; update `HANDOFF.md`.
3. **Accept baseline as final** — archive the project.

## Constraints

- Historical research/simulation only; no broker/live/paper execution, no credentials, no paid/proprietary data.
- Do not modify `STRATEGY_RULES.txt`, frozen configs, raw data, or canonical artifacts. Any strategy change = separately named, versioned experiment with explicit diff from baseline.
- Do not edit `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization.
- Keep `HANDOFF.md` compact.

(End of file - total 29 lines)