"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows_to_change = set()
        cols_to_change = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_change.add(i)
                    cols_to_change.add(j)
        for r in rows_to_change:
            matrix[r] = [0] * n
        for c in cols_to_change:
            for i in range(m):
                matrix[i][c] = 0
