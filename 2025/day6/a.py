import numpy as np

# content = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """.split("\n")

with open("./input.txt") as f:
    content =f.read().splitlines()


numbers = []
for line in content[:-1]:
    numbers.append(list(map(int, line.split())))

operators = np.array(content[-1].split())

numbers = np.array(numbers)

sum_mask = operators == "+"
product_mask = operators == "*"

sum_columns = numbers[:, sum_mask]
product_columns = numbers[:, product_mask]

sum_result = np.sum(sum_columns, axis=0)
product_result = np.prod(product_columns, axis=0)

final_result = np.empty(numbers.shape[1], dtype=numbers.dtype)
final_result[sum_mask] = sum_result
final_result[product_mask] = product_result
print(np.sum(final_result))
