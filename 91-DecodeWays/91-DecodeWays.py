# Last updated: 09/08/2026, 17:06:30
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3
4        dp = [amount + 1] * (amount +1)
5        dp[0] = 0
6
7        for a in range(1, amount+1):
8            for c in coins:
9                if a - c >= 0:
10                    dp[a] = min(dp[a], 1 + dp[a-c])
11
12        return dp[amount] if dp[amount]!= amount+1 else -1
13