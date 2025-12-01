with open("./input.txt") as f:
    lines = f.read().split()

current = 50
zero_count = 0
for line in lines:
    direction = 1 if line[0] == "R" else -1
    magnitude = int(line[1:])
    diff = direction * magnitude
    new = current + diff

    if new > current:
        passes = new // 100 - current // 100
    else:
        passes = (current - 1) // 100 - (new - 1) // 100

    zero_count += passes

    current = new % 100

print(zero_count)
