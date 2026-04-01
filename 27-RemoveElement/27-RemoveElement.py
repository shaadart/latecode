# Last updated: 4/1/2026, 7:02:22 AM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        nums[:] = [item for item in nums if item != val]
4        return len(nums)
5