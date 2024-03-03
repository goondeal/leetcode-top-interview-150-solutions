"""[[ EASY ]]"""
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Approach:
            watch this video (https://www.youtube.com/watch?v=Y0lT9Fck7qI&ab_channel=NeetCode)
            to figure out how this problem diverged to fibonacci series.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        a, b = 1, 1

        for _ in range(n-1):
            a, b = a+b, a
        
        return a
