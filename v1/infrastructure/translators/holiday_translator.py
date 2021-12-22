from datetime import datetime
from typing import Any

from v1.domain.holiday import Holiday


DATE: dict = {
    'FROM': '%Y-%m-%d',
    'TO': '%Y/%m/%d'
}


def format_date(date: str) -> str:
    formatted_date: datetime = datetime.strptime(date, DATE["FROM"])
    return formatted_date.strftime(DATE["TO"])


class HolidayTranslator:

    def __init__(self):
        pass

    def translate(self, holiday: dict) -> Holiday or None:
        category: str or None = holiday["type"].upper()

        return Holiday(
            date=format_date(holiday["date"]),
            name=holiday["name"],
            category=category
        )

    def clean(self, holiday: Holiday) -> Holiday:
        if holiday is not None:
            return holiday


def create_holiday_translator() -> Any:
    return lambda: HolidayTranslator()
