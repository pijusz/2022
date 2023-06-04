with open("./17/input.txt") as f:
    content = f.read()


def parseInput(s):
    return [{">": complex(1), "<": complex(-1)}[c] for c in s if c in "<>"]


pieceStrs = [
    """####""",
    """.#.
###
.#.""",
    """..#
..#
###""",
    """#
#
#
#""",
    """##
##""",
]


def pieceSet():
    pl = list()
    for ps in pieceStrs:
        d = set()
        minx, miny = 0, 0
        for y, line in enumerate(ps.splitlines()):
            for x, c in enumerate(line):
                if c == "#":
                    minx = min(x, minx)
                    miny = min(-y, miny)
                    d.add(complex(x, -y))
        d = {coord - complex(minx, miny) for coord in d}
        # print(d)
        pl.append(d)
    return pl


pieces = pieceSet()
noPieces = len(pieces)


def height(m):
    return int(max((r.imag for r in m)))


def collision(piece, offset, m):
    for coord in piece:
        offsetCord = coord + offset
        if offsetCord in m:
            return False
        if not (0 <= offsetCord.real <= 6):
            return False
    return True


def fallingRock(rockMap, piece, windPattern, round):
    pos = complex(2, height(rockMap) + 4)
    move = windPattern[round]
    round = (round + 1) % len(windPattern)
    while True:
        newPos = pos + move
        if not collision(piece, newPos, rockMap):
            newPos = pos
        pos = newPos
        newPos = pos - complex(0, 1)
        if not collision(piece, newPos, rockMap):
            rockMap.update({coord + pos for coord in piece})
            return round
        pos = newPos
        move = windPattern[round]
        round = (round + 1) % len(windPattern)


def fallingRocks(pl, windPattern, noMoves):
    m = {complex(x, 0) for x in range(7)}
    round = 0
    s = dict()
    move = 0
    extraheight = 0
    skip = None
    repetitions = 2
    while move < noMoves and (skip is None or skip + move < noMoves):
        idx = (round, move % len(pl))
        if idx in s and skip is None:
            if len(s[idx]) > repetitions:
                last = [
                    (p1[0] - p2[0], p1[1] - p2[1])
                    for p1, p2 in zip(
                        s[idx][-repetitions:], s[idx][-(repetitions - 1) :]
                    )
                ]
                if all((last[0] == ll for ll in last)):
                    skipDelta, heightDelta = -last[0][0], -last[0][1]
                    skipCycles = (noMoves - move) // skipDelta
                    skip = skipDelta * skipCycles
                    print("Stable change .. skipping", skip, heightDelta * skipCycles)
                    extraheight += heightDelta * skipCycles
                    continue
        else:
            s[idx] = list()
        s[idx].append((move, height(m)))
        round = fallingRock(m, pl[move % noPieces], windPattern, round)
        move += 1
    return height(m) + extraheight


windPattern = parseInput(content)
print(fallingRocks(pieces, windPattern, 1000000000000))
