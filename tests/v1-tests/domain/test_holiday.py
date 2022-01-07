from unittest import TestCase
from v1.domain.holiday import Holiday


class TestHoliday(TestCase):

    def test_holiday_instance_must_have_been_created(self):
        holiday: Holiday = Holiday(
            date='2021/12/25',
            category='NATIONAL',
            name='Natal'
        )

        json_holiday: dict = {
            'date': '2021/12/25',
            'name': 'Natal',
            'type': 'NATIONAL'
        }
        self.assertEqual(holiday.to_json(), json_holiday, 'Holiday json was not correctly created')
