# Last updated: 08/08/2026, 17:27:38
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        rob1, rob2 = 0,0
4        n = len(nums)
5        for i in nums:
6            newrob = max(i+rob1, rob2)
7            rob1 = rob2
8            rob2 = newrob
9
10        return rob2
11        