"""[[ MEDIUM ]]"""
class Solution:
    def maxProfit(self, prices):
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
