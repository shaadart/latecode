# Last updated: 09/08/2026, 12:02:58
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        n = len(s)
4        res = ""
5        reslen = 0
6
7        for i in range(n):
8            #odd length
9            l,r, = i,i
10            while l>=0 and r < n and s[l] == s[r]:
11                if reslen < (r - l + 1):
12                    res = s[l:r+1]
13                    reslen = r - l + 1 
14
15                l-=1
16                r+=1
17
18            #even length
19            l,r = i, i+1
20            while l>=0 and r<n and s[l] == s[r]:
21                if reslen < (r-l+1):
22                    res = s[l:r+1]
23                    reslen = r-l+1
24
25                l-=1
26                r+=1
27
28        return res