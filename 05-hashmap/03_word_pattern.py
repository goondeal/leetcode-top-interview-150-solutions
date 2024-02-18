"""[[ EASY ]]"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        history = {}
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if words[i] in history:
                if pattern[i] != history[words[i]]:
                    return False
            else:
                history[words[i]] = pattern[i]
        return len(history) == len(set(history.values()))


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordPattern(pattern="abba", s="dog cat cat dog"))  # true
    print(sol.wordPattern(pattern="abba", s="dog cat cat fish"))  # false
    print(sol.wordPattern(pattern="aaaa", s="dog cat cat dog"))  # false
