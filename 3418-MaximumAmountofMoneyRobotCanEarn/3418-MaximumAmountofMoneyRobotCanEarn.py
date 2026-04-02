# Last updated: 4/2/2026, 3:07:57 PM
1class Solution:
2    def maximumAmount(self, coins):
3        m = len(coins)
4        n = len(coins[0])
5
6        dp = [[[None] * 3 for _ in range(n)] for _ in range(m)]
7
8        def solve(coins, i, j, neu):
9            if i == m - 1 and j == n - 1:
10                if coins[i][j] < 0 and neu > 0:
11                    return 0
12                return coins[i][j]
13
14            if i >= m or j >= n:
15                return float('-inf')
16
17            if dp[i][j][neu] is not None:
18                return dp[i][j][neu]
19
20            # take
21            take = coins[i][j] + max(
22                solve(coins, i + 1, j, neu),
23                solve(coins, i, j + 1, neu)
24            )
25
26            # skip
27            skip = float('-inf')
28            if coins[i][j] < 0 and neu > 0:
29                skip = max(
30                    solve(coins, i + 1, j, neu - 1),
31                    solve(coins, i, j + 1, neu - 1)
32                )
33
34            dp[i][j][neu] = max(take, skip)
35            return dp[i][j][neu]
36
37        return solve(coins, 0, 0, 2)