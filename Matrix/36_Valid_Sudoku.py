import numpy as np


def isValidSudoku(board: list[list[str]]) -> bool:
    sudoku = np.array(board)
    for i in range(9):
        row = sudoku[i]
        row = row[row != '.']
        if len(row) != len(set(row)):
            return False

        column = sudoku[:, i]
        column = column[column != '.']
        if len(column) != len(set(column)):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            m_b = sudoku[i:i+3, j:j+3]
            m_b = m_b[m_b != '.']
            if len(m_b) != len(set(m_b)):
                return False
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# true

print(isValidSudoku(board))
