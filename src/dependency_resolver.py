from typing import Any

import boto3

from src.application import FebrabanHolidayApplicationService
from src.infrastructure import HolidayServiceImpl, HolidayDynamoRepository, CalendarGateway, PROPERTIES, CalendarClient


def _get_dynamo_client() -> Any:
    def get_endpoint_url() -> str or None:
        return f'http://{PROPERTIES.get("HOST")}:{PROPERTIES.get("PORT")}' if PROPERTIES.get("ENV") == "local" else None

    endpoint_url: str or None = get_endpoint_url()

    session = boto3.Session()
    return session.resource(
        service_name="dynamodb",
        region_name="us-east-1",
        endpoint_url=endpoint_url
    )

def create_holiday_application_service():
    return FebrabanHolidayApplicationService(
        HolidayServiceImpl(
            CalendarGateway(
                CalendarClient(
                    PROPERTIES.get("CALENDAR_API_URL"),
                ),
            ),
        ),
        HolidayDynamoRepository(
            _get_dynamo_client(),
        ),
    )
