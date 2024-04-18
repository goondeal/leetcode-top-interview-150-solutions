"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        Algorithm:
            Minimum number of arrows is the total number of intersected parts in overlaping intervals.
            See "merge intervals" problem

        Time Complexity: O(nlg(n))
        Time Complexity: O(n)
        '''
        n = len(points)
        if n < 2:
            return n
        sorted_points = sorted(points, key=lambda i: i[0])
        print(sorted_points)
        _min, _max = [x for x in sorted_points[0]]
        count = 1
        for i in sorted_points:
            if i[0] <= _max:
                _min = max(_min, i[0])
                _max = min(_max, i[1])
            else:
                _min, _max = i
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])) # 2
