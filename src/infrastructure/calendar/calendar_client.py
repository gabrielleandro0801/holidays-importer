import requests
from typing import List, Any
from src.infrastructure.logger.log import logger


REQUEST_SECONDS_TIMEOUT = 5


class CalendarClient:

    def __init__(self, url: str):
        self._url: str = url

    def list(self, year: int) -> List[dict]:
        complete_url: str = f"{self._url}{year}"
        logger.info({"event": "list", "detail": "Getting holidays from API", "url": complete_url})

        response = requests.get(url=complete_url, timeout=REQUEST_SECONDS_TIMEOUT)
        return response.json()


def create_calendar_client() -> Any:
    return lambda: CalendarClient(
        url='https://brasilapi.com.br/api/feriados/v1/'
    )
