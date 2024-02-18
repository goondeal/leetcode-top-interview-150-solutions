"""[[ EASY ]]"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else: # nums[mid] == target:
                return mid
        return low


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert(nums=[1,3,5,6], target=5)) # 2
    print(s.searchInsert(nums=[1,3,5,6], target=2)) # 1
    print(s.searchInsert(nums=[1,3,5,6], target=7)) # 4
    print(s.searchInsert(nums=[1,3,5,6], target=0)) # 0
    print(s.searchInsert(nums=[1], target=1)) # 0
