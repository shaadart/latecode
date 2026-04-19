# Last updated: 4/19/2026, 8:00:26 PM
1class Solution:
2    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
3        i,j = 0,1
4
5        while i < len(nums1) and j < len(nums2):
6            i+=nums1[i]>nums2[j]
7            j+=1
8
9        return j-i-1
10        