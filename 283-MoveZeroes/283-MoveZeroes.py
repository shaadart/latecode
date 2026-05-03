# Last updated: 5/3/2026, 11:49:18 AM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        minprod = nums[0]
4        maxprod = nums[0]
5        result = nums[0]
6
7        for i in range(1, len(nums)):
8            if nums[i] < 0: 
9                maxprod, minprod = minprod, maxprod
10
11            maxprod = max(nums[i] , maxprod * nums[i])
12            minprod = min(nums[i] , minprod * nums[i])
13
14
15
16            result = max(maxprod, result)
17        return result
18
19        