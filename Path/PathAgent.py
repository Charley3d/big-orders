from .Path import Path
from .PathDefault import PathDefault

class PathAgent:
    def __init__(self):
        self.lib: Path = PathDefault()

    def register_lib(self, lib: Path):
        self.lib = lib

    def get_orders_file(self) -> str:
        return self.lib.get_orders_file()