import uuid
from datetime import datetime
from typing import Any

from src import create_holiday_application_service
from src.application import FebrabanHolidayApplicationService
from src.infrastructure import logger, set_global_uuid


def get_year_from_event(lambda_event: Any) -> int:
    return lambda_event["year"] if "year" in lambda_event else datetime.now().year


application_service: FebrabanHolidayApplicationService = create_holiday_application_service()


def main(event: dict, context: Any):
    set_global_uuid(str(uuid.uuid4()))
    logger.info({"event": "entrypoint", "detail": "Application started its job"})

    year: int = get_year_from_event(event)
    application_service.import_holidays(year)
    logger.info({"event": "entrypoint", "details": "Application finished its job"})


if __name__ == "__main__":
    event = {
        "year": 2025
    }
    main(event, "")
