"""[[ MEDIUM ]]"""
class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        result = 0
        for num in nums:
            if num in s:
                res = 1
                s.remove(num)
                x = 1
                while num+x in s:
                    res += 1
                    s.remove(num+x)
                    x += 1
                x = 1
                while num-x in s:
                    res += 1
                    s.remove(num-x)
                    x += 1
            if res > result:
                result = res
        return result
        

if __name__ == '__main__':
    # nums = [100,4,200,1,3,2]
    nums = [0,3,7,2,5,8,4,6,0,1]
    s = Solution()
    result = s.longestConsecutive(nums)
    print('result =', result)
