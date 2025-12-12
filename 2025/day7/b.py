from pprint import pprint

with open("./input.txt") as f:
    diagram = f.read().split()

diagram = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".split()

diagram = list(map(list, diagram))
N = len(diagram)
M = len(diagram[0])

# Track (position, timeline_count) - how many timelines have a particle at each position
# Using a dict: position -> number of timelines with a particle there
timelines = {diagram[0].index("S"): 1}

for i in range(1, N):
    line = diagram[i]
    splitters = set(j for j, char in enumerate(line) if char == "^")

    new_timelines = {}
    for pos, count in timelines.items():
        if pos in splitters:
            left = pos - 1
            right = pos + 1
            if left >= 0:
                new_timelines[left] = new_timelines.get(left, 0) + count
            if right < M:
                new_timelines[right] = new_timelines.get(right, 0) + count
        else:
            new_timelines[pos] = new_timelines.get(pos, 0) + count

    timelines = new_timelines

total_timelines = sum(timelines.values())
print(total_timelines)
