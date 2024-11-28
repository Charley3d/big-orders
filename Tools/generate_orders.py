import json
import random

import constants

def generate_orders(num_orders, output_file):
    actions = ["add", "multiply"]
    orders = []

    for order_id in range(1, num_orders + 1):
        num_instructions = random.randint(1, 10)  # Each order will have between 1 and 10 instructions
        instructions = []

        for _ in range(num_instructions):
            action = random.choice(actions)
            value = random.randint(1, 10)  # Random value between 1 and 100 for the action
            instructions.append({constants.ACTION_ATTR: action, constants.VALUE_ATTR: value})

        orders.append({constants.ORDER_ID_ATTR: order_id, constants.INSTRUCTIONS_ATTR: instructions})

    with open(output_file, "w") as file:
        json.dump(orders, file, indent=4)

    print(f"Generated {num_orders} orders and saved to {output_file}")

# Generate 100,000 orders and save them to a file
generate_orders(100000, "../Assets/orders.json")