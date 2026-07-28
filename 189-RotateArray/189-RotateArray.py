# Last updated: 28/07/2026, 12:41:22
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        n = len(nums)
4        k %= n
5
6        r = nums[:n-k]
7        l = nums[n-k:]
8        nums[:] = l + r
9