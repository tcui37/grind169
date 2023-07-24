class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[False for i in range(n)] for j in range(m)]

        def neighbors(i, j):
            return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

        def dfs(i, j, m, n, seen):
            sum_ = 0
            for a, b in neighbors(i, j):
                if a >= 0 and a <= m - 1 and b >= 0 and b <= n - 1:
                    if seen[a][b] == False and grid[a][b] == 1:
                        seen[a][b] = True
                        sum_ += dfs(a, b, m, n, seen)

            return sum_ + 1

        max_so_far = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and seen[i][j] == False:
                    seen[i][j] = True
                    max_so_far = max(max_so_far, dfs(i, j, m, n, seen))
        return max_so_far
