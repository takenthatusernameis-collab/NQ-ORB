"""Data loading utilities."""
import os
import csv
from datetime import datetime
from typing import Dict, List, Any
import pandas as pd
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")

class DataLoader:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir

    def load_csv(self, filepath: str) -> pd.DataFrame:
        df = pd.read_csv(filepath)
        df['datetime'] = pd.to_datetime(df['datetime'])
        if df['datetime'].dt.tz is None:
            df['datetime'] = df['datetime'].dt.tz_localize(UTC)
        else:
            df['datetime'] = df['datetime'].dt.tz_convert(UTC)
        df = df.sort_values('datetime').reset_index(drop=True)
        return df

    def to_et(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df['datetime_et'] = df['datetime'].dt.tz_convert(ET)
        df['date'] = df['datetime_et'].dt.date
        df['time_et'] = df['datetime_et'].dt.time
        return df
