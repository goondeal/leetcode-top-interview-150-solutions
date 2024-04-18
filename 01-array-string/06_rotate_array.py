"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = nums[:]
        for i in range(n):
            idx = (i+k) % n
            nums[idx] = arr[i]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = nums[:]
        for i in range(n):
            idx = (i+k) % n
            nums[idx] = arr[i]
