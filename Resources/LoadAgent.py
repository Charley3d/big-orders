from typing import Dict

from .LoadJsonFile import LoadJsonFile
from .LoadResources import LoadResources


class LoadAgent:
    def __init__(self):
        self.loader: LoadResources = LoadJsonFile()

    def register_file_lib(self, loader: LoadResources):
        self.loader = loader

    def load(self, filepath) -> Dict:
        return self.loader.load(filepath)
