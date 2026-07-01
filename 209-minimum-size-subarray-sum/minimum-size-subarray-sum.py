from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        j = 0
        curr_sum = 0
        minlen = float("inf")

        while j<n:
            curr_sum+=nums[j]

            while curr_sum>=target:
                minlen = min(minlen, j-i+1)
                curr_sum -= nums[i]
                i+=1

            j+=1

        return minlen if minlen != float('inf') else 0
