from aocd import get_data

data = get_data(day=8, year=2022).split("\n")

matrix = []
matrix_list = []
for idx, line in enumerate(data):
    matrix_list = []
    for idx, integer in enumerate(line):
        matrix_list.append(int(integer))
    matrix.append(matrix_list)


taller_than = []
visible_trees = 0


for row_idx, row in enumerate(matrix):
    for col_idx, col in enumerate(row):
        if any(
            [
                all(
                    [
                        row[col_idx] > row[character]
                        for character in range(col_idx + 1, len(row))
                    ]
                ),
                all(
                    [
                        row[col_idx] > row[character]
                        for character in range(col_idx - 1, -1, -1)
                    ]
                ),
                all(
                    [
                        matrix[row_idx][col_idx] > matrix[character][col_idx]
                        for character in range(row_idx - 1, -1, -1)
                    ]
                ),
                all(
                    [
                        matrix[row_idx][col_idx] > matrix[character][col_idx]
                        for character in range(row_idx + 1, len(row))
                    ]
                ),
            ]
        ):
            visible_trees += 1

print(visible_trees)
