# Something wrong redoing


class FileStructure:
    def __init__(
        self,
        name: str,
        parent: object | None,
        size: int | None = None,
        is_file: bool = False,
    ):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = size
        self.is_file = is_file

    def add_child(self, child) -> None:
        self.children.append(child)

    def get_children(self) -> list[object]:
        return self.children

    def get_parent(self) -> object:
        return self.parent

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int | None:
        return self.size

    def get_child_by_name(self, name: str) -> object | None:
        for child in self.children:
            if child.get_name() == name:
                return child
        return None

    def calc_size(self) -> None:
        if self.is_file:
            return
        self.size = 0
        for child in self.children:
            child.calc_size()
            self.size += child.get_size()


def commands(line: str, struct: FileStructure) -> FileStructure | object | None:
    if line[:7] == "$ cd ..":
        struct.calc_size()
        return struct.get_parent()
    if line[:4] == "$ cd":
        dir_name = line[5:]
        dir_struct = struct.get_child_by_name(dir_name)
        if dir_struct is not None:
            return dir_struct
        return FileStructure(line[5:], struct)
    if line[:4] == "$ ls":
        return
    if line[0:3] == "dir":
        struct.add_child(FileStructure(line[4:], struct))
        return
    new_file = line.split(" ")
    struct.add_child(FileStructure(new_file[1], struct, int(new_file[0]), True))
    return


def get_sizes(struct: FileStructure) -> None:
    if struct.is_file:
        return
    for child in struct.children:
        get_sizes(child)
    if struct.size and struct.size <= 100000:
        sizes.append(struct.size)


with open("./7/input.txt", "r") as f:
    content = f.read()

lines = content.splitlines()

file_structure = FileStructure("/", None)

current_struct = file_structure
possible_struct = None

for line in lines[1:]:
    if possible_struct is None:
        possible_struct = commands(line, current_struct)
    elif isinstance(current_struct, FileStructure):
        current_struct = possible_struct
        possible_struct = commands(line, current_struct)  # type: ignore

sizes = []
# find all file structures that are below in 100000 size

get_sizes(file_structure)

print("Answer #1: ", sum(sizes))
