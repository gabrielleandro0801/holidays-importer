from typing import Any
from datetime import datetime
from v1.infrastructure.logger.log import logger
from v1.application.febraban_holiday_application_service import *


def get_year_from_event(lambda_event: Any) -> int:
    return lambda_event["year"] if 'year' in lambda_event else datetime.now().year


def main(lambda_event: Any, context: Any):
    logger.info({"event": "handler", "detail": "Application started its job"})
    application_service: FebrabanHolidayApplicationService = configure_application_service()
    application_service.import_holidays(year=get_year_from_event(lambda_event=lambda_event))

    logger.info({"event": "handler", "detail": "Application finished its job"})


if __name__ == '__main__':
    event = {
        'year': 2025
    }
    main(event, '')
