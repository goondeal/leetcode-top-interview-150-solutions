"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Approach:
            Explaination here:
                https://leetcode.com/problems/single-number-ii/discuss/4824352/Explained-With-A-Story
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        x, y = 0, 0
        for num in nums:
            x = (x ^ num) & ~y
            y = (y ^ num) & ~x

        return x


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2,2,3,2]))
    print(s.singleNumber([0,1,0,1,0,1,99]))