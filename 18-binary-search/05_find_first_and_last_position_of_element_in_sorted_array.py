"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def _get_first_index(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                if mid == 0 or nums[mid-1] != target:
                    return mid
                else:
                    high = mid - 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
    
    def _get_last_index(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                if mid == n-1 or nums[mid+1] != target:
                    return mid
                else:
                    low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums:
            first_index = self._get_first_index(nums, target)
            if first_index != -1:
                last_index = self._get_last_index(nums, target)
                return [first_index, last_index]
        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange(nums=[5,7,7,8,8,10], target=8))
    print(s.searchRange(nums=[5,7,7,8,8,10], target=6))
    print(s.searchRange(nums=[], target=6))
