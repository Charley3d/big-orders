from abc import ABC, abstractmethod
from typing import List

class Instruction(ABC):
    @abstractmethod
    def operation(self, total: float, value: List[float]) -> float:
        pass