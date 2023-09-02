class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        start = min(coins)
        memo = {i: float("inf") for i in range(amount + 1)}
        for coin in coins:
            memo[coin] = 1
        memo[0] = 0

        for i in range(start, amount + 1):
            for d in coins:
                if d <= i:
                    memo[i] = min(memo[i], memo[i - d] + 1)
        return memo[amount] if memo[amount] != float("inf") else -1
