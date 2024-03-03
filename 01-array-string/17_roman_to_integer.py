"""[[ EASY ]]"""
class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        Approach:
            Use dictionary of convertions.
            Traverse [s] and get each char value from the dictionary.
            Add to or subtract from the result, this value, depending on the next char value.
            Return the result
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)-1):
            num = dictionary.get(s[i])
            next = dictionary.get(s[i+1])
            result += -num if num < next else num

        return result + dictionary.get(s[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))  # 3
    print(s.romanToInt('LVIII'))  # 58
    print(s.romanToInt('MCMXCIV'))  # 1994
