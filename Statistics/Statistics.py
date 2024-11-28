import time


class Statistics:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.optimization_operations = 0
        self.orders_total = 0
        self.valid_orders_total = 0
        self.invalid_orders_total = 0

    def execution_start(self):
        self.start_time = time.time()
        pass

    def execution_end(self, message: str = "Execution time: "):
        self.end_time = time.time()
        print(f"{message}{self.get_execution_time():.4f} seconds")

    def get_execution_time(self):
        return self.end_time - self.start_time

    def increment_optimization_operations(self):
        self.optimization_operations += 1

    def increment_orders_total(self):
        self.orders_total += 1

    def increment_valid_orders_total(self):
        self.valid_orders_total += 1

    def increment_invalid_orders_total(self):
        self.invalid_orders_total += 1

    def print_operations_total(self):
        print(f"Total optimization operations: {self.optimization_operations}")

    def print_orders_total(self):
        print(f"Total orders: {self.orders_total}")
        print(f"Valid orders: {self.valid_orders_total}")
        print(f"Invalid orders: {self.invalid_orders_total}")

