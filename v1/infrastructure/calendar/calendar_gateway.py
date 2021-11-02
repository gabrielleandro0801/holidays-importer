from typing import List

from v1.domain.holiday import Holiday
from v1.infrastructure.calendar.calendar_client import CalendarClient
from v1.infrastructure.translators.holiday_translator import HolidayTranslator

constants = {
    'year': 2021,
    'city': 'Sao_Paulo',
    'state': 'SP'
}


class CalendarGateway:

    def __init__(self, calendar_client: CalendarClient, holiday_translator: HolidayTranslator):
        self.calendar_client: CalendarClient = calendar_client
        self.translator: HolidayTranslator = holiday_translator

    def list(self) -> List[Holiday]:
        holidays: List[dict] = self.calendar_client.list(params=constants)
        holidays: List[Holiday] = [self.translator.translate(holiday) for holiday in holidays]
        return list(filter(self.translator.clean, holidays))


def create_calendar_gateway():
    return CalendarGateway(
        calendar_client=CalendarClient(
            url="https://613550c660d2900017c3bf60.mockapi.io/mundo/feriados",
            token=""
        ),
        holiday_translator=HolidayTranslator()
    )
