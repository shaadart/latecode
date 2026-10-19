# Last updated: 19/10/2026, 16:22:06
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        if k == 1:
            return 0
        #variables
        min_diff = float('inf')
        

        #sorting o(n)       
        nums.sort()

        #sliding window o(n)
        for i in range(len(nums)-k+1):
            current_diff = nums[i+k-1] - nums[i]
            min_diff = min(current_diff, min_diff)

        return min_diff

            



