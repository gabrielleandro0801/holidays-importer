from unittest import TestCase, mock
from unittest.mock import patch

from src.domain.holiday import Holiday
from src.domain.holiday_service import HolidayService

LIST_FEBRABAN_HOLIDAYS_RESPONSE = None


class TestHolidayService(TestCase):

    @mock.patch('src.infrastructure.calendar.calendar_gateway.CalendarGateway', autospec=True)
    def setUp(self, mock_calendar_gateway) -> None:
        self.holiday_service = HolidayService(mock_calendar_gateway)

    @patch('src.domain.holiday_service.HolidayService.list_febraban_holidays',
           return_value=LIST_FEBRABAN_HOLIDAYS_RESPONSE)
    def test_list_febraban_holidays_must_have_been_called_with_specified_year(self, list_febraban_holidays_response):
        year = 2021

        self.holiday_service.list_febraban_holidays(year)
        list_febraban_holidays_response.assert_called_with(2021)

    def test_holidays_list_duplications_must_have_been_removed(self):
        first_holiday = Holiday(
            date='2021/10/12',
            category='NATIONAL',
            name='Nossa Senhora Aparecida'
        )
        second_holiday = Holiday(
            date='2021/12/25',
            category='NATIONAL',
            name='Natal'
        )
        third_holiday = Holiday(
            date='2021/31/01',
            category='NATIONAL',
            name='Ano Novo'
        )

        holidays_list_with_duplication = [
            first_holiday,
            first_holiday,
            second_holiday,
            second_holiday,
            third_holiday
        ]

        clean_holiday_list = [
            first_holiday,
            second_holiday,
            third_holiday
        ]

        response = self.holiday_service.remove_duplication(holidays_list_with_duplication)
        self.assertEqual(response, clean_holiday_list, 'The list of holidays have not been cleaned')
