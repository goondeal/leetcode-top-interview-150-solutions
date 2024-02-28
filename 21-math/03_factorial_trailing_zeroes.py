"""[[ MEDIUM ]]"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        Algorithm:
            - Trailing zeros of the factorial of n is the number of (2,5) pairs of the factorial series (1,2, ..., n-1, n)
                taking into account the multiplicity. For exabmle 25 is the multiplication of 2 fives.
            - number of 2s is always bigger than or equals the 5s. So, Count the fives.
        
        See the discussions on this problems:
            - https://leetcode.com/problems/factorial-trailing-zeroes/discuss/?currentPage=1&orderBy=hot&query=
        
        Time Complexity: O(log5(n))
        Space Complexity: O(1)
        '''
        result = 0
        num = n // 5
        while num > 0:
            result += num
            num //= 5
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes(3))
    print(s.trailingZeroes(5))
    print(s.trailingZeroes(0))
    print(s.trailingZeroes(10))
    print(s.trailingZeroes(25))
