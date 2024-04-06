"""[[ MEDIUM ]]"""
class Solution:
    def _is_palindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n-1-i]:
                return False
        return True
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = s[0]
        for i in range(n):
            for j in range(n, i, -1):
                if j - i > len(result) and self._is_palindrome(s[i:j]):
                    result = s[i:j]
                    break
        return result
    

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
