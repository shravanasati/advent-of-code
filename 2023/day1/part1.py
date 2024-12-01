def _find_first_number(s: str) -> str:
    for i in s:
        if i.isdigit():
            return i

    return "0"


def leftmost(s: str):
    return _find_first_number(s)


def rightmost(s: str):
    return _find_first_number(s[::-1])


if __name__ == "__main__":
    # N = 4
    # inputs: list[str] = []
    # for _ in range(N):
    #     inputs.append(input())

    with open("./input.txt") as f:
        inputs = f.read().splitlines()

    sum_ = 0
    for inp in inputs:
        sum_ += int(f"{leftmost(inp)}{rightmost(inp)}")
    print(sum_)
