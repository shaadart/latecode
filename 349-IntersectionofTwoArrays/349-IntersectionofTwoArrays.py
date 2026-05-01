# Last updated: 5/1/2026, 10:53:59 PM
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        lsum = 0
4        rsum = sum(nums)
5
6        for i in range(len(nums)):
7            rsum -= nums[i]
8            
9            if lsum == rsum:
10                return i
11            lsum += nums[i]
12
13        return -1