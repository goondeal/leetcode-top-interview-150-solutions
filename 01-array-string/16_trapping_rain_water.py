"""[[ HARD ]]"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Approach:
            For each bar in [height], Calculate the max height of water it can hold above it.
            That height of water equals the minimum of: max bar height until it (including it), and max bar height after it (including it).   
            The pure water height above each bar equals total water height minus the bar height.
            Steps:
                1) Construct 2 lists [max_befor], and [max_after] of the same size of [height].
                2) Traverse [height] and calculate for each bar, the max bar height before it (inclusive), and the max bar height after it (inclusive).
                3) Calculate pure water heights.
                4) Return result, which equals sum of pure water heights.
                
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        n = len(height)
        if n < 3:
            return 0

        max_before = [height[0]] * n
        max_after = [height[-1]] * n
        for i in range(1, n):
            idx = n - 1 - i
            max_before[i] = max(height[i], max_before[i-1])
            max_after[idx] = max(height[idx], max_after[idx+1])

        water_height = [min(max_before[i], max_after[i]) - height[i]
                        for i in range(n)]
        return sum(water_height)
        

if __name__ == '__main__':
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(s.trap([4, 2, 0, 3, 2, 5]))  # 9
