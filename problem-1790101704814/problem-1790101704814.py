# Last updated: 22/09/2026, 23:58:24
1class Solution:
2    def removeElement(self, nums: list[int], val: int) -> int:
3        nums[:] = [item for item in nums if item!=val]
4        return len(nums)
5        