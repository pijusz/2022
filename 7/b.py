def get_dirs(
    current_dir,
    data: list[str],
    prev_dir,
):
    while data:
        cmd = data.pop(0)
        if cmd == "$ ls":
            while data and not data[0].startswith("$"):
                a, b = data.pop(0).split(" ")
                current_dir[prev_dir + (b,)] = {} if a == "dir" else int(a)
        elif cmd.endswith(".."):
            return
        else:
            c = cmd.split(" ")[-1]
            p = prev_dir + (c,)
            get_dirs(current_dir[p], data, prev_dir + p)
    return current_dir


def get_space(current_dir, key: str):
    size = 0
    for child_key, value_or_dir in current_dir.items():
        if isinstance(value_or_dir, int):
            size += value_or_dir
        else:
            size += get_space(value_or_dir, child_key)
    space[key] = size
    return size


# general idea of using tuples as keys, super stupid in huge data sets
with open("./7/input.txt", "r") as file:
    data = file.read().splitlines()[1:]
    init_dir = {"/": {}}
    dirs = get_dirs(init_dir["/"], data, ("/",))

space = {}
get_space(dirs, key="/")
print("Answer #1: ", sum(v for v in space.values() if v <= 100000))

needed_space = 70000000 - max(space.values())
print("Answer #2: ", min([v for v in space.values() if v > 30000000 - needed_space]))
