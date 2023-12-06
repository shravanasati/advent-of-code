import re


WORDS_TO_NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    # "zero": 0,
}


def _find_all_numbers(s: str):
    initial = 0
    pattern = r"(" + r"\d|" + r"|".join(WORDS_TO_NUMBERS.keys()) + r")"
    regex = re.compile(pattern)
    numbers = []
    position = 1
    while position < len(s) + 1:
        substring = s[initial:position]
        if match := regex.search(substring):
            matched_str = match.group(0)
            if matched_str.isdigit():
                numbers.append(int(matched_str))
            else:
                numbers.append(WORDS_TO_NUMBERS[matched_str])
                position -= 1
            initial = position

        position += 1

    return numbers


if __name__ == "__main__":
    # N = 7
    # inputs: list[str] = []
    # for _ in range(N):
    #     inputs.append(input())

    with open("./input.txt") as f:
        inputs = f.read().splitlines()

    # inputs = ["hzdlftdtfqfdbxgsix9onetwo13"]

    # print(len(inputs))

    sum_ = 0
    for inp in inputs:
        numbers = _find_all_numbers(inp)
        calibration_number = numbers[0] * 10 + numbers[-1]
        print(inp, calibration_number)
        sum_ += calibration_number

    print(sum_)