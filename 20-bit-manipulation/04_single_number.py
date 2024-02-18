"""[[ EASY ]]"""
from typing import List
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda t, n: t^n, nums)


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         s = set()
#         for x in nums:
#             if x in s:
#                 s.remove(x)
#             else:
#                 s.add(x)
#         return list(s)[0]
