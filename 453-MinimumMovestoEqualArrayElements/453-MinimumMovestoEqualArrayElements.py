# Last updated: 01/11/2026, 20:26:25
1class Solution:
2    def minMoves(self, nums: list[int]) -> int:
3        mn = min(nums)
4        ans = 0
5        for i in range(len(nums)):
6            ans+= nums[i]-mn
7
8        return ans
9        