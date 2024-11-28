from typing import Dict

class OrdersOuput:
    def __init__(self):
        self._output = {"results": []}

    def append(self, order_id, total)-> Dict:
        self._output["results"].append({"order_id": order_id, "final_total": total})
        return self._output

    def get_output(self) -> Dict:
        return self._output
