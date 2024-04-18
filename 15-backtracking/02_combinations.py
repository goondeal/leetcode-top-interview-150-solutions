"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        pointers = list(range(k))
        result = []
        while pointers[0] <= n - k:
            # print(pointers)
            result.append([nums[pointers[i]] for i in range(k)])
            pointers[-1] += 1

            i = k - 1
            while i > -1 and pointers[i] > n-k+i:
                pointers[i-1] += 1
                i -= 1
            
            for i in range(1, k):
                if pointers[i] > n-k+i:
                    pointers[i] = pointers[i-1] + 1
            
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
    print(s.combine(1, 1))
    print(s.combine(5, 3))
