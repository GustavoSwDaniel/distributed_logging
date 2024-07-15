from abc import ABC, abstractmethod
from typing import List

class IGetLogsUseCase(ABC):

    abstractmethod
    def execute(self, limit: int, offset: int) -> List: pass