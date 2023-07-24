class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        if m == 1 and n == 1:
            return 1

        def neighbors(i, j):
            neighbors = []
            if i > 0:
                neighbors.append((i - 1, j))
            if i < m - 1:
                neighbors.append((i + 1, j))
            if j > 0:
                neighbors.append((i, j - 1))
            if j < n - 1:
                neighbors.append((i, j + 1))
            return neighbors

        memo = [[None for j in range(n)] for i in range(m)]
        parent = [[None for j in range(n)] for i in range(m)]

        # find 'valleys' of the matrix
        for i in range(m):
            for j in range(n):
                if min([matrix[a][b] for a, b in neighbors(i, j)]) >= matrix[i][j]:
                    memo[i][j] = 1
                    parent[i][j] = None

        def dp(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            max_i, max_i, max_p = max(
                [
                    (a, b, dp(a, b))
                    for a, b in neighbors(i, j)
                    if matrix[i][j] > matrix[a][b]
                ],
                key=lambda x: x[-1],
            )
            memo[i][j] = 1 + max_p
            parent[i][j] = max_i, max_i
            return 1 + max_p

        max_i, max_j, max_p = -1, -1, -1
        for i in range(m):
            for j in range(n):
                if dp(i, j) >= max_p:
                    max_i, max_j, max_p = i, j, dp(i, j)
        return max_p
        # rv = []
        # while parent[max_i][max_j] is not None:
        #     rv.append(matrix[max_i][max_j])
        #     max_i,max_j = parent[max_i][max_j]

        # rv.reverse()
        # return rv
