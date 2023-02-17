from .calendar_client import CalendarClient
from .calendar_gateway import CalendarGateway
from ..properties import PROPERTIES

url: str = PROPERTIES.get("CALENDAR_API_URL")


def create_calendar_gateway():
    return CalendarGateway(CalendarClient(url))
