def isValidSudoku(board: list[list[str]]) -> bool:
    seen = set()
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                # print(seen)
                num = board[i][j]
                # Check row
                if (i, num) in seen:
                    print(seen)
                    return False
                seen.add((i, num))
                # Check column
                if (j+10, num) in seen:
                    print(seen)
                    return False
                seen.add((j+10, num))

                # Check subgrid
                if (i//3, j//3, num) in seen:
                    return False
                seen.add((i//3, j//3, num))

    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# true

print(isValidSudoku(board))
