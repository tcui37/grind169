from collections import deque


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1
        on = 0

        def get_neighbors(i, j):
            for a, b in [
                (i + 2, j + 1),
                (i + 1, j + 2),
                (i - 2, j + 1),
                (i - 1, j + 2),
                (i - 2, j - 1),
                (i - 1, j - 2),
                (i + 2, j - 1),
                (i + 1, j - 2),
            ]:
                yield a, b

        def on_board(i, j):
            return i >= 0 and i <= n - 1 and j >= 0 and j <= n - 1

        memo = [[[None for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]

        def get_p(i, j, k, p):
            if not on_board(i, j):
                return 0
            if k == 0:
                return p
            if memo[k][i][j]:
                return memo[k][i][j]
            else:
                total_p = 0
                for a, b in get_neighbors(i, j):
                    total_p += get_p(a, b, k - 1, p / 8)
            memo[k][i][j] = total_p
            return total_p

        return get_p(row, column, k, 1)
