"""[[ MEDIUM ]]"""
class Solution:
    def _calc_area(self, arr, i, j):
        w = j - i
        h = min(arr[i], arr[j])
        return w * h
    
    def _get_next_greater(self, arr, start, end):
        k = start + 1
        while k < end and arr[k] <= arr[start]:
            k += 1
        return k

    def _get_last_greater(self, arr, start, end):
        k = end - 1
        while k > start and arr[k] <= arr[end]:
            k -= 1
        return k

    def maxArea(self, height):
        n = len(height)
        i, j = 0, n-1
        area = self._calc_area(height, i, j)
        while i < j:
            if height[i] < height[j]:
                i = self._get_next_greater(height, i, j)
            elif height[j] < height[i]:
                j = self._get_last_greater(height, i, j)
            else:
                i = self._get_next_greater(height, i, j)
                j = self._get_last_greater(height, i, j)
            a = self._calc_area(height, i, j)
            area = max(area, a)
        return area


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    result = s.maxArea(height)
    print('result =', result)
