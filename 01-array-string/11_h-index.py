"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)        
        citations_sorted = sorted(citations)
        h_index = 0
        for i in range(n):
            h = min(n-i, citations_sorted[i])
            if h >= h_index:
                h_index = h
        return h_index
