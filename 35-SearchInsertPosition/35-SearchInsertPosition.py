# Last updated: 02/08/2026, 12:46:58
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        for i in range(len(nums)):
4            if nums[i] == target:
5                return i
6
7            elif nums[i] > target:
8                return i
9
10        return len(nums)