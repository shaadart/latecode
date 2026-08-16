# Last updated: 17/08/2026, 02:41:48
1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        s = 0
4        out = []
5
6        for i in range(len(nums)):
7            s += nums[i]
8            out.append(s)
9
10
11        return out
12
13        