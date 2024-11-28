from abc import abstractmethod, ABC
from typing import Dict

class LoadResources(ABC):
    @abstractmethod
    def load(self, file) -> Dict:
        pass