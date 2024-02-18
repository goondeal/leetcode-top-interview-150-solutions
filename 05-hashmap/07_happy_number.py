"""[[ EASY ]]"""
class Solution:
    def isHappy(self, n: int) -> bool:
        nums_square = {str(num): num*num for num in range(10)}
        num = (n*n) if len(str(n)) == 1 else n
        while len(str(num)) > 1:
            print('num =', num)
            num = sum([nums_square[digit] for digit in str(num)])
        return num in {1, 7}


if __name__ == '__main__':
    sol = Solution()
    print(sol.isHappy(19))  # true
    print(sol.isHappy(234))  # true
    print(sol.isHappy(5))  # true
    print(sol.isHappy(1111111))  # true
