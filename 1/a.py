with open("./1/input.txt", "r") as f:
    content = f.read()

elfs = content.split("\n\n")
elfs_food = []

for elf in elfs:
    elf_calories = 0
    for line in elf.split("\n"):
        if len(line) != 0:
            elf_calories += int(line)
    elfs_food.append(elf_calories)

print("result #1: ", max(elfs_food))

elfs_food.sort(reverse=True)

print("result #2: ", sum(elfs_food[:3]))
