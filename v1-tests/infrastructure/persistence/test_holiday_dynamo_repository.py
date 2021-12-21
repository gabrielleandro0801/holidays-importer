from unittest import TestCase

from v1.domain.holiday import Holiday
from v1.infrastructure.persistence.holiday_dynamo_repository import translate_holiday_to_dynamo

HOLIDAY = Holiday(
    date='2021-12-25',
    name='Natal',
    category='NATIONAL'
)


class TestHolidayDynamoRepository(TestCase):

    def test_holiday_must_be_dict_when_given_as_object(self):
        response = translate_holiday_to_dynamo(HOLIDAY)
        self.assertIsInstance(response, dict, 'Holiday was not returned as a dict')
