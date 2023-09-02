class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0 for i in range(n)]

        def dp(i):
            if i >= n:
                return 0
            if memo[i] > 0:
                return memo[i]
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    memo[i] = max(memo[i], dp(j))
            memo[i] = memo[i] + 1
            return memo[i]

        return max(dp(i) for i in range(n))
