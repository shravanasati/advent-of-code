from collections import defaultdict, deque

with open("./input.txt") as f:
    devices = f.read().splitlines()
# devices = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out
# """.splitlines()

device_map: dict[str, set[str]] = defaultdict(set)

for device_line in devices:
    device, outputs = device_line.split(":")
    device_map[device.strip()].update(outputs.split())

visited = set[str]()
queue = deque(["you"])
paths = 0

while queue:
    device = queue.popleft()
    if device in visited:
        continue

    visitable_devices = device_map[device]
    if "out" in visitable_devices:
        paths += 1

    queue.extend(visitable_devices)

print(paths)
