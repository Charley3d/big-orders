import json

from .WriteResources import WriteResources


class WriteJsonFile(WriteResources):
    def write(self, file, data):
        with open(file, 'w') as json_file:
            json.dump(data, json_file, indent=4)