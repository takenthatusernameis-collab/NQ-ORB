"""Technical indicators."""
import pandas as pd
import numpy as np


def wilder_atr(df: pd.DataFrame, length: int = 14) -> pd.Series:
    """Wilder's smoothed ATR.

    First value is the simple mean of the first `length` true ranges;
    subsequent values use Wilder's exponential smoothing
    ATR[i] = (ATR[i-1]*(length-1) + TR[i]) / length.

    The result is NaN for the first `length-1` rows (no ATR until enough TRs).
    """
    high = df['high']
    low = df['low']
    close = df['close']
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    atr = pd.Series(index=df.index, dtype=float)
    if len(tr) < length:
        return atr  # not enough data

    # Seed: SMA of first `length` true ranges (index 0..length-1)
    seed = tr.iloc[:length].mean()
    atr.iloc[length - 1] = seed

    # Wilder smoothing for the rest
    prev = seed
    for i in range(length, len(tr)):
        prev = (prev * (length - 1) + tr.iloc[i]) / length
        atr.iloc[i] = prev

    return atr