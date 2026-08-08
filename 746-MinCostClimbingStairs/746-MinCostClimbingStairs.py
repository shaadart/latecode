# Last updated: 08/08/2026, 13:26:39
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        cost.append(0)
4        n = len(cost)
5        for i in range(n-3, -1, -1):
6            cost[i] += min(cost[i+2], cost[i+1])
7
8        return min(cost[0], cost[1])
9
10        