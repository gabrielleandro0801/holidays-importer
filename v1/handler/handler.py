from v1.application.febraban_holiday_application_service import FebrabanHolidayApplicationService, \
    configure_application_service
from v1.infrastructure.logger.log import logger


def main(event, context):
    logger.info({"event": "handler", "detail": "Application started its job"})
    application_service: FebrabanHolidayApplicationService = configure_application_service()
    application_service.import_holidays()

    logger.info({"event": "handler", "detail": "Application finished its job"})


if __name__ == '__main__':
    main('', '')
