class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        rv = 0
        window_size = 0
        i = 0
        freq = {}
        max_freq = 0
        for j, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1
            max_freq = max(max_freq, freq[c])
            window_size = j - i + 1
            while window_size - max_freq > k:
                freq[s[i]] -= 1
                if freq[s[i]] == 0:
                    del freq[s[i]]
                i = i + 1
                window_size = j - i + 1
            rv = max(rv, window_size)
        return rv
