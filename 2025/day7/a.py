from pprint import pprint

with open("./input.txt") as f:
    diagram = f.read().split()

# diagram = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............
# """.split()

diagram = list(map(list, diagram))
N = len(diagram)
M = len(diagram[0])

beam = [diagram[0].index("S")]

split_count = 0
for i in range(1, N):
    line = diagram[i]
    splitters = [j for j, char in enumerate(line) if char == "^"]
    splitter_set = set(splitters)

    new_beam = set()
    for splitter_index in splitters:
        # only split if there's actually a beam hitting this splitter
        if splitter_index in beam:
            if splitter_index - 1 >= 0:
                new_beam.add(splitter_index - 1)
            if splitter_index + 1 < M:
                new_beam.add(splitter_index + 1)

    considerable_splitters = [s for s in splitters if s in beam]
    split_count += len(considerable_splitters)

    # remove beams that hit splitters, add the new split beams
    beam = [b for b in beam if b not in splitter_set]
    beam.extend(new_beam)

    for b in beam:
        line[b] = "|"

pprint(diagram)
print(split_count)
