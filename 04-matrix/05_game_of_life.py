"""[[ MEDIUM ]]"""
class Solution:
    def _get_element_neighbors_count(self, board, i, j):
        m, n = len(board), len(board[0])
        result = [0, 0]

        # get top neighbor
        if i > 0:
            result[board[i-1][j]] += 1
            # get top-left neighbor
            if j > 0:
                result[board[i-1][j-1]] += 1
            # get top-right neighbor
            if j < n-1:
                result[board[i-1][j+1]] += 1
                
        # get bottom neighbor
        if i < m-1:
            result[board[i+1][j]] += 1
            # get bottom-left neighbor
            if j > 0:
                result[board[i+1][j-1]] += 1
            # get bottom-right neighbor
            if j < n-1:
                result[board[i+1][j+1]] += 1
                
        # get left neighbor
        if j > 0:
            result[board[i][j-1]] += 1
        # get right neighbor
        if j < n-1:
            result[board[i][j+1]] += 1

        return result    


    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        result = [row[:] for row in board]
        for i in range(m):
            for j in range(n):
                element = board[i][j]
                neighbors_count = self._get_element_neighbors_count(board, i, j)
                if element:
                    result[i][j] = 1 if neighbors_count[1] in {2, 3} else 0
                else:
                    result[i][j] = 1 if neighbors_count[1] == 3 else 0
        for i in range(m):
            for j in range(n):
                board[i][j] = result[i][j]
                

if __name__ == '__main__':
    board = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0],
    ]
    s = Solution()
    print('id =', id(board), 'board before =', board)
    s.gameOfLife(board)
    print('id =', id(board), 'board after =', board)
    # [0,0,0],
    # [1,0,1],
    # [0,1,1],
    # [0,1,0]