"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def _index_to_2d_index(self, idx, n):
        return divmod(idx, n)
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Algorithm:
            Consider the input matrix as if it was a list of the rows of the matrix inline.
            Then use binary search to search for the target in it.
        
        
        Notes:
            The helper method "_index_to_2d_index" calculate the matrix index (2D) from a list index (1D).
            For example: index=11 (0-based) in a list of length=12 is row=2, col=3 (0-based) of 3x4 matrix.
        
        Time Complexity: O(lg(m*n))
        Space Complexity: O(1)
        '''
        m, n = len(matrix), len(matrix[0])
        low = 0
        high = m * n - 1
        while low <= high:
            mid = (low + high) // 2
            row, col = self._index_to_2d_index(mid, n)
            num = matrix[row][col]
            if num > target:
                high = mid - 1
            elif num < target:
                low = mid + 1
            else: # num == target
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3))
    print(s.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=13))
