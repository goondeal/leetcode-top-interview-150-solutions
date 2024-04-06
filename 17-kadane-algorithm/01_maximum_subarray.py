"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Approach:
            Start with a growing window and calculate the sum when adding each new element.
            If the sum is negative, start a new window.

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        max_sum = nums[0]
        cur_sum = 0
        for x in nums:
            cur_sum = max(0, cur_sum)
            cur_sum += x
            max_sum = max(max_sum, cur_sum)
        return max_sum
