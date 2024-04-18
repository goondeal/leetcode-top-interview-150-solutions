"""[[ HARD ]]"""
from typing import List
from heapq import heappop, heappush


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_capital = w
        profits_heap = []
        store_heap = []
        for i in range(len(profits)):
            heappush(profits_heap, (-profits[i], capital[i]))
        
        for i in range(k):
            if not profits_heap:
                break
            tmp = max_capital
            while profits_heap:
                p = heappop(profits_heap)
                if p[1] <= max_capital:
                    max_capital += -p[0]
                    break
                else:
                    heappush(store_heap, p)
            if max_capital == tmp:
                break
            if len(store_heap) < len(profits_heap):
                for i in range(len(store_heap)):
                    heappush(profits_heap, heappop(store_heap))
            else:
                for i in range(len(profits_heap)):
                    heappush(store_heap, heappop(profits_heap))
                profits_heap, store_heap = store_heap, profits_heap
            
        return max_capital


if __name__ == '__main__':
    s = Solution()
    print(s.findMaximizedCapital(2, 0, [1,2,3], [0, 1, 1])) # 4
    print(s.findMaximizedCapital(3, 0, [1,2,3], [0, 1, 2])) # 6
