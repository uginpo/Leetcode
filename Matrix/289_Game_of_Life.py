def gameOfLife(board: list[list[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    M = len(board)
    N = len(board[0])

    for row in board:
        print(row)
    print()

    for i in range(M):
        for j in range(N):
            count = live_neighbors(board, i, j)
            if board[i][j] == 0 and count == 3:
                board[i][j] = 2
            elif board[i][j] == 1 and (count < 2 or count > 3):
                board[i][j] = 3

    for i in range(M):
        for j in range(N):
            match board[i][j]:
                case 2:
                    board[i][j] = 1
                case 3:
                    board[i][j] = 0

    for row in board:
        print(row)


def live_neighbors(board, i, j) -> int:
    M = len(board)
    N = len(board[0])
    res = 0
    top = i-1 if i != 0 else 0
    bottom = i+2 if i != M-1 else M
    left = j-1 if j != 0 else 0
    right = j+2 if j != N-1 else N

    for row in range(top, bottom):
        for column in range(left, right):
            a = board[row][column]
            res += 0 if (a == 0 or a == 2) else 1

    res -= board[i][j]
    return res


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
# output [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
gameOfLife(board)

"""
1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""
