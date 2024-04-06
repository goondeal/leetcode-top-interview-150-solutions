"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        nums = list(digits)
        n = len(nums)
        pointers = [0] * n
        result = []
        while pointers[0] < len(d[nums[0]]):
            # print(pointers)
            chars = [d[nums[i]][pointers[i] %
                                len(d[nums[i]])] for i in range(n)]
            result.append(''.join(chars))

            pointers[-1] += 1
            i = 1
            while i < n:
                # for i in range(n):
                idx = n - 1 - i
                div = pointers[idx+1] // len(d[nums[idx+1]])
                pointers[idx] = div
                i += 1
            # print('hello')
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
    print(s.letterCombinations(''))
    print(s.letterCombinations('2'))
