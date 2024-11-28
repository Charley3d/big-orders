from Instructions.InstructionsAgent import InstructionsAgent
from Resources import WriteAgent, WriteOrJsonFile, WriteJsonFile
from Statistics import Statistics
from .OrdersOuput import OrdersOuput
import constants


class OrdersInput:
    def __init__(self):
        self._instructions_agent = InstructionsAgent()
        self._orders_output = OrdersOuput()
        self._write_agent = WriteAgent()
        self._write_agent.register_file_lib(WriteOrJsonFile())
        self._statistics = Statistics()

    def process(self, json_data):
        if not json_data: return

        self._statistics.execution_start()
        total = 0
        for order in json_data:
            self._statistics.increment_orders_total()
            if not self.is_valid_order(order):
                self._statistics.increment_invalid_orders_total()
                continue

            self._statistics.increment_valid_orders_total()
            previous_operation = None
            optimized_instructions = []

            for instruction in order[constants.INSTRUCTIONS_ATTR]:
                if len(optimized_instructions) > 0 and previous_operation == instruction[constants.ACTION_ATTR]:
                    optimized_instructions[-1][previous_operation].append(instruction[constants.VALUE_ATTR])
                    self._statistics.increment_optimization_operations()
                else:
                    optimized_instruction = {instruction[constants.ACTION_ATTR]: [instruction[constants.VALUE_ATTR]]}
                    optimized_instructions.append(optimized_instruction)

                previous_operation = instruction[constants.ACTION_ATTR]

            total = self.execute_instructions(optimized_instructions, total)
            self._orders_output.append(order[constants.ORDER_ID_ATTR], total)
            total = 0

        output = self._orders_output.get_output()
        self._statistics.execution_end("Execution time w/o IO: ")
        self._statistics.print_orders_total()
        self._statistics.print_operations_total()
        self._write_agent.write("./results_output.json", output)

        return total

    def execute_instructions(self, optimized_instructions, total) -> float:
        for instruction in optimized_instructions:
            for operation, values in instruction.items():
                instruction = self._instructions_agent.get_instruction(operation)
                total = instruction.operation(total, values)
        return total

    def is_valid_order(self, order) -> bool:
        if constants.ORDER_ID_ATTR not in order or constants.INSTRUCTIONS_ATTR not in order:
            return False

        return True
