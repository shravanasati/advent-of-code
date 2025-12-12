from math import prod
from pathlib import Path


def chunk_columns(columns):
    """Yield contiguous non-empty column groups, splitting on all-space columns."""
    current = []
    for column in columns:
        if all(char == " " for char in column):
            if current:
                yield current
                current = []
            continue
        current.append(column)
    if current:
        yield current


def column_value(column, digit_rows):
    digits = [char for char in column[:digit_rows] if char != " "]
    if not digits:
        return None
    return int("".join(digits))


def solve_problem(columns, digit_rows):
    operator = next((col[-1] for col in columns if col[-1] in {"+", "*"}), None)
    if operator is None:
        raise ValueError("Operator missing for problem")

    values = [
        value
        for column in reversed(columns)
        if (value := column_value(column, digit_rows)) is not None
    ]
    if operator == "+":
        return sum(values)
    return prod(values)


def main():
    input_path = Path(__file__).with_name("input.txt")
    rows = input_path.read_text().splitlines()
    if not rows:
        raise ValueError("Empty worksheet")

    width = max(len(row) for row in rows)
    padded_rows = [row.ljust(width) for row in rows]
    digit_rows = len(padded_rows) - 1
    if digit_rows <= 0:
        raise ValueError("Worksheet missing operator row")

    columns = list(zip(*padded_rows))
    total = sum(
        solve_problem(problem, digit_rows) for problem in chunk_columns(columns)
    )
    print(total)


if __name__ == "__main__":
    main()
