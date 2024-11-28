import orjson

from .WriteResources import WriteResources


class WriteOrJsonFile(WriteResources):
    def write(self, file, data):
        with open(file, 'wb') as json_file:
            json_file.write(orjson.dumps(data))