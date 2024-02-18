"""[[ EASY ]]"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = []
        
        for c in s:
            if c.isalnum():
                s_alnum.append(c.lower())
        
        n = len(s_alnum)
        for i in range(n//2):
            if s_alnum[i] != s_alnum[n-1-i]:
                return False
        return True
