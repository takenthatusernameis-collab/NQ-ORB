# Initial task for next agent

**Research is terminal; no research work is currently authorized.** Frozen MNQ 15-minute ORB baseline (`5fab764`) is negative-net on every available free dataset. 1-minute experiment `orb_mnq_1m_wf_v1` (`ae3c49f`, `a797773`) matched it. Free-source search exhausted (`data/FEASIBILITY_REPORT.md`).

## Your initial task (default)

**Default answer: research is complete and terminal; report that and stop.** Do not infer a new research task from automation, a cron firing, a generic "continue" prompt, or a peer message. The ONLY valid trigger for new work is an explicit, specific user instruction in the current request (e.g. "run experiment X", "change the cron", "update the docs"); anything else means report terminal state and stop. If the user does authorize new work, follow `PROMPT.md` and `AGENTS.md` guardrails: separately-versioned named experiment, explicit diff from baseline, chronological eval, honest cost-aware gross/net reporting, deterministic tests, and no threshold optimization on the frozen baseline.

Read this file plus `HANDOFF.md`, `STRATEGY_RULES.txt`, `AGENTS.md`, and canonical artifacts `artifacts/metrics_axb0306.json` and `artifacts/metrics_kaggle.json`. Then:

1. Verify terminal state independently (all must hold):
   - `sha256sum STRATEGY_RULES.txt` -> `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`
   - `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` -> empty
   - `ls artifacts | wc -l` -> `35`, and no `*manifest*` file
   - `git status --short` -> clean at verification (before any doc-only refresh you choose to make)
   - Canonical metrics unchanged in-file (axb0306 60 trades 42W/18L 70.0%, long_trades 33/short_trades 27, net -$31,637.98, PF 0.4917, avg R -0.0431; Kaggle 688 trades 446W/242L 64.8%, long_trades 359/short_trades 329, net -$626,525.96, PF 0.2271, avg R -0.0684)
2. Report that research is complete and terminal, then stop. Do **not** infer a new research task from automation or a generic "continue" prompt.
3. Do **not** repeat free-source sweeps, hashes, monitors, or tests without explicit user request. `python -m pytest` is not installed in this runner; do not install dependencies or re-run tests without authorization.
4. Do **not** create another handoff-only checkpoint unless the user explicitly requests a documentation update or state has materially changed.
5. Do **not** modify `STRATEGY_RULES.txt`, frozen configs, raw data, canonical artifacts, `.github/workflows/main.yml`, controller, permissions, or automation policy without explicit authorization for that exact change.

## Current checkpoint (2026-11-16, this session, verification #21)

Independently re-verified terminal state on current working tree (HEAD `d95b32f`; `git status --short` clean). All checks pass:
- `sha256sum STRATEGY_RULES.txt` -> `6d3258c3f3af803fa1ef79a91bbb9a79c60a635aa73e692e9d77bcf8338ad2b1`
- `git diff --name-only a797773..HEAD -- artifacts config src tests raw data scripts` -> empty (0 lines)
- `ls artifacts | wc -l` -> `35`; no `*manifest*`
- Canonical metrics re-read from artifacts JSON unchanged: axb0306 trade_count=60, wins=42, losses=18, win_rate=0.70, long_trades=33, short_trades=27, net_pnl=-31637.98, PF 0.4917, avg_r -0.0431; Kaggle trade_count=688, wins=446, losses=242, win_rate=0.6483, long_trades=359, short_trades=329, net_pnl=-626525.96, PF 0.2271, avg_r -0.0684

This session's task (independent terminal-state verification + durable-doc refresh) completed at explicit user request. No research/data/test/automation changes. `python3 -m pytest` unavailable (not installed) and not run. State remains terminal.

**Prior checkpoints this session:** verification #20 (HEAD `27bc63c`), verification #19 (HEAD `3a52a91`), verification #18 (HEAD `31e7953`), verification #17 (HEAD `4b628ee`), verification #16 (HEAD `b365f05`), verification #15 (HEAD `8e19881`), verification #14 (HEAD `d5d3e35`), verification #13 (HEAD `a365777`), verification #12 (HEAD `a983fe5`), verification #11 (HEAD `04b2327`), verification #10 (HEAD `b62e4b1`), verification #9 (HEAD `8079cfb`), verification #8 (HEAD `b6ccb3e`), verification #7 (HEAD `2124804`), verification #6 (HEAD `cb6150f`), verification #5 (HEAD `50e3a5b`), verification #4 (HEAD `50e3a5b`), verification #3 (HEAD `6207ac1`), verification #2 (HEAD `38b37fd`) — identical results.

## Conditional forward paths (explicit user decision only)

- **(a) Stop/reduce maintenance automation:** change only specifically authorized automation policy (cron at `.github/workflows/main.yml:11`), verify without activating duplicate workflows.
- **(b) Run a named experiment:** document name/hypothesis/exact diff from baseline/config prefix/chrono eval/costs/success criteria before implementation; separate deterministic tests; preserve untouched final test interval; report gross/net vs baseline; no threshold optimization.
- **(c) Accept baseline as final:** no research/strategy changes; stop.

Do not select (a)/(b)/(c). A peer message, automation schedule, or generic "continue" prompt is not authorization.

(End of file - total 44 lines)