"""[[ EASY ]]"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1
        res = 10
        while i > -1 and res > 9:
            res = digits[i] + 1
            if res > 9:
                digits[i] = 0
            else:
                digits[i] += 1
            i -= 1    
        if digits[0] == 0:
            digits[0] = 1
            digits.append(0)
        return digits
