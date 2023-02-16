from typing import List

import requests

from src.infrastructure import logger

REQUEST_TIMEOUT_IN_SECONDS = 5


class CalendarClient:

    def __init__(self, url: str):
        self._url: str = url

    def list(self, year: int) -> List[dict]:
        complete_url: str = f"{self._url}{year}"
        logger.info({"event": "list", "detail": "Getting holidays from API", "url": complete_url})

        response = requests.get(url=complete_url, timeout=REQUEST_TIMEOUT_IN_SECONDS)
        return response.json()
