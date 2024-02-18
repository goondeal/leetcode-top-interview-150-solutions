"""[[ EASY ]]"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        m, n = len(s), len(t)
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m


if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence(s='ace', t='abcde'))  # true
    print(s.isSubsequence(s='aec', t='abcde'))  # false
    print(s.isSubsequence(s='abc', t='ahbgdc'))  # true
    print(s.isSubsequence(s='axc', t='ahbgdc'))  # false
