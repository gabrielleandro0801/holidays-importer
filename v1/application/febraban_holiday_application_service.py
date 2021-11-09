import boto3
from typing import List

from v1.domain.holiday import Holiday
from v1.domain.holiday_filter import HolidayFilter
from v1.domain.holiday_service import HolidayService
from v1.infrastructure.calendar.calendar_gateway import create_calendar_gateway
from v1.infrastructure.persistence.holiday_dynamo_repository import HolidayDynamoRepository, get_dynamo_client


class FebrabanHolidayApplicationService:

    def __init__(self, holiday_service: HolidayService, holiday_repository: HolidayDynamoRepository):
        self.holiday_service = holiday_service
        self.holiday_repository = holiday_repository

    def import_holidays(self) -> None:
        holidays: List[Holiday] = self.holiday_service.list_febraban_holidays()
        self.holiday_repository.save(holidays=holidays)


def configure_application_service() -> FebrabanHolidayApplicationService:
    session = boto3.session.Session()

    return FebrabanHolidayApplicationService(
        holiday_service=HolidayService(
            calendar_gateway=create_calendar_gateway(),
            holiday_filter=HolidayFilter()
        ),
        holiday_repository=HolidayDynamoRepository(
            dynamo_client=get_dynamo_client(session=session)
        )
    )
