# Last updated: 6/13/2026, 11:04:20 AM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6
7        for i in range(k):
8            rem = nums.pop()
9            nums.insert(0, rem)
10
11        return nums
12        