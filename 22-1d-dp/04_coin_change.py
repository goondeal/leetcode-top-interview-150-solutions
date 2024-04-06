"""[[ MEDIUM ]]"""
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        Approach:
            Full explaination: https://www.youtube.com/watch?v=H9bfqozjoqs&ab_channel=NeetCode
        
        Time Complexity: O(amount*len(coins))
        Space Complexity: O(amount)
        '''
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1], 0)) # 0
    print(s.coinChange([2], 3)) # -1
    print(s.coinChange([1,2,5], 11)) # 3
    print(s.coinChange([186,419,83,408], 6249)) # 20
    print(s.coinChange([1, 3, 5, 6], 26)) # 5
    print(s.coinChange([244,125,459,120,316,68,357,320], 9793)) # 23
