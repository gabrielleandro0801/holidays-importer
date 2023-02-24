from unittest import TestCase
from src.domain.holiday import Holiday
from faker import Faker
fake = Faker()


class TestHoliday(TestCase):

    def setUp(self) -> None:
        self.subject = Holiday(
            date="2021/12/25",
            category="NATIONAL",
            name="Natal"
        )

    def test_is_category_must_return_a_bool(self):
        random_category = fake.name()
        response = self.subject.is_category(random_category)

        self.assertEqual(False, response, "is_category did not return false")
        self.assertFalse(response)
        self.assertIsInstance(response, bool)

    def test_to_json_must_return_a_dict(self):
        response = self.subject.to_json()
        expected_response: dict = {
            "date": "2021/12/25",
            "name": "Natal",
            "type": "NATIONAL"
        }

        self.assertEqual(expected_response, response, "to_json did not return the expected dict")
        self.assertIsInstance(response, dict)
