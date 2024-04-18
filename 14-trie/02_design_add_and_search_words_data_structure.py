"""[[ MEDIUM ]]"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.node = TrieNode()
        

    def addWord(self, word: str) -> None:
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
        

    def _dfs(self, node, word, start):
        n = len(word)
        c = word[start]
        if start == n - 1:
            if c == '.':
                return any([child.is_end_of_word for child in node.children if child])
            else:
                idx = ord(word[start]) - ord('a')
                return node.children[idx] and node.children[idx].is_end_of_word
        
        if c == '.':
            children = [child for child in node.children if child]
            if not children:
                return False
            for child in children:
                if self._dfs(child, word, start+1):
                    return True
        else:
            idx = ord(word[start]) - ord('a')
            next_node = node.children[idx]
            return next_node and self._dfs(next_node, word, start+1)
        
    def search(self, word: str) -> bool:
        node = self.node
        return self._dfs(node, word, 0)
    