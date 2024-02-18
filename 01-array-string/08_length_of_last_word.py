"""[[ EASY ]]"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1

        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord('hello  world'))
    print(s.lengthOfLastWord('     '))
    print(s.lengthOfLastWord('   fly me   to   the moon  '))
    print(s.lengthOfLastWord('luffy is still joyboy'))
