# Last updated: 4/27/2026, 11:14:52 AM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        s1 = "".join(sorted(s))
4        s2 = "".join(sorted(t))
5
6        return s1==s2
7
8        