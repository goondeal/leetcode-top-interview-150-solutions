"""[[ HARD ]]"""
from typing import List


class Solution:
    def _add_once(self, d, val):
        d[val] = d.get(val, 0) + 1


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        Approach:
            Build a word dictionary contains words and their frequencies.
            Slide the window on [s] and build a similar dictionary for it.
            Compare the 2 dictionaries and if the window is valid, append that location to result.
            
        Time Complexity: O(m*n); where m is len(s), and n is len(words)
        Space Complexity: O(m + n)
        '''
        # Get word length and window length.
        word_len = len(words[0])
        window_len = len(words) * word_len

        # Build a dictionary of words and their frequency.
        word_dict = {}
        for w in words:
            self._add_once(word_dict, w)

        result = []
        # Slide the window on the string.
        for i in range(len(s) - window_len + 1):
            j = i
            # Build a dictionary of words in the window.
            history = {}
            while j - i < window_len:
                w = s[j:j+word_len]
                # The word must be in word_dict and does not exceed the frequency.
                if history.get(w, 0) < word_dict.get(w, 0):
                    self._add_once(history, w)
                    j += word_len
                else:
                    break
            # If valid window
            if j - i == window_len: # same as: if history == word_dict:
                result.append(i)
            
        return result


if __name__ == '__main__':
    s = Solution()
    print(
        s.findSubstring(
            s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]
        )  # []
    )
    print(
        s.findSubstring(
            s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]
        )  # [6, 9, 12]
    )
    print(
        s.findSubstring(
            s="barfoothefoobarman", words=["bar", "foo"]
        )  # [0, 9]
    )
    print(
        s.findSubstring(
            s="wordgoodgoodgoodbestword", words=["word", "good", "best", "good"]
        )  # [8]
    )
    print(
        s.findSubstring(
            s="aaaaaaaaaaaaaa", words=["aa", "aa"]
        )  # [0,1,2,3,4,5,6,7,8,9,10]
    )
