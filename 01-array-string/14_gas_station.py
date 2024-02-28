"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diffs = [gas[i]-cost[i] for i in range(n)]
        if sum(diffs) >= 0:
            i = 0
            while i < n:
                if diffs[i] >= 0:
                    summ = 0
                    j = i
                    while summ >= 0 and j < n:
                        summ += diffs[j]
                        j += 1
                    if j == n:
                        return i
                    else:
                        i = j-1
                i += 1
        
        return -1
        