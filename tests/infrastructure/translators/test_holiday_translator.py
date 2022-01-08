from unittest import TestCase

from src.domain.holiday import Holiday
from src.infrastructure.translators.holiday_translator import HolidayTranslator, format_date


class TestHolidayTranslator(TestCase):
    def setUp(self) -> None:
        self.holiday_translator = HolidayTranslator()

    def test_must_translate_holiday_dict_to_holiday_object(self):
        holiday_dict = {
            'date': '2021-12-25',
            'name': 'Natal',
            'type': 'national'
        }

        response = self.holiday_translator.translate(holiday=holiday_dict)
        self.assertIsInstance(response, Holiday)

    def test_must_return_none_when_holiday_is_none(self):
        holiday = None

        response = self.holiday_translator.clean(holiday)
        self.assertIsNone(response, 'Response was not None')

    def test_must_return_holiday_object_when_holiday_dict_is_valid(self):
        holiday = Holiday(
            date='2021-12-25',
            name='Natal',
            category='NATIONAL'
        )

        response = self.holiday_translator.clean(holiday)
        self.assertNotEqual(response, None, 'Holiday was returned as None')

    def test_must_format_date_from_dashes_to_slashes(self):
        date = '2021-12-25'

        formatted_date = format_date(date=date)
        self.assertEqual(formatted_date, '2021/12/25', 'Date was not formatted correctly')
