from abc import ABC, abstractmethod


class WriteResources(ABC):
    @abstractmethod
    def write(self, file, data):
        pass