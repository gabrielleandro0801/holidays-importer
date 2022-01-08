from datetime import datetime
from typing import Any
from src.infrastructure.logger.log import logger
import src.application.febraban_holiday_application_service as application


def get_year_from_event(lambda_event: Any) -> int:
    return lambda_event["year"] if 'year' in lambda_event else datetime.now().year


application_service: application.FebrabanHolidayApplicationService = application.create_application_service()


def main(lambda_event: Any, context: Any):
    logger.info({"event": "handler", "detail": "Application started its job"})
    application_service.import_holidays(year=get_year_from_event(lambda_event=lambda_event))
    logger.info({"event": "handler", "detail": "Application finished its job"})


if __name__ == '__main__':
    event = {
        'year': 2025
    }
    main(event, '')
