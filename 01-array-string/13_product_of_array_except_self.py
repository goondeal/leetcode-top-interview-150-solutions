"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Given that division is not allowed.
        Algorithm:
            1) Construst 2 new arrays with the same length of [nums], 
                products_before: that holds the product of the numbers preceding each num in [nums].
                products_after: that holds the product of the numbers succeeding each num in [nums].
            2) The result of the product-except-self for each ith num is products_before[i] * products_after[i].
            3) Calculate and return the result.
        
        Time Complexity: O(n)
        space Complexity: O(n)
        '''
        
        n = len(nums)
        
        products_before = [1] * n
        for i in range(1, n):
            products_before[i] = nums[i-1] * products_before[i-1]
        
        products_after = [1] * n
        for i in range(n-2, -1, -1):
            products_after[i] = nums[i+1] * products_after[i+1]
        
        result = []
        for i in range(n):
            result.append(products_before[i]*products_after[i])
        return result
        