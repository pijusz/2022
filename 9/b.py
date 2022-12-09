def add_tuple(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def do_move(move: str) -> tuple[int, int]:
    if move[0] == "R":
        return (1, 0)
    if move[0] == "L":
        return (-1, 0)
    if move[0] == "U":
        return (0, 1)
    if move[0] == "D":
        return (0, -1)
    return (0, 0)


def catchup(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    x = tail[0]
    y = tail[1]
    distance_x = head[0] - tail[0]
    distance_y = head[1] - tail[1]
    fake_distance = abs(distance_x) + abs(distance_y)
    if abs(distance_x) == 1 and fake_distance > 2:
        x = head[0]
    if abs(distance_y) == 1 and fake_distance > 2:
        y = head[1]
    if distance_x > 1:
        x = x + 1
    if distance_x < -1:
        x = x - 1
    if distance_y > 1:
        y = y + 1
    if distance_y < -1:
        y = y - 1
    return (x, y)


def snake(moves: list[tuple[str, int]], snake_length: int) -> set[tuple[int, int]]:
    cursors: list[tuple[int, int]] = [(0, 0) for _ in range(snake_length)]
    visits_tail: set[tuple[int, int]] = {cursors[0]}
    for move in moves:
        for step in range(move[1]):
            cursors[0] = add_tuple(cursors[0], do_move(move[0]))
            for cursor_idx in range(1, len(cursors)):
                cursors[cursor_idx] = catchup(
                    cursors[cursor_idx - 1], cursors[cursor_idx]
                )
            visits_tail.add(cursors[-1])
    return visits_tail


moves: list[tuple[str, int]] = []

with open("./9/input.txt") as f:
    content = f.readlines()

for line in content:
    line = line.strip().split(" ")
    moves.append((line[0], int(line[1])))


print("Answer #1: ", len(snake(moves, 2)))
print("Answer #2: ", len(snake(moves, 10)))
