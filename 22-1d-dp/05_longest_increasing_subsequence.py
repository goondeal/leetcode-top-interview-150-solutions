"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        max_seq_count = [1] * n
        for i in range(n-2, -1, -1):
            max_ = 0
            for j in range(i+1, n):
                if nums[j] > nums[i] and max_seq_count[j] > max_:
                    max_ = max_seq_count[j]
            max_seq_count[i] += max_
        return max(max_seq_count)
