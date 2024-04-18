"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def _get_num_from_board_index(self, i, j, n):
        r = n - 1 - i
        c = j if r % 2 == 0 else (n - 1 - j)
        return n * r + c + 1

    def _get_board_index_from_num(self, num, n):
        r, c = divmod(num-1, n)
        i = n - 1 - r
        j = c if r % 2 == 0 else (n - 1 - c)
        return i, j

    def _find_min_moves(self, n, graph, curr, sol_graph, moves):
        # discard the solutions with more moves.
        if moves > sol_graph[n*n]:
            return

        queue = set()
        for num in curr:
            if moves < sol_graph.get(num, 0):
                sol_graph[num] = moves
            queue |= graph.get(num, set())

        # (queue != curr) condition is to prevent no-solution recursion
        if queue and queue != curr:
            self._find_min_moves(n, graph, queue, sol_graph, moves+1)

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        graph = {}

        # save mandatory moves
        mandatory_moves = {}
        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val != -1:
                    mandatory_moves[self._get_num_from_board_index(
                        i, j, n)] = val
        for i in range(n*n):
            num = i + 1
            graph[num] = {mandatory_moves.get(
                x, x) for x in range(num+1, min(num+7, n*n+1))}

        sol_graph = {key: n*n+1 for key in graph}
        self._find_min_moves(n, graph, [1], sol_graph, 0)
        return sol_graph[n*n] if sol_graph[n*n] != n*n+1 else -1


if __name__ == '__main__':
    s = Solution()
    print(s.snakesAndLadders([
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]))  # 4
    print(s.snakesAndLadders([
        [-1, -1],
        [-1, -1],
    ]))  # 1
    print(s.snakesAndLadders([[-1, 4, -1], [6, 2, 6], [-1, 3, -1]]))  # 2
    print(s.snakesAndLadders([
        [-1, 1, 2, -1],
        [2, 13, 15, -1],
        [-1, 10, -1, -1],
        [-1, 6, 2, 8]
    ]))  # 2
    print(s.snakesAndLadders([
        [-1, -1, 30, 14, 15, -1],
        [23,  9, -1, -1, -1, 9],
        [12,  5, 7,  24, -1, 30],
        [10, -1, -1, -1, 25, 17],
        [32, -1, 28, -1, -1, 32],
        [-1, -1, 23, -1, 13, 19]
    ]))  # 2
