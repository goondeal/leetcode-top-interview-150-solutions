"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def _to_be_flipped(self, grid, row, col, res):
        m, n = len(grid), len(grid[0])
        if grid[row][col] == 'O':
            if row in {0, m-1} or col in {0, n-1}:
                return False
            res.add((row, col))
            if row > 0 and (row-1, col) not in res and not self._to_be_flipped(grid, row-1, col, res):
                return False

            if row < m-1 and (row+1, col) not in res and not self._to_be_flipped(grid, row+1, col, res):
                return False

            if col > 0 and (row, col-1) not in res and not self._to_be_flipped(grid, row, col-1, res):
                return False

            if col < n-1 and (row, col+1) not in res and not self._to_be_flipped(grid, row, col+1, res):
                return False
        return True
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                res = set()
                region = self._to_be_flipped(board, i, j, res)
                if region:
                    for pos in res:
                        board[pos[0]][pos[1]] = 'X'
