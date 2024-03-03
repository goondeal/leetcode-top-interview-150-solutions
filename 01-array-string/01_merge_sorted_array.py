"""[[ EASY ]]"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.

        Approach:
            Since the arrays are sorted, max elements are at the end.
            1) So, compare the max element of [nums1] with the max element of [nums2].
            2) Set the max of them in the end of allocated spaces (trailing zeros) in nums1.
            3) pick the next element to compare.
            4) Repeat.

        Time Complexity: O(m+n)
        Space Complexity: O(1)
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0 and i >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    s.merge(nums1=nums1, m=3, nums2=nums2, n=3)
    print(nums1)
