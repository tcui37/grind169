class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        memo = [[-1 for j in range(n)] for i in range(m)]

        def lcs(i, j, s1, s2):
            if i > len(s1) - 1 or j > len(s2) - 1:
                return 0
            if memo[i][j] >= 0:
                return memo[i][j]
            memo[i][j] = max(
                1 + lcs(i + 1, j + 1, s1, s2) if s1[i] == s2[j] else -1,
                lcs(i + 1, j, s1, s2),
                lcs(i, j + 1, s1, s2),
            )
            return memo[i][j]

        return lcs(0, 0, text1, text2)
