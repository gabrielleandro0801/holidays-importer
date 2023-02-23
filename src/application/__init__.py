from .febraban_holiday import FebrabanHolidayApplicationService
from ..domain import HolidayService, HolidayRepository


def create_application_service(service: HolidayService, repository: HolidayRepository):
    return FebrabanHolidayApplicationService(service, repository)
