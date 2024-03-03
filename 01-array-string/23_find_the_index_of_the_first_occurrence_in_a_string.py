"""[[ EASY ]]"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        Approach:
            Brute force algorithm.

        Time Complexity: O((n-m)*m); n=len(haystack), m=len(needle)
        Space Complexity: O(1)
        '''
        n = len(haystack)
        m = len(needle)
        
        if m > n:
            return -1
        
        i = 0
        while i <= n-m:
            j = 0
            while j < m and i+j < n and haystack[i+j] == needle[j]:
                j += 1
            if j == m:
                return i
            i += 1
        return -1
