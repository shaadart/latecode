# Last updated: 19/10/2026, 16:21:04
class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        temp_nums = nums[1:]
        
        temp_nums.sort()

        return (nums[0] + temp_nums[0] + temp_nums[1])

        