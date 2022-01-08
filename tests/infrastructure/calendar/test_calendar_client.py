from unittest import TestCase
from src.infrastructure.calendar.calendar_client import CalendarClient
import json
import requests_mock

BASE_URL = 'http://localhost:5000/'


class TestCalendarClient(TestCase):

    def setUp(self) -> None:
        self.calendar_client = CalendarClient(BASE_URL)

    @requests_mock.mock()
    def test_must_return_ok_response_for_valid_year(self, mock_request):
        year = 2021
        RESPONSE = [
            {"date": "2021-10-12", "name": "Nossa Senhora Aparecida", "type": "national"},
            {"date": "2021-12-25", "name": "Natal", "type": "national"}
        ]

        mock_request.get(url=f'{BASE_URL}{year}', text=json.dumps(RESPONSE), status_code=200)
        response = self.calendar_client.list(2021)
        self.assertEqual(response, RESPONSE, '200 - Ok response not obtained')

    @requests_mock.mock()
    def test_must_return_error_response_for_invalid_year(self, mock_request):
        year = 0
        RESPONSE = {
            "message": "Ano fora do intervalo suportado entre 1900 e 2199.",
            "type": "feriados_range_error",
            "name": "NotFoundError"
        }

        mock_request.get(url=f'{BASE_URL}{year}', text=json.dumps(RESPONSE), status_code=404)
        response = self.calendar_client.list(year)
        self.assertEqual(response, RESPONSE, '404 - Not Found response not obtained')
