"""[[ EASY ]]"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        history = {}
        for i in range(len(nums)):
            if nums[i] in history:
                if i - history[nums[i]] <= k:
                    return True
            history[nums[i]] = i
        return False

if __name__ == '__main__':
    nums, k = [1,2,3,1], 3
    s = Solution()
    result = s.containsNearbyDuplicate(nums, k)
    print('result =', result)
