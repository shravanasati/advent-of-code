with open("./input.txt") as f:
	lines = f.read().split()

current = 50
zero_count = 0
for line in lines:
	current += (1 if line[0] == 'R' else -1) * int(line[1:])
	current %= 100
	if current == 0:
		zero_count += 1

print(zero_count)