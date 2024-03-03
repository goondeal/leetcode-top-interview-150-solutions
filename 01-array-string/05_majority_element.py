"""[[ EASY ]]"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Approach:
            Using variables [num] to track the majority element, and [c] to track the count of that element.
            Traverse [nums] elements and increase [c] by one if element equals [num] or decrease [c] by one otherwise.
            Reassign [num] when [c] equals 0
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        c = 1
        num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != num:
                if c == 0:
                    num = nums[i]
                    c += 1
                else:
                    c -= 1
            else:
                c += 1
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement(nums=[3, 2, 3]))
    print(s.majorityElement(nums=[2,2,1,1,1,2,2]))
