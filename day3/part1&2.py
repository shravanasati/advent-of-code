from functools import reduce
import operator
import re

with open("./input.txt") as f:
    matrix = f.read().splitlines()
# matrix = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """.splitlines()

XMAX = len(matrix[0])
YMAX = len(matrix)
number_regex = re.compile(r"\d+")
symbol_regex = re.compile(r"\$|#|%|\/|@|-|\*|\+|\&|\=")
star_regex = re.compile(r"\*")
# keeps a record of indices of star with a list of adjacent numbers
star_table: dict[tuple[int, int], list[int]] = {}
part_sum = 0
for i, line in enumerate(matrix):
    numbers = number_regex.finditer(line)
    for num in numbers:
        jstart, jend = num.span()
        jend -= 1  # ? num.span() returns end index 1 extra
        above_diagonal_start = (i - 1, jstart - 1)
        above_diagonal_end = (i - 1, jend + 1)
        below_diagonal_start = (i + 1, jstart - 1)
        below_diagonal_end = (i + 1, jend + 1)
        coordinates = [
            (i, jstart - 1),
            (i, jend + 1),
            above_diagonal_start,
            above_diagonal_end,
            below_diagonal_start,
            below_diagonal_end,
        ]
        # add all column indices in between diagonals
        for ci in range(above_diagonal_start[1] + 1, above_diagonal_end[1]):
            coordinates.append((above_diagonal_start[0], ci))
        for ci in range(below_diagonal_start[1] + 1, below_diagonal_end[1]):
            coordinates.append((below_diagonal_start[0], ci))
        coordinates = filter(
            lambda t: t[0] > 0 and t[1] > 0 and t[0] < XMAX and t[1] < YMAX,
            coordinates,
        )
        for x, y in coordinates:
            if star_regex.match(matrix[x][y]):
                if star_table.get((x, y)):
                    star_table[(x, y)].append(int(num.group()))
                else:
                    star_table[(x, y)] = [int(num.group())]
            if symbol_regex.match(matrix[x][y]):
                # print(num.group())
                part_sum += int(num.group())
                break


print(part_sum)
print(sum([reduce(operator.mul, v) for _, v in star_table.items() if len(v) > 1]))
