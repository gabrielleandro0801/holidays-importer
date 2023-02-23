from typing import List

from src.domain import Holiday
from . import CalendarClient
from ..translators import HolidayTranslator


class CalendarGateway:

    def __init__(self, client: CalendarClient):
        self.client: CalendarClient = client

    def list(self, year: int) -> List[Holiday]:
        holidays: List[dict] = self.client.list(year)
        holidays: List[Holiday] = [HolidayTranslator.translate(holiday) for holiday in holidays]
        return list(filter(HolidayTranslator.clean, holidays))
