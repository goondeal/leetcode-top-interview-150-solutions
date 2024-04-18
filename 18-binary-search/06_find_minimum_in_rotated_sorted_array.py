"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= nums[mid-1]:
                return nums[mid]
            
            # Decide which part of [nums] is sorted.
            if nums[mid] >= nums[low]:
                if nums[low] <= nums[high]:
                    # The left part of [nums] is sorted, and if the target exists, It must be in this part.
                    high = mid - 1
                else:
                    # If the target exists, It can not be in this part.
                    low = mid + 1
            
            # The right part of [nums] is sorted
            else:
                if nums[mid] <= nums[high]:
                    # If the target exists, It must be in this part.
                    # So, search in it.
                    high = mid - 1
                else:
                    # If the target exists, It can not be in this part.
                    # So, drop it and search in the other part.
                    low = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findMin(nums=[3,4,5,1,2]))
    print(s.findMin(nums=[4,5,6,7,0,1,2]))
    print(s.findMin(nums=[5,1,2,3,4]))
    print(s.findMin(nums=[2,1]))
    print(s.findMin(nums=[1]))
