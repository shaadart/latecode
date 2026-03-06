# Last updated: 3/6/2026, 12:23:18 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        
4        rev = 0 
5        neg = False
6        if x < 0:
7            neg = True
8            x = abs(x)
9
10        
11            
12
13        while x!=0:
14            dig = x % 10
15            rev = rev * 10 + dig
16            x //=10
17
18        if rev < -2**31 or rev > 2**31 - 1:
19            return 0
20
21        if neg:
22            return -rev
23
24        else: 
25            return rev
26
27
28        