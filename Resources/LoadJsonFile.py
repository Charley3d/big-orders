import json
from typing import Dict

from .LoadResources import LoadResources


class LoadJsonFile(LoadResources):
    def load(self, filepath) -> Dict:
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data
