from unittest import TestCase
from src.domain.holiday import Holiday
from faker import Faker
fake = Faker()


class TestHoliday(TestCase):

    def setUp(self) -> None:
        self.holiday = Holiday(
            date='2021/12/25',
            category='NATIONAL',
            name='Natal'
        )

    def test_is_category_must_return_a_bool(self):
        random_category = fake.name()
        response = self.holiday.is_category(random_category)

        self.assertEqual(False, response, 'is_category did not return false')
        self.assertFalse(response)
        self.assertIsInstance(response, bool)
