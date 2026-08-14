# Last updated: 14/08/2026, 21:01:18
1class Solution:
2    def maximumLengthSubstring(self, s: str) -> int:
3        seen = {}
4
5        left = 0
6        n = len(s)
7        count = 0
8
9        for right in range(len(s)):
10            seen[s[right]] = seen.get(s[right], 0) + 1
11
12            while seen[s[right]] > 2:
13                seen[s[left]] -= 1
14                left +=1
15
16            count = max(count, right - left + 1)
17
18        return count  
19
20
21
22
23        