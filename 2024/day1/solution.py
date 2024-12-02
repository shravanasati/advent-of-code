from collections import Counter


with open("./input.txt") as f:
    content = f.read().splitlines()

l1: list[int] = []
l2: list[int] = []

for line in content:
    num1, num2 = map(int, line.split())
    l1.append(num1)
    l2.append(num2)

l1.sort()
l2.sort()

distance_sum = sum([abs(l1[i] - l2[i]) for i in range(len(l1))])
print(distance_sum)

# part 2
l2_count = Counter(l2)
similarity_score_sum = sum((n * l2_count[n]) for n in l1)
print(similarity_score_sum)
