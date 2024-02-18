"""[[ MEDIUM ]]"""
class Solution:
    def canJump(self, nums):
        j = 0
        for num in nums:
            if j < 0:
                return False
            if num > j:
                j = num
            j -= 1        
        return  True



if __name__ == '__main__':
    nums = [2,3,1,1,4]
    # nums = [3,2,1,0,4]
    s = Solution()
    result = s.canJump(nums)
    print('result =', result)
