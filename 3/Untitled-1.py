s = "JCMMBzDMJcZZCjDzSBDNJgdfdQlqlLNdhgGLhp"
ss = "hqBqJsqHhHvhHHqlBvlfpHQQwLVzVwtVzjzttjQVSjMjwL"

# a = 1
# b = 2
# c = 3
#  ...
# z = 26
# A = 27
# B = 28
#  ...
# Z = 52

answer: int = 0
for char in s:
    if char.islower():
        answer += ord(char) - 96
    else:
        answer += ord(char) - 38

print(answer)
