"""[[ MEDIUM ]]"""
class Solution:
    def _min_jumps(self, nums, history={}, start=0):
        if history.get(start) != None:
            return history.get(start)
        n = len(nums) - start
        num = nums[start]
        if n == 1:
            result = 0
        elif num == 0:
            result = n + start
        elif num >= n-1:
            result = 1
        else:
            result = 1 + min([self._min_jumps(nums, history, start+i) for i in range(num, 0, -1)])
        history[start] = result
        return result

    def jump(self, nums):
        return self._min_jumps(nums, history={}, start=0)


if __name__ == '__main__':
    s = Solution()
    for nums in [[2,3,1,1,4], [2,3,0,1,4], [0], [1,2,3]]:
        result = s.jump(nums)
        print('result =', result)
