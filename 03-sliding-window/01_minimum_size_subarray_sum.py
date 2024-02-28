"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        Algorithm:
            It's easy to get the brute force algorithm but it is O(n^2).
            So, instead of adding the numbers at each move, just store the sum and add to or subtract from it
            when moving the window (i, j).
            1) Initialize 2 pointers i, j to use as a sliding window to loop through the [nums].
            2) Track the sum of the sliding window by storing it in a variable.
            3) Track the max_len.

        Notice the initialization value of [min_len], and the last line.
        That is for an edge case in which the [target] is grater than the sum of all [nums].

        Time Complexity: O(n)
        space Complexity: O(1)
        '''
        n = len(nums)
        i = 0
        j = 0
        summ = 0
        min_len = n + 1
        while i < n and j < n:
            summ += nums[j]
            if summ >= target:
                length = j - i + 1
                if length < min_len:
                    min_len = length
                summ -= nums[i]
                summ -= nums[j]
                i += 1
            else:
                j += 1

        return 0 if min_len > n else min_len


if __name__ == '__main__':
    s = Solution()
    result = s.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3])
    print('result =', result)
