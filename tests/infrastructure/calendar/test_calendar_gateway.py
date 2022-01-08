from unittest import TestCase, mock
from src.infrastructure.calendar.calendar_gateway import CalendarGateway


class TestCalendarGateway(TestCase):

    def setUp(self) -> None:
        self.calendar_client = mock.Mock()
        self.translator = mock.Mock()
        self.calendar_gateway = CalendarGateway(self.calendar_client, self.translator)

    def test_calendar_client_must_have_been_called_with_right_year(self):
        year = 2021
        self.calendar_client.list.return_value = []

        self.calendar_gateway.list(year)
        self.calendar_client.list.assert_called_with(year=year)

    def test_translator_must_have_been_called_any_time(self):
        year = 2021

        client_response = [
            {
                "date": "2021-10-12",
                "name": "Nossa Senhora Aparecida",
                "type": "national"
            }
        ]
        self.calendar_client.list.return_value = client_response

        self.calendar_gateway.list(year)
        self.translator.translate.assert_called()
