"""[[ MEDIUM ]]"""
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        Approach:
            1) Construct a heap of pairs that are each element of [nums1] with the first element of [nums2].
            2) For k times:
                1) Pop the minimum pair sum from the heap.
                2) Append this pair to [result].
                3) Push the next pair (with the same first element of the just-poped one) into the heap.
            3) Return result.

        Time Complexity: O( max(n1, klg(n1)) )
        Space Complexity: O(n)
        '''
        n1, n2 = len(nums1), len(nums2)
        result = []
        h = []

        for i in range(n1):
            heapq.heappush(h, (nums1[i]+nums2[0], [i, 0]))

        for _ in range(k):
            # Get min pair sum, and append it to the result.
            e = heapq.heappop(h)
            idx1, idx2 = e[1]
            result.append([nums1[idx1], nums2[idx2]])

            if idx2 < n2 - 1:
                heapq.heappush(
                    h, (nums1[idx1] + nums2[idx2+1], [idx1, idx2+1]))

        return result


if __name__ == '__main__':
    s = Solution()
    # [[1,2],[1,4],[1,6]]
    print(s.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))

    # [[1, 1], [1, 1]]
    print(s.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))

    # [[-10,3],[-10,5],[-10,6],[-10,7],[-10,8],[-4,3],[-4,5],[-4,6],[-4,7],[0,3]]
    print(s.kSmallestPairs(
        nums1=[-10, -4, 0, 0, 6],
        nums2=[3, 5, 6, 7, 8, 100],
        k=10
    ))
