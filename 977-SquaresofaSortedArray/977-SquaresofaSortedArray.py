# Last updated: 19/11/2026, 07:23:21
1class Solution:
2    def sortedSquares(self, nums: list[int]) -> list[int]:
3        for i in range(len(nums)):
4            nums[i] *= nums[i]
5
6        nums.sort()
7        return nums 