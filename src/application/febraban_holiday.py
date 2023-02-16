from typing import List

from src.domain import Holiday, HolidayService, HolidayRepository


class FebrabanHolidayApplicationService:

    def __init__(self, service: HolidayService, repository: HolidayRepository):
        self.holiday_service = service
        self.holiday_repository = repository

    def import_holidays(self, year: int) -> None:
        holidays: List[Holiday] = self.holiday_service.list_febraban_holidays(year)
        self.holiday_repository.save(holidays)
