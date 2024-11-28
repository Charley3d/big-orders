import os

import constants
from Path import Path


class PathDefault(Path):
    current_path = os.getcwd()
    script_dir = os.path.dirname(os.path.abspath(__file__))

    def get_path(self, filename: str) -> str:
        parent_dir = os.path.join(self.script_dir, os.pardir)
        full_path = os.path.abspath(os.path.join(parent_dir, filename))

        return full_path

    def get_orders_file(self) -> str:
        return self.get_path(constants.ORDERS_FILENAME)