import numpy as np
from math import lcm


def is_divisible(a: int, b: int) -> bool:
    if b % 2 == 0:
        return str(a)[-1] % 2 == 0
    return a % b == 0


def operation(a: int, b: int, op: str) -> int:
    if b == -1:
        if op == "+":
            return a + a
        if op == "*":
            return a * a
    if op == "+":
        return a + b
    if op == "*":
        return a * b
    return 0


with open("./11/input.txt") as f:
    content = f.readlines()

monkeys = []
BOREDOM_DROP = 3
ROUNDS = 10000

for i in range(0, len(content), 7):
    monkey = {
        "items": [],
        "operation": {
            "type": None,  # sum or multiply "+", "*"
            "value": None,
        },
        "divider": None,
        "if_true_target": None,
        "if_false_target": None,
        "inspected": 0,
    }
    # item parse
    items_str = content[i + 1].split(":")[1].strip().split(",")
    for item in items_str:
        monkey["items"].append(int(item))
    # operation parse
    if "+" in content[i + 2].strip():
        monkey["operation"]["type"] = "+"
    if "*" in content[i + 2].strip():
        monkey["operation"]["type"] = "*"
    value = content[i + 2].split(" ")[-1]
    if "old" in value:
        monkey["operation"]["value"] = -1
    else:
        monkey["operation"]["value"] = int(value)
    monkey["divider"] = int(content[i + 3].strip().split(" ")[-1])
    monkey["if_true_target"] = int(content[i + 4].strip().split(" ")[-1])
    monkey["if_false_target"] = int(content[i + 5].strip().split(" ")[-1])

    monkeys.append(monkey)

dividers = [monkey["divider"] for monkey in monkeys]
base = lcm(*dividers)


for round in range(ROUNDS):
    for monkey in monkeys:
        while len(monkey["items"]) > 0:
            monkey_item = monkey["items"].pop(0)
            new_worry = operation(
                monkey_item,
                monkey["operation"]["value"],
                monkey["operation"]["type"],
            )
            # Part 1
            # new_worry = new_worry // BOREDOM_DROP
            # Part 2
            new_worry = new_worry % base
            if new_worry % monkey["divider"] == 0:
                monkeys[monkey["if_true_target"]]["items"].append(new_worry)
            else:
                monkeys[monkey["if_false_target"]]["items"].append(new_worry)
            monkey["inspected"] += 1

inspects = [monkey["inspected"] for monkey in monkeys]
inspects.sort(reverse=True)
print("Answer ", inspects[0] * inspects[1])
