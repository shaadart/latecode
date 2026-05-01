class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r,maxP = 1,0
      

        while r < len(prices):
            if prices[r-1] < prices[r]:
                maxP += prices[r] - prices[r - 1]
            r+=1
       

        return maxP 
        