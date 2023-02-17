from typing import Any

import boto3

from .holiday_dynamo_repository import HolidayDynamoRepository
from src.infrastructure.properties import PROPERTIES


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


def create_holiday_repository():
    return HolidayDynamoRepository(_get_dynamo_client())
