from unittest.mock import patch
from unittest import TestCase, mock
from v1.application.febraban_holiday_application_service import FebrabanHolidayApplicationService

IMPORT_HOLIDAYS_RESPONSE = None


class TestFebrabanHolidayApplicationService(TestCase):

    @mock.patch('v1.infrastructure.persistence.holiday_dynamo_repository.HolidayDynamoRepository', autospec=True)
    @mock.patch('v1.domain.holiday_service.HolidayService', autospec=True)
    def setUp(self, mock_holiday_service, mock_holiday_repository) -> None:
        self.holiday_service = mock_holiday_service
        self.holiday_repository = mock_holiday_repository
        self.application_service = FebrabanHolidayApplicationService(self.holiday_service, self.holiday_repository)

    @patch('v1.application.febraban_holiday_application_service.FebrabanHolidayApplicationService.import_holidays',
           return_value=IMPORT_HOLIDAYS_RESPONSE)
    def test_import_holidays_must_have_been_called_with_specified_year(self, import_holidays_response):
        year = 2021

        self.application_service.import_holidays(year)
        import_holidays_response.assert_called_with(2021)
