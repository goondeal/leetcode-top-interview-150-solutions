"""[[ HARD ]]"""
"""[[ MEDIUM ]]"""




from typing import List
class Solution:
    def _add_once(self, d, val):
        if val in d:
            d[val] += 1
        else:
            d[val] = 1


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words)
        l = len(words[0])

        result = []
        word_dict = {}
        for w in words:
            self._add_once(word_dict, w)

        i = j = 0
        history = {}

        while i <= n-l:
            # print(i, j, history)
            while j - i <= m*l:
                w = s[j:j+l]
                if history.get(w, 0) < word_dict.get(w, 0):
                    self._add_once(history, w)
                    j += l
                    # print(i, j, history)
                else:
                    break
            
            if history == word_dict:
                result.append(i)
            i += 1
            j = i
            history = {}
            
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
