# Last updated: 28/07/2026, 12:15:33
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6
7        nums1[m:] = nums2 
8        nums1.sort()
9