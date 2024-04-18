"""[[ MEDIUM ]]"""
class Solution:
    def groupAnagrams(self, strs):
        history = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in history:
                history[key].append(word)
            else:
                history[key] = [word]
        
        return list(history.values())


if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    s = Solution()
    result = s.groupAnagrams(strs)
    print('result =', result)
