from datetime import datetime


def get_utc_time():
    """Return utc time."""
    now_utc = datetime.utcnow()
    return now_utc
