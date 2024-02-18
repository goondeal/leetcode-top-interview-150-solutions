"""[[ EASY ]]"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        start = 0
        end = x
        while start < end:
            num = (start + end) // 2
            r = num*num
            if r == x:
                return num
            else:
                if r > x:
                    end = num
                else:
                    if start == num:
                        return num
                    start = num  
        return end                  
