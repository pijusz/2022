# First Column, What opponent plays
# A for Rock
# B for Paper
# C for Scissors

# Second Column, What I play
# X for Rock
# Y for Paper
# Z for Scissors

# Score for selected shape
# 1 for Rock
# 2 for Paper
# 3 for Scissors

# Score for result
# 0 for Lost
# 3 for Draw
# 6 for Win

data: list[tuple[str, str]] = []

with open("./2/input.txt", "r") as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        line = line.replace("\n", "").split(" ")
        data.append((line[0], line[1]))

# Part 1
score = 0

#   X, Y, Z
# A 4, 8, 3
# B 1, 5, 9
# C 7, 2, 6
result_matrix = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]

idx: list[tuple[int, int]] = []

# change letters to indexes
for i in range(len(data)):
    idx.append((ord(data[i][0]) - 65, ord(data[i][1]) - 88))

# calculate score
for i in idx:
    score += result_matrix[i[0]][i[1]]

print("Part #1 score: ", score)

# Part 2
score2 = 0


# Second Column, I need to Win/Loose/Draw
# X for Loose
# Y for Draw
# Z for Win

#   X, Y, Z
# A 4, 8, 3
# B 1, 5, 9
# C 7, 2, 6

# Opp -> Me -> Choice
# A -> X -> Z
# A -> Y -> X
# A -> Z -> Y
# B -> X -> X
# B -> Y -> Y
# B -> Z -> Z
# C -> X -> Y
# C -> Y -> Z
# C -> Z -> X


choice_matrix = [[2, 0, 1], [0, 1, 2], [1, 2, 0]]

# convert suggestions to choices
idx2: list[tuple[int, int]] = []
for i in range(len(data)):
    idx2.append(
        (
            ord(data[i][0]) - 65,
            choice_matrix[ord(data[i][0]) - 65][ord(data[i][1]) - 88],
        )
    )

# calculate score
for i in idx2:
    score2 += result_matrix[i[0]][i[1]]

print("Part #2 score: ", score2)
