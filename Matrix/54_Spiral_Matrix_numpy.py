import numpy as np


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    if len(matrix) == 0:
        return []

    new_array = []
    matrix = np.array(matrix)
    while True:
        if len(matrix) == 0:
            break
        row = list(matrix[0])
        new_array.extend(row)
        print(f'{new_array=}')
        matrix = matrix[1:]
        matrix = np.rot90(matrix)
    print(matrix)

    return new_array


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(spiralOrder(matrix))
