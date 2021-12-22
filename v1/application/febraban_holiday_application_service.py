import boto3
from typing import List, Any
from v1.domain.holiday import Holiday
from v1.domain.holiday_service import HolidayService, create_holiday_service
from v1.infrastructure.persistence.holiday_dynamo_repository import HolidayDynamoRepository, \
    create_holiday_dynamo_repository


class FebrabanHolidayApplicationService:

    def __init__(self, holiday_service: HolidayService, holiday_repository: HolidayDynamoRepository):
        self.holiday_service = holiday_service
        self.holiday_repository = holiday_repository

    def import_holidays(self, year: int) -> None:
        holidays: List[Holiday] = self.holiday_service.list_febraban_holidays(year=year)
        self.holiday_repository.save(holidays=holidays)


def create_application_service() -> FebrabanHolidayApplicationService:
    session = boto3.session.Session()

    holiday_service_factory: Any = create_holiday_service()
    repository_factory: Any = create_holiday_dynamo_repository(session=session)

    return FebrabanHolidayApplicationService(
        holiday_service=holiday_service_factory(),
        holiday_repository=repository_factory()
    )
