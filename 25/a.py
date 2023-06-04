def snafu_to_dec(snafu: str) -> int:
    return sum(digit[char] * (5**idx) for idx, char in enumerate(snafu[::-1]))


def dec_to_snafu(dec: int) -> str:
    snafu = ""
    while dec:
        digit = (dec + 2) % 5 - 2
        snafu += digits[digit + 2]
        dec = (dec - digit) // 5
    return snafu[::-1]


with open("./25/input.txt") as f:
    data = f.read().strip().splitlines()


digits = [
    "=",
    "-",
    "0",
    "1",
    "2",
]

digit = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2,
}

numbers: list[tuple[str, int, str]] = []

for line in data:
    numbers.append((line, snafu_to_dec(line), dec_to_snafu(snafu_to_dec(line))))

s = sum(num[1] for num in numbers)

print("Answer #1: ", dec_to_snafu(s))
