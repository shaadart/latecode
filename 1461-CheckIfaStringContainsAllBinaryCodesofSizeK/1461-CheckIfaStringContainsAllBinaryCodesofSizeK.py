# Last updated: 2/24/2026, 3:41:34 AM
1class Solution:
2    def hasAllCodes(self, s: str, k: int) -> bool:
3
4
5        seen = set()
6
7        for i in range(len(s) - k + 1):
8            seen.add(s[i:i+k])
9
10        return len(seen) == 2 **k
11        # um = []
12        # for i in range(0,len(s)-k+1):
13        #     temp = []
14        #     for j in range(i,k+i):
15                
16        #         temp.append(s[j])
17        #     if temp not in um:
18        #         um.append(temp)
19
20        # if len(um) == 2**k:
21        #     return True
22        # else: 
23        #     return False
24
25
26
27
28
29        