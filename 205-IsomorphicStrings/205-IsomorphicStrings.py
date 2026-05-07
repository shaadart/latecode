# Last updated: 5/7/2026, 11:14:53 PM
1class Solution:
2    def replaceDigits(self, s: str) -> str:
3        s = list(s)
4        for i in range(1, len(s), 2):
5            s[i] = chr(ord(s[i-1])+ int(s[i]))
6
7        return "".join(s)
8        