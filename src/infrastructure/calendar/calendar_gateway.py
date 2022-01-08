from typing import List, Any
from src.domain.holiday import Holiday
import src.infrastructure.calendar.calendar_client as client
import src.infrastructure.translators.holiday_translator as translator


class CalendarGateway:

    def __init__(self, calendar_client: client.CalendarClient, holiday_translator: translator.HolidayTranslator):
        self.calendar_client: client.CalendarClient = calendar_client
        self.translator: translator.HolidayTranslator = holiday_translator

    def list(self, year: int) -> List[Holiday]:
        holidays: List[dict] = self.calendar_client.list(year=year)
        holidays: List[Holiday] = [self.translator.translate(holiday) for holiday in holidays]
        return list(filter(self.translator.clean, holidays))


def create_calendar_gateway() -> Any:
    calendar_client_factory: Any = client.create_calendar_client()
    holiday_translator_factory: Any = translator.create_holiday_translator()

    return lambda: CalendarGateway(
        calendar_client=calendar_client_factory(),
        holiday_translator=holiday_translator_factory()
    )
