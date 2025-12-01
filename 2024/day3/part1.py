from functools import reduce
from operator import mul
import re

with open("./input.txt") as f:
    content = f.read()

# content = """
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# """

pattern = re.compile(r"mul\((\d+),(\d+)\)")
answer = sum((reduce(mul, map(int, match.groups()))) for match in pattern.finditer(content))
print(answer)
