"""[[ HARD ]]"""
class Solution:
    def _add_once(self, d, val):
        d[val] = d.get(val, 0) + 1

    def _remove_once(self, d, val):
        if val in d:
            if d[val] < 2:
                del d[val]
            else:
                d[val] -= 1

    def minWindow(self, s: str, t: str) -> str:
        '''
        Approach:
            1) Build a dictionary for chars in t along with their frequency to handle duplicates.
            2) Initialize 2 variables: "have" to track how many characters you fulfilled in the window,
                and "need" as the count of distinct chars in t that you need to fulfill in the window.
            3) Loop through each char in s and try to fulfill a complete window starts from its place, If found,
                compare its length to the existing result and reassign the result if the length is shorter.
        
        Time Complexity: O(n*m); where n is len(s), and m is len(t)
        Space Complexity: O(m)
        '''
        s_len = len(s)
        t_len = len(t)

        if t_len > s_len:
            return ''

        # Build a dictionary of chars in [t] and their frequency.
        char_dict = {}
        for c in t:
            self._add_once(char_dict, c)

        result = [-1, -1]
        result_len = s_len + 1
        have, need = 0, len(char_dict)
        history = {}
        j = 0
        for i in range(s_len-t_len+1):
            if s[i] in char_dict:
                while j < s_len:
                    c = s[j]
                    if c in char_dict:
                        self._add_once(history, c)
                        if history[c] == char_dict[c]:
                            have += 1
                        if have == need:
                            j += 1
                            break
                    j += 1
                while s_len+1 > j > i+1:
                    c = s[j-1]
                    if c in char_dict:
                        if history.get(c, 0) - 1 >= char_dict[c]:
                            self._remove_once(history, c)
                        else:
                            break
                    j -= 1
                if have == need:
                    if j - i < result_len:
                        result = [i, j]
                        result_len = j - i

                self._remove_once(history, s[i])
                if history.get(s[i], 0) < char_dict[s[i]]:
                    have -= 1
        return s[result[0]: result[1]] if result_len < s_len+1 else ''


if __name__ == '__main__':
    s = Solution()

    # # print(s.minWindow('ADOBECODEBANC', 'ABC'))
    assert (s.minWindow('ADOBECODEBANC', 'ABC') == 'BANC')
    # # # print(s.minWindow('a', 'a'))
    assert (s.minWindow('a', 'a') == 'a')  # a
    assert (s.minWindow('a', 'aa') == '')  # ''
    assert (s.minWindow('abc', 'ac') == 'abc')  # abc
    # # # # print(s.minWindow('ab', 'a'))
    assert (s.minWindow('ab', 'a') == 'a')  # a

    # # # print(s.minWindow('aaaaaaaaaaaabbbbbcdd', 'abcdd'))
    assert (s.minWindow('aaaaaaaaaaaabbbbbcdd', 'abcdd') == 'abbbbbcdd')
    # # print(s.minWindow('cabwefgewcwaefgcf', 'cae')) # cwae
    assert (s.minWindow('cabwefgewcwaefgcf', 'cae') == 'cwae')  # cwae
    assert (s.minWindow('aa', 'aa') == 'aa')  # aa
    assert (s.minWindow('bdab', 'ab') == 'ab')  # ab
    # # print(s.minWindow('acbba', 'aab')) # acbba
    assert (s.minWindow('acbba', 'aab') == 'acbba')  # acbba
    # print(s.minWindow('bbaac', 'aba'))  # acbba
    assert(s.minWindow('bbaac', 'aba') == 'baa') # acbba
