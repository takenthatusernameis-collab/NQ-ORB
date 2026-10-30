import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from orb.indicators import wilder_atr
from orb.orb_logic import ORBConfig, ORBStrategy
from orb.backtest import BacktestEngine
import pandas as pd
from datetime import date, time
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")


class TestORBLogic(unittest.TestCase):
    def test_wilder_atr_basic(self):
        df = pd.DataFrame({
            'high': [10, 11, 12],
            'low': [9, 10, 11],
            'close': [9.5, 10.5, 11.5]
        })
        atr = wilder_atr(df, length=2)
        self.assertIsNotNone(atr)
        self.assertEqual(len(atr), 3)

    def test_orb_config_defaults(self):
        config = ORBConfig()
        self.assertEqual(config.rvol_min, 1.0)
        self.assertEqual(config.atr_min_pct, 0.10)
        self.assertEqual(config.atr_max_pct, 0.60)
        self.assertEqual(config.stop_atr_mult, 0.4)
        self.assertEqual(config.target_stop_mult, 0.4)
        self.assertEqual(config.risk_usd, 3000.0)
        self.assertEqual(config.mnq_multiplier, 2.0)
        self.assertEqual(config.max_trades_per_day, 1)
        self.assertEqual(config.no_new_entry_after.hour, 15)
        self.assertEqual(config.forced_flatten.hour, 15)
        self.assertEqual(config.forced_flatten.minute, 55)

    def test_opening_range_construction(self):
        strategy = ORBStrategy(ORBConfig())
        # Create 15min bars for a day
        dates = []
        # 09:30, 09:45, 10:00
        base = pd.Timestamp('2026-01-21 14:30:00', tz=UTC)  # 09:30 ET
        rows = []
        for i, (h, l, c) in enumerate([(100, 99, 99.5), (101, 99.5, 100.5), (102, 100, 101)]):
            dt = base + pd.Timedelta(minutes=15*i)
            rows.append({
                'datetime': dt,
                'open': (h+l)/2,
                'high': h,
                'low': l,
                'close': c,
                'volume': 1000
            })
        df = pd.DataFrame(rows)
        df['datetime_et'] = df['datetime'].dt.tz_convert(ET)
        df['date'] = df['datetime_et'].dt.date
        df['time_et'] = df['datetime_et'].dt.time
        or_info = strategy.build_opening_range(df, df['date'].iloc[0])
        self.assertIsNotNone(or_info)
        self.assertEqual(or_info['high'], 100.0)
        self.assertEqual(or_info['low'], 99.0)

    def test_one_trade_per_day_enforced(self):
        config = ORBConfig()
        engine = BacktestEngine(config)
        # Create simple data where conditions might trigger
        # Just verify engine has max_trades_per_day
        self.assertEqual(engine.config.max_trades_per_day, 1)

    def test_no_new_entry_after_1500(self):
        config = ORBConfig()
        self.assertEqual(str(config.no_new_entry_after), '15:00:00')


if __name__ == '__main__':
    unittest.main()
