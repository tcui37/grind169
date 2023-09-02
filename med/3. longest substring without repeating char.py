class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        bigL = 0
        i = -1
        for j, c in enumerate(s):
            i = max(i, last.get(c, -1))
            bigL = max(bigL, j - i)
            last[c] = j
        return bigL
