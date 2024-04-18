"""[[ MEDIUM ]]"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        n = self.node
        word_len = len(word)
        for i in range(word_len):
            idx = ord(word[i]) - ord('a')
            if n.children[idx]:
                if i == word_len - 1:
                    n.children[idx].is_end_of_word = True
            else:
                n.children[idx] = TrieNode()
                n.children[idx].is_end_of_word = i == word_len - 1
            n = n.children[idx]
        

    def search(self, word: str) -> bool:
        n = self.node
        word_len = len(word)
        for i in range(word_len):
            idx = ord(word[i]) - ord('a')
            n = n.children[idx]
            if not n or (i == word_len-1 and not n.is_end_of_word):
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        n = self.node
        for i in range(len(prefix)):
            idx = ord(prefix[i]) - ord('a')
            n = n.children[idx]
            if not n:
                return False
        return True


# Requirements message sent to Applicants before the interview
# 	Any Database editor installed
# 	any development langauge editor installed
