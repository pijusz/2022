class Node:
    def __init__(self, data: int):
        # self.data = data # part 1
        self.data = data * 811589153  # part 2
        self.next: Node = None  # type: ignore
        self.prev: Node = None  # type: ignore


def get_data(nodes: list[Node], node_start: Node) -> list[int]:
    p: list[int] = []
    current_node = node_start
    for _ in range(len(nodes)):
        p.append(current_node.data)
        current_node = current_node.next
    return p


def get_all_nodes(nodes: list[Node], node_start: Node) -> list[Node]:
    node_list: list[Node] = []
    current_node = node_start
    for _ in range(len(nodes)):
        node_list.append(current_node)
        current_node = current_node.next
    return node_list


def get_nodes(
    node: Node, moves: int, len: int
) -> tuple[Node, Node] | tuple[None, None]:
    # if node negative go left, if node positive go right
    # optimization  reduce moves by len
    if abs(moves) > len:
        moves = abs(moves) % (len - 1)
    if moves < 0:
        for _ in range(abs(moves)):
            node = node.prev
        return node.prev, node
    if moves > 0:
        for _ in range(moves):
            node = node.next
        return node, node.next
    return None, None


def get_node(start_node: Node, move: int) -> Node:
    if move < 0:
        for _ in range(abs(move)):
            start_node = start_node.prev
        return start_node
    if move > 0:
        for _ in range(move):
            start_node = start_node.next
        return start_node
    return start_node


def find_node(nodes: list[Node], data: int) -> Node:
    for node in nodes:
        if node.data == data:
            return node
    return nodes[0]


data: list[Node] = []
with open("./20/test.txt") as f:
    data = [Node(int(line, 10)) for line in f.readlines()]


# connect nodes
for i in range(len(data) - 1):
    data[i].next = data[i + 1]
    data[i + 1].prev = data[i]
# add first and last node
data[0].prev = data[-1]
data[-1].next = data[0]

first_node = data[0]
for idx, node in enumerate(data):
    print("Node: ", idx, "/", len(data))
    # remove from list
    if node.data == 0:
        continue
    node.prev.next = node.next
    node.next.prev = node.prev
    left, right = get_nodes(node, node.data, len(data))
    if left and right:
        left.next = node
        right.prev = node
        node.prev = left
        node.next = right

nodes = get_all_nodes(data, first_node)
print("Nodes: ", [node.data for node in nodes])

# for i in range(11):
#     print("Move: ", i)
#     first_node = find_node(data, 0)
#     nodes = get_all_nodes(data, first_node)
#     print("Nodes: ", [node.data for node in nodes])
#     for node in nodes:
#         if node.data == 0:
#             continue
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         left, right = get_nodes(node, node.data, len(data))
#         if left and right:
#             left.next = node
#             right.prev = node
#             node.prev = left
#             node.next = right

node = find_node(data, 0)
print(
    "Answer #1: ",
    get_node(node, 1000).data,
    get_node(node, 2000).data,
    get_node(node, 3000).data,
    get_node(node, 1000).data + get_node(node, 2000).data + get_node(node, 3000).data,
)
