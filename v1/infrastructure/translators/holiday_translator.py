from v1.domain.holiday import Holiday

HOLIDAYS_TYPE: dict = {
    '1': 'NACIONAL',
    '3': 'MUNICIPAL',
    '4': 'FACULTATIVO'
}

DATE: dict = {
    'FROM': '%d/%m/%Y',
    'TO': '%Y-%m-%d'
}


def format_date(date: str) -> str:
    from datetime import datetime
    formatted_date = datetime.strptime(date, DATE["FROM"])
    return formatted_date.strftime(DATE["TO"])


def get_category_name(type_code: str) -> str or None:
    return HOLIDAYS_TYPE[type_code] if type_code in HOLIDAYS_TYPE else None


class HolidayTranslator:

    def __init__(self):
        pass

    def translate(self, holiday: dict) -> Holiday or None:
        category_name: str or None = get_category_name(type_code=str(holiday["type_code"]))

        if category_name is None:
            return

        return Holiday(
            date=format_date(holiday["date"]),
            name=holiday["name"],
            category=category_name
        )

    def clean(self, holiday: Holiday) -> Holiday:
        if holiday is not None:
            return holiday
