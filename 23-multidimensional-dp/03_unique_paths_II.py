"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[n-1][m-1] == 1:
            return 0
        result = [[None for _ in range(m)] for _ in range(n)]
        for c in range(m-1, -1, -1):
            for r in range(n-1, -1, -1):
                neighbors = [1] if r == n-1 and c == m-1 else []
                # right
                if c < m-1 and obstacleGrid[r][c+1] == 0 and result[r][c+1] > 0:
                    neighbors.append(result[r][c+1])
                # bottom
                if r < n-1 and obstacleGrid[r+1][c] == 0 and result[r+1][c] > 0:
                    neighbors.append(result[r+1][c])
                result[r][c] = max(sum(neighbors), len(neighbors))
                # print(r, c, neighbors, result)
        return result[0][0]


if __name__ == '__main__':
    s = Solution()
    # print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(s.uniquePathsWithObstacles([[0, 1], [0, 0]]))
    print(s.uniquePathsWithObstacles([[0, 0], [0, 1]]))
