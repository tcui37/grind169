class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = [[None for i in range(n)] for j in range(n)]
        for i in range(n):
            memo[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                memo[i][i + 1] = True
            else:
                memo[i][i + 1] = False

        def dp(i, j, s):
            if memo[i][j] != None:
                return memo[i][j]
            memo[i][j] = dp(i + 1, j - 1, s) and s[i] == s[j]
            dp(i + 1, j, s)
            dp(i, j - 1, s)
            memo[i][j] = dp(i + 1, j - 1, s) and s[i] == s[j]
            return memo[i][j]

        dp(0, n - 1, s)
        s = 0
        for i in range(n):
            for j in range(n):
                if memo[i][j] == True:
                    s += 1
        print(memo)
        return s
