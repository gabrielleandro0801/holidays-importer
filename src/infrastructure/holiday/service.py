from typing import List

from src.domain import Holiday, HolidayService
from ..calendar import CalendarGateway


class HolidayServiceImpl(HolidayService):

    def __init__(self, calendar_gateway: CalendarGateway):
        self.calendar_gateway: CalendarGateway = calendar_gateway

    def list_febraban_holidays(self, year: int) -> List[Holiday]:
        holidays: List[Holiday] = self.calendar_gateway.list(year)
        return remove_duplication(holidays)


def remove_duplication(holidays: List[Holiday]) -> List[Holiday]:
    clean_holidays: dict = {}

    for holiday in holidays:
        if holiday.date not in clean_holidays:
            clean_holidays[holiday.date] = holiday

    return list(clean_holidays.values())
