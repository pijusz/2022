import re


class BP:
    def __init__(self):
        # resources
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geode = 0
        # blueprint costs
        self.c_ore = 0
        self.c_clay = 0
        self.c_obsidian = (0, 0)
        self.c_geode = (0, 0)
        # bots
        self.b_ore = 1
        self.b_clay = 0
        self.b_obsidian = 0
        self.b_geode = 0

    def tick(self):
        self.ore += self.b_ore
        self.clay += self.b_clay
        self.obsidian += self.b_obsidian
        self.geode += self.b_geode

    def build(self, t: str):
        if t == "ore":
            self.b_ore += 1
            self.ore -= self.c_ore
        elif t == "clay":
            self.b_clay += 1
            self.ore -= self.c_clay
        elif t == "obsidian":
            self.b_obsidian += 1
            self.ore -= self.c_obsidian[0]
            self.clay -= self.c_obsidian[1]
        elif t == "geode":
            self.b_geode += 1
            self.ore -= self.c_geode[0]
            self.obsidian -= self.c_geode[1]


with open("./19/test.txt", "r") as f:
    content = f.readlines()

bps: list[tuple[int, int, tuple[int, int, int], tuple[int, int, int]]] = []

for line in content:
    bp = []
    for section in line.split(": ")[1].split(". "):
        r = []
        for x, y in re.findall(r"(\d+) (\w+)", section):
            x = int(x)
            y = ["ore", "clay", "obsidian"].index(y)
            r.append((x, y))
        bp.append(r)
    bps.append(
        [
            bp[0][0][0],
            bp[1][0][0],
            (bp[2][0][0], bp[2][1][0], 0),
            (bp[3][0][0], 0, bp[3][1][0]),
        ]
    )

# blueprint format
# ore, clay, obsidian, geode
# [ore, ore, (ore, clay, obs), (ore, clay, obsidian)]
print(bps)
