class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mn = min(nums)
        ans = 0
        for i in range(len(nums)):
            ans+= nums[i]-mn

        return ans
        