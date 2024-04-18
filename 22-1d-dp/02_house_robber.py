"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Approach:
            At any num of [nums], the best (max) you can get is the maximum of: max you can get at the next number,
            and the sum of num with the max at the second next element.
            Traverse the [nums] from the end to the start to calculate the max of the first num.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        n = len(nums)
        a, b = 0, 0
        for i in range(n):
            x = nums[n-1-i]
            a, b = max(x+b, a), a 
        return a
