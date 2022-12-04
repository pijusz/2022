# unloading ships
# each section has unique ID
# each elf is assigned array of sections
# assignments can overlap


def parse(data_line: str | None) -> tuple[int, int, int, int]:
    sections = line.split(",")
    section_1 = sections[0].split("-")
    section_2 = sections[1].split("-")

    section_1_start = int(section_1[0])
    section_1_end = int(section_1[1])
    section_2_start = int(section_2[0])
    section_2_end = int(section_2[1])

    return section_1_start, section_1_end, section_2_start, section_2_end


data: list[tuple[int, int, int, int]] = []

with open("./4/input.txt", "r") as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        data.append(parse(line.strip()))

# answer #1
fully_contained = 0
# answer #2
partially_contained = 0

for line in data:
    # check if section_1 is fully contained in section_2
    if line[0] >= line[2] and line[1] <= line[3]:
        fully_contained += 1
        continue
    # check if section_1 is fully contained in section_2
    if line[2] >= line[0] and line[3] <= line[1]:
        fully_contained += 1
        continue
    # partial overlap
    if line[0] <= line[2] and line[1] >= line[2]:
        partially_contained += 1
        continue
    if line[2] <= line[0] and line[3] >= line[0]:
        partially_contained += 1
        continue

print("Answer #1 ", fully_contained)
print("Answer #2 ", fully_contained + partially_contained)
