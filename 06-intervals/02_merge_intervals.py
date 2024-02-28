"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Algorithm:
            1) sort intervals.
            2) traverse the sorted intervals searching for any overlapping intervals to merge
            and push the result to the results list.
        
        Time Complexity: O(nlg(n)) # cost of sorting
        Time Complexity: O(n)
        '''
        n = len(intervals)
        if n < 2:
            return intervals
        sorted_intervals = sorted(intervals, key=lambda i: i[0])
        result = [sorted_intervals[0]]
        for i in sorted_intervals:
            if i[0] <= result[-1][1]:
                result[-1][0] = min(result[-1][0], i[0])
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)
        return result
        

if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3], [2,6], [8,10], [15,18]])) # [[1,6], [8,10], [15,18]]
    print(s.merge([[1,4], [4,5]])) # [[1,5]]
    print(s.merge([[1,4], [0,0]])) # [[0,0], [1,4]]
