"""[[ EASY ]]"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Approach:
            Use 2 pointers i, and j where i is the place to set in the first greater num you face with j.
            Traverse the [nums] with j till you find a num greater than nums[i], then get it to i+1 index, and move the pointers.

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        n = len(nums)
        if n < 2:
            return n
        
        i, j = 0, 1
        # loop till you find an int which is greater than the currrent (nums[i])
        while j < n:
            if nums[j] <= nums[i]:
                j += 1
            else:
                # When found, replace it in the right order which is [i+1].
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1
        
        return i + 1


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,1,2,2,3])) # 3
    print(s.removeDuplicates([0,0,1,1,1,1,2,3,3])) # 4
