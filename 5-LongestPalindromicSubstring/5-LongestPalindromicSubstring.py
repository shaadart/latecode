# Last updated: 09/08/2026, 11:44:45
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        n = len(s)
4        res = ""
5        reslen = 0
6        for i in range(n):
7            #odd length
8            l,r = i , i
9            while l>=0 and r<n and s[l] == s[r]:
10                if r-l+1 > reslen:
11                    res = s[l:r+1]
12                    reslen = r-l+1
13                l-=1
14                r+=1
15
16            #even length
17            l,r = i,i+1
18            while l>=0 and r<n and s[l] == s[r]:
19                if r-l+1>reslen:
20                    res = s[l:r+1]
21                    reslen = r - l +1
22
23                l-=1
24                r+=1
25
26            
27        return res
28
29
30
31
32
33        