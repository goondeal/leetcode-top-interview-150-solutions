"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        Approach:
        Full explaination: https://www.youtube.com/watch?v=fxT9KjakYPM&ab_channel=NeetCodeIO

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        total = 0
        cur_max, cur_min = 0, 0
        max_sum, min_sum = nums[0], nums[0]

        for x in nums:
            total += x
            cur_max = max(cur_max + x, x)
            cur_min = min(cur_min + x, x)
            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)
        return max_sum if max_sum < 0 else max(max_sum, total - min_sum)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubarraySumCircular([-2]))  # -2
    print(s.maxSubarraySumCircular([1, -2, 3, -2]))  # 3
    print(s.maxSubarraySumCircular([5, -3, 5]))  # 10
    print(s.maxSubarraySumCircular([-3, -2, -3]))  # -2
    print(s.maxSubarraySumCircular([0, 5, 8, -9, 9, -7, 3, -2]))  # 16
    print(s.maxSubarraySumCircular([-92, 78, -45, -63, 1, 34, 81, 50, 14, 91, -77, -54, 13, -88, 24, 37, -12, 59, -48, -62, 57,
                                    -22, -8, 85, 48, 71, 12, 1, -20, 36, -32, -14, 39, 46, -41, 75, 13, -
                                    23, 98, 10, -88, 64, 50, 37, -95, -32, 46, -91, 10, 79, -11, 43,
                                    -94, 98, 79, 42, 51, 71, 4, -30, 2, 74, 4, 10, 61, 98, 57, 98, 46, 43, -
                                    16, 72, 53, -69, 54, -96, 22, 0, -7, 92, -69, 80, 68, -73, -24,
                                    -92, -21, 82, 32, -1, -6, 16, 15, -29, 70, -66, -85, 80, 50, -3]))  # 1437
