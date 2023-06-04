from collections import deque

with open("./18/input.txt") as f:
    data = [tuple(map(int, line.split(","))) for line in f.readlines()]


deltas3d = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def openSides(l):
    s = set(l)
    return sum(
        ((x + dx, y + dy, z + dz) not in s for x, y, z in s for dx, dy, dz in deltas3d)
    )


def enclosedSpace(s, start, limits):
    space = set([start])
    rem = deque([start])
    while rem:
        x, y, z = rem.popleft()
        for dx, dy, dz in deltas3d:
            xx, yy, zz = x + dx, y + dy, z + dz
            if (xx, yy, zz) in s or (xx, yy, zz) in space:
                continue
            if xx < limits[0][0] or xx > limits[0][1]:
                return set()
            if yy < limits[1][0] or yy > limits[1][1]:
                return set()
            if zz < limits[2][0] or zz > limits[2][1]:
                return set()
            space.add((xx, yy, zz))
            rem.append((xx, yy, zz))
    return space


def reallyOpenSides(l):
    occupied = set(l)
    xs = {x for x, y, z in occupied}
    ys = {y for x, y, z in occupied}
    zs = {z for x, y, z in occupied}
    limits = ((min(xs), max(xs)), (min(ys), max(ys)), (min(zs), max(zs)))
    count = 0
    enclosed = set()
    for x, y, z in l:
        for dx, dy, dz in deltas3d:
            xx, yy, zz = x + dx, y + dy, z + dz
            if (xx, yy, zz) in occupied or (xx, yy, zz) in enclosed:
                continue
            volume = enclosedSpace(occupied, (xx, yy, zz), limits)
            if volume:
                enclosed |= volume
            else:
                count += 1
    return count


print(reallyOpenSides(data))
