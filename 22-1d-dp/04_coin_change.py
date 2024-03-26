"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount == 0:
        #     return 0
        sorted_coins = sorted(coins, reverse=True)
        print(sorted_coins)
        result = 0
        # while amount > 0:
        divs = []
        mods = []
        for coin in sorted_coins:
            div, mod = divmod(amount, coin)
            divs.append(div)
            mods.append(mod)

            # result += div
            # amount = mod
            # print('coin =', coin, 'result =', result, 'amount =', amount)
            # if amount == 0:
            #     break
        print(divs)
        print(mods)
        # return result if not amount else -1
    
if __name__ == '__main__':
    s = Solution()
    # print(s.coinChange([1], 0)) # 0
    # print(s.coinChange([2], 3)) # -1
    # print(s.coinChange([1,2,5], 11)) # 3
    print(s.coinChange([186,419,83,408], 6249)) # 20
