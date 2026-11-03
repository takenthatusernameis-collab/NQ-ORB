"""Build raw/NQ_15min.csv from the free getdata-finance NQ 1m sample.

The NQ 1m sample (raw/NQ_1min_getdata.csv, 2026-02-02..2026-07-31) is the
first genuinely free NQ/MNQ-equivalent 1-minute source found since the last
sweep. This script aggregates it to 15-minute bars using the SAME convention
as the frozen axb0306 raw series: timestamps are the bar OPEN time in
America/New_York, bars are aligned to the 09:30 ET cash open, and only the
cash-session window 09:30..16:14 ET is retained (matching axb0306's
13:15..20:14 UTC-equivalent coverage).

No strategy logic, parameters, or thresholds are touched. This is data
preparation only; the frozen STRATEGY_RULES.txt v1.0 is run unchanged.
"""
import csv
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")

SRC = "raw/NQ_1min_getdata.csv"
DST = "raw/NQ_15min_getdata.csv"

# Cash session retained: 09:30 ET open bar through the 16:00 ET close bar.
# (axb0306 15min series ends at 16:00 ET; 16:15 ET bar is absent in both.)
SESSION_START = 9 * 60 + 30   # 09:30
SESSION_END_EXCL = 16 * 60 + 15  # exclusive -> last bar starts 16:00


def et_minutes(dt_utc: datetime) -> int:
    et = dt_utc.astimezone(ET)
    return et.hour * 60 + et.minute, et


def main():
    bars = {}
    with open(SRC) as f:
        for r in csv.DictReader(f):
            dt = datetime.fromisoformat(r["datetime"].replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=UTC)
            mins, et = et_minutes(dt)
            if mins < SESSION_START or mins >= SESSION_END_EXCL:
                continue
            # Bar open = floor to 15 min from 09:30 ET.
            idx = (mins - SESSION_START) // 15
            total = SESSION_START + idx * 15
            open_et = et.replace(hour=total // 60, minute=total % 60,
                                 second=0, microsecond=0)
            key = (et.date(), idx)
            o = float(r["open"])
            h = float(r["high"])
            l = float(r["low"])
            c = float(r["close"])
            v = int(r["volume"])
            if key in bars:
                b = bars[key]
                b["high"] = max(b["high"], h)
                b["low"] = min(b["low"], l)
                b["close"] = c
                b["volume"] += v
            else:
                bars[key] = {"open": o, "high": h, "low": l, "close": c,
                             "volume": v, "open_et": open_et}

    rows = []
    for (d, idx) in sorted(bars):
        b = bars[(d, idx)]
        rows.append((b["open_et"], b["open"], b["high"], b["low"], b["close"], b["volume"]))

    with open(DST, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["datetime", "open", "high", "low", "close", "volume"])
        for ts, o, h, l, c, v in rows:
            w.writerow([ts.strftime("%Y-%m-%dT%H:%M:%S"), o, h, l, c, v])

    print(f"Wrote {len(rows)} 15min bars to {DST}")
    print(f"First: {rows[0][0]}  Last: {rows[-1][0]}")


if __name__ == "__main__":
    main()