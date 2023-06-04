import numpy as np
from math import sqrt


def parse(
    content: list[str],
) -> tuple[
    list[tuple[tuple[int, int], tuple[int, int]]],
    set[tuple[int, int]],
    set[tuple[int, int]],
]:
    data: list[tuple[tuple[int, int], tuple[int, int]]] = []
    sensors: set[tuple[int, int]] = set()
    beacons: set[tuple[int, int]] = set()

    for line in content:
        l = (
            line.strip()
            .replace("Sensor at x=", "")
            .replace(": closest beacon is at x=", ", ")
            .replace("y=", "")
        )
        s = l.split(", ")
        points: tuple[tuple[int, int], tuple[int, int]] = (
            (int(s[0]), int(s[1])),
            (int(s[2]), int(s[3])),
        )
        sensors.add(points[0])
        beacons.add(points[1])
        data.append(points)
    return data, sensors, beacons


def get_min_max(data: set[tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    # find min and max of coordinates of coordinate array
    x_min: int = 9999999999
    y_min: int = 9999999999
    x_max: int = -9999999999
    y_max: int = -9999999999
    for coords in data:
        if x_min > coords[0]:
            x_min = coords[0]
        if y_min > coords[1]:
            y_min = coords[1]
        if x_max < coords[0]:
            x_max = coords[0]
        if y_max < coords[1]:
            y_max = coords[1]
    return (x_min, y_min), (x_max, y_max)


def m_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def is_inside(a: tuple[int, int], b: tuple[int, int], d: int) -> bool:
    return m_distance(a, b) <= d


def is_between(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    return is_inside(a, b, m_distance(b, c))


def emulate_zone(
    matrix: np.ndarray,
    data: list[tuple[tuple[int, int], tuple[int, int]]],
    sensors: set[tuple[int, int]],
    beacons: set[tuple[int, int]],
    NORM_X: int,
    NORM_Y: int,
):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for sensor, beacon in data:
                if is_between(
                    (x, y),
                    (sensor[0] + NORM_X, sensor[1] + NORM_Y),
                    (beacon[0] + NORM_X, beacon[1] + NORM_Y),
                ):
                    matrix[x, y] = 1
                matrix[sensor[0] + NORM_X, sensor[1] + NORM_Y] = 2
                matrix[beacon[0] + NORM_X, beacon[1] + NORM_Y] = 3


def emulate_line(
    y: int, data: list[tuple[tuple[int, int], tuple[int, int]]], min_x: int, max_x: int
):
    num = 0
    pos = np.zeros(abs(min_x - max_x) + 1, dtype=int)
    for x in range(len(pos)):
        for sensor, beacon in data:
            if pos[x] != 0:
                break
            if y == sensor[1] and (x - NORM_X) == sensor[0]:
                pos[x] = 2
            elif y == beacon[1] and (x - NORM_X) == beacon[0]:
                pos[x] = 3
            elif is_between(
                (x - NORM_X, y),
                (sensor[0], sensor[1]),
                (beacon[0], beacon[1]),
            ):
                pos[x] = 1
                num += 1
    return num


# CHECK_Y = 10
CHECK_Y = 2000000

with open("./15/input.txt") as f:
    content = f.readlines()

data, sensors, beacons = parse(content)
points: set[tuple[int, int]] = set()
points = points.union(sensors)
points = points.union(beacons)
coord_min, coord_max = get_min_max(points)
NORM_X = coord_min[0] * -1
NORM_Y = coord_min[1] * -1

# matrix = np.zeros((coord_max[0] + NORM_X + 1, coord_max[1] + NORM_Y + 1), dtype=int)

# emulate_zone(matrix, data, sensors, beacons, NORM_X, NORM_Y)
print("Answer #1 ", emulate_line(CHECK_Y, data, coord_min[0], coord_max[0]))


# matrix_T = matrix.T

# for y in range(len(matrix_T)):
#     for x in range(len(matrix_T[0])):
#         if matrix_T[y, x] == 0:
#             print(".", end="")
#         if matrix_T[y, x] == 2:
#             print("S", end="")
#         if matrix_T[y, x] == 3:
#             print("B", end="")
#         if matrix_T[y, x] == 1:
#             print("#", end="")
#     print("")

# print("Answer #1: ", (matrix_T[CHECK_Y + NORM_Y] == 1).sum())
