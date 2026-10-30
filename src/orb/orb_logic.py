"""Core ORB logic."""
from dataclasses import dataclass
from datetime import time, date
from typing import Optional, List, Dict, Any
import pandas as pd
import numpy as np
from zoneinfo import ZoneInfo

from .indicators import wilder_atr

ET = ZoneInfo("America/New_York")

@dataclass
class ORBConfig:
    or_start = time(9, 30)
    or_end = time(9, 45)
    no_new_entry_after = time(15, 0)
    forced_flatten = time(15, 55)
    rvol_lookback = 20
    rvol_min = 1.0
    atr_length = 14
    atr_min_pct = 0.10
    atr_max_pct = 0.60
    stop_atr_mult = 0.4
    target_stop_mult = 0.4
    risk_usd = 3000.0
    mnq_multiplier = 2.0
    max_trades_per_day = 1
    # Contract microstructure
    tick_size = 0.25
    # Execution costs (per side). Commission and exchange/clearing fees are
    # flat per-side amounts; slippage is per-contract per-side.
    commission_per_side = 2.25
    fee_per_side = 0.62
    slippage_ticks = 1

class ORBStrategy:
    def __init__(self, config: ORBConfig = None):
        self.config = config or ORBConfig()

    def build_opening_range(self, df_15m: pd.DataFrame, trading_date: date):
        df = df_15m.copy()
        or_mask = (df['time_et'] >= self.config.or_start) & (df['time_et'] < self.config.or_end)
        or_bars = df[or_mask & (df['date'] == trading_date)]
        if len(or_bars) == 0:
            return None
        or_high = or_bars['high'].max()
        or_low = or_bars['low'].min()
        return {'high': or_high, 'low': or_low, 'bars': or_bars}
