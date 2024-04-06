"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def perm(self, store, nums, result):
        n = len(nums)
        # print(nums)
        if n == 1:
            store.append(nums[0])
            result.append(store)
        else:
            for i in range(n):
                self.perm(store+[nums[i]], nums[:i]+nums[i+1:], result)
    

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.perm([], nums, result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
