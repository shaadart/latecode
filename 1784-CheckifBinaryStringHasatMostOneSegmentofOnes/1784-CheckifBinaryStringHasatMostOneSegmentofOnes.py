# Last updated: 3/6/2026, 12:51:57 PM
1class Solution:
2    def checkOnesSegment(self, s: str) -> bool:
3        
4        count = 0 
5        n = len(s)
6        i = 0
7
8        while i < n:
9
10            if s[i] == '1':
11                count+=1
12                while i < n and s[i] == "1":
13                    i+=1
14
15            else: 
16                i+=1
17
18        
19        if count == 1:
20            return True
21
22        return False
23
24
25        