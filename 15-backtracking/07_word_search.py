"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def _get_neighbors(self, board, pos, pos_history):
        n, m = len(board), len(board[0])
        row, col = pos
        result = []
        # top
        if row > 0 and (row-1, col) not in pos_history:
            result.append((row-1, col))
        # bottom
        if row < n-1 and (row+1, col) not in pos_history:
            result.append((row+1, col))
        # left
        if col > 0 and (row, col-1) not in pos_history:
            result.append((row, col-1))
        # right
        if col < m-1 and (row, col+1) not in pos_history:
            result.append((row, col+1))
        return result
    
    def _search_word(self, board, pos, word, i, pos_history):
        n = len(word)
        row, col = pos
        if i == n-1:
            return word[i] == board[row][col]
        else:
            if word[i] == board[row][col]:
                pos_history.add(pos)
                return any([self._search_word(board, p, word, i+1, pos_history.copy()) for p in self._get_neighbors(board, pos, pos_history)])
            else:
                return False
            
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        return any([self._search_word(board, (i, j), word, 0, set()) for i in range(n) for j in range(m)])


if __name__ == '__main__':
    s = Solution()
    print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")) # True
    print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")) # True
    print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")) # False
