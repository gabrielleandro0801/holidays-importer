from typing import List, Any

from src.domain import Holiday, HolidayRepository
from src.infrastructure import logger

TABLE_NAME = "my_holidays"


class HolidayDynamoRepository(HolidayRepository):

    def __init__(self, dynamo_client: Any):
        self.dynamo_client = dynamo_client

    def save(self, holidays: List[Holiday]) -> None:
        table = self.dynamo_client.Table(TABLE_NAME)

        with table.batch_writer() as batch:
            for holiday in holidays:
                holiday_to_insert: dict = translate_holiday_to_dynamo(holiday)
                logger.info({"event": "save", "detail": "Saving holiday", "holiday": holiday_to_insert})

                batch.put_item(
                    Item=holiday_to_insert
                )


def translate_holiday_to_dynamo(holiday: Holiday) -> dict:
    return holiday.to_json()
