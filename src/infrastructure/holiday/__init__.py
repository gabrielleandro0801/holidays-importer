from .service import HolidayServiceImpl
from src.infrastructure.calendar.calendar_gateway import CalendarGateway


def create_holiday_service(calendar_gateway: CalendarGateway):
    return HolidayServiceImpl(calendar_gateway)
