import re
import numpy as np


def print_t(m):
    for x, row in enumerate(m):
        for y, col in enumerate(row):
            if x == cur_loc[0] and y == cur_loc[1]:
                print("X", end="")
            elif col == 0:
                print(" ", end="")
            elif col == 1:
                print("#", end="")
            elif col == 2:
                print(">", end="")
            elif col == 3:
                print("^", end="")
            elif col == 4:
                print("<", end="")
            elif col == 5:
                print("v", end="")
            elif col == 6:
                print(".", end="")
        print()


def check(loc: tuple[int, int], shape: tuple[int, int], m: np.ndarray) -> bool:
    if loc[0] < 0 or loc[1] < 0 or loc[0] >= shape[0] or loc[1] >= shape[1]:
        return False
    if m[loc] == 0:
        return False
    return True


def get_tile(
    m: np.ndarray, cur_loc: tuple[int, int], direction: str
) -> tuple[int, int]:
    shape = m.shape
    current = cur_loc
    loc: tuple[int, int] = (0, 0)
    if direction == "R":
        # m[loc] = 2
        loc = (current[0], current[1] + 1)
        if not check(loc, shape, m):
            # get first non zero in row
            wall = np.where(m[loc[0]] == 1)[0][0]
            loc = (loc[0], np.where(m[loc[0]] > 1)[0][0])
            if loc[1] < wall:
                m[cur_loc] = 2
                cur_loc = loc
        elif m[loc] > 1:
            m[cur_loc] = 2
            cur_loc = loc
    elif direction == "U":
        # m[loc] = 3
        loc = (cur_loc[0] - 1, cur_loc[1])
        if not check(loc, shape, m):
            # get last non zero in y axis
            wall = np.where(m[:, loc[1]] == 1)[0][-1]
            loc = (
                np.where(m[:, loc[1]] > 1)[0][-1],
                loc[1],
            )
            if loc[0] > wall:
                m[cur_loc] = 3
                cur_loc = loc
        elif m[loc] > 1:
            m[cur_loc] = 3
            cur_loc = loc
    elif direction == "L":
        # m[loc] = 4
        loc = (cur_loc[0], cur_loc[1] - 1)
        if not check(loc, shape, m):
            # get last non zero in row
            wall = np.where(m[loc[0]] == 1)[0][-1]
            loc = (loc[0], np.where(m[loc[0]] > 1)[0][-1])
            if loc[1] > wall:
                m[cur_loc] = 4
                cur_loc = loc
        elif m[loc] > 1:
            m[cur_loc] = 4
            cur_loc = loc
    elif direction == "D":
        # m[loc] = 5
        loc = (cur_loc[0] + 1, cur_loc[1])
        if not check(loc, shape, m):
            # get last non zero in y axis
            wall = np.where(m[:, loc[1]] == 1)[0][0]
            loc = (
                np.where(m[:, loc[1]] > 1)[0][0],
                loc[1],
            )
            if loc[0] < wall:
                m[cur_loc] = 5
                cur_loc = loc
        elif m[loc] > 1:
            m[cur_loc] = 5
            cur_loc = loc
    return cur_loc


def get_dir(direction: str, move: str | int) -> str:
    if isinstance(move, int):
        return direction
    if move == "L":
        if direction == "R":
            return "U"
        elif direction == "U":
            return "L"
        elif direction == "L":
            return "D"
        elif direction == "D":
            return "R"
    elif move == "R":
        if direction == "R":
            return "D"
        elif direction == "U":
            return "R"
        elif direction == "L":
            return "U"
        elif direction == "D":
            return "L"
    return direction


def parse_moves(content_moves: str) -> list[str or int]:
    moves = []
    for x in re.findall(r"(\d+|L|R)", content_moves):
        if x.isdigit():
            moves.append(int(x))
        else:
            moves.append(x)
    return moves


def parse_map(content_map: str):
    lines = content_map.split("\n")
    width = max([len(line) for line in lines])
    m = np.zeros((len(lines), width), dtype=int)
    for l_i, line in enumerate(content_map.split("\n")):
        for c_i, char in enumerate(line):
            if char == "#":
                m[l_i, c_i] = 1
            if char == ".":
                m[l_i, c_i] = 6
    return m


with open("./22/input.txt", "r") as f:
    content = f.read()

content_map, content_moves = content.split("\n\n")
moves = parse_moves(content_moves)
m = parse_map(content_map)


direction = "R"
cur_loc = (0, 51)
# cur_loc = (0, 8)
for move in moves:
    if isinstance(move, str):
        direction = get_dir(direction, move)
        continue
    for _ in range(move):
        cur_loc = get_tile(m, cur_loc, direction)

print((cur_loc[0] + 1) * 1000 + (cur_loc[1] + 1) * 4, direction)
