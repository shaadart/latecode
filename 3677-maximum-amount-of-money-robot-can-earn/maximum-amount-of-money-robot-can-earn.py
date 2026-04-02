class Solution:
    def maximumAmount(self, coins):
        m = len(coins)
        n = len(coins[0])

        dp = [[[None] * 3 for _ in range(n)] for _ in range(m)]

        def solve(coins, i, j, neu):
            if i == m - 1 and j == n - 1:
                if coins[i][j] < 0 and neu > 0:
                    return 0
                return coins[i][j]

            if i >= m or j >= n:
                return float('-inf')

            if dp[i][j][neu] is not None:
                return dp[i][j][neu]

            # take
            take = coins[i][j] + max(
                solve(coins, i + 1, j, neu),
                solve(coins, i, j + 1, neu)
            )

            # skip
            skip = float('-inf')
            if coins[i][j] < 0 and neu > 0:
                skip = max(
                    solve(coins, i + 1, j, neu - 1),
                    solve(coins, i, j + 1, neu - 1)
                )

            dp[i][j][neu] = max(take, skip)
            return dp[i][j][neu]

        return solve(coins, 0, 0, 2)