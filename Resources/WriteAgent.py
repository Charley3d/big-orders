from typing import Dict

from .WriteJsonFile import WriteJsonFile
from .WriteResources import WriteResources


class WriteAgent:
    def __init__(self):
        self.writer: WriteResources = WriteJsonFile()

    def register_file_lib(self, writer: WriteResources):
        self.writer = writer

    def write(self, filepath, output: Dict):
        return self.writer.write(filepath, output)
