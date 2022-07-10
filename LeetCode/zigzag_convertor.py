# link: https://leetcode.com/problems/zigzag-conversion/

import math
def zigzag_convertor(s, numRows=1):
    """
    encode string s by its zigzag version, and it works as follows:

    s = "PAYPALISHIRING"
    numRows = 3

    encoded string:
    P    A     H     N
    A  P L  S  I  I  G
    Y    I     R

    read it line by line: PAHNAPLSIGYIR

    Parameters
    ----------
    s: str
        A string

    numRows: int, default 1
        Number of rows for distributing the letters in zigzag manner

    Returns
    -------
    out: str
        encoded string through zigzag conversion
    """
    if len(s) == 1 or numRows == 1 or numRows >= len(s):
        return s

    # calculate number of columns
    # `n` is numRows.
    # n + n-2 + n + n-2 + n + n-2
    # 1 (n - 1) + 1
    # 2 (n - 1)
    # 3 (n - 1) + 1
    # 4 (n - 1)
    # 5 (n - 1) + 1

    n_s = len(s)
    numCols = math.ceil((n_s - 1) / (numRows - 1))

    lst = [[None] * numCols for _ in range(numRows)]

    i = 0
    j = 0
    for x in s:
        lst[i][j] = x

        r = j % numRows
        if (r == 0 or r == numRows - 1) and (i < numRows - 1):
            i += 1
        else:
            i -= 1
            j += 1


    encoded_s = ""
    for i in range(numRows):
        for j in range(numCols):
            if lst[i][j] is not None:
                encoded_s += lst[i][j]

    return encoded_s
