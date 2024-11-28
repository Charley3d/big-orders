from Instructions import InstructionsAgent, InstructionAdd, InstructionMultiply
from Orders import OrdersInput
from Resources import LoadJsonFile, LoadAgent, LoadOrJsonFile
from Path import PathAgent, PathDefault
from Statistics import Statistics


def register_instructions():
    instructions_agent = InstructionsAgent()

    instructions_agent.register_instruction("add", InstructionAdd())
    instructions_agent.register_instruction("multiply", InstructionMultiply())

def get_order_data():
    path_agent = PathAgent()
    load_agent = LoadAgent()

    path_agent.register_lib(PathDefault())
    load_agent.register_file_lib(LoadOrJsonFile())

    data = load_agent.load(path_agent.get_orders_file())

    return data


if __name__ == "__main__":
    statistics = Statistics()
    statistics.execution_start()

    register_instructions()

    order_data = get_order_data()
    orders_input = OrdersInput()

    orders_input.process(order_data)

    statistics.execution_end("Total Execution time: ")
