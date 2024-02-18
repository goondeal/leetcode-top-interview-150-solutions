"""[[ EASY ]]"""
class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n < 3:
            return n
        end = n
        prev, current = 0, 2
        while current < end:
            if nums[current] == nums[prev]:
                i, j = current, current+1
                while j < end:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                end -= 1    
            else:
                prev += 1 
                current += 1
        return end


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    nums = [0,0,1,1,1,1,2,3,3]
    s = Solution()
    result = s.removeDuplicates(nums)
    print('nums =', nums)
    print('result =', result)
