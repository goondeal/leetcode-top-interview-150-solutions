"""[[ HARD ]]"""
from typing import List


class Solution:
    def _search(self, board, word):
        pass

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        char_set = set()
        for row in board:
            char_set |= set(row)
        
        result = []
        for word in words:
            if self._search(board, word):
                result.append(word)
        return result

