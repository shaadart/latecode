# Last updated: 4/20/2026, 10:34:23 PM
1class Solution:
2    def maxDistance(self, colors: List[int]) -> int:
3        n = len(colors)
4        ans = 0 
5
6        for i in range(n):
7            if colors[i] != colors[0]:
8                ans = max(ans, i)
9
10            if colors[i] != colors[-1]:
11                ans = max(ans, n-1-i)
12
13        return ans
14        