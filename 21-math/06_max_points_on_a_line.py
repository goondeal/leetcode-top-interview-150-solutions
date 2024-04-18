"""[[ HARD ]]"""
from typing import List


class Solution:
    def _is_line(self, p1, p2, p3):
        return (p1[1] - p2[1]) * (p1[0] - p3[0]) == (p1[1] - p3[1]) * (p1[0] - p2[0])
    
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        Algorithm:
            - Any 3 points p1, p3, and p3 form a line if the slop of p1 and p2 equals the slope of p1 and p3.
            - Using the brute force algorithm, as the input constraints allows that.
        
        Time Complexity: O(N^3)
        Space Complexity: O(1)

        Notes:
            - The helper method "_is_line" checks if a 3 points form a line by calculating the slopes.
                The used equation just compares the 2 slope fractions using multiplication instead of division
                to escape from any unexpected results with float division or comparison.
        '''
        n = len(points)
        if n < 3:
            return n
        
        result = 1
        for i in range(n-2):
            for j in range(i+1, n-1):
                points_count = 2
                for k in range(j+1, n):
                    if self._is_line(points[i], points[j], points[k]):
                        points_count += 1
                result = max(result, points_count)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxPoints([[1,1],[2,2],[3,3]])) # 3
    print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])) # 4
