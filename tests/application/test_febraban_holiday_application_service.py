from unittest import TestCase, mock

from faker import Faker

from src.application import FebrabanHolidayApplicationService
from src.domain.holiday import Holiday

fake = Faker()

LIST_FEBRABAN_HOLIDAYS_EMPTY_RESPONSE = []
LIST_FEBRABAN_HOLIDAYS_FULL_RESPONSE = [Holiday('2021-12-25', 'Natal', 'NATIONAL')]

SAVE_RESPONSE = None


class TestFebrabanHolidayApplicationService(TestCase):

    def setUp(self) -> None:
        self.holiday_service = mock.Mock()

        self.holiday_repository = mock.Mock()
        self.holiday_repository.save.return_value = SAVE_RESPONSE

        self.subject = FebrabanHolidayApplicationService(self.holiday_service, self.holiday_repository)

    def test_list_febraban_holidays_must_have_been_called_with_right_year(self):
        year = fake.unique.random_int()
        self.holiday_service.list_febraban_holidays.return_value = LIST_FEBRABAN_HOLIDAYS_EMPTY_RESPONSE

        self.subject.import_holidays(year)
        self.holiday_service.list_febraban_holidays.assert_called_once_with(year)
        self.holiday_repository.save.assert_called_once_with(LIST_FEBRABAN_HOLIDAYS_EMPTY_RESPONSE)

    def test_save_must_have_been_called_with_right_holidays(self):
        year = fake.unique.random_int()
        self.holiday_service.list_febraban_holidays.return_value = LIST_FEBRABAN_HOLIDAYS_FULL_RESPONSE

        self.subject.import_holidays(year)
        self.holiday_repository.save.assert_called_once_with(LIST_FEBRABAN_HOLIDAYS_FULL_RESPONSE)
        self.holiday_repository.save.assert_called_once_with(LIST_FEBRABAN_HOLIDAYS_FULL_RESPONSE)
