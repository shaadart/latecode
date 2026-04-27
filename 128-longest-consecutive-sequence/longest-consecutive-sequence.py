from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        out = []
        nums.sort()
        n = len(nums)
        temp = [nums[0]]

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                continue  # skip duplicates

            if nums[i] == nums[i-1] + 1:
                temp.append(nums[i])
            else:
                if len(temp) > len(out):
                    out = temp[:]
                temp = [nums[i]]

        # final check
        if len(temp) > len(out):
            out = temp

        return len(out)