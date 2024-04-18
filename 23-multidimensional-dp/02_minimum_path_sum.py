"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        result = [[None for _ in range(m)] for _ in range(n)]
        for c in range(m-1, -1, -1):
            for r in range(n-1, -1, -1):
                neighbors = []
                # right
                if c < m-1:
                    neighbors.append(result[r][c+1])
                # bottom
                if r < n-1:
                    neighbors.append(result[r+1][c])
                result[r][c] = grid[r][c] + min(neighbors if neighbors else [0])
        return result[0][0]

if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
