"""[[ MEDIUM ]]"""
class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        p = abs(n)
        res = self.myPow(x*x, p//2) * (1 if p % 2 == 0 else x)
        return res if n > 0 else 1/res


if __name__ == '__main__':
    x, n = 2, -2
    s = Solution()
    result = s.myPow(x, n)
    print('result =', result)
