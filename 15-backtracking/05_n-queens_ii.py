"""[[ HARD ]]"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        '''
        Approach:
            starting at the first row:
                for each col:
                    try to place a queen in this position,
                    with a way of mark this position to avoid placing the next queen in a place that could be attacked by the previous queens.
                    Do the same for the next row

        Time Complexity: O(N^2)
        Space Complexity: O(N)
        '''
        cols = set()
        # Positive diagonals start from bottom-left to top-right, with the pattern of r + c is constant for all positions on a diagonal.
        pos_diag = set()  # r + c
        # Negative diagonals start from top-left to bottom-right, with the pattern of r - c is constant for all positions on a diagonal.
        neg_diag = set()  # r - c

        result = []  # could be just a counter int.

        def _track(row, path):
            if row == n:
                nonlocal result
                result.append(path)
                # print(path)
            else:
                for col in range(n):
                    # if position is a possible attack, pass it.
                    if col in cols or row + col in pos_diag or row - col in neg_diag:
                        continue

                    # place a queen here.
                    cols.add(col)
                    pos_diag.add(row + col)
                    neg_diag.add(row - col)
                    path.append((row, col))
                    # move to the next row
                    _track(row + 1, path)
                    # remove the queen from this place before trying the next col.
                    cols.remove(col)
                    pos_diag.remove(row + col)
                    neg_diag.remove(row - col)
                    path.pop()

        _track(0, [])
        return len(result)


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 10):
        s.totalNQueens(i)
