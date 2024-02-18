"""[[ EASY ]]"""
class Solution:
    def summaryRanges(self, nums) -> bool:
        i = 1
        n = len(nums)
        result = []
        if n > 0:
            a = nums[0]
            b = None
            while i < n:
                if nums[i] == nums[i-1] + 1:
                    b = nums[i]
                else:
                    result.append(str(a) + (f'->{b}' if b != None else ''))
                    a = nums[i]
                    b = None
                i += 1
            result.append(str(a) + (f'->{b}' if b != None else ''))
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.summaryRanges())  # true
