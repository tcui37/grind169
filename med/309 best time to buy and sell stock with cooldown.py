class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [None for price in prices]
        n = len(prices)

        def dp(i, n, memo):
            if i >= n:
                return 0
            if memo[i]:
                return memo[i]
            # dont buy
            memo[i] = dp(i + 1, n, memo)
            # buy, but try selling at each day
            for j in range(i + 1, n):
                memo[i] = max(memo[i], -prices[i] + prices[j] + dp(j + 2, n, memo))
            return memo[i]

        return dp(0, n, memo)
