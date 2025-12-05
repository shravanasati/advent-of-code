"""
Docstring for 2025.day5.a
with open("./input.txt") as f:
    input = f.read()
# input = \"""3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32
# \"""

ranges, ids = input.split("\n\n")
ranges = ranges.split()

fresh = set[int]()
for range_ in ranges:
    lower, upper = map(int, range_.split("-"))
    fresh.update(range(lower, upper+1))
ids = set(map(int, ids.split()))

print(len(ids.intersection(fresh)))
"""

import bisect

with open("./input.txt") as f:
    input = f.read()


ranges, ids = input.split("\n\n")
range_list = []
for range_ in ranges.split():
    lower, upper = map(int, range_.split("-"))
    range_list.append((lower, upper))

# Sort ranges by lower bound
range_list.sort()

ids = list(map(int, ids.split()))

fresh_count = 0
for id_ in ids:
    # Binary search to find the first range with lower <= id_
    idx = bisect.bisect_right(range_list, (id_, float('inf'))) - 1
    
    # Check if id_ falls within any range from idx onwards
    for i in range(max(0, idx - 1), len(range_list)):
        lower, upper = range_list[i]
        if lower > id_:
            break
        if lower <= id_ <= upper:
            fresh_count += 1
            break

print(fresh_count)