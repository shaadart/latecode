# Last updated: 19/10/2026, 16:20:35
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        output = []

        for i in range(n):
            output.append(nums[(i + nums[i]) % n])


        return output

        