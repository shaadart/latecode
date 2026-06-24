# Last updated: 6/24/2026, 8:20:28 PM
1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        out = {}
4        pattern = list(pattern)
5        s = s.split()
6
7        if len(pattern) != len(s):
8            return False
9
10        # build output
11        for i in range(len(pattern)):
12            if pattern[i] in out:
13                if out[pattern[i]] != s[i]:
14                    return False
15
16            elif s[i] in out.values():
17                return False
18
19            else:
20                out[pattern[i]] = s[i]
21
22        return True
23