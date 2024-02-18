"""[[ EASY ]]"""
class Solution:
    def majorityElement(self, nums):
        c = 1
        num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != num:
                if c == 0:
                    num = nums[i]
                    c += 1
                else:
                    c -= 1
            else:
                c += 1
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement(nums=[3, 2, 3]))
    print(s.majorityElement(nums=[2,2,1,1,1,2,2]))
