"""[[ MEDIUM ]]"""
class Solution:
    def _is_valid_digits(self, digits_list, dim=9):
        digits_set = set(digits_list)
        return len(digits_list) == len(digits_set) and digits_set.issubset(set([str(x) for x in range(1, dim+1)]))


    def isValidSudoku(self, board) -> bool:
        dim = len(board)
        # validate rows
        for row in board:
            nums = [x for x in row if x != '.']
            if not self._is_valid_digits(nums):
                return False

        # validate columns
        for i in range(dim):
            col = [board[j][i] for j in range(dim) if board[j][i] != '.']
            if not self._is_valid_digits(col):
                return False
        
        # validate sub-boxes
        for i in range(0, dim, 3):
            for j in range(0, dim, 3):
                box = []
                for k in range(i, i+3):
                    box += [x for x in board[k][j:j+3] if x != '.']
                if not self._is_valid_digits(box):
                    return False

        return True