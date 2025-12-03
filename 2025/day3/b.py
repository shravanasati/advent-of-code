from pathlib import Path


with (Path(__file__).parent / "input.txt").open() as f:
    banks = f.read().split()

banks = """987654321111111
811111111111119
234234234234278
818181911112111
""".split()


def max_joltage(bank: str, k: int = 12) -> int:
    if len(bank) < k:
        return int(bank)

    stack = []
    to_remove = len(bank) - k

    for digit in bank:
        while stack and stack[-1] < digit and to_remove > 0:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    result = "".join(stack[:k])
    return int(result)


s = 0
for bank in banks:
    s += max_joltage(bank)

print(s)
