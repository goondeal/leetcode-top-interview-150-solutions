"""[[ MEDIUM ]]"""
# class Solution:
#     def spiralOrder(self, matrix):
#         m, n = len(matrix), len(matrix[0])
#         border_top = 0
#         border_right = n
#         border_bottom = m
#         border_left = 0
#         i, j = 0, 0
#         result = []
#         while i >= border_left and i <= border_right and j >= border_top and j <= border_bottom:
#             result.append(matrix[i][j])
#             if i == border_top:
#                 if j == border_right:
#                     # border_bottom -= 1
#                     i += 1
#                 else:
#                     j += 1

#             elif j == border_right:
#                 if i == border_top:
#                     border_left -= 1
#                 i += 1
#             elif i == border_bottom:
#                 if j == border_right:
#                     border_top -= 1
#                 j -= 1
#             elif j == border_left:
#                 if i == border_bottom:
#                     border_right -= 1
#                 i -= 1
#         return result

# class Solution:
#     def spiralOrder(self, matrix):
#         m, n = len(matrix), len(matrix[0])
#         border_top = 0
#         border_right = n - 1
#         border_bottom = m -1
#         border_left = -1
#         i, j = 0, 0
#         result = []
#         stop = 0
#         while i >= border_top and i <= border_bottom and j >= border_left and j <= border_right and stop < 20:
#             stop += 1
#             print(f'(i, j) = ({i}, {j})   =>  ', matrix[i][j], f'  borders = ({border_top}, {border_right}, {border_bottom}, {border_left})')
#             result.append(matrix[i][j])
#             if i == border_top:
#                 if j == border_right:
#                     i += 1
#                     border_left += 1
#                 elif j == border_left:
#                     j += 1
#                     border_bottom -= 1
#                 else:
#                     j += 1
#             elif j == border_right:
#                 if i == border_bottom:
#                     j -= 1
#                     border_top += 1
#                 else:
#                     i += 1
#             elif i == border_bottom:
#                 if j == border_left:
#                     i -= 1
#                     border_right -= 1
#                 else:
#                     j -= 1
#             elif j == border_left:
#                 if i == border_top:
#                     j += 1
#                     border_bottom -= 1
#                 else:
#                     i -= 1
#         return result


class Solution:

    def _pop_row(self, matrix, row=0):
        return matrix.pop(row)

    def _pop_col(self, matrix, col=-1):
        return [row.pop(col) for row in matrix]

    def spiralOrder(self, matrix):
        result = []
        m = matrix.copy()
        last = 'l'
        stop = 0
        while any(m) and stop < 20:
            stop += 1
            if last == 'l':
                result += self._pop_row(matrix=m, row=0)
                last = 't'
            elif last == 't':
                result += self._pop_col(matrix=m, col=-1)
                last = 'r'
            elif last == 'r':
                result += self._pop_row(matrix=m, row=-1)[::-1]
                last = 'b'
            elif last == 'b':
                result += self._pop_col(matrix=m, col=0)[::-1]
                last = 'l'
        return result


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix3 = [[2, 5, 8], [4, 0, -1]]

    s = Solution()
    print(s.spiralOrder(matrix))
    print(s.spiralOrder(matrix2))
    print(s.spiralOrder(matrix3))
