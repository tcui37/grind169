class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxl, maxm, maxL = 0, 0, 0
        for i in range(n):
            l, m = i, i
            while l - 1 >= 0 and m + 1 <= n - 1 and s[l - 1] == s[m + 1]:
                l -= 1
                m += 1

            if m - l + 1 > maxL:
                maxl, maxm, maxL = l, m, m - l + 1

        for i, j in zip(range(0, n - 1), range(1, n)):
            if s[i] != s[j]:
                continue
            l, m = i, j
            while l - 1 >= 0 and m + 1 <= n - 1 and s[l - 1] == s[m + 1]:
                l -= 1
                m += 1
            if m - l + 1 > maxL:
                maxl, maxm, maxL = l, m, m - l + 1

        return s[maxl : maxm + 1]
