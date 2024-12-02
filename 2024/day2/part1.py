reports = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".splitlines()

# with open("./input.txt") as f:
#     reports = f.read().splitlines()

safe_count = 0
for report in reports:
    levels = tuple(map(int, report.split()))
    last_level = levels[0]
    sign = (levels[1] - last_level) > 0
    is_safe = True
    for current_level in levels[1:]:
        diff = abs(current_level - last_level)
        if diff < 1 or diff > 3:
            is_safe = False
            break
        new_sign = current_level - last_level > 0
        if new_sign != sign:
            is_safe = False
            break
        last_level = current_level

    if is_safe:
        safe_count += 1

print(safe_count)
