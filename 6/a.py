# content is 1 line of string
# marker is when 4 chars in a row are the different

with open("./6/input.txt", "r") as f:
    content = f.read()


def get_marker(content: str, length: int) -> int:
    for i in range(length - 1, len(content)):
        # find 4 characters that are different in a row
        if len(set(content[i - (length - 1) : i + 1])) == length:
            return i + 1
    return -1


print("Answer #1: ", get_marker(content, 4))
print("Answer #2: ", get_marker(content, 14))
