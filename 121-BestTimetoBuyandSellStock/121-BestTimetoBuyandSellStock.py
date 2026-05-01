# Last updated: 5/1/2026, 9:32:54 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        l,r, maxP = 0,1,0
4        n = len(prices)
5
6        while r < n:
7            if prices[l] < prices[r]:
8                profit = prices[r] - prices[l]
9                maxP = max(profit, maxP)
10
11            else:
12                l = r
13
14            r+=1
15
16        return maxP
17
18        