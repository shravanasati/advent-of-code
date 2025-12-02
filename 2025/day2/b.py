with open("./input.txt") as f:
    ranges = f.read().split(",")

# ranges = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124""".split(",")


def is_invalid(n: int) -> bool:
    ns = str(n)
    return ns in (ns + ns)[1:-1]

invalid_counter = 0
for range_ in ranges:
    lower, upper = map(int, range_.split("-"))
    for i in range(lower, upper + 1):
        if is_invalid(i):
            invalid_counter += i

print(f"{invalid_counter=}")
