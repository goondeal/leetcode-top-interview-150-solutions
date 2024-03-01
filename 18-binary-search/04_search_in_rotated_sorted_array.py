"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            # Decide which part of [nums] is sorted.
            if nums[mid] >= nums[low]:
                if nums[low] <= target <= nums[mid]:
                    # The left part of [nums] is sorted, and if the target exists, It must be in this part.
                    high = mid - 1
                else:
                    # If the target exists, It can not be in this part.
                    low = mid + 1
            
            # The right part of [nums] is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    # If the target exists, It must be in this part.
                    # So, search in it.
                    low = mid + 1
                else:
                    # If the target exists, It can not be in this part.
                    # So, drop it and search in the other part.
                    high = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums=[4,5,6,7,0,1,2], target=0))
    print(s.search(nums=[4,5,6,7,0,1,2], target=3))
    print(s.search(nums=[1], target=3))


