from typing import List, Any

from v1.domain.holiday import Holiday
from v1.infrastructure.calendar.calendar_client import CalendarClient, create_calendar_client
from v1.infrastructure.translators.holiday_translator import HolidayTranslator, create_holiday_translator


class CalendarGateway:

    def __init__(self, calendar_client: CalendarClient, holiday_translator: HolidayTranslator):
        self.calendar_client: CalendarClient = calendar_client
        self.translator: HolidayTranslator = holiday_translator

    def list(self, year: int) -> List[Holiday]:
        holidays: List[dict] = self.calendar_client.list(year=year)
        holidays: List[Holiday] = [self.translator.translate(holiday) for holiday in holidays]
        return list(filter(self.translator.clean, holidays))


def create_calendar_gateway() -> Any:
    calendar_client_factory: Any = create_calendar_client()
    holiday_translator_factory: Any = create_holiday_translator()

    return lambda: CalendarGateway(
        calendar_client=calendar_client_factory(),
        holiday_translator=holiday_translator_factory()
    )
