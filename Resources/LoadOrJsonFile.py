from typing import Dict

import orjson

from .LoadResources import LoadResources


class LoadOrJsonFile(LoadResources):
    def load(self, filepath) -> Dict:
        with open(filepath, 'rb') as file:
            data = orjson.loads(file.read())
        return data