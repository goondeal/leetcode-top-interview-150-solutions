"""[[ MEDIUM ]]"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Approach:
            Brute-force approach using a heap.

        Time Complexity: O(nlg(n))
        Space Complexity: O(n)
        '''
        h = []
        for x in nums:
            heapq.heappush(h, x)
        return heapq.nlargest(k, h)[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], k = 2)) # 5
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], k = 4)) # 4
