# Last updated: 5/7/2026, 10:46:54 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        freqs = {}
4        freqt= {}
5
6        for i in range(len(s)):
7            # print(freqs[s[i]])
8            # print(freqs[s[i]])
9            freqs[s[i]] = freqs.get(s[i], 0) + 1
10
11        for i in range(len(t)):
12            freqt[t[i]] = freqt.get(t[i], 0) + 1
13            
14        return freqs == freqt
15
16
17        