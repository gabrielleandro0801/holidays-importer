import boto3
from typing import List, Any
from src.domain.holiday import Holiday
from src.domain.holiday_service import HolidayService, create_holiday_service
import src.infrastructure.persistence.holiday_dynamo_repository as repository


class FebrabanHolidayApplicationService:

    def __init__(self, holiday_service: HolidayService, holiday_repository: repository.HolidayDynamoRepository):
        self.holiday_service = holiday_service
        self.holiday_repository = holiday_repository

    def import_holidays(self, year: int) -> None:
        holidays: List[Holiday] = self.holiday_service.list_febraban_holidays(year=year)
        self.holiday_repository.save(holidays=holidays)


def create_application_service() -> FebrabanHolidayApplicationService:
    session = boto3.session.Session()

    holiday_service_factory: Any = create_holiday_service()
    repository_factory: Any = repository.create_holiday_dynamo_repository(session=session)

    return FebrabanHolidayApplicationService(
        holiday_service=holiday_service_factory(),
        holiday_repository=repository_factory()
    )
