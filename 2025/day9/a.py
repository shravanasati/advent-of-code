from itertools import combinations

with open("./input.txt") as f:
	coords = f.read().split()

# coords = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3
# """.split()

coords = list(map(lambda c: list(c)[::-1], map(lambda c: map(int, c.split(",")), coords)))

max_area = float("-inf")
for a, b in combinations(coords, 2):
	max_area = max(max_area, (a[0] - b[0] + 1) * (a[1] - b[1] + 1))

print(max_area)
