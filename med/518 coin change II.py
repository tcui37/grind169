class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # amount, coin
        memo = [[-1 for i in range(len(coins))] for _ in range(amount + 1)]

        def ways(i, amt):
            if amt == 0:
                return 1
            if i == len(coins):
                return 0
            if memo[amt][i] != -1:
                return memo[amt][i]
            if coins[i] > amt:
                memo[amt][i] = ways(i + 1, amt)
            else:
                memo[amt][i] = ways(i, amt - coins[i]) + ways(i + 1, amt)
            return memo[amt][i]

        return ways(0, amount)
