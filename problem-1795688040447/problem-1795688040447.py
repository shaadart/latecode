# Last updated: 26/11/2026, 15:44:00
1class Solution:
2    def findMiddleIndex(self, nums: list[int]) -> int:
3        leftsum = 0
4        rightsum = sum(nums)
5        n = len(nums)
6        i = 0
7        while i<n:
8            rightsum -= nums[i]
9            if leftsum == rightsum:
10                return i
11
12            leftsum += nums[i]
13
14
15            i+=1
16        return -1
17