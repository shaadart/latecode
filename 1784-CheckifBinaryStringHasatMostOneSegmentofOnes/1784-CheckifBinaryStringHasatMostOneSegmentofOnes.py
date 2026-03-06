# Last updated: 3/6/2026, 12:54:35 PM
1class Solution:
2    def checkOnesSegment(self, s: str) -> bool:
3        
4        count = 0 
5        n = len(s)
6        i = 0 
7        while i < n:
8
9            if s[i] == '1':
10                count+=1
11                while i < n and s[i] == "1":
12                    i+=1
13
14            else: 
15                i+=1
16
17        
18        if count == 1:
19            return True
20
21        return False
22
23
24        