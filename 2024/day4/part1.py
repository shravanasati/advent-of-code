with open("./input.txt") as f:
    content = f.read().splitlines()

content = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".splitlines()


def row_search(mat: list[str]):
    count = 0
    for row in mat:
        count += row.count("XMAS")
        count += row.count("SAMX")
    return count


def column_search(mat: list[str]):
    count = 0
    transposed = [
        "".join([mat[i][j] for i in range(len(mat))]) for j in range(len(mat[0]))
    ]

    for col in transposed:
        count += col.count("XMAS")
        count += col.count("SAMX")
    return count


# def diagonal_search(mat: list[str]):
#     diagonals = []
#     n = len(mat) - 1
#     ptr = [n, 0]
#     for _ in range(2 * len(mat) - 1):
#         ptr[0] += -1