# Big Orders

## **Context**
You are working for a company that manages a real-time customer order processing system. Your task is to develop a microservice that analyzes and optimizes these orders to reduce processing costs.

---

## **Exercise: Order Management System**

### **Description**
A customer order contains multiple instructions. Each instruction corresponds to an action performed on a shared total. Your task is to create a program that can:

1. Read a batch of orders from a JSON file.
2. Process the instructions in the order they appear, while optimizing repetitive actions.
3. Output the results of the processed orders along with performance statistics (e.g., total execution time, number of instructions optimized).

---

### **Input:**
A JSON file containing a list of orders with the following structure:

```json
[
  {
    "order_id": 1,
    "instructions": [
      {"action": "add", "value": 5},
      {"action": "multiply", "value": 3},
      {"action": "add", "value": 5}
    ]
  },
  {
    "order_id": 2,
    "instructions": [
      {"action": "multiply", "value": 2},
      {"action": "add", "value": 10}
    ]
  }
]
```

Each instruction consists of:
- **Action:** The operation to perform (`add` or `multiply`).
- **Value:** The value associated with the action.

All orders share a common total initialized at `0`.

---

### **Output:**
Your program should output:

1. A list of results for each order, showing the final total after all instructions are applied.
2. Global performance statistics, including:
   - Total execution time.
   - Number of instructions executed.
   - Number of optimizations applied (e.g., merging similar operations).

---

### **Example Output:**

#### **Input:**
```json
[
  {
    "order_id": 1,
    "instructions": [
      {"action": "add", "value": 5},
      {"action": "multiply", "value": 3},
      {"action": "add", "value": 5}
    ]
  }
]
```

#### **Output:**
```json
{
  "results": [
    {
      "order_id": 1,
      "final_total": 30
    }
  ]
}
```

Statistics should be visible in console.

---

### **Constraints:**
1. You may use **JavaScript**, **C#**, or **Python**.
2. The program must handle a file containing up to **100,000 orders** efficiently.
3. Include **unit tests** to validate your solution.

---

## **Evaluation Criteria:**

1. **Efficiency:**
   - The program should process large datasets quickly.

2. **Readability:**
   - Your code should be clean, well-documented, and follow best practices.

3. **Modularity:**
   - The code should be structured to allow future extensions (e.g., adding new actions).

4. **Robustness:**
   - Handle edge cases (e.g., empty orders, invalid instructions).

5. **Testing:**
   - Provide comprehensive unit tests covering standard and edge cases.

---
