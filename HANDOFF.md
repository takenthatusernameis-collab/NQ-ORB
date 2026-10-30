# NQ ORB — Durable Handoff

Date initialized: 2026-10-30
Repository: takenthatusernameis-collab/NQ-ORB
Status: bootstrap complete; strategy implementation and empirical validation have not yet been performed.

## Initial authoritative state

- `STRATEGY_RULES.txt` contains the user-specified NQ ORB rules and MNQ 15-minute showcase preset.
- `PROMPT.md` specifies the first Kilo research/engineering task.
- `AGENTS.md` defines research, auditability, and no-live-trading constraints.
- `.github/workflows/main.yml` is based on the latest established Kilo workflow version identified in the account's EMA hourly continuation repository on 2026-10-30.
- The workflow's generic controller progress helper and four targeted regression tests are included in this repository so the latest workflow's declared dependencies are present.
- There is no validated historical backtest, no performance result, and no live trading authorization.

## Next task — execute first

Complete the first objective in `PROMPT.md`: conduct a free-data feasibility audit for historical MNQ/NQ 15-minute OHLCV and 1-minute-or-better execution data. The key blocking requirement is an honest, verifiable 15:55 ET forced flatten. Do not claim an exact forced exit using 15-minute bars alone.

If a valid free dataset is found, document provenance and coverage, then implement the exact frozen showcase baseline and deterministic tests. If not, record the strongest verified free-data options and precisely what remains untestable. Do not buy data, request credentials, or weaken the rules.

## Mandatory handoff update

At the end of each substantive session, record:
- exact files changed and commit SHA;
- source/data provenance and coverage;
- commands executed and actual test results;
- backtest outputs only when reproducibly generated;
- unresolved blockers and uncertainty;
- the next bounded task.

Do not claim empirical validation from unit tests or synthetic fixtures. Do not change the frozen strategy, launch a nested Kilo workflow, or enable live trading.
