from abc import ABC, abstractmethod
from typing import List

from src.domain import Holiday


class HolidayService(ABC):

    @abstractmethod
    def list_febraban_holidays(self, year: int) -> List[Holiday]:
        pass
