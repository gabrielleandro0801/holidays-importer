from abc import abstractmethod, ABC
from typing import List

from src.domain import Holiday


class HolidayRepository(ABC):

    @abstractmethod
    def save(self, holidays: List[Holiday]) -> None:
        pass
