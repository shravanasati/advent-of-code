with open("./input.txt") as f:
    input = f.read()

ranges, _ = input.split("\n\n")
range_list = []

for range_ in ranges.split():
    lower, upper = map(int, range_.split("-"))
    range_list.append((lower, upper))

# Sort ranges by lower bound
range_list.sort()

# Merge overlapping ranges
merged = []
for lower, upper in range_list:
    if merged and lower <= merged[-1][1] + 1:
        # Overlapping or adjacent - merge
        merged[-1] = (merged[-1][0], max(merged[-1][1], upper))
    else:
        # Non-overlapping - add new range
        merged.append((lower, upper))

# Count total IDs in merged ranges
total = sum(upper - lower + 1 for lower, upper in merged)
print(total)