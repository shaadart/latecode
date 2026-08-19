# Last updated: 19/08/2026, 20:30:52
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        i = 0
4        while i < (len(haystack)):
5            window = haystack[i:i+len(needle)]
6            # print(window)
7
8            if needle == window:
9                return i
10            i+=1
11
12        return -1
13