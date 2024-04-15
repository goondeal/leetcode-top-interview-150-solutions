"""[[ HARD ]]"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        first_min = first_max = prices[0]
        second_min = second_max = prices[-1]
        first_half_profits = [0] * n
        second_half_profits = [0] * n
        max_profit = 0
        for i in range(1, n):
            p = prices[i]
            if p < first_min:
                first_min = first_max = p
            elif p > first_max:
                first_max = p
            first_half_profits[i] = max(first_half_profits[i - 1], first_max - first_min)
            
            back_index = n - 1 - i
            p = prices[back_index]
            if p < second_min:
                second_min = p
            elif p > second_max:
                second_min = second_max = p            
            second_half_profits[back_index] = max(second_half_profits[back_index + 1], second_max - second_min)
            if back_index <= n // 2:
                max_profit = max(max_profit, first_half_profits[i] + second_half_profits[i], first_half_profits[back_index] + second_half_profits[back_index])
        # print(first_half_profits)
        # print(second_half_profits)
        return max_profit # max([first_half_profits[i] + second_half_profits[i] for i in range(n)])



if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([3,3,5,0,0,3,1,4])) # 6
    print(s.maxProfit([1,2,3,4,5])) # 4
    print(s.maxProfit([7,6,4,3,1])) # 0
    print(s.maxProfit([1,2,4,2,5,7,2,4,9,0])) # 13
    print(s.maxProfit([1])) # 0
    print(s.maxProfit([1, 4])) # 3
