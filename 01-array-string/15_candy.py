"""[[ HARD ]]"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        Approach:
            Construct a result list of ones with the same size of [ratings]. congrats! you fulfilled the first condition.
            To fulfill the second condition:
                Traverse [ratings] forward (left-to-right). If a ratings[i] > ratings[i-1] give it one more candy in [result] than its neighbor (result[i] = result[i-1] + 1)
                Traverse [ratings] backward (right-to-left). If a ratings[i] > ratings[i+1] give it one more candy (if needs) in [result] than its neighbor.

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        n = len(ratings)
        # Construct result list
        result = [1] * n
        # Traverse ratings forward
        for i in range(1, n):
            # If higher rating, give one more candy.
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1] + 1

        # Traverse ratings backward
        for i in range(n-2, -1, -1):
            # If higher rating, give one more candy (if needed).
            if ratings[i] > ratings[i+1]:
                result[i] = max(result[i], result[i+1] + 1)

        return sum(result)


if __name__ == '__main__':
    s = Solution()
    print(s.candy([1, 0, 2]))  # 5
    print(s.candy([1, 2, 2]))  # 4
    print(s.candy([1, 3, 2, 2, 1]))  # 7
    print(s.candy([1, 2, 87, 87, 87, 2, 1]))  # 13
    print(s.candy([1, 3, 4, 5, 2]))  # 11
