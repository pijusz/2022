import numpy as np

with open("./10/input.txt") as f:
    content = f.readlines()


data: list[tuple[str, int | None]] = []

for line in content:
    line = line.strip().split(" ")
    if len(line) > 1:
        data.append((line[0], int(line[1])))
    else:
        data.append((line[0], None))

# # register
# x = 1
# strengths: list[int] = []

# cycles: list[int | None] = [None]
# cycle_num = 0

# for idx, instruction in enumerate(data):
#     if instruction[0] == "noop":
#         cycles.append(None)
#         cycle_num += 1
#     if instruction[0] == "addx":
#         cycles.append(instruction[1])
#         cycle_num += 2
#     instr = cycles.pop(0)
#     if instr is not None:
#         x += instr
#     if (cycle_num + 20) % 40 == 0 or (
#         (cycle_num + 20) % 40 == 1 and len(strengths) < (cycle_num + 20) // 40
#     ):
#         num = (cycle_num + 20) % 40
#         if num == 1:
#             strengths.append(x * (cycle_num - 1))
#         else:
#             strengths.append(x * cycle_num)

# print("Answer #1 ", sum(strengths))


x = 1

cycles: list[int | None] = [None]
cycle_num = 0

screen = np.zeros(shape=(6 * 40), dtype=int)

# cycle loop
for screen_idx in range(len(screen)):
    if len(data) > 0:
        instruction = data.pop(0)
        if instruction[0] == "noop":
            cycles.append(None)
        if instruction[0] == "addx":
            cycles.append(None)
            cycles.append(instruction[1])
    instr = cycles.pop(0)
    if instr is not None:
        x += instr
    # 8 is the sprite to print
    if x == screen_idx % 40 or x + 1 == screen_idx % 40 or x - 1 == screen_idx % 40:
        screen[screen_idx] = 8


print("Answer #2")
for num in range(0, len(screen), 40):
    for i in range(40):
        if screen[num + i] == 8:
            print("#", end="")
        else:
            print(".", end="")
    print("\n")
