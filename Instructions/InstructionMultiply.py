from functools import reduce
from typing import List

from .Instruction import Instruction


class InstructionMultiply(Instruction):
    def operation(self, total: float, value: List[float]) -> float:
        return total * reduce(lambda x,y: x*y, value)