import requests
from typing import List
from v1.infrastructure.logger.log import logger


class CalendarClient:

    def __init__(self, url: str, token: str):
        self._url: str = url
        self._token: str = token

    def list(self, params: dict) -> List[dict]:
        params["token"] = self._token
        logger.info({"event": "list", "detail": "Getting holidays from API", "url": self._url, "params": params})

        response = requests.get(url=self._url, params=params)
        return response.json()
