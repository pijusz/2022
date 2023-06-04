def calc(op: str, a: int, b: int) -> int:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a // b
    return 0


def find_int(data: dict[str, int | tuple[str, str, str]], s: str) -> int:  # type: ignore
    if isinstance(data[s], int):
        return data[s]  # type: ignore
    if isinstance(data[s], tuple):
        return calc(data[s][1], find_int(data[s][0]), find_int(data[s][2]))  # type: ignore


def parse_data() -> dict[str, int | tuple[str, str, str]]:
    with open("./21/input.txt") as f:
        content = f.readlines()

    data: dict[str, int | tuple[str, str, str]] = {}

    for line in content:
        l = line.strip().split(": ")
        if l[1].isnumeric():
            data[l[0]] = int(l[1])
        else:
            data[l[0]] = tuple(l[1].split(" "))
    return data


print("Answer #1 ", find_int(parse_data(), "root"))
