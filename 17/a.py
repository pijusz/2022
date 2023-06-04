import numpy as np

with open("./17/input.txt") as f:
    winds = f.read()

# shapes = {
#     "-": "####",
#     "+": ".#.\n###\n.#.",
#     "J": "..#\n..#\n###",
#     "I": "#\n#\n#\n#",
#     "#": "##\n##",
# }


def next_wind(current: int, winds: str) -> int:
    mx = len(winds)
    if current + 1 < mx:
        return current + 1
    return 0


def next_shape(current: int, shapes: list) -> int:
    mx = len(shapes)
    if current + 1 < mx:
        return current + 1
    return 0


def get_active(matrix: np.ndarray) -> list[tuple[int, int]]:
    active: list[tuple[int, int]] = []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x, y] == 1:
                active.append((x, y))
    return active


def lock_shapes(matrix: np.ndarray, coords: list[tuple[int, int]]):
    for x, y in coords:
        matrix[x, y] = 2


def cleanup_matrix(matrix: np.ndarray) -> int:
    columns = np.zeros(len(matrix[0]), dtype=int)
    for column in columns:
        for x in range(len(matrix) - 1, 0, -1):
            if matrix[x, column] == 2:
                columns[column] = x
    lowest = np.max(columns)
    removed = len(matrix) - lowest
    matrix = np.delete(matrix, np.s_[lowest : len(matrix)], axis=0)
    return removed


def can_down(matrix: np.ndarray, coords: list[tuple[int, int]]) -> bool:
    for x, y in coords:
        if x == len(matrix) - 1:
            return False
        if matrix[x + 1, y] == 2:
            return False
    return True


def can_left(matrix: np.ndarray, coords: list[tuple[int, int]]) -> bool:
    for x, y in coords:
        if y == 0:
            return False
        if matrix[x, y - 1] == 2:
            return False
    return True


def can_right(matrix: np.ndarray, coords: list[tuple[int, int]]) -> bool:
    for x, y in coords:
        if y == len(matrix[0]) - 1:
            return False
        if matrix[x, y + 1] == 2:
            return False
    return True


def move_down(
    matrix: np.ndarray, coords: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    new_coords: list[tuple[int, int]] = []
    for x, y in coords:
        matrix[x, y] = 0
        matrix[x + 1, y] = 1
        new_coords.append((x + 1, y))
    return new_coords


def move_left(
    matrix: np.ndarray, coords: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    new_coords: list[tuple[int, int]] = []
    for x, y in coords:
        matrix[x, y] = 0
        matrix[x, y - 1] = 1
        new_coords.append((x, y - 1))
    return new_coords


def move_right(
    matrix: np.ndarray, coords: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    new_coords: list[tuple[int, int]] = []
    for x, y in coords:
        matrix[x, y] = 0
        matrix[x, y + 1] = 1
        new_coords.append((x, y + 1))
    return new_coords


shapes = [
    np.array([[0, 0, 1, 1, 1, 1, 0]], dtype=np.int0),  # -
    np.array(
        [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0]],
        dtype=np.int0,
    ),  # +
    np.array(
        [[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0]],
        dtype=np.int0,
    ),  # J
    np.array(
        [
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
        ],
        dtype=np.int0,
    ),  # I
    np.array([[0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0]], dtype=np.int0),  # #
]

EMPTY = np.array(
    [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
    dtype=np.int0,
)

APPEAR_FROM_LEFT = 2
APPEAR_FROM_BOTTOM = 3
ROCK_LIMIT = 2022


height = 0

matrix = np.zeros((0, 7), dtype=np.int0)

print(np.vstack([shapes[0], EMPTY, matrix]))

cr_wind = 0
cr_shape = 0
for i in range(ROCK_LIMIT):
    if i % 100 == 0:
        print("ROCK ", i)
    is_moving = True
    matrix = np.vstack([shapes[cr_shape], EMPTY, matrix])
    while is_moving:
        wind = winds[cr_wind]
        if can_down(matrix):
            pass

        cr_wind = next_wind(cr_wind, winds)
    cr_shape = next_shape(cr_shape, shapes)
    # possible optimization is matrix cleanup from bottom
