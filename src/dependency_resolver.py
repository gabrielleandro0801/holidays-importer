from src.application import FebrabanHolidayApplicationService, create_application_service
from src.infrastructure import holiday_service_factory
from src.infrastructure.persistence import create_holiday_repository as holiday_repository_factory


def create_holiday_application_service() -> FebrabanHolidayApplicationService:
    return create_application_service(
        holiday_service_factory(),
        holiday_repository_factory(),
    )
