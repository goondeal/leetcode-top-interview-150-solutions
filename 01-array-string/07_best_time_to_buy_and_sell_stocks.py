"""[[ EASY ]]"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Approach:
            Traverse [prices] to find the minimum and the maximum elements of [prices] where the minimum preceeds the maximum.
            [max_profit] is the difference between them.

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        buy = sell = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            x = prices[i]
            if x > sell:
                sell = x
                max_profit = max(max_profit, sell - buy)
            if x < buy:
                buy = sell = x

        return max_profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
