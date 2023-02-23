from .logger import *
from .holiday import HolidayServiceImpl, create_holiday_service
from .persistence import HolidayDynamoRepository
from .calendar import CalendarClient, CalendarGateway, create_calendar_gateway

def holiday_service_factory():
    return create_holiday_service(create_calendar_gateway())
