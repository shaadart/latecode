# Last updated: 5/1/2026, 9:52:35 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        r,maxP = 1,0
4      
5
6        while r < len(prices):
7            if prices[r-1] < prices[r]:
8                maxP += prices[r] - prices[r - 1]
9            r+=1
10       
11
12        return maxP 
13        