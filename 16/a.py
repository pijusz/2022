def get_graph_nodes(valves: dict) -> tuple[dict[tuple[str, str], int], set[str]]:
    nodes: set[str] = {START_VALVE}
    graph: dict[tuple[str, str], int] = {}
    # we assume that START_VALUE is wont ever be opened,
    # then limit wont be reduced by 1
    for valve in valves:
        if valves[valve]["flow"] == 0 and valve != START_VALVE:
            continue
        nodes.add(valve)
        for other_valve in valves:
            if valve == other_valve or valves[other_valve]["flow"] == 0:
                continue
            # actually you might not want to open valves by default
            graph[(valve, other_valve)] = 1
    return graph, nodes


def get_graph_distances(graph: dict[tuple[str, str], int]):
    for start_valve, end_valve in graph:
        visited = []
        queue: list[tuple[str, int]] = [(start_valve, 0)]
        while queue:
            current_valve, distance = queue.pop(0)
            if current_valve == end_valve:
                graph[(start_valve, end_valve)] = distance
                break
            if current_valve in visited:
                continue
            visited.append(current_valve)
            for tunnel in valves[current_valve]["tunnels"]:
                queue.append((tunnel, distance + 1))


def get_routes_limit(
    graph: dict[tuple[str, str], int], nodes: set[str], start_node: str, limit: int
) -> list[list[tuple[str, int]]]:
    routes: list[list[tuple[str, int]]] = []
    # there is possibility you want to go back
    # node, is_open, flow, time
    queue: list[tuple[int, list[tuple[str, int]]]] = [
        (0, [(start_node, 0)]),
        (0, [(start_node, valves[start_node]["flow"])]),
    ]
    while queue:
        weight, route = queue.pop(0)
        stop, flow = route[-1]
        for node in nodes:
            if stop == node or stop != START_VALVE:
                continue
            # if close node route
            if weight + graph[stop, node] <= limit:
                w = weight + graph[stop, node]
                queue.append(
                    (
                        weight + graph[stop, node],
                        route + [(node, 0)],
                    )
                )
            else:
                routes.append(route)
                continue
            # if open node route
            # optimization: if already in route opened, we will not open it again
            if (
                weight + graph[stop, node] + 1 <= limit
                and (node, valves[node]["flow"]) not in route
            ):
                queue.append(
                    (
                        weight + graph[stop, node] + 1,
                        route + [(node, valves[node]["flow"])],
                    )
                )
            else:
                routes.append(route)
                continue
    return routes


# node, is_open, flow, time
def get_route_pressure(route: list[tuple[str, int]], time_limit: int):
    pressure = 0
    for t in range(time_limit):
        w = 0
        for idx, node in enumerate(route):
            if idx == 0:
                continue
            w += graph[route[idx - 1][0], route[idx][0]]
            if w < t:
                pressure += node[1]
    return pressure


with open("./16/test.txt", "r") as f:
    content = f.read().splitlines()


TIME_LEFT = 30  # minutes
MOVE_PRICE = 1  # minutes
OPEN_PRICE = 1  # minutes
START_VALVE = "AA"

valves: dict = {}

for line in content:
    line = (
        line.replace("Valve ", "")
        .replace(" has flow rate=", ";")
        .replace("; tunnels lead to valves ", ";")
        .replace("; tunnel leads to valve ", ";")
    )
    sp = line.split(";")
    valves[sp[0]] = {
        "flow": int(sp[1]),
        "tunnels": sp[2].split(", "),
        "is_open": False,
        "distances": {},
    }


pressure = 0
current_valve = START_VALVE

graph, nodes = get_graph_nodes(valves)
get_graph_distances(graph)

# get shortest distance for each valve pair in 'graph' using 'valves' and weight 1 for each move
pressures = []
routes = get_routes_limit(graph, nodes, START_VALVE, TIME_LEFT)
for route in routes:
    pressures.append(get_route_pressure(route, TIME_LEFT))
print("Answer 1: ", max(pressures))
