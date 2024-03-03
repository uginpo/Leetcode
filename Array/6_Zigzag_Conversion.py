
def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    result = [''] * numRows
    index, step = 0, 1

    for char in s:
        result[index] += char

        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1

        index += step

    return ''.join(result)


s = "ABCDE"
numRows = 2
s = "PAYPALISHIRING"

s = "PAYPALISHIRING"
numRows = 3
numRows = 4

print(convert(s, numRows))

"""
P   A   H   N
A P L S I I G
Y   I   R
"""
# PAHNAPLSIIGYIR

"""
P     I    N
A   L S  I G
Y A   H R
P     I
"""
# PINALSIGYAHRPI
