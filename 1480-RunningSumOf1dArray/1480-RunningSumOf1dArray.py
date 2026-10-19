# Last updated: 19/10/2026, 16:24:28
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        out = []

        for i in range(len(nums)):
            s += nums[i]
            out.append(s)


        return out

        