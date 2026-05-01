class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r, maxP = 0,1,0
        n = len(prices)

        while r < n:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)

            else:
                l = r

            r+=1

        return maxP

        