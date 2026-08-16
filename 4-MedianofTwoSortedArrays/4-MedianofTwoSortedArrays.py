# Last updated: 16/08/2026, 12:17:06
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3
4        
5        nums3 = nums1 + nums2
6        nums3.sort()
7        n = len(nums3)
8
9        if n%2 == 1:
10            return nums3[n // 2]
11
12        return (nums3[n // 2] + nums3[n // 2-1]) / 2
13        