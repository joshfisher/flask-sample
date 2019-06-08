from datetime import datetime


def isnatural(input: str) -> bool:
    for c in input:
        if not c.isdigit():
            return False
    return True


def fmt_date(date: datetime) -> str:
    return date.replace(microsecond=0).isoformat()
