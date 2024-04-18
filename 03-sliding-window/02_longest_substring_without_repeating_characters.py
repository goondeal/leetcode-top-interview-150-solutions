"""[[ MEDIUM ]]"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Algorithm:
            1) Initialize 2 pointers i, j to use as a sliding window to loop through the string.
            2) Use a hash set to track the repeating chars.
            3) Track the max_len.

        Notice that the last line is for an edge case in which the length of the input is 1.

        Time Complexity: O(n)
        space Complexity: O(n)
        '''
        n = len(s)
        i = 0
        j = 0
        log = set()
        max_len = 0
        while i < n and j < n:
            if s[j] in log:
                length = j - i
                if length >= max_len:
                    max_len = length
                log.remove(s[i])
                i += 1
            else:
                log.add(s[j])
                j += 1
        return max(len(log), max_len)
