# Last updated: 19/10/2026, 16:28:14
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)
        nums.sort()
        for i in range(count):

            if nums[i] != i:
                return i

        return count
        