"""[[ EASY ]]"""
from typing import List


class Solution:
    def _get_commen_prefix_two_strs(self, s1: str, s2: str) -> str:
        n = min(len(s1), len(s2))
        i = 0
        while i < n and s1[i] == s2[i]:
            i += 1
        return s1[:i]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Approach:
            Using variable [common_prefeix] to track the longest common prefix,
            Traverse [strs] and update the [common_prefeix] to be the common prefix between
                [common_prefeix] and current str of [strs].
            Return [common_prefeix]
            
        Time Complexity: O(n*s) ; n=len(strs), s=max([len(str) for str in strs])
        Space Complexity: O(s)
        '''
        n = len(strs)
        if n == 0:
            return ''
        
        common_prefix = strs[0]
        i = 1
        while i < n and common_prefix:
            common_prefix = self._get_commen_prefix_two_strs(common_prefix, strs[i])
            i += 1

        return common_prefix
