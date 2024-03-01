"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        Approach:
            * Normal binary search but with the condition of a peak element (previous_element < peak and next_element < peak).
            * Take into account the edge cases (first and last elements of the array),
                where you compare only one adjacent element
        
        Time Complexity: O(lg(n))
        Space Complexity: O(1)
        '''
        n = len(nums)
        if n == 1:
            return 0
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            num = nums[mid]
            prev_num = nums[mid-1]
            next_num = nums[min(n-1,mid+1)]
            if (mid == 0 or num > prev_num) and (mid == n-1 or num > next_num):
                return mid
            elif mid < n-1 and num < next_num:
                low = mid + 1
            else: #if mid > 0 and num < prev: # num == target
                high = mid - 1
        return False
