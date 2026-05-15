# Last updated: 5/16/2026, 12:14:15 AM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        return nums[bisect_left(nums, True, key=lambda n: n <= nums[-1])]