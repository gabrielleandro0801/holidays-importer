import os
from typing import List, Any
from v1.domain.holiday import Holiday
from v1.infrastructure.logger.log import logger

TABLE_NAME = 'my_holidays'

ENV = os.getenv('ENV', 'local')
HOST = os.getenv('LOCALSTACK_HOSTNAME', 'localhost')
PORT = os.getenv('EDGE_PORT', '4566')


def get_endpoint_url() -> str or None:
    options: dict = {
        'local': f'http://{HOST}:{PORT}'
    }
    return options[ENV] if ENV in options else None


def get_dynamo_client(session: Any) -> Any:
    endpoint_url: str or None = get_endpoint_url()
    return session.resource(
        service_name='dynamodb',
        region_name='us-east-1',
        endpoint_url=endpoint_url
    )


def translate_holiday_to_dynamo(holiday: Holiday) -> dict:
    return holiday.to_json()


class HolidayDynamoRepository:

    def __init__(self, dynamo_client: Any):
        self.dynamo_client = dynamo_client

    def save(self, holidays: List[Holiday]) -> None:
        table = self.dynamo_client.Table(TABLE_NAME)

        with table.batch_writer() as batch:
            for holiday in holidays:
                holiday_to_insert: dict = translate_holiday_to_dynamo(holiday=holiday)
                logger.info({"event": "save", "detail": "Saving holiday", "holiday": holiday_to_insert})

                batch.put_item(
                    Item=holiday_to_insert
                )
