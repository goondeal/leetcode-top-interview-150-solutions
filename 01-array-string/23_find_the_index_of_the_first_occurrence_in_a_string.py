"""[[ EASY ]]"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        
        if m > n:
            return -1
        
        i = 0
        while i < n:
            j = 0
            while j < m and i+j < n and haystack[i+j] == needle[j]:
                j += 1
            if j == m:
                return i
            i += 1
        return -1
