def rotate(matrix: list[list[int]]) -> None:
    N = len(matrix)
    for row in matrix:
        print(row)

    for i in range(N):
        for j in range(i+1, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print()
    for row in matrix:
        print(row)

    for i in range(N):
        for j in range(N//2):
            matrix[i][j], matrix[i][N-j-1] = matrix[i][N-j-1], matrix[i][j]

    print()
    for row in matrix:
        print(row)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

rotate(matrix)
"[[7,4,1],[8,5,2],[9,6,3]]"
