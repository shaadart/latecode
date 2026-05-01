# Last updated: 5/1/2026, 9:52:54 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        #this is a two pointer shit, not sliding window
4        r,maxP = 1,0
5      
6
7        while r < len(prices):
8            if prices[r-1] < prices[r]:
9                maxP += prices[r] - prices[r - 1]
10            r+=1
11       
12
13        return maxP 
14        