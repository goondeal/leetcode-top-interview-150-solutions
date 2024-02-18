"""[[ EASY ]]"""
class Solution:
    def removeElement(self, nums, val):
        """
        Algorithm:
            Traverse the array linearly, if the element has value equals [val],
            replace it with the next non-val element.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count


if __name__ == '__main__':
    nums, val = [0,1,2,2,3,0,4,2], 2
    # nums, val = [3,2,2,3], 3
    # nums, val = [1], 1
    s = Solution()
    result = s.removeElement(nums, val)
    print('nums =', nums)
    print('result =', result)
    print('nums_result =', nums[:result])
