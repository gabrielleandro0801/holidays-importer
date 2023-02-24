from unittest import TestCase, mock

from faker import Faker

from src.domain.holiday import Holiday
from src.infrastructure import HolidayServiceImpl

fake = Faker()

LIST_FEBRABAN_HOLIDAYS_RESPONSE = None


class TestHolidayService(TestCase):

    def setUp(self) -> None:
        self.calendar_gateway = mock.Mock()
        self.calendar_gateway.list.return_value = []

        self.holiday_service = HolidayServiceImpl(self.calendar_gateway)

    def test_list_specified_year(self):
        year = fake.unique.random_int()

        self.holiday_service.list_febraban_holidays(year)
        self.calendar_gateway.list.assert_called_with(year)

    def test_holidays_list_must_have_no_duplications(self):
        year = fake.unique.random_int()
        duplicated_holidays = [
            Holiday(
                date="2021/10/12",
                category="NATIONAL",
                name="Nossa Senhora Aparecida"
            ),
            Holiday(
                date="2021/10/12",
                category="NATIONAL",
                name="Nossa Senhora Aparecida"
            ),
            Holiday(
                date="2021/10/12",
                category="NATIONAL",
                name="Nossa Senhora Aparecida"
            )
        ]

        self.calendar_gateway.list.return_value = duplicated_holidays
        response = self.holiday_service.list_febraban_holidays(year)
        self.assertEqual(len(response), 1, "Holidays list is greater than 1")
