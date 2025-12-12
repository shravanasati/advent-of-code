import heapq
from itertools import combinations
import math

with open("./input.txt") as f:
    coordinates = f.read().split()
threshold = 1000


# coordinates = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689
# """.split()
# threshold = 10

coordinates = list(map(lambda x: tuple(map(int, x.split(","))), coordinates))

point = tuple[int, ...]


def distance_3d(p1: point, p2: point):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

n_coords = len(coordinates)

circuits: list[set[tuple[int, ...]]] = [set([p]) for p in coordinates]

smallest_pairs = sorted(
    combinations(coordinates, 2), key=lambda p: distance_3d(p[0], p[1])
)
for i in range(len(smallest_pairs)):
    p1, p2 = smallest_pairs[i]
    print(p1, p2)

    c1 = next(c for c in circuits if p1 in c)
    c2 = next(c for c in circuits if p2 in c)
    if c1 is not c2:
        c1.update(c2)
        circuits.remove(c2)

    circuit_size = max(len(c) for c in circuits)
    if circuit_size == n_coords:
        print(p1[0] * p2[0])
        break
