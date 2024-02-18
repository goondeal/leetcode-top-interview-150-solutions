"""[[ EASY ]]"""
from typing import List

class Solution:
    def commen_prefix_two_strs(self, s1, s2):
        n = len(s1) if len(s1) < len(s2) else len(s2)
        i = 0
        while i < n and s1[i] == s2[i]:
            i += 1
        return s1[:i]    
            
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ''
        elif n == 1:
            return strs[0]
        else:
            common_prefix = self.commen_prefix_two_strs(strs[0], strs[1])
        
        i = 2
        while i < n and common_prefix != '':
            common_prefix = self.commen_prefix_two_strs(common_prefix, strs[i])
            i += 1
        
        return common_prefix
