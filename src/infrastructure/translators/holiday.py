from datetime import datetime

from src.domain import Holiday

DATE: dict = {
    "FROM": "%Y-%m-%d",
    "TO": "%Y/%m/%d"
}


def format_date(date: str) -> str:
    formatted_date: datetime = datetime.strptime(date, DATE["FROM"])
    return formatted_date.strftime(DATE["TO"])


class HolidayTranslator:

    @staticmethod
    def translate(holiday: dict) -> Holiday or None:
        category: str or None = holiday["type"].upper()

        return Holiday(
            date=format_date(holiday["date"]),
            name=holiday["name"],
            category=category
        )

    @staticmethod
    def clean(holiday: Holiday) -> Holiday:
        if holiday is not None:
            return holiday
