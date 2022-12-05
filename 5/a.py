def get_input() -> tuple[list[list[str]], list[tuple[int, int, int]]]:
    cargo_str: list[str] = []
    moves: list[tuple[int, int, int]] = []
    is_moves = False
    with open("./5/input.txt", "r") as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0 and is_moves:
                break
            if len(line) == 0:
                is_moves = True
                continue
            if is_moves:
                moves.append(get_move(line))
            else:
                cargo_str.append(line)
        cargo = get_cargo(cargo_str)
    return cargo, moves


def get_move(line: str) -> tuple[int, int, int]:
    parts = line.split(" ")
    return int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1


def get_cargo(lines: list[str]) -> list[list[str]]:
    cargo_list: list[list[str]] = [[] for i in range((len(lines[0]) + 1) // 4)]
    lines.reverse()
    lines = lines[1:]
    for line_i in range(len(lines)):
        cargo_stack = 0
        for i in range(0, len(lines[line_i]) + 1, 4):
            if lines[line_i][i + 1].isupper():
                cargo_list[cargo_stack].append(lines[line_i][i + 1])
            cargo_stack += 1
    return cargo_list


cargo, moves = get_input()
# answer 1
for move in moves:
    for i in range(move[0]):
        cargo[move[2]].append(cargo[move[1]].pop())

answer_1 = "".join(c[-1] for c in cargo)
print("Answer #1 ", answer_1)

cargo, moves = get_input()
# answer 2
for move in moves:
    cargo[move[2]] += cargo[move[1]][-move[0] :]
    cargo[move[1]] = cargo[move[1]][: -move[0]]

answer_2 = "".join(c[-1] for c in cargo)
print("Answer #2 ", answer_2)
