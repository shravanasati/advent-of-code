from functools import reduce
from operator import mul
import re

with open("./input.txt") as f:
    content = f.read()

# content = """
# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# """

mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
dont_pattern = re.compile(r"don't\(\)")
do_pattern = re.compile(r"do\(\)")

enabled = True
pointer = 0
while pointer < len(content):
    ...
