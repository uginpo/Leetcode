def setZeroes(matrix: list[list[int]]) -> None:

    zero_dict = {"i": set(),
                 "j": set()}

    for row in matrix:
        print(row)
    print()

    M = len(matrix)
    N = len(matrix[0])

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                zero_dict['i'].add(i)
                zero_dict['j'].add(j)

    i_lst = zero_dict['i']
    j_lst = zero_dict['j']
    for i in i_lst:
        for j in range(N):
            matrix[i][j] = 0

    for i in range(M):
        for j in j_lst:
            matrix[i][j] = 0

    print(f'{zero_dict=}')

    for row in matrix:
        print(row)

    return None


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]

setZeroes(matrix)
