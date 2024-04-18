"""[[ HARD ]]"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        # Ensure nums1 is the smaller array
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        n = n1 + n2
        half = (n1 + n2) // 2  # the half size
        low, high = 0, n1 - 1
        while True:
            mid1 = (low + high) // 2
            mid2 = half - mid1 - 2

            l1 = nums1[mid1] if mid1 >= 0 else float('-inf')
            r1 = nums1[mid1 + 1] if mid1 + 1 < n1 else float('inf')
            l2 = nums2[mid2] if mid2 >= 0 else float('-inf')
            r2 = nums2[mid2 + 1] if mid2 + 1 < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                # partition is correct
                if n % 2 == 1:
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                # Move towards the left side of nums1
                high = mid1 - 1
            else:
                # Move towards the right side of nums1
                low = mid1 + 1


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([0, 0], [0, 0]))  # 0
    print(s.findMedianSortedArrays([1, 2], [3, 4]))  # 2.5
    print(s.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))  # 5.5
    print(s.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8]))  # 5
    print(s.findMedianSortedArrays([2, 2, 4, 4], [2, 2, 4, 4]))  # 3
