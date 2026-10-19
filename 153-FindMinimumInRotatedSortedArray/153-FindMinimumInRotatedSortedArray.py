# Last updated: 19/10/2026, 16:29:58
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return nums[bisect_left(nums, True, key=lambda n: n <= nums[-1])]