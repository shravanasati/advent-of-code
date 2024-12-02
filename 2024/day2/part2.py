# reports = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """.splitlines()

with open("./input.txt") as f:
    reports = f.read().splitlines()


def check_strictly_ascending(levels: tuple[int, ...]):
    violators = 0
    for i in range(1, len(levels)):
        if levels[i] - levels[i - 1] <= 0:
            violators += 1

    return violators


def check_strictly_descending(levels: tuple[int, ...]):
    violators = 0
    for i in range(1, len(levels)):
        if levels[i] - levels[i - 1] >= 0:
            violators += 1

    return violators


def check_diff(levels: tuple[int, ...]):
    i = 1
    gap = 1
    while i < len(levels):
        diff = abs(levels[i] - levels[i - gap])
        if diff < 1 or diff > 3:
            gap += 1

        if gap > 2:
            return False

        i += 1

    return True


safe_count = 0
for report in reports:
    levels = tuple(map(int, report.split()))

    strictly_ascending = check_strictly_ascending(levels)
    strictly_descending = check_strictly_descending(levels)
    if strictly_ascending > 1 and strictly_descending > 1:
        continue

    if not check_diff(levels):
        continue

    safe_count += 1

print(safe_count)
