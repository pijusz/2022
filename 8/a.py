import numpy as np


with open("./8/input.txt") as f:
    # read the numbers into 2d list
    data = [[int(x) for x in line.strip()] for line in f.readlines()]


def get_column(data: list[list[int]], col: int) -> list[int]:
    return [row[col] for row in data]


def get_row(data: list[list[int]], row: int) -> list[int]:
    return data[row]


def get_left_of_cell(data: list[list[int]], row: int, col: int) -> list[int]:
    if col == 0:
        return []
    else:
        return get_row(data, row)[:col]


def get_right_of_cell(data: list[list[int]], row: int, col: int) -> list[int]:
    if col == len(data[0]) - 1:
        return []
    else:
        return get_row(data, row)[col + 1 :]


def get_top_of_cell(data: list[list[int]], row: int, col: int) -> list[int]:
    if row == 0:
        return []
    else:
        return get_column(data, col)[:row]


def get_bottom_of_cell(data: list[list[int]], row: int, col: int) -> list[int]:
    if row == len(data) - 1:
        return []
    else:
        return get_column(data, col)[row + 1 :]


def get_scene_row_score(data: list[int], cell: int, is_reverse: bool = False) -> int:
    score = 0
    if len(data) == 0:
        return score
    if is_reverse:
        # reverse iterate through the list
        for idx in range(len(data) - 1, -1, -1):
            if data[idx] >= cell:
                return score + 1
            score += 1
    else:
        for idx in range(len(data)):
            if data[idx] >= cell:
                return score + 1
            score += 1
    return score


def is_invisible(
    cell: int, left: list[int], right: list[int], top: list[int], bottom: list[int]
) -> bool:
    # can't max on empty array
    if len(left) == 0 or len(right) == 0 or len(top) == 0 or len(bottom) == 0:
        return False
    elif (
        max(left) >= cell
        and max(right) >= cell
        and max(top) >= cell
        and max(bottom) >= cell
    ):
        return True
    return False


invisible = 0

# could have enumeration where it stops when finding just equal or higher, rather than doing max
for row_i, row in enumerate(data):
    for col_i, cell in enumerate(row):
        left = get_left_of_cell(data, row_i, col_i)
        right = get_right_of_cell(data, row_i, col_i)
        top = get_top_of_cell(data, row_i, col_i)
        bottom = get_bottom_of_cell(data, row_i, col_i)
        if is_invisible(cell, left, right, top, bottom):
            invisible += 1

cells = len(data) * len(data[0])

print("Answer #1:", cells - invisible)

scene_scores = np.zeros(shape=(len(data), len(data[0])), dtype=np.int32)

for row_i, row in enumerate(data):
    for col_i, cell in enumerate(row):
        top = get_top_of_cell(data, row_i, col_i)
        left = get_left_of_cell(data, row_i, col_i)
        right = get_right_of_cell(data, row_i, col_i)
        bottom = get_bottom_of_cell(data, row_i, col_i)
        top_score = get_scene_row_score(top, cell, True)
        left_score = get_scene_row_score(left, cell, True)
        right_score = get_scene_row_score(right, cell, False)
        bottom_score = get_scene_row_score(bottom, cell, False)
        scene_scores[row_i, col_i] = left_score * right_score * top_score * bottom_score

print("Answer #2:", np.max(scene_scores))
