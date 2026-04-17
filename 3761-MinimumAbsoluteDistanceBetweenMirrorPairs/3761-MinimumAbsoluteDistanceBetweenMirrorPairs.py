# Last updated: 4/18/2026, 12:29:00 AM
1class Solution:
2    def minMirrorPairDistance(self, nums: List[int]) -> int:
3        def rotate_num(num):
4            reverse = 0
5            while num!=0:
6                digit = num % 10
7                reverse = (reverse * 10) + digit
8                num = num//10
9            
10            return reverse
11
12        pairmap = {}
13        dist = float('inf')
14
15        for i in range(len(nums)):
16            x = nums[i]
17            R = rotate_num(x)
18
19            if x in pairmap:
20                dist = min(dist, i - pairmap[x])
21            pairmap[R] = i
22
23        return -1 if dist == float('inf') else dist
24
25
26
27    
28        