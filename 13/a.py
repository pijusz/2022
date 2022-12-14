import functools
from typing import Literal


def compare_int(a: int, b: int) -> None | bool:
    if a == b:
        return None
    elif a > b:
        return False
    return True


def SHIT_comparer(left: list, right: list) -> bool | None:
    for i in range(max([len(left), len(right)])):
        if i == len(right):
            return False
        if i == len(left):
            return True
        a = left[i]
        b = right[i]
        if isinstance(a, int) and isinstance(b, int):
            cmp = compare_int(a, b)
            if isinstance(cmp, bool):
                return cmp
        if isinstance(a, int) and isinstance(b, list):
            return SHIT_comparer([a], b)
        if isinstance(a, list) and isinstance(b, int):
            return SHIT_comparer(a, [b])
        if isinstance(a, list) and isinstance(b, list):
            res = SHIT_comparer(a, b)
            if isinstance(res, bool):
                return res


def compare(left: list, right: list) -> Literal[1, 0, -1]:
    if isinstance(left, int) and isinstance(right, int):
        return -1 if left < right else 1 if left > right else 0
    elif isinstance(left, list) and isinstance(right, list):
        min_len = min(len(left), len(right))
        for i in range(min_len):
            cmp = compare(left[i], right[i])
            if cmp != 0:
                return cmp
        return -1 if len(left) < len(right) else 1 if len(left) > len(right) else 0
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    else:
        raise ValueError(f"Cannot compare: {left} and {right}")


with open("./13/input.txt", "r") as f:
    content = f.read().splitlines()

data = []

for tup in range(0, len(content), 3):
    data.append((eval(content[tup]), eval(content[tup + 1])))

answers = []

for i, value in enumerate(data):
    res = compare(value[0], value[1])
    if res <= 0:
        answers.append(i + 1)

# TTFTFTFF
print("Answer #1: ", sum(answers))

part_2_1 = [[2]]
part_2_2 = [[6]]

# unwrap tuples
data = [item for sublist in data for item in sublist]
data.append(part_2_1)
data.append(part_2_2)

# sort with compare function
s = sorted(data, key=functools.cmp_to_key(compare))


answer_2 = 1
for i, value in enumerate(s):
    if str(value) == str(part_2_1):
        answer_2 *= i + 1
    if str(value) == str(part_2_2):
        answer_2 *= i + 1


print("Answer #1: ", answer_2)
