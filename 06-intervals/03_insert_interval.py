"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Algorithm:
            1) Make a new [result] list.
            2) Traverse [intervals] till you find the index to insert in the [newInterval].
                This is the index where newInterval[0] <= intervals[i][0].
            3) While you did not reach the insertion index push the intervals you pass into [result].
            4) Push the [newInterval] into [result] paying attention to possible merge.
            5) Push the remaining intervals into [result] paying attention to possible merges.
            6) Reassign [intervals] to [result] and return it.
        
        Time Complexity: O(n)
        Time Complexity: O(n)

        Notes:
            - Since [intervals] is sorted, and to optimize the silution,
                Binary search can be used to find the insertion index, but it stills O(n).
            - [newInterval] is going to be merged into [result] as the same way as
                the second part of [intervals] after the insertion index.
                So, instead of code duplication, and since the [intervals] is going to be dropped any way,
                Considered the [newInterval] is the first interval of the second part of [intervals] and merge all.

        '''
        n = len(intervals)

        result = []
        # find the insertion place.
        i = 0
        while i < n and newInterval[0] > intervals[i][0]:
            result.append(intervals[i])
            i += 1
        
        # set newInterval to be ready to merge it into result with the remaining intervals. 
        if n == 0 or i == 0:
            result.append(newInterval)
        else:
            intervals[i-1] = newInterval
            i -= 1
        # merge the remaining intervals (including newInterval) into result.
        while i < n:
            if intervals[i][0] <= result[-1][1]:
                result[-1][0] = min(result[-1][0], intervals[i][0])
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
            i += 1
        # reassign and return
        intervals = result
        return intervals


if __name__ == '__main__':
    s = Solution()
    print(s.insert([[1,3],[6,9]], [2,5])) # [[1,5],[6,9]]
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,2],[3,10],[12,16]]
    print(s.insert([], [5,7])) # [[5,7]]
    print(s.insert([[1,5]], [1,7])) # [[1,7]]
