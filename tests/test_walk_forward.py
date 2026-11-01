"""Tests for the walk-forward evaluation helper.

These exercise the split accounting logic with synthetic trade ledgers so
the walk-forward windowing contract is pinned without depending on the
canonical artifacts (which are regenerated, not asserted here).
"""
import json
import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import walk_forward as wf


def _make_trade(i, pnl=10.0, date=None):
    return {
        'date': date or f"2026-01-{i+1:02d}",
        'direction': 'long',
        'net_pnl': pnl,
        'gross_pnl': pnl + 5.0,
        'exit_time': f"2026-01-{i+1:02d} 16:00:00-05:00",
    }


def test_walk_forward_yields_windows():
    trades = [_make_trade(i, pnl=float(i) - 50.0) for i in range(300)]
    wins = list(wf.walk_forward(trades, window_trades=100, step_trades=50))
    # train 0:100 -> test 100:200 ; 0:150->150:250 ; 0:200->200:300
    assert len(wins) == 3
    assert wins[0] == (0, 100, 100, 200)
    assert wins[1] == (0, 150, 150, 250)
    assert wins[2] == (0, 200, 200, 300)


def test_walk_forward_too_short_returns_nothing():
    trades = [_make_trade(i) for i in range(50)]
    assert list(wf.walk_forward(trades, window_trades=100, step_trades=50)) == []


def test_walk_forward_load_trades(tmp_path):
    p = tmp_path / "trades.json"
    p.write_text(json.dumps([_make_trade(0), _make_trade(1)]))
    out = wf.load_trades(str(p))
    assert len(out) == 2


def test_walk_forward_main_writes_output(tmp_path, monkeypatch):
    trades = [_make_trade(i, pnl=float(i) - 50.0) for i in range(300)]
    out_path = tmp_path / "wf.json"
    monkeypatch.setattr(sys, "argv", [
        "walk_forward.py", "--source", "kaggle",
        "--window-trades", "100", "--step-trades", "50",
        "--out", str(out_path),
    ])
    # Bypass the artifact file check by stubbing load_trades with synthetic data.
    monkeypatch.setattr(wf, "load_trades", lambda p: trades)
    wf.main()
    data = json.loads(out_path.read_text())
    assert data["n_windows"] == 3
    assert data["total_trades"] == 300
    assert all("test" in w and "train" in w for w in data["windows"])


def test_walk_forward_final_window_untouched():
    """The last test window must extend to the end of the ledger."""
    trades = [_make_trade(i) for i in range(300)]
    wins = list(wf.walk_forward(trades, window_trades=100, step_trades=100))
    assert wins[-1] == (0, 200, 200, 300)