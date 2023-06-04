import numpy as np
from collections import deque


def minMax(data: list[tuple[int, int, int]]) -> tuple[int, int]:
    mn = data[0][0]
    mx = data[0][0]
    for i in data:
        mn = min(mn, i[0], i[1], i[2])
        mx = max(mx, i[0], i[1], i[2])
    return (mn, mx)


with open("./18/input.txt") as f:
    data = [tuple(map(int, line.split(","))) for line in f.splitlines()]  # type: ignore

mn, mx = minMax(data)

matrix = np.zeros((mx + 1, mx + 1, mx + 1), dtype=int)

sides = 0

for cube in data:
    matrix[cube] = 1


def neighbours(c: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    n = []
    # check up and down
    for i in [-1, 1]:
        n.append((c[0], c[1] + i, c[2]))
        n.append((c[0], c[1], c[2] + i))
        n.append((c[0] + i, c[1], c[2]))
    return n


def countNeighbours(c: tuple[int, int, int]) -> int:
    count = 0
    ns = neighbours(c)
    for n in ns:
        try:
            if matrix[n] == 1:
                count += 1
        except:
            pass
    return 6 - count


for cube in data:
    sides = sides + countNeighbours(cube)

print(sides)
