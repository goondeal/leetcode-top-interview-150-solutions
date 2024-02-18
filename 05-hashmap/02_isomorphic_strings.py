"""[[ EASY ]]"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        history = {}
        for i in range(len(s)):
            if s[i] in history:
                if t[i] != history[s[i]]:
                    return False
            else:
                history[s[i]] = t[i]
        return len(history) == len(set(history.values()))


if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic(s='egg', t='add'))  # true
    print(s.isIsomorphic(s='foo', t='bar'))  # false
    print(s.isIsomorphic(s='paper', t='title'))  # true
    print(s.isIsomorphic(s='bbbaaaba', t='aaabbbba'))  # false
    print(s.isIsomorphic(s='badc', t='baba'))  # false
