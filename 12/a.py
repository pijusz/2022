import numpy as np


def can_go(a: int, b: int) -> bool:
    return a >= (b - 1)
    # return a == b or a == (b - 1)


def shortest_distance(
    start: tuple[int, int],
    end: tuple[int, int],
    vertices: dict[tuple[int, int], set[tuple[int, int]]],
) -> int:
    visited: set[tuple[int, int]] = set()
    queue: list[tuple[tuple[int, int], int]] = [(start, 0)]
    while queue:
        vertex, distance = queue.pop(0)
        if vertex == end:
            return distance
        if vertex not in visited:
            visited.add(vertex)
            for neighbour in vertices[vertex]:
                queue.append((neighbour, distance + 1))
    return -1


def get_matrix(data: list[str]) -> tuple[tuple[int, int], tuple[int, int], np.ndarray]:
    startCoords: tuple[int, int] = (-1, -1)
    endCoords: tuple[int, int] = (-1, -1)
    matrix = np.zeros((len(data), len(data[0])), dtype=int)
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "S":
                startCoords = (y, x)
                matrix[y][x] = ord("a") - 97
            elif data[y][x] == "E":
                endCoords = (y, x)
                matrix[y][x] = ord("z") - 97
            else:
                matrix[y][x] = ord(data[y][x]) - 97
    return startCoords, endCoords, matrix


def get_vertex_map(matrix: np.ndarray) -> dict[tuple[int, int], set[tuple[int, int]]]:
    vertices: dict[tuple[int, int], set[tuple[int, int]]] = {}
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            vertices[(y, x)] = set()
            # up
            if y > 0 and can_go(matrix[y][x], matrix[y - 1][x]):
                vertices[(y, x)].add((y - 1, x))
            # down
            if y < len(matrix) - 1 and can_go(matrix[y][x], matrix[y + 1][x]):
                vertices[(y, x)].add((y + 1, x))
            # left
            if x > 0 and can_go(matrix[y][x], matrix[y][x - 1]):
                vertices[(y, x)].add((y, x - 1))
            # right
            if x < len(matrix[y]) - 1 and can_go(matrix[y][x], matrix[y][x + 1]):
                vertices[(y, x)].add((y, x + 1))
    return vertices


with open("./12/input.txt") as f:
    data = f.read().strip().splitlines()


startCoords, endCoords, matrix = get_matrix(data)
vertices = get_vertex_map(matrix)


print("Answer #1: ", shortest_distance(startCoords, endCoords, vertices))

distances: list[int] = []

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[y][x] == 0:
            distance = shortest_distance((y, x), endCoords, vertices)
            if distance > 0:
                distances.append(shortest_distance((y, x), endCoords, vertices))

print("Answer #2: ", min(distances))
