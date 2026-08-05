# Last updated: 05/08/2026, 11:52:28
1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        left, right = 0, len(nums)-1
4
5        while left < right:
6            mid = (left+right)//2
7
8            if nums[mid] < nums[mid+1]:
9                left = mid+1
10
11            else:
12                right = mid
13
14        return left
15