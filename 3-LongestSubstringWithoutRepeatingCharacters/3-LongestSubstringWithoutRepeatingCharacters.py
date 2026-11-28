# Last updated: 28/11/2026, 13:03:20
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        left = 0 
4        seen = set()
5        ans = 0
6
7        for right in range(len(s)):
8            while s[right] in seen:
9                seen.remove(s[left])
10                left+=1
11
12
13            seen.add(s[right])
14            ans = max(ans, right-left + 1)
15            
16        return ans
17