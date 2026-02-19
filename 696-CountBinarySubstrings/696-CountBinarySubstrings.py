# Last updated: 2/20/2026, 12:25:20 AM
1class Solution:
2    def countBinarySubstrings(self, s: str) -> int:
3        curr = 1 
4        prev = 0 
5        ans = 0
6        n = len(s)
7        for i in range(1, n):
8            
9            if s[i] == s[i-1]:
10                curr+=1
11
12            else: 
13                ans+= min(prev, curr) 
14                prev = curr
15                curr = 1
16                
17
18        return ans+(min(curr,prev))
19        