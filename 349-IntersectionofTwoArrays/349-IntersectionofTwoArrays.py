# Last updated: 5/1/2026, 10:40:50 AM
1class Solution:
2    def firstUniqChar(self, s: str) -> int:
3        freq = {}
4
5        for ch in s:
6            freq[ch] = freq.get(ch, 0) + 1
7
8          
9
10        for i, ch in enumerate(s):
11            if freq[ch] == 1:
12                return i
13            
14        return -1
15        