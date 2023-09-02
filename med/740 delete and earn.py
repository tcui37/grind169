class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        val = {}
        for num in nums:
            val[num] = val.get(num, 0) + 1
        for key in val:
            val[key] = key * val[key]
        # map each unique num to frequency * key_value
        key_list = list(val.keys())
        key_list.sort()
        n = len(key_list)
        memo = [-1 for i in range(n)]

        def dp(i):
            if i >= n:
                return 0
            if memo[i] >= 0:
                return memo[i]
            val[key_list[i]]

            # not a diff of one apart
            if i + 1 < n and key_list[i + 1] - key_list[i] > 1:
                memo[i] = val[key_list[i]] + dp(i + 1)
            memo[i] = max(memo[i], dp(i + 1), val[key_list[i]] + dp(i + 2))
            return memo[i]

        return dp(0)
