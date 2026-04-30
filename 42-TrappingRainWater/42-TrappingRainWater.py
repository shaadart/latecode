# Last updated: 4/30/2026, 1:27:19 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        n = len(height)
4
5        def getleftmaxarr(height, n):
6            left = [0] * n
7            left[0] = height[0]
8            for i in range(1, n):
9                left[i] = max(left[i-1], height[i])
10            return left
11
12        def getrightmaxarr(height, n):
13            right = [0] * n
14            right[n-1] = height[n-1]
15            for i in range(n-2, -1, -1):
16                right[i] = max(right[i+1], height[i])
17            return right
18
19        leftmaxarr = getleftmaxarr(height, n)
20        rightmaxarr = getrightmaxarr(height, n)
21
22        sum = 0
23        for i in range(1, len(height)):
24
25            trap = min(leftmaxarr[i], rightmaxarr[i]) - height[i]
26            sum = sum + trap 
27
28        return sum