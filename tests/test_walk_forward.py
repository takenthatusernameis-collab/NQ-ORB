"""Tests for the walk-forward evaluation helper.

These exercise the split accounting logic with synthetic trade ledgers so
the walk-forward windowing contract is pinned without depending on the
canonical artifacts (which are regenerated, not asserted here).
"""
import json
import os
import sys
from pathlib import Path

import pandas as pd
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


def _dates(n, start="2026-01-01"):
    """Return n consecutive calendar days starting at `start`."""
    base = pd.Timestamp(start)
    return [(base + pd.Timedelta(days=i)).strftime("%Y-%m-%d") for i in range(n)]


def test_walk_forward_date_60_20_20_single_split():
    """Date-based 60/20/20 yields exactly one split by trading date."""
    dates = _dates(100)
    trades = [_make_trade(i, pnl=float(i), date=dates[i]) for i in range(100)]
    out = list(wf.walk_forward_date_60_20_20(trades, min_train_days=30))
    assert len(out) == 1
    train, val, test, meta = out[0]
    assert meta["n_days"] == 100
    assert meta["train_days"] == 60
    assert meta["val_days"] == 20
    assert meta["test_days"] == 20
    assert len(train) + len(val) + len(test) == len(trades)
    # Contiguous and non-overlapping by date.
    assert meta["train_dates"][-1] < meta["val_dates"][0]
    assert meta["val_dates"][-1] < meta["test_dates"][0]
    # Final test window is the tail of the calendar (last 20%).
    assert meta["test_dates"][0] == dates[80]
    assert meta["val_dates"][0] == dates[60]
    assert meta["test_dates"][-1] == dates[99]


def test_walk_forward_date_60_20_20_too_short_returns_nothing():
    """Fewer than 30 distinct trading dates yields no split."""
    dates = _dates(29)
    trades = [_make_trade(i, date=dates[i]) for i in range(29)]
    assert list(wf.walk_forward_date_60_20_20(trades)) == []


def test_walk_forward_date_main_writes_output(tmp_path, monkeypatch):
    """date_60_20_20 mode writes a single-window artifact with val + test."""
    dates = _dates(100)
    trades = [_make_trade(i, pnl=float(i) - 50.0, date=dates[i]) for i in range(100)]
    out_path = tmp_path / "wf_date.json"
    monkeypatch.setattr(sys, "argv", [
        "walk_forward.py", "--source", "kaggle",
        "--method", "date_60_20_20", "--out", str(out_path),
    ])
    monkeypatch.setattr(wf, "load_trades", lambda p: trades)
    wf.main()
    data = json.loads(out_path.read_text())
    assert data["method"] == "date_based_chronological_60_20_20"
    assert data["n_windows"] == 1
    assert data["train_days"] == 60
    assert data["val_days"] == 20
    assert data["test_days"] == 20
    w = data["windows"][0]
    assert "val" in w
    assert w["test"]["count"] > 0
    assert w["test_dates"]["start"] < w["test_dates"]["end"]


def test_walk_forward_date_60_20_20_final_test_untouched():
    """The last 20% of trading dates form the untouched test window."""
    dates = _dates(100)
    trades = [_make_trade(i, date=dates[i]) for i in range(100)]
    out = list(wf.walk_forward_date_60_20_20(trades))[0]
    train, val, test, meta = out
    assert meta["test_dates"][0] == dates[80]
    assert meta["test_dates"][-1] == dates[99]
    assert all(t["date"] in set(meta["test_dates"]) for t in test)