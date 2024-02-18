"""[[ EASY ]]"""
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)-1):
            num = map.get(s[i])
            next = map.get(s[i+1])
            result += -num if num < next else num

        return result + map.get(s[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))  # 3
    print(s.romanToInt('LVIII'))  # 58
    print(s.romanToInt('MCMXCIV'))  # 1994
