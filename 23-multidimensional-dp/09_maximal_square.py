"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        max_square = 0
        i = 0
        while i < n - max_square:
            j = 0
            while j < m - max_square:
                if matrix[i][j] == '1':
                    tmp = 1
                    for k in range(min(n-i, m-j)-1):
                        if any([matrix[i+k+1][a] == '0' for a in range(j, j+k+2)]) \
                                or any([matrix[a][j+k+1] == '0' for a in range(i, i+k+2)]):
                            break
                        tmp += 1

                    max_square = max(max_square, tmp)
                j += 1
            i += 1
        return max_square ** 2


if __name__ == '__main__':
    s = Solution()
    print(s.maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
          "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))  # 4
    print(s.maximalSquare([["0", "0", "0", "1"], ["1", "1", "0", "1"], [
          "1", "1", "1", "1"], ["0", "1", "1", "1"], ["0", "1", "1", "1"]]))  # 9
    print(s.maximalSquare([
        ["1", "0", "1", "1", "0", "1"],
        ["1", "1", "1", "1", "1", "1"],
        ["0", "1", "1", "0", "1", "1"],
        ["1", "1", "1", "0", "1", "0"],
        ["0", "1", "1", "1", "1", "1"],
        ["1", "1", "0", "1", "1", "1"]
    ]))  # 4
