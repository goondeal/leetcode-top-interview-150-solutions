"""[[ MEDIUM ]]"""
class Solution:
    def _binary_search(self, arr, low, high, x):
        if high >= low:    
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self._binary_search(arr, low, mid - 1, x)
            else:
                return self._binary_search(arr, mid + 1, high, x)
        return -1

    def twoSum(self, numbers, target):
        n = len(numbers)
        for i in range(n):
            j = self._binary_search(numbers, i+1, n-1, target-numbers[i])
            if j != -1:
                return [i+1, j+1]


if __name__ == '__main__':
    # nums, target = [2,7,11,15], 9
    nums, target = [2,3,4], 6
    s = Solution()
    result = s.twoSum(nums, target)
    print('result =', result)
