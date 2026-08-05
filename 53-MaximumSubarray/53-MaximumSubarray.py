# Last updated: 05/08/2026, 10:04:26
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        left = 0 
4        seen = set()
5        ans = 0
6
7        for right in range(len(s)):
8            while s[right] in seen:
9                seen.remove(s[left])
10                left += 1
11
12            seen.add(s[right])
13
14            ans = max(ans, right-left + 1)
15
16        
17        return ans