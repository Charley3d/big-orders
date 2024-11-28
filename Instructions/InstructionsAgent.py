from typing import Dict

from .Instruction import Instruction


class InstructionsAgent:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.instructions: Dict[str, Instruction] = {}
        return cls._instance


    def register_instruction(self, instruction_name: str, instruction: Instruction):
        self._instance.instructions[instruction_name.lower()] = instruction

    def get_instruction(self, instruction_name: str) -> Instruction:
        return self._instance.instructions.get(instruction_name.lower())

    def get_instructions(self) -> Dict[str, Instruction]:
        return self._instance.instructions