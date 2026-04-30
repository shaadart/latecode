# Last updated: 4/30/2026, 10:22:58 AM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        count = len(nums)
4        nums.sort()
5        for i in range(count):
6
7            if nums[i] != i:
8                return i
9
10        return count
11        