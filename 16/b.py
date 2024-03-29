import re


def solve(graph, flows):
    def find(graph, flows, start):
        frontier = [(0, [start], set())]
        for i in range(1, 31):
            if i > 5:
                frontier.sort(reverse=True)
                frontier = frontier[:3000]
            new_frontier = []
            for pressure, path, opened in frontier:
                location = path[-1]

                p = sum(flows[o] for o in opened)
                pressure += p

                for neigh in graph[location]:
                    new_frontier.append((pressure, path + [neigh], opened.copy()))

                if flows[location] > 0 and location not in opened:
                    new_frontier.append((pressure, path, opened | {location}))
            frontier = new_frontier
        return max(frontier)

    pressure, path, opened = find(graph, flows, "AA")
    return f"{pressure} {len(path) - 1} {opened}"


def solve2(graph, flows):
    def find(graph, flows, start):
        def options(graph, flows, location, path, opened):
            options = []
            for neigh in graph[location]:
                options.append((path + [neigh], opened.copy()))
            if flows[location] > 0 and location not in opened:
                options.append((path, opened | {location}))
            return options

        frontier = [(0, ([start], [start]), set())]
        for i in range(1, 27):
            if i > 5:
                frontier.sort(reverse=True)
                frontier = frontier[:9000]
            new_frontier = []
            for pressure, paths, opened in frontier:
                me = paths[0][-1]
                elephant = paths[1][-1]

                p = sum(flows[o] for o in opened)
                pressure += p

                for my_paths, op in options(graph, flows, me, paths[0], opened):
                    for elephant_paths, elephant_options in options(
                        graph, flows, elephant, paths[1], op
                    ):
                        new_frontier.append(
                            (pressure, [my_paths, elephant_paths], elephant_options)
                        )

            frontier = new_frontier
        return max(frontier)

    pressure, path, opened = find(graph, flows, "AA")
    return f"{pressure} {len(path) - 1} {opened}"


with open("./16/input.txt") as f:
    input = re.findall(r"Valve (\w\w).*?rate=(\d+).*?valves? (.*)", f.read())
    flows = dict((start, int(rate)) for start, rate, _ in input)
    graph = dict(
        (start, nabes.replace(" ", "").split(",")) for start, _, nabes in input
    )

print("Answer #1 ", solve2(graph, flows))
