# Last updated: 30/08/2026, 16:04:24
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        l = 0 
4        r = sum(nums)
5
6        for i in range(len(nums)):
7            r-=nums[i]
8            if r == l:
9                return i
10
11            l+=nums[i]
12
13        return -1