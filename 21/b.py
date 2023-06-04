import sympy


def operation(op: str, a, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b
    return 0


def solve(lines):
    monkeys: dict = {"humn": sympy.Symbol("x")}
    for a in lines:
        name, expr = a.split(": ")
        if name in monkeys:
            continue
        if expr.isdigit():
            monkeys[name] = sympy.Integer(expr)
        else:
            left, op, right = expr.split()
            if left in monkeys and right in monkeys:
                if name == "root":
                    print("Answer #2 ", sympy.solve(monkeys[left] - monkeys[right]))
                    break
                monkeys[name] = operation(op, monkeys[left], monkeys[right])
            else:
                lines.append(a)
    return monkeys["humn"]


lines = []
with open("./21/input.txt") as f:
    for line in f.readlines():
        lines.append(line.strip())

solve(lines)
