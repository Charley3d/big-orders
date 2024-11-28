from abc import ABC, abstractmethod


class Path(ABC):
    @abstractmethod
    def get_path(self, filename: str) -> str:
        pass

    @abstractmethod
    def get_orders_file(self) -> str:
        pass