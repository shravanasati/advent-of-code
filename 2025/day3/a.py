from pathlib import Path


with (Path(__file__).parent / "input.txt").open() as f:
    banks = f.read().split()
# banks = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """.split()


def max_joltage(bank: str) -> int:
    max_jolt = int(bank[0]) * 10 + int(bank[1])

    max_fst = int(bank[0])
    for i in range(1, len(bank)):
        current = int(bank[i])
        joltage = max_fst * 10  + current
        max_jolt = max(max_jolt, joltage)
        max_fst = max(max_fst, current)

    return max_jolt


s = 0
for bank in banks:
    s += max_joltage(bank)

print(s)
