from typing import List, Any
from src.domain.holiday import Holiday
import src.infrastructure.calendar.calendar_gateway as gateway


class HolidayService:

    def __init__(self, calendar_gateway: gateway.CalendarGateway):
        self.calendar_gateway: gateway.CalendarGateway = calendar_gateway

    def list_febraban_holidays(self, year: int) -> List[Holiday]:
        holidays: List[Holiday] = self.calendar_gateway.list(year=year)
        return self.remove_duplication(holidays=holidays)

    def remove_duplication(self, holidays: List[Holiday]) -> List[Holiday]:
        clean_holidays = {}

        for holiday in holidays:
            if holiday.date not in clean_holidays:
                clean_holidays[holiday.date] = holiday

        return list(clean_holidays.values())


def create_holiday_service() -> Any:
    calendar_gateway_factory: Any = gateway.create_calendar_gateway()
    return lambda: HolidayService(
        calendar_gateway=calendar_gateway_factory()
    )
