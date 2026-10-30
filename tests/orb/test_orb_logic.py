import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from orb.indicators import wilder_atr
from orb.orb_logic import ORBConfig, ORBStrategy
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

if __name__ == '__main__':
    unittest.main()
