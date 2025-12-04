# with open("./input.txt") as f:
#     grid = f.read().split()
grid = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".split()

ROW_MIN = 0
ROW_MAX = len(grid)
COL_MIN = 0
COL_MAX = len(grid[0])

accessible = 0

for i, row in enumerate(grid):
    for j, item in enumerate(row):
        if item != "@":
            continue

        adjacent = filter(
            lambda c: c[0] >= ROW_MIN
            and c[0] < ROW_MAX
            and c[1] >= COL_MIN
            and c[1] < COL_MAX,
            [
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1),
            ],
        )

        paper_count = sum(grid[c[0]][c[1]] == "@" for c in adjacent)
        if paper_count < 4:
            accessible += 1

print(accessible)
