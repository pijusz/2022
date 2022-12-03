# 2 compartments per each line cut in half
# only single item per compartment
# items signed by [a-z][A-Z] they equal to 1-26 and 27-52


def get_priority(item: str) -> int:
    priority = 0
    for char in item:
        if char.islower():
            priority += ord(char) - 96
        else:
            priority += ord(char) - 38
    return priority


def get_halfs(data: list[str]) -> list[tuple[str, str]]:
    rucksacks = []
    for line in data:
        half_line = len(line) // 2
        rucksacks.append((line[:half_line], line[half_line:]))
    return rucksacks


def get_triplets(data: list[str]) -> list[tuple[str, str, str]]:
    triplets = []
    for line in range(0, len(data), 3):
        triplets.append((data[line], data[line + 1], data[line + 2]))
    return triplets


def get_shared_items(rucksacks: list[tuple[str, str]]) -> str:
    items: str = ""
    for rucksack in rucksacks:
        for item in rucksack[0]:
            if item in rucksack[1]:
                items += item
                break
    return items


def get_shared_items_of_n_tuple(rucksacks: list[tuple[str, str, str]]) -> str:
    items: str = ""
    for rucksack in rucksacks:
        for item in rucksack[0]:
            if item in rucksack[1] and item in rucksack[2]:
                items += item
                break
    return items


data: list[str] = []

with open("./3/input.txt", "r") as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        data.append(line.strip())


print("Answer #1 ", get_priority(get_shared_items(get_halfs(data))))
print("Answer #2 ", get_priority(get_shared_items_of_n_tuple(get_triplets(data))))
