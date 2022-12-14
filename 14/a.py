import numpy as np

SAND_START = (500, 0)
SANDBOX_SIZE = (1000, 1000)


def parse(lines: list[str]) -> list[list[tuple[int, int]]]:
    rocks = []
    i = 0
    for line in lines:
        rocks.append([])
        coord_str = line.strip().split(" -> ")
        coord = [int(x) for x in coord_str[0].split(",")]
        for coord in coord_str:
            x, y = [int(x) for x in coord.split(",")]
            rocks[i].append((int(x), int(y)))
        i += 1
    return rocks


def draw_rock(cave: np.ndarray, rocks: list[tuple[int, int]]):
    for i in range(len(rocks) - 1):
        rock_start = rocks[i]
        rock_end = rocks[i + 1]
        if rock_start[0] == rock_end[0]:
            for y in range(
                min(rock_start[1], rock_end[1]), max(rock_start[1], rock_end[1]) + 1
            ):
                cave[rock_start[0], y] = 1
        if rock_start[1] == rock_end[1]:
            for x in range(
                min(rock_start[0], rock_end[0]), max(rock_start[0], rock_end[0]) + 1
            ):
                cave[x, rock_start[1]] = 1


def get_min_max_cave(cave: np.ndarray) -> tuple[int, int, int, int]:
    min_x = min_y = 1001
    max_x = max_y = -1
    for x in range(cave.shape[0]):
        for y in range(cave.shape[1]):
            if cave[x, y] != 0:
                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x
                if y < min_y:
                    min_y = y
                if y > max_y:
                    max_y = y
    return min_x, max_x, 0, max_y


def is_out_of_bounds(arr_shape: tuple[int, int, int, int], x: int, y: int) -> bool:
    return x < arr_shape[0] or x > arr_shape[1] or y < arr_shape[2] or y > arr_shape[3]


def emulate_sandgrain(
    cave: np.ndarray, start: tuple[int, int], min_max: tuple[int, int, int, int]
) -> bool:
    if cave[start[0], start[1]] == 2:
        return False
    x, y = start
    cave[x, y] = 2
    while True:
        if is_out_of_bounds(min_max, x, y):
            cave[x, y] = 0
            return False
        if cave[x, y + 1] == 0:
            cave[x, y] = 0
            cave[x, y + 1] = 2
            y += 1
        elif cave[x - 1, y + 1] == 0:
            cave[x, y] = 0
            cave[x - 1, y + 1] = 2
            x -= 1
            y += 1
        elif cave[x + 1, y + 1] == 0:
            cave[x, y] = 0
            cave[x + 1, y + 1] = 2
            x += 1
            y += 1
        else:
            return True


def emulate_sandfall(cave: np.ndarray, start: tuple[int, int]) -> int:
    sand = 0
    min_max = get_min_max_cave(cave)
    while emulate_sandgrain(cave, start, min_max):
        sand += 1
    return sand


with open("./14/input.txt", "r") as f:
    lines = f.readlines()

rocks: list[list[tuple[int, int]]] = parse(lines)

# 0 - empty, 1 - rock, 2 - sand
cave = np.zeros(SANDBOX_SIZE, dtype=int)

for rock_line in rocks:
    draw_rock(cave, rock_line)

answer_1 = emulate_sandfall(cave, SAND_START)
print("Answer #1 ", answer_1)

# Part 2
min_max = get_min_max_cave(cave)
inf_line = [(0, min_max[3] + 2), (SANDBOX_SIZE[0] - 1, min_max[3] + 2)]
draw_rock(cave, inf_line)

answer_2 = emulate_sandfall(cave, SAND_START)
print("Answer #2 ", answer_1 + answer_2)
