"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def _get_adjacents(self, grid, row, col, res):
        m, n = len(grid), len(grid[0])
        if grid[row][col] == '1':
            # print('row =', row, 'col =', col)
            res.add((row, col))
            # top
            if row > 0 and (row-1, col) not in res:
                self._get_adjacents(grid, row-1, col, res)
            # bottom
            if row < m-1 and (row+1, col) not in res:
                self._get_adjacents(grid, row+1, col, res)
            # left
            if col > 0 and (row, col-1) not in res:
                self._get_adjacents(grid, row, col-1, res)
            # right
            if col < n-1 and (row, col+1) not in res:
                self._get_adjacents(grid, row, col+1, res)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        map_dict = {(i, j): grid[i][j] for i in range(m) for j in range(n)}
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) in map_dict:
                    result += 1
                    print(i, j, result)
                    adj = set()
                    self._get_adjacents(grid, i, j, adj)
                    print(adj)
                    for pos in adj:
                        if pos in map_dict:
                            del map_dict[pos]
        return result


if __name__ == '__main__':
    s = Solution()
    print(
        s.numIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ]
        )
    )  # 1
    print(
        s.numIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ]
        )
    )  # 3
