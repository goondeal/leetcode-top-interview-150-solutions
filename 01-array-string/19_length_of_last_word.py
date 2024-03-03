"""[[ EASY ]]"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        Approach:
            Start from the end of [s], Get the first non-space char.
            From it, Count the non-space chars towards the start of [s] or till you face a space char.

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        # Get the first non-space char from the end.
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count the non-space chars
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
