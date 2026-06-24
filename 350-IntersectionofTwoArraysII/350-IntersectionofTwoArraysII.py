# Last updated: 6/24/2026, 9:06:59 PM
1class Solution:
2    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        r = []
4
5        for i in range(len(nums1)):
6            if nums1[i] in nums2:
7                r.append(nums1[i])
8                nums2.remove(nums1[i])
9
10        return r
11        