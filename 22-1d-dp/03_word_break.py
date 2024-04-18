"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        words = set(wordDict)
        for i in range(n-1, -1, -1):
            dp[i] = s[i:] in words or any([s[i:j] in words for j in range(i, n) if dp[j]])
        return dp[0]


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode", wordDict = ["leet","code"])) # true
    print(s.wordBreak("applepenapple", wordDict = ["apple","pen"])) # true
    print(s.wordBreak("catsandog", wordDict = ["cats","dog","sand","and","cat"])) # false
    print(s.wordBreak("catsandog", ["cat","cats","dog","an"])) # true
    print(s.wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])) # false
