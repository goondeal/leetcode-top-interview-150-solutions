"""[[ EASY ]]"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = [0] * 26
        freq_t = [0] * 26
        st = ord('a')
        
        for c in s:
            freq_s[ord(c)-st] += 1
        
        for c in t:
            freq_t[ord(c)-st] += 1
        
        return freq_s == freq_t
