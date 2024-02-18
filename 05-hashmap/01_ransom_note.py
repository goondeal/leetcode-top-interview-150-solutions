"""[[ EASY ]]"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_dict = {}
        magazine_dict = {}
        for c in ransomNote:
            note_dict[c] = note_dict.get(c, 0) + 1
        for c in magazine:
            magazine_dict[c] = magazine_dict.get(c, 0) + 1
        for key in note_dict:
            if note_dict[key] > magazine_dict.get(key, 0):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct(ransomNote='a', magazine='b'))  # false
    print(s.canConstruct(ransomNote='aa', magazine='ab'))  # false
    print(s.canConstruct(ransomNote='aa', magazine='aab'))  # true
    print(s.canConstruct(ransomNote='aab', magazine='baa'))  # true
