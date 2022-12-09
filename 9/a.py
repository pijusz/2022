def is_separated(cursor_head: tuple[int, int], cursor_tail: tuple[int, int]) -> bool:
    distance_horizontal = abs(cursor_head[0] - cursor_tail[0])
    distance_vertical = abs(cursor_head[1] - cursor_tail[1])
    if distance_horizontal > 1 or distance_vertical > 1:
        return True
    return False


def get_new_tail(
    cursor_head: tuple[int, int], cursor_tail: tuple[int, int]
) -> tuple[int, int]:
    distance_horizontal = cursor_head[0] - cursor_tail[0]
    distance_vertical = cursor_head[1] - cursor_tail[1]
    fake_distance = abs(distance_horizontal) + abs(distance_vertical)
    x = cursor_tail[0]
    y = cursor_tail[1]
    if distance_horizontal > 1:
        x = x + 1
    elif distance_horizontal < -1:
        x = x - 1
    if distance_vertical > 1:
        y = y + 1
    elif distance_vertical < -1:
        y = y - 1
    if abs(distance_horizontal) == 1 and fake_distance > 2:
        x = cursor_head[0]
    if abs(distance_vertical) == 1 and fake_distance > 2:
        y = cursor_head[1]
    return (x, y)


data: list[tuple[str, int]] = []

with open("./9/input.txt") as f:
    content = f.readlines()

for line in content:
    line = line.strip().split(" ")
    data.append((line[0], int(line[1])))

cursor_head: tuple[int, int] = (0, 0)
cursor_tail: tuple[int, int] = (0, 0)

visits_head: set[tuple[int, int]] = {cursor_head}
visits_tail: set[tuple[int, int]] = {cursor_tail}

for move in data:
    if move[0] == "R":
        for i in range(move[1]):
            cursor_head = (cursor_head[0] + 1, cursor_head[1])
            visits_head.add(cursor_head)
            if is_separated(cursor_head, cursor_tail):
                cursor_tail = get_new_tail(cursor_head, cursor_tail)
                visits_tail.add(cursor_tail)
    if move[0] == "L":
        for i in range(move[1]):
            cursor_head = (cursor_head[0] - 1, cursor_head[1])
            visits_head.add(cursor_head)
            if is_separated(cursor_head, cursor_tail):
                cursor_tail = get_new_tail(cursor_head, cursor_tail)
                visits_tail.add(cursor_tail)
    if move[0] == "U":
        for i in range(move[1]):
            cursor_head = (cursor_head[0], cursor_head[1] + 1)
            visits_head.add(cursor_head)
            if is_separated(cursor_head, cursor_tail):
                cursor_tail = get_new_tail(cursor_head, cursor_tail)
                visits_tail.add(cursor_tail)
    if move[0] == "D":
        for i in range(move[1]):
            cursor_head = (cursor_head[0], cursor_head[1] - 1)
            visits_head.add(cursor_head)
            if is_separated(cursor_head, cursor_tail):
                cursor_tail = get_new_tail(cursor_head, cursor_tail)
                visits_tail.add(cursor_tail)

print("Answer #1: ", len(visits_tail))
